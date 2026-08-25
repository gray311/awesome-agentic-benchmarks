#!/usr/bin/env python3
"""Validate the task-level scientific discovery registry without dependencies."""

from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "data" / "discovery-tasks.json"
DOC_PATH = ROOT / "docs" / "discovery-tasks.md"
ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SEMVER_PATTERN = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")
DOMAINS = {
    "quantum-compilation",
    "astrodynamics",
    "scientific-algorithms",
    "ai-foundations",
    "mathematics-discovery",
    "interactive-world-discovery",
}
DIRECTIONS = {"minimize", "maximize"}
OUTCOMES = {"improved", "matched-reference", "below-reference", "not-yet-scored"}
TASK_TYPES = {
    "artifact-optimization",
    "interactive-rule-discovery",
    "scientific-investigation",
    "environment-learning",
}
REQUIRED_TASK_FIELDS = {
    "id",
    "name",
    "domain",
    "source_suite",
    "question",
    "input",
    "output",
    "metric",
    "evaluation",
    "environment",
    "reference_result",
    "reported_result",
    "outcome",
    "evidence_urls",
    "integrity_notes",
}


def is_https_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def is_iso_date(value: object) -> bool:
    if not isinstance(value, str):
        return False
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def expected_outcome(direction: str, reference: float, reported: float) -> str:
    if reported == reference:
        return "matched-reference"
    is_improvement = reported < reference if direction == "minimize" else reported > reference
    return "improved" if is_improvement else "below-reference"


def validate() -> list[str]:
    errors: list[str] = []
    try:
        registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"Cannot load {REGISTRY_PATH}: {exc}"]

    if not SEMVER_PATTERN.fullmatch(str(registry.get("registry_version", ""))):
        errors.append("registry_version must use MAJOR.MINOR.PATCH format")
    if not is_iso_date(registry.get("last_updated")):
        errors.append("last_updated must be an ISO date")

    suites = registry.get("source_suites")
    if not isinstance(suites, list) or not suites:
        return errors + ["source_suites must be a non-empty array"]
    suite_ids: set[str] = set()
    for index, suite in enumerate(suites):
        prefix = f"source_suites[{index}]"
        suite_id = suite.get("id")
        if not isinstance(suite_id, str) or not ID_PATTERN.fullmatch(suite_id):
            errors.append(f"{prefix}.id must be kebab-case")
        elif suite_id in suite_ids:
            errors.append(f"duplicate source suite id: {suite_id}")
        else:
            suite_ids.add(suite_id)
        if suite.get("result_status") not in {
            "source-reported",
            "independently-reproduced",
            "independently-certified",
        }:
            errors.append(f"{prefix}.result_status is invalid")
        evaluated_model = suite.get("evaluated_model")
        if evaluated_model is not None and (
            not isinstance(evaluated_model, str) or not evaluated_model
        ):
            errors.append(f"{prefix}.evaluated_model must be null or a non-empty string")
        for field in ("task_count", "public_task_count"):
            if not isinstance(suite.get(field), int) or suite[field] < 0:
                errors.append(f"{prefix}.{field} must be a non-negative integer")
        if (
            isinstance(suite.get("task_count"), int)
            and isinstance(suite.get("public_task_count"), int)
            and suite["public_task_count"] > suite["task_count"]
        ):
            errors.append(f"{prefix}.public_task_count cannot exceed task_count")
        families = suite.get("model_families")
        if not isinstance(families, list) or not families:
            errors.append(f"{prefix}.model_families must be a non-empty array")
        for field in ("paper", "repository", "task_catalogue"):
            if not is_https_url(suite.get(field)):
                errors.append(f"{prefix}.{field} must be an HTTPS URL")

    tasks = registry.get("tasks")
    if not isinstance(tasks, list) or not tasks:
        return errors + ["tasks must be a non-empty array"]

    docs = DOC_PATH.read_text(encoding="utf-8") if DOC_PATH.exists() else ""
    seen_ids: set[str] = set()
    for index, task in enumerate(tasks):
        prefix = f"tasks[{index}]"
        if not isinstance(task, dict):
            errors.append(f"{prefix} must be an object")
            continue
        missing = REQUIRED_TASK_FIELDS - task.keys()
        if missing:
            errors.append(f"{prefix} missing fields: {', '.join(sorted(missing))}")
            continue

        task_id = task["id"]
        if not isinstance(task_id, str) or not ID_PATTERN.fullmatch(task_id):
            errors.append(f"{prefix}.id must be kebab-case")
        elif task_id in seen_ids:
            errors.append(f"duplicate task id: {task_id}")
        else:
            seen_ids.add(task_id)

        if task["domain"] not in DOMAINS:
            errors.append(f"{task_id}: invalid domain")
        if "task_type" in task and task["task_type"] not in TASK_TYPES:
            errors.append(f"{task_id}: invalid task_type")
        if task["source_suite"] not in suite_ids:
            errors.append(f"{task_id}: source_suite does not reference a declared suite")
        if task["outcome"] not in OUTCOMES:
            errors.append(f"{task_id}: invalid outcome")

        metric = task["metric"]
        direction = metric.get("direction")
        if direction not in DIRECTIONS:
            errors.append(f"{task_id}: invalid metric direction")

        reference_result = task["reference_result"]
        reported_result = task["reported_result"]
        if reference_result is None or reported_result is None:
            if task["outcome"] != "not-yet-scored":
                errors.append(f"{task_id}: missing results require not-yet-scored outcome")
            reference = reported = None
        elif not isinstance(reference_result, dict) or not isinstance(reported_result, dict):
            errors.append(f"{task_id}: results must be objects or null")
            reference = reported = None
        else:
            reference = reference_result.get("score")
            reported = reported_result.get("score")
            if not isinstance(reference, (int, float)) or not isinstance(reported, (int, float)):
                errors.append(f"{task_id}: result scores must be numeric")
        if isinstance(reference, (int, float)) and isinstance(reported, (int, float)) and direction in DIRECTIONS:
            expected = expected_outcome(direction, float(reference), float(reported))
            if task["outcome"] != expected:
                errors.append(
                    f"{task_id}: outcome is {task['outcome']!r}, expected {expected!r}"
                )

        evidence_urls = task["evidence_urls"]
        if not isinstance(evidence_urls, list) or not evidence_urls:
            errors.append(f"{task_id}: evidence_urls must be a non-empty array")
        elif any(not is_https_url(url) for url in evidence_urls):
            errors.append(f"{task_id}: every evidence URL must use HTTPS")

        if task["name"] not in docs:
            errors.append(f"{task_id}: task name is missing from docs/discovery-tasks.md")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print(f"Discovery-task validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    print(
        f"Discovery-task registry is valid: {len(registry['tasks'])} tasks from "
        f"{len(registry['source_suites'])} source suite(s), version "
        f"{registry['registry_version']}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
