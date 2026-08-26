#!/usr/bin/env python3
"""Validate benchmark launch dates, GitHub stars, and catalog coverage."""

from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "benchmark-metadata.json"
README_PATH = ROOT / "README.md"
DOC_PATH = ROOT / "docs" / "benchmark-release-and-stars.md"
DISCOVERY_PATH = ROOT / "data" / "discovery-tasks.json"
CUA_GUI_PATH = ROOT / "data" / "cua-gui-benchmarks.json"
ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LAUNCH_PATTERNS = {
    "year": re.compile(r"^[0-9]{4}$"),
    "month": re.compile(r"^[0-9]{4}-(0[1-9]|1[0-2])$"),
    "day": re.compile(r"^[0-9]{4}-(0[1-9]|1[0-2])-([0-2][0-9]|3[01])$"),
}
CATALOG_ROW = re.compile(r"^\| \*\*([^*]+)\*\* \|", re.MULTILINE)


def is_https(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def is_date(value: object) -> bool:
    if not isinstance(value, str):
        return False
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def validate() -> list[str]:
    errors: list[str] = []
    registry = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    snapshot = registry.get("star_snapshot_as_of")
    if not is_date(snapshot):
        errors.append("star_snapshot_as_of must be an ISO date")

    entries = registry.get("benchmarks")
    if not isinstance(entries, list) or not entries:
        return errors + ["benchmarks must be a non-empty array"]

    ids: set[str] = set()
    names: set[str] = set()
    docs = DOC_PATH.read_text(encoding="utf-8")
    for index, entry in enumerate(entries):
        prefix = f"benchmarks[{index}]"
        benchmark_id = entry.get("id")
        name = entry.get("name")
        if not isinstance(benchmark_id, str) or not ID_PATTERN.fullmatch(benchmark_id):
            errors.append(f"{prefix}.id must be kebab-case")
        elif benchmark_id in ids:
            errors.append(f"duplicate benchmark id: {benchmark_id}")
        ids.add(str(benchmark_id))
        if not isinstance(name, str) or not name:
            errors.append(f"{prefix}.name must be non-empty")
        elif name in names:
            errors.append(f"duplicate benchmark name: {name}")
        names.add(str(name))

        launch = entry.get("launch", {})
        precision = launch.get("precision")
        value = launch.get("value")
        if precision not in LAUNCH_PATTERNS or not LAUNCH_PATTERNS[precision].fullmatch(str(value)):
            errors.append(f"{benchmark_id}: launch value does not match precision")
        if not is_https(launch.get("source")):
            errors.append(f"{benchmark_id}: launch source must use HTTPS")

        github = entry.get("github", {})
        repo = github.get("repository")
        stars = github.get("stars")
        status = github.get("status")
        if status == "available":
            if not isinstance(repo, str) or repo.count("/") != 1:
                errors.append(f"{benchmark_id}: available GitHub entry needs owner/repo")
            if not isinstance(stars, int) or stars < 0:
                errors.append(f"{benchmark_id}: available GitHub entry needs a star count")
            if github.get("stars_as_of") != snapshot:
                errors.append(f"{benchmark_id}: stars_as_of must match registry snapshot")
        elif status in {"repository-unavailable", "no-official-repository"}:
            if stars is not None or github.get("stars_as_of") is not None:
                errors.append(f"{benchmark_id}: unavailable GitHub metadata must use null stars")
        else:
            errors.append(f"{benchmark_id}: invalid GitHub status")

        if isinstance(name, str) and f"**{name}**" not in docs:
            errors.append(f"{benchmark_id}: missing from metadata documentation")

    readme = README_PATH.read_text(encoding="utf-8")
    papers_heading = "## Papers"
    if papers_heading not in readme:
        errors.append("README is missing the Papers section")
        catalog_names: set[str] = set()
    else:
        catalog_names = set(CATALOG_ROW.findall(readme[readme.index(papers_heading) :]))
    cua_gui = json.loads(CUA_GUI_PATH.read_text(encoding="utf-8"))
    cua_gui_names = {entry["name"] for entry in cua_gui.get("benchmarks", [])}
    missing_catalog = sorted(catalog_names - names - cua_gui_names)
    if missing_catalog:
        errors.append("README catalog entries missing metadata: " + ", ".join(missing_catalog))

    discovery = json.loads(DISCOVERY_PATH.read_text(encoding="utf-8"))
    missing_sources = sorted(
        suite["name"] for suite in discovery["registry_suites"] if suite["id"] not in ids
    )
    if missing_sources:
        errors.append("discovery source suites missing metadata: " + ", ".join(missing_sources))

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print(f"Benchmark-metadata validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    registry = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    available = sum(b["github"]["status"] == "available" for b in registry["benchmarks"])
    print(f"Benchmark metadata is valid: {len(registry['benchmarks'])} benchmarks, {available} GitHub star snapshots.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
