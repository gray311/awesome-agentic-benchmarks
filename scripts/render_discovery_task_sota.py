#!/usr/bin/env python3
"""Build the all-in-one discovery-task reference and its SOTA snapshot."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TASK_PATH = ROOT / "data" / "discovery-tasks.json"
SOTA_PATH = ROOT / "data" / "discovery-task-sota.json"
DOC_PATH = ROOT / "docs" / "all-discovery-tasks.md"
AS_OF = "2026-08-25"
SIMPLETES_PAPER = "https://arxiv.org/html/2604.19341"
SIMPLETES_ARTIFACTS = "https://github.com/wq-will/SimpleTES/tree/main/best_results"
ARC_BOARD = "https://arcprize.org/leaderboard/community"
ARC_SCORECARD = "https://arcprize.org/scorecards/08b98aa0-5df0-42c0-b501-856f553a21e9"
ARC_REPORT = "https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf"
ARC_FT09_REPLAY = "https://arcprize.org/replay/591e7e51-5004-4510-9e03-eca2b2d81edb?frame=19"
DIG_PAPER = "https://arxiv.org/html/2608.12593"
DIG_SITE = "https://digbench.ai/"

SUITE_LABELS = {
    "simpletes": "SimpleTES",
    "arc-agi-3": "ARC-AGI-3",
    "dig-bench": "DiG-bench",
}


def build_sota(registry: dict) -> dict:
    records = []
    for task in registry["tasks"]:
        suite = task["source_suite"]
        if suite == "simpletes":
            result = task["reported_result"]
            records.append(
                {
                    "task_id": task["id"],
                    "status": "task-level-current-best",
                    "scope": "task-level",
                    "system": result["system"] if task["id"] == "sum-difference-problem" else "SimpleTES + gpt-oss-120b",
                    "score": result["score"],
                    "metric": task["metric"],
                    "as_of": AS_OF,
                    "evidence_status": "source-reported-current-best",
                    "evidence_urls": [SIMPLETES_PAPER, SIMPLETES_ARTIFACTS],
                    "notes": (
                        "Best result located under the released task evaluator. This is a source-reported record, not an independent global certification."
                    ),
                }
            )
        elif suite == "arc-agi-3":
            evidence = [ARC_BOARD, ARC_SCORECARD, ARC_REPORT]
            note = (
                "The official community page reports Tycho at 100.0% on the public-demo suite, but labels community results self-reported and does not expose an attributable per-game breakdown. The suite score must not be copied into this task row."
            )
            if task["id"] == "arc-agi-3-ft09":
                evidence.append(ARC_FT09_REPLAY)
                note += " A public ft09 replay reaches 100%, but its model and harness fields are blank."
            records.append(
                {
                    "task_id": task["id"],
                    "status": "suite-level-only",
                    "scope": "suite-level",
                    "system": None,
                    "score": None,
                    "metric": task["metric"],
                    "as_of": AS_OF,
                    "evidence_status": "community-self-reported-no-task-breakdown",
                    "suite_best": {
                        "system": "Tycho",
                        "score": 100.0,
                        "metric_name": "ARC-AGI-3 public-demo RHAE score",
                        "unit": "percent",
                    },
                    "evidence_urls": evidence,
                    "notes": note,
                }
            )
        elif suite == "dig-bench":
            records.append(
                {
                    "task_id": task["id"],
                    "status": "suite-level-only",
                    "scope": "suite-level",
                    "system": None,
                    "score": None,
                    "metric": task["metric"],
                    "as_of": AS_OF,
                    "evidence_status": "source-reported-no-task-breakdown",
                    "suite_best": {
                        "system": "Claude Opus 5, basic harness",
                        "score": 50,
                        "metric_name": "games won",
                        "unit": "games out of 70",
                    },
                    "human_reference": "Every game was solved by at least one human on the first attempt.",
                    "evidence_urls": [DIG_PAPER, DIG_SITE],
                    "notes": (
                        "The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA."
                    ),
                }
            )
        else:
            raise ValueError(f"No SOTA policy for source suite {suite!r}")

    return {
        "$schema": "../schema/discovery-task-sota.schema.json",
        "snapshot_date": AS_OF,
        "definition": "Best result located under the exact published task contract; suite aggregates are never imputed to individual tasks.",
        "records": records,
    }


def link(url: str, label: str) -> str:
    return f"[{label}]({url})"


def number_text(value: int | float) -> str:
    """Preserve the decimal precision recorded in JSON while avoiding integer .0."""
    return str(value)


def score_text(record: dict) -> str:
    if record["status"] == "task-level-current-best":
        score = number_text(record["score"])
        direction = "↓" if record["metric"]["direction"] == "minimize" else "↑"
        return f"**{score} {direction}** — {record['system']}"
    best = record["suite_best"]
    return f"**Not published per task** — suite best: {best['system']}, {number_text(best['score'])} {best['unit']}"


def render_doc(registry: dict, sota: dict) -> str:
    records = {record["task_id"]: record for record in sota["records"]}
    counts = Counter(task["source_suite"] for task in registry["tasks"])
    domains = Counter(task["domain"] for task in registry["tasks"])
    lines = [
        "# All Discovery Tasks and Current SOTA",
        "",
        f"> Evidence snapshot: **{AS_OF}** · **{len(registry['tasks'])} tasks** · **{len(counts)} source suites**",
        "",
        "This is the single-file lookup for every task in the discovery registry. It records the agent-visible question and input, required output, evaluator, environment, metric, and the best result that could be traced to the exact task contract.",
        "",
        "## SOTA policy",
        "",
        "- **Task-level current best** means a result was located for that exact evaluator and task version. It may still be source-reported rather than independently reproduced.",
        "- **Suite-level only** means the source publishes an aggregate but no attributable per-task result. The aggregate is shown as context and is never imputed to a task.",
        "- Runtime results are hardware-sensitive; interactive results are harness-, budget-, game-version-, and run-count-sensitive.",
        "- `Current` means best located from primary sources by the snapshot date, not a guarantee that an unpublished or incomparable result does not exist.",
        "",
        "### Coverage",
        "",
        "| Evidence scope | Tasks | Interpretation |",
        "|---|---:|---|",
        "| Task-level current best | 28 | SimpleTES result and released artifact located |",
        "| Suite-level only | 24 | ARC-AGI-3 (3) and DiG-bench (21) publish no attributable per-task result table |",
        "",
        "### Source-suite snapshot",
        "",
        "| Source | Launch | GitHub stars | Tasks here | Current best evidence |",
        "|---|---:|---:|---:|---|",
        "| [SimpleTES](https://github.com/wq-will/SimpleTES) | 2026-04 | 169 | 28 | 28 task-level source-reported best results; current paper uses gpt-oss-120b |",
        "| [ARC-AGI-3](https://arcprize.org/arc-agi/3/) | 2026-04-22 | 69 | 3 | Tycho 100.0% public-demo aggregate; community self-reported, no attributable per-game table |",
        "| [DiG-bench](https://digbench.ai/) | 2026-08-12 | 24 | 21 | Claude Opus 5 basic harness: 50/70 games; no per-game table |",
        "",
        f"GitHub stars are the repository snapshots recorded on {AS_OF}; they are popularity metadata, not quality or SOTA evidence.",
        "",
        "## Master SOTA index",
        "",
        "| # | Task | Domain | Source | Metric | Current SOTA | Evidence |",
        "|---:|---|---|---|---|---|---|",
    ]

    for index, task in enumerate(registry["tasks"], 1):
        record = records[task["id"]]
        metric = task["metric"]
        direction = "↓" if metric["direction"] == "minimize" else "↑"
        status = "task-level, source-reported" if record["scope"] == "task-level" else "suite-level only"
        lines.append(
            f"| {index} | [{task['name']}](#{task['id']}) | {task['domain']} | {SUITE_LABELS[task['source_suite']]} | {metric['name']} ({direction}) | {score_text(record)} | {status} |"
        )

    lines.extend(["", "## Full task contracts", ""])
    current_domain = None
    for task in registry["tasks"]:
        if task["domain"] != current_domain:
            current_domain = task["domain"]
            lines.extend([f"## {current_domain.replace('-', ' ').title()}", ""])
        record = records[task["id"]]
        metric = task["metric"]
        direction = "minimize ↓" if metric["direction"] == "minimize" else "maximize ↑"
        evidence = " · ".join(
            link(url, f"source {index}") for index, url in enumerate(record["evidence_urls"], 1)
        )
        reference = task["reference_result"]
        reference_text = (
            f"{reference['system']}: {number_text(reference['score'])}" if reference is not None else "No matched task-level reference published"
        )
        lines.extend(
            [
                f"<a id=\"{task['id']}\"></a>",
                "",
                f"### {task['name']}",
                "",
                f"- **ID / source:** `{task['id']}` · {SUITE_LABELS[task['source_suite']]}",
                f"- **Question:** {task['question']}",
                f"- **Agent input:** {task['input']}",
                f"- **Required output:** {task['output']}",
                f"- **Evaluation:** {task['evaluation']}",
                f"- **Environment:** {task['environment']}",
                f"- **Metric:** {metric['name']} · {direction} · {metric['unit']}",
                f"- **Prior reference:** {reference_text}",
                f"- **Current SOTA:** {score_text(record)}",
                f"- **Evidence status:** `{record['evidence_status']}` as of {record['as_of']}",
                f"- **Primary evidence:** {evidence}",
                f"- **SOTA note:** {record['notes']}",
                f"- **Integrity note:** {task['integrity_notes']}",
                "",
            ]
        )

    lines.extend(
        [
            "## Maintenance",
            "",
            "The machine-readable SOTA snapshot is [`data/discovery-task-sota.json`](../data/discovery-task-sota.json). Regenerate both artifacts after changing the task registry:",
            "",
            "```bash",
            "python scripts/render_discovery_task_sota.py",
            "python scripts/render_discovery_task_sota.py --check",
            "```",
            "",
            "For a new record, provide the exact task/version, complete system and harness, score, run count or uncertainty when available, resource envelope, and primary result artifact. A suite leaderboard screenshot alone is insufficient for a task-level SOTA claim.",
            "",
        ]
    )
    return "\n".join(lines)


def serialize_sota(sota: dict) -> str:
    return json.dumps(sota, indent=2, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if generated files are stale")
    args = parser.parse_args()
    registry = json.loads(TASK_PATH.read_text(encoding="utf-8"))
    sota = build_sota(registry)
    expected = {SOTA_PATH: serialize_sota(sota), DOC_PATH: render_doc(registry, sota)}

    if args.check:
        stale = [path for path, content in expected.items() if not path.exists() or path.read_text(encoding="utf-8") != content]
        if stale:
            for path in stale:
                print(f"stale generated file: {path.relative_to(ROOT)}", file=sys.stderr)
            return 1
        print(f"Discovery SOTA artifacts are current: {len(sota['records'])} task records.")
        return 0

    for path, content in expected.items():
        path.write_text(content, encoding="utf-8")
        print(f"wrote {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
