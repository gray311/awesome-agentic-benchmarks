#!/usr/bin/env python3
"""Render the CUA/GUI benchmark registry as a readable Markdown reference."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "cua-gui-benchmarks.json"
OUTPUT_PATH = ROOT / "docs" / "cua-gui-benchmarks.md"
FAMILIES = ("GPT", "Claude", "GLM", "Kimi", "Qwen")


def escape(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def link(label: str, url: str | None) -> str:
    return f"[{label}]({url})" if url else label


def group_for(item: dict) -> str:
    if item["evaluation_unit"] == "safety-adversarial":
        return "Safety, privacy, prompt injection, and robustness"
    if item["artifact_type"] in {"arena", "evaluation-suite"}:
        return "Arenas and evaluation suites"
    if item["evaluation_unit"] in {"static-grounding", "offline-trajectory"}:
        return "GUI grounding and offline action prediction"
    platforms = set(item["platforms"])
    if "mobile" in platforms and "desktop" not in platforms:
        return "Mobile computer use"
    if "web" in platforms and not ({"desktop", "mobile", "terminal"} & platforms):
        return "Browser, web, and enterprise workflows"
    return "Desktop and hybrid computer use"


GROUP_ORDER = (
    "Desktop and hybrid computer use",
    "Browser, web, and enterprise workflows",
    "Mobile computer use",
    "GUI grounding and offline action prediction",
    "Safety, privacy, prompt injection, and robustness",
    "Arenas and evaluation suites",
)


def render(data: dict) -> str:
    items = data["benchmarks"]
    type_counts = Counter(item["artifact_type"] for item in items)
    unit_counts = Counter(item["evaluation_unit"] for item in items)
    year_2026 = sum(item["launch"]["value"].startswith("2026") for item in items)
    groups = {name: [] for name in GROUP_ORDER}
    for item in items:
        groups[group_for(item)].append(item)

    lines = [
        "# Computer-Use and GUI Agent Benchmarks",
        "",
        f"> Evidence snapshot: **{data['last_updated']}** · GitHub stars: **{data['star_snapshot_as_of']}** · **{len(items)} artifacts**, including **{year_2026} launched in 2026**.",
        "",
        "This registry separates the thing being evaluated from the software used to run it. A benchmark contains evaluation tasks; an offline dataset contains recorded states or trajectories; an arena aggregates human preferences; an evaluation suite normalizes other benchmarks. These labels are not interchangeable.",
        "",
        "## Evaluation units",
        "",
        "| Unit | What one scored example is |",
        "|---|---|",
    ]
    for key, description in data["evaluation_unit_definitions"].items():
        lines.append(f"| `{key}` | {escape(description)} |")

    lines += [
        "",
        "The central comparison rule is:",
        "",
        "> **score = model + scaffold + observation + action space + environment version + step/compute budget + evaluator + attempt policy**",
        "",
        "A ScreenSpot click-accuracy result is therefore not comparable to an OSWorld task-success result, and even two OSWorld scores are not comparable unless their versions and protocols match.",
        "",
        "## Registry composition",
        "",
        "| View | Counts |",
        "|---|---|",
        f"| Artifact type | {', '.join(f'`{k}` {v}' for k, v in sorted(type_counts.items()))} |",
        f"| Evaluation unit | {', '.join(f'`{k}` {v}' for k, v in sorted(unit_counts.items()))} |",
        f"| Launch year | 2026: **{year_2026}** · earlier: **{len(items) - year_2026}** |",
        "",
        "## Reported model-family coverage",
        "",
        "A check means a primary benchmark or model source reports an evaluated **agent** result for that family. It does not mean the row is directly comparable to another benchmark or scaffold. Blank means no verified result was attached in this snapshot—not that the family cannot run the task.",
        "",
        "| Benchmark | GPT | Claude | GLM | Kimi | Qwen | Evidence |",
        "|---|:---:|:---:|:---:|:---:|:---:|---|",
    ]
    coverage_items = [item for item in items if item["reported_model_families"]]
    coverage_items.sort(key=lambda item: (-len(item["reported_model_families"]), item["name"].lower()))
    for item in coverage_items:
        marks = ["✓" if family in item["reported_model_families"] else "" for family in FAMILIES]
        evidence = link("source", item["model_evidence"])
        lines.append(f"| {escape(item['name'])} | {' | '.join(marks)} | {evidence} |")

    lines += [
        "",
        "## Dated score snapshots",
        "",
        "These are orientation points, not a normalized leaderboard. Each statement retains the benchmark/version wording in the machine-readable record.",
        "",
    ]
    for item in items:
        if item["headline_result"]:
            lines.append(f"- **{item['name']}** — {item['headline_result']} {link('source', item['model_evidence'] or item['links']['primary'])}")

    lines += ["", "## Complete catalog", ""]
    for group_name in GROUP_ORDER:
        group_items = sorted(groups[group_name], key=lambda item: (item["launch"]["value"], item["name"].lower()), reverse=True)
        lines += [
            f"### {group_name}",
            "",
            "| Benchmark | Launch | Stars | Artifact / unit | Scale | Models reported | Primary artifacts |",
            "|---|---:|---:|---|---|---|---|",
        ]
        for item in group_items:
            github = item["github"]
            if github:
                stars = f"{github['stars']:,}"
                repo_url = f"https://github.com/{github['repository']}"
                stars = link(stars, repo_url)
            else:
                stars = "N/A"
            models = ", ".join(item["reported_model_families"]) or "—"
            artifacts = [link("Primary", item["links"]["primary"])]
            if item["links"].get("code") and item["links"]["code"] != item["links"]["primary"]:
                artifacts.append(link("Code", item["links"]["code"]))
            if item["links"].get("leaderboard"):
                artifacts.append(link("Leaderboard", item["links"]["leaderboard"]))
            lines.append(
                f"| **{escape(item['name'])}** | {item['launch']['value']} | {stars} | "
                f"`{item['artifact_type']}` / `{item['evaluation_unit']}` | {escape(item['scale'])} | "
                f"{escape(models)} | {' · '.join(artifacts)} |"
            )

        lines += [
            "",
            "<details>",
            f"<summary><strong>Evaluation contracts: {group_name}</strong></summary>",
            "",
            "| Benchmark | Input question | Agent-visible input | Required output | Evaluation | Environment |",
            "|---|---|---|---|---|---|",
        ]
        for item in group_items:
            lines.append(
                f"| **{escape(item['name'])}** | {escape(item['question'])} | {escape(item['input'])} | "
                f"{escape(item['output'])} | {escape(item['metric'])} | {escape(item['environment'])} |"
            )
        lines += ["", "</details>", ""]

    lines += [
        "## Integrity and maintenance notes",
        "",
        "- Live-web results age when sites, authentication, CAPTCHAs, or task validity change. Use a dated task manifest.",
        "- Shared-repository stars describe the host method/toolkit, not benchmark popularity. Repository scope is preserved in the JSON.",
        "- A zero-star repository is a verified numeric zero on the snapshot date; `N/A` means no verified official GitHub repository.",
        "- Offline action accuracy tests perception/policy imitation; it does not establish live end-to-end task success.",
        "- LLM/VLM judges require their exact model, prompt, evidence access, and human-agreement audit.",
        "- Safety benchmarks should report both task utility and unsafe-action/attack success; refusal alone is not general computer-use competence.",
        "",
        "## Machine-readable source",
        "",
        "Every row above is generated from [`data/cua-gui-benchmarks.json`](../data/cua-gui-benchmarks.json). CI validates required task contracts, artifact labels, launch sources, star snapshots, evaluation-unit vocabulary, and five-family coverage.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail if the rendered document is stale")
    args = parser.parse_args()
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    rendered = render(data)
    if args.check:
        current = OUTPUT_PATH.read_text(encoding="utf-8") if OUTPUT_PATH.exists() else ""
        if current != rendered:
            print(f"{OUTPUT_PATH.relative_to(ROOT)} is stale; run {Path(__file__).name}")
            return 1
        print(f"{OUTPUT_PATH.relative_to(ROOT)} is up to date ({len(data['benchmarks'])} artifacts).")
        return 0
    OUTPUT_PATH.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"Rendered {len(data['benchmarks'])} CUA/GUI artifacts to {OUTPUT_PATH.relative_to(ROOT)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
