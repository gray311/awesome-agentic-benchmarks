#!/usr/bin/env python3
"""Validate the benchmark registry without third-party dependencies."""

from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "data" / "benchmarks.json"
README_PATH = ROOT / "README.md"
ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SEMVER_PATTERN = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")
RSI_LEVELS = {
    "supporting-capability",
    "enabling-capability",
    "advanced-enabling-capability",
    "direct-ai-improvement",
    "agent-self-improvement",
    "recursive-self-improvement",
}
FEEDBACK_LEVELS = {"none", "weak", "medium", "strong"}
MODEL_FAMILIES = {"gpt", "claude", "glm", "kimi", "qwen"}
MODEL_COVERAGE_STATUSES = {
    "verified-agent",
    "verified-target",
    "verified-judge",
    "verified-multiple-roles",
    "not-yet-verified",
}
MODEL_ROLES = {"agent-model", "target-model", "judge-model"}
REQUIRED_FIELDS = {
    "id",
    "name",
    "organization",
    "release_year",
    "summary",
    "classification",
    "status",
    "urls",
    "task_suite",
    "input",
    "output",
    "evaluation",
    "environment",
    "score_snapshots",
    "integrity",
    "rsi_relevance",
    "model_coverage",
    "sources",
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


def validate() -> list[str]:
    errors: list[str] = []

    try:
        registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"Cannot load {REGISTRY_PATH}: {exc}"]

    version = registry.get("registry_version")
    if not isinstance(version, str) or not SEMVER_PATTERN.fullmatch(version):
        errors.append("registry_version must use MAJOR.MINOR.PATCH format")

    if not is_iso_date(registry.get("last_updated")):
        errors.append("last_updated must be an ISO date")

    benchmarks = registry.get("benchmarks")
    if not isinstance(benchmarks, list) or not benchmarks:
        return errors + ["benchmarks must be a non-empty array"]

    readme = README_PATH.read_text(encoding="utf-8")
    seen_ids: set[str] = set()
    ordered_ids: list[str] = []

    for index, benchmark in enumerate(benchmarks):
        prefix = f"benchmarks[{index}]"
        if not isinstance(benchmark, dict):
            errors.append(f"{prefix} must be an object")
            continue

        missing = sorted(REQUIRED_FIELDS - benchmark.keys())
        if missing:
            errors.append(f"{prefix} missing fields: {', '.join(missing)}")
            continue

        benchmark_id = benchmark["id"]
        if not isinstance(benchmark_id, str) or not ID_PATTERN.fullmatch(benchmark_id):
            errors.append(f"{prefix}.id must be kebab-case")
            benchmark_id = str(benchmark_id)
        if benchmark_id in seen_ids:
            errors.append(f"duplicate benchmark id: {benchmark_id}")
        seen_ids.add(benchmark_id)
        ordered_ids.append(benchmark_id)

        if benchmark["name"] not in readme:
            errors.append(f"{benchmark_id}: name is missing from README.md")

        for label, url in benchmark["urls"].items():
            if not is_https_url(url):
                errors.append(f"{benchmark_id}.urls.{label} must be an HTTPS URL")

        task_count = benchmark["task_suite"].get("evaluation_units")
        if not isinstance(task_count, int) or task_count <= 0:
            errors.append(f"{benchmark_id}: evaluation_units must be a positive integer")

        time_limit = benchmark["environment"].get("time_limit_hours")
        if not isinstance(time_limit, (int, float)) or time_limit <= 0:
            errors.append(f"{benchmark_id}: time_limit_hours must be positive")

        rsi = benchmark["rsi_relevance"]
        if rsi.get("level") not in RSI_LEVELS:
            errors.append(f"{benchmark_id}: invalid RSI relevance level")
        if rsi.get("closed_loop_feedback") not in FEEDBACK_LEVELS:
            errors.append(f"{benchmark_id}: invalid feedback-loop level")

        classification = benchmark["classification"]
        primary_dimension = classification.get("primary_dimension")
        if not isinstance(primary_dimension, str) or not ID_PATTERN.fullmatch(
            primary_dimension
        ):
            errors.append(f"{benchmark_id}: primary_dimension must be kebab-case")
        capabilities = classification.get("capabilities")
        if not isinstance(capabilities, list) or not capabilities:
            errors.append(f"{benchmark_id}: capabilities must be a non-empty array")

        coverage = benchmark["model_coverage"]
        if not is_iso_date(coverage.get("as_of")):
            errors.append(f"{benchmark_id}: model_coverage.as_of must be an ISO date")
        families = coverage.get("families")
        if not isinstance(families, dict) or set(families) != MODEL_FAMILIES:
            errors.append(
                f"{benchmark_id}: model_coverage must explicitly contain GPT, Claude, GLM, Kimi, and Qwen"
            )
        else:
            for family_name, family in families.items():
                family_prefix = f"{benchmark_id}.model_coverage.{family_name}"
                status = family.get("status")
                if status not in MODEL_COVERAGE_STATUSES:
                    errors.append(f"{family_prefix}: invalid status")
                    continue

                role_fields = {
                    "agent_models": "verified-agent",
                    "target_models": "verified-target",
                    "judge_models": "verified-judge",
                }
                for field_name in role_fields:
                    values = family.get(field_name)
                    if not isinstance(values, list):
                        errors.append(f"{family_prefix}.{field_name} must be an array")

                evidence = family.get("evidence")
                if not isinstance(evidence, list):
                    errors.append(f"{family_prefix}.evidence must be an array")
                    continue
                if status == "not-yet-verified" and evidence:
                    errors.append(
                        f"{family_prefix}: not-yet-verified entries cannot carry evidence"
                    )
                if status != "not-yet-verified" and not evidence:
                    errors.append(f"{family_prefix}: verified status requires evidence")
                for evidence_index, item in enumerate(evidence):
                    item_prefix = f"{family_prefix}.evidence[{evidence_index}]"
                    if item.get("role") not in MODEL_ROLES:
                        errors.append(f"{item_prefix}: invalid model role")
                    if not is_https_url(item.get("url")):
                        errors.append(f"{item_prefix}.url must be HTTPS")
                    if not is_iso_date(item.get("accessed")):
                        errors.append(f"{item_prefix}.accessed must be an ISO date")

        sources = benchmark["sources"]
        if not isinstance(sources, list) or len(sources) < 2:
            errors.append(f"{benchmark_id}: at least two primary sources are required")
        else:
            for source_index, source in enumerate(sources):
                if not is_https_url(source.get("url")):
                    errors.append(
                        f"{benchmark_id}.sources[{source_index}].url must be HTTPS"
                    )
                if not is_iso_date(source.get("accessed")):
                    errors.append(
                        f"{benchmark_id}.sources[{source_index}].accessed must be an ISO date"
                    )

        for snapshot_index, snapshot in enumerate(benchmark["score_snapshots"]):
            if not is_iso_date(snapshot.get("as_of")):
                errors.append(
                    f"{benchmark_id}.score_snapshots[{snapshot_index}].as_of must be an ISO date"
                )
            if snapshot.get("scale") == "0-100":
                for entry_index, entry in enumerate(snapshot.get("entries", [])):
                    score = entry.get("score")
                    if not isinstance(score, (int, float)) or not 0 <= score <= 100:
                        errors.append(
                            f"{benchmark_id}.score_snapshots[{snapshot_index}].entries[{entry_index}].score must be in [0, 100]"
                        )

    if ordered_ids != sorted(ordered_ids):
        errors.append("benchmark entries must be sorted by id")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print(f"Registry validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    print(
        f"Registry is valid: {len(registry['benchmarks'])} benchmarks, "
        f"version {registry['registry_version']}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
