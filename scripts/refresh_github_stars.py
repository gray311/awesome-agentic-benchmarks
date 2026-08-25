#!/usr/bin/env python3
"""Refresh GitHub star snapshots and regenerate the human-readable table."""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "benchmark-metadata.json"
DOC_PATH = ROOT / "docs" / "benchmark-release-and-stars.md"


def github_stars(repository: str, token: str | None) -> int:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "awesome-agentic-benchmarks-star-refresh",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = Request(f"https://api.github.com/repos/{repository}", headers=headers)
    with urlopen(request, timeout=30) as response:
        payload = json.load(response)
    return int(payload["stargazers_count"])


def render_doc(registry: dict) -> str:
    rows: list[str] = []
    for benchmark in sorted(registry["benchmarks"], key=lambda item: item["name"].casefold()):
        launch = benchmark["launch"]
        github = benchmark["github"]
        launch_cell = f"[{launch['value']}]({launch['source']})"
        stars_cell = "N/A"
        repository = github["repository"]
        if repository:
            snapshot = "unavailable" if github["stars"] is None else f"{github['stars']:,}"
            stars_cell = (
                f"[{repository}](https://github.com/{repository}) · "
                f"![GitHub stars](https://img.shields.io/github/stars/{repository}?style=flat&label=stars) · "
                f"snapshot {snapshot}"
            )
            if github["repository_scope"] != "benchmark-specific":
                stars_cell += f" · {github['repository_scope']}"
        rows.append(
            f"| **{benchmark['name']}** | {launch_cell} | "
            f"{launch['precision']} / {launch['basis']} | {stars_cell} |"
        )

    return f"""# Benchmark Launch Dates and GitHub Stars

**Metadata snapshot:** {registry['star_snapshot_as_of']}

This table covers every benchmark currently listed in the main README catalog, plus the task-source suites in the discovery registry.

## Interpretation

- **Launch** means the earliest public artifact verified by this repository: paper, official release, dataset, project, or repository. It is not necessarily the date of the latest benchmark version.
- Precision is explicit. `2026-06` means only the month is asserted; it must not be rendered as an invented day.
- **Stars** are repository-level popularity metadata, not benchmark quality or capability scores.
- The numeric snapshot is GitHub's `stargazers_count` on {registry['star_snapshot_as_of']}. The badge is live and may be newer.
- `shared-suite` means the repository hosts several evaluations, so its stars cannot be attributed solely to that benchmark. `toolkit` means the stars belong to an official integration/toolkit repository.
- `N/A` means no official GitHub repository was verified. It does not mean zero stars.

The machine-readable source is [data/benchmark-metadata.json](../data/benchmark-metadata.json).

## Complete catalog

| Benchmark | Launch | Precision / basis | Official GitHub and stars |
|---|---|---|---|
{chr(10).join(rows)}

## Maintenance

Star counts are intentionally dated because they change continuously. Run `python scripts/refresh_github_stars.py` to query GitHub and rebuild this page. A launch date should change only when stronger primary evidence establishes an earlier public release; later versions belong in version history, not the launch field.
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--render-only",
        action="store_true",
        help="Regenerate the Markdown table without making GitHub API requests.",
    )
    args = parser.parse_args()
    registry = json.loads(DATA_PATH.read_text(encoding="utf-8"))

    if not args.render_only:
        token = os.environ.get("GITHUB_TOKEN")
        failures: list[str] = []
        refreshed: dict[str, int] = {}
        for benchmark in registry["benchmarks"]:
            github = benchmark["github"]
            repository = github["repository"]
            if not repository or github["status"] == "repository-unavailable":
                continue
            try:
                refreshed[benchmark["id"]] = github_stars(repository, token)
            except (HTTPError, URLError, KeyError, ValueError) as exc:
                failures.append(f"{repository}: {exc}")
        if failures:
            print("Star refresh aborted; no files were changed:", file=sys.stderr)
            for failure in failures:
                print(f"- {failure}", file=sys.stderr)
            return 1

        snapshot = datetime.now(timezone.utc).date().isoformat()
        for benchmark in registry["benchmarks"]:
            if benchmark["id"] in refreshed:
                benchmark["github"]["stars"] = refreshed[benchmark["id"]]
                benchmark["github"]["stars_as_of"] = snapshot
        registry["star_snapshot_as_of"] = snapshot
        registry["last_updated"] = snapshot
        DATA_PATH.write_text(json.dumps(registry, indent=2) + "\n", encoding="utf-8")

    DOC_PATH.write_text(render_doc(registry), encoding="utf-8")
    print(
        f"Rendered {len(registry['benchmarks'])} benchmark metadata rows at "
        f"snapshot {registry['star_snapshot_as_of']}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
