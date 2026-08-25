#!/usr/bin/env python3
"""Validate the computer-use and GUI benchmark registry."""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "data" / "cua-gui-benchmarks.json"
ARTIFACT_TYPES = {"benchmark", "offline-dataset", "arena", "evaluation-suite"}
UNITS = {
    "static-grounding", "offline-trajectory", "interactive-episode",
    "long-horizon-workflow", "arena-preference", "safety-adversarial",
}
FAMILIES = {"GPT", "Claude", "GLM", "Kimi", "Qwen"}
REQUIRED = {
    "id", "name", "artifact_type", "platforms", "evaluation_unit", "launch",
    "scale", "question", "input", "output", "metric", "environment", "github",
    "links", "reported_model_families", "model_evidence", "headline_result", "status",
}


def is_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def main() -> int:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    items = data.get("benchmarks", [])
    errors: list[str] = []
    if len(items) < 60:
        errors.append(f"expected at least 60 curated CUA/GUI artifacts, found {len(items)}")
    ids = [item.get("id") for item in items]
    if len(ids) != len(set(ids)):
        errors.append("benchmark IDs must be unique")
    if set(data.get("evaluation_unit_definitions", {})) != UNITS:
        errors.append("evaluation_unit_definitions must exactly cover the allowed unit vocabulary")

    github_repos: dict[str, tuple[int, str]] = {}
    covered_families: set[str] = set()
    for index, item in enumerate(items):
        label = item.get("id", f"row-{index}")
        missing = REQUIRED - item.keys()
        if missing:
            errors.append(f"{label}: missing {sorted(missing)}")
            continue
        if item["artifact_type"] not in ARTIFACT_TYPES:
            errors.append(f"{label}: invalid artifact_type {item['artifact_type']!r}")
        if item["evaluation_unit"] not in UNITS:
            errors.append(f"{label}: invalid evaluation_unit {item['evaluation_unit']!r}")
        if not item["platforms"] or len(item["platforms"]) != len(set(item["platforms"])):
            errors.append(f"{label}: platforms must be a non-empty unique list")
        for field in ("scale", "question", "input", "output", "metric", "environment", "status"):
            if not isinstance(item[field], str) or not item[field].strip():
                errors.append(f"{label}: {field} must be a non-empty string")
        launch = item["launch"]
        if set(launch) != {"value", "precision", "source"}:
            errors.append(f"{label}: launch must contain value, precision, source")
        elif launch["precision"] not in {"day", "month", "year"} or not is_url(launch["source"]):
            errors.append(f"{label}: invalid launch precision/source")
        if not is_url(item["links"].get("primary")):
            errors.append(f"{label}: links.primary must be an https URL")
        github = item["github"]
        if github is not None:
            if set(github) != {"repository", "stars", "scope"}:
                errors.append(f"{label}: github must contain repository, stars, scope")
            elif not isinstance(github["stars"], int) or github["stars"] < 0 or "/" not in github["repository"]:
                errors.append(f"{label}: invalid GitHub repository or star count")
            else:
                prior = github_repos.get(github["repository"])
                current = (github["stars"], data["star_snapshot_as_of"])
                if prior and prior != current:
                    errors.append(f"{label}: inconsistent shared-repository star snapshot")
                github_repos[github["repository"]] = current
        families = item["reported_model_families"]
        if len(families) != len(set(families)) or not set(families) <= FAMILIES:
            errors.append(f"{label}: invalid or duplicate model families")
        if families and not is_url(item["model_evidence"]):
            errors.append(f"{label}: reported families require an https model_evidence source")
        if not families and item["model_evidence"] is not None:
            errors.append(f"{label}: model_evidence without reported family")
        covered_families.update(families)
        if item["evaluation_unit"] == "arena-preference" and item["artifact_type"] != "arena":
            errors.append(f"{label}: arena-preference requires artifact_type arena")

    if covered_families != FAMILIES:
        errors.append(f"five-family coverage incomplete: have {sorted(covered_families)}")
    type_counts = Counter(item.get("artifact_type") for item in items)
    if type_counts["benchmark"] < 45 or type_counts["offline-dataset"] < 5:
        errors.append(f"artifact mix is unexpectedly narrow: {dict(type_counts)}")
    if sum(item.get("launch", {}).get("value", "").startswith("2026") for item in items) < 20:
        errors.append("expected at least 20 verified 2026 CUA/GUI artifacts")

    if errors:
        print(f"CUA/GUI validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(
        f"CUA/GUI registry is valid: {len(items)} artifacts, "
        f"{sum(item['launch']['value'].startswith('2026') for item in items)} from 2026, "
        f"all five target model families covered."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
