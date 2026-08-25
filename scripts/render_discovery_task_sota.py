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
EINSTEIN_ERDOS = "https://einsteinarena.com/problems/erdos-min-overlap"
EINSTEIN_AC2 = "https://einsteinarena.com/problems/second-autocorrelation-inequality"
EINSTEIN_AC3 = "https://einsteinarena.com/problems/third-autocorrelation-inequality"
EINSTEIN_CIRCLE = "https://einsteinarena.com/problems/circle-packing"
ERDOS_CERTIFICATION = "https://github.com/bzanghi/erdos-minimum-overlap-bochner/blob/main/MINIMUM_OVERLAP_STATE_2026-07-25b.md"
MLEVOLVE = "https://github.com/InternScience/MLEvolve"
KSEARCH = "https://github.com/caoshiyi/K-Search"
SLD_RESULTS = "https://huggingface.co/datasets/pkuHaowei/scaling_law_discovery_results"
SLD_CODE = "https://github.com/linhaowei1/SLD"
TTT_DISCOVER = "https://test-time-training.github.io/discover/"
EFT_PAPER = "https://arxiv.org/html/2606.29082"
ALPHAEVOLVE_PAPER = "https://arxiv.org/abs/2511.02864"
HADAMARD_29 = "https://maths-people.anu.edu.au/~brent/maxdet/order29/"


# Overrides are deliberately sparse. A task absent from this map has a released
# source result, but no independently maintained current record was located for
# the exact evaluator contract. Never promote such a result to global SOTA.
CURRENT_RECORDS = {
    "circle-packing-n26": {
        "status": "live-leaderboard-best", "scope": "task-level",
        "system": "AlphaEvolve (tied on the live board)", "score": 2.6359830849,
        "evidence_status": "official-live-leaderboard",
        "evidence_urls": [EINSTEIN_CIRCLE, ALPHAEVOLVE_PAPER, SIMPLETES_PAPER, MLEVOLVE],
        "notes": "EinsteinArena lists AlphaEvolve first at 2.6359830849, with several agents tied at displayed precision. SimpleTES reports 2.635983 and MLEvolve 2.6359830395; neither should be presented as the unique current record.",
    },
    "circle-packing-n32": {
        "status": "tie-at-published-precision", "scope": "task-level",
        "system": "nanodiscover + Qwen3-8B / Finch-8B (EFT), tied at published precision", "score": 2.939573,
        "evidence_status": "cross-paper-tie-at-published-precision",
        "evidence_urls": [EFT_PAPER, SIMPLETES_PAPER, ALPHAEVOLVE_PAPER],
        "notes": "EFT Table 6 reports 2.939573 for both nanodiscover + Qwen3-8B and nanodiscover + Finch-8B, above the 2.939572 SimpleTES source result at displayed precision. The two 2.939573 entries are tied only at published precision; full-precision artifacts are needed to order them.",
    },
    "erdos-minimum-overlap": {
        "status": "live-leaderboard-best", "scope": "task-level",
        "system": "CodexProLong", "score": 0.38085857,
        "evidence_status": "official-live-leaderboard-with-certification-caveat",
        "evidence_urls": [EINSTEIN_ERDOS, ERDOS_CERTIFICATION, TTT_DISCOVER, SIMPLETES_PAPER],
        "notes": "EinsteinArena's live leader is CodexProLong. The independent certification note verifies a slightly older 0.3808590566148069 construction and explains why a widely cited lower SimpleTES number was affected by normalization; leaderboard rank and rigorous certification are therefore reported separately.",
    },
    "hadamard-determinant-n29": {
        "status": "tie-at-published-precision", "scope": "task-level",
        "system": "Orrick et al. human record (matched by SimpleTES)", "score": 0.935673,
        "evidence_status": "historical-record-matched-by-agent",
        "evidence_urls": [HADAMARD_29, SIMPLETES_PAPER],
        "notes": "The order-29 construction predates SimpleTES. SimpleTES matches the normalized determinant at published precision; it did not originate the record.",
    },
    "scaling-law-domain-mix": {
        "status": "artifact-reported-best", "scope": "task-level",
        "system": "SLDAgent + Gemini-3-Pro-Preview", "score": 0.993529,
        "evidence_status": "official-results-dataset",
        "evidence_urls": [SLD_RESULTS, SLD_CODE, SIMPLETES_PAPER],
        "notes": "Computed from the released SLDBench result records for the domain_mixture split. It exceeds the 0.991 SimpleTES source result under the matched split metric.",
    },
    "scaling-law-lr-bsz": {
        "status": "artifact-reported-best", "scope": "task-level",
        "system": "SLDAgent + GPT-5", "score": 0.847918,
        "evidence_status": "official-results-dataset",
        "evidence_urls": [SLD_RESULTS, SLD_CODE, SIMPLETES_PAPER],
        "notes": "Computed from the released SLDBench result records for the lr_bsz split. It exceeds the 0.712 SimpleTES source result.",
    },
    "scaling-law-parallel": {
        "status": "precision-ambiguous", "scope": "task-level", "system": None, "score": None,
        "evidence_status": "incomparable-published-precision",
        "evidence_urls": [SLD_RESULTS, SLD_CODE, SIMPLETES_PAPER],
        "notes": "The official SLDBench result dataset has SLDAgent + Claude Sonnet 4.5 at 0.999971, while SimpleTES reports 1.000 only to three decimals. The rounded number cannot establish a strict win or tie, so no unique current record is assigned.",
        "candidates": [
            {"system": "SLDAgent + Claude Sonnet 4.5", "score": 0.999971},
            {"system": "SimpleTES + gpt-oss-120b (rounded)", "score": 1.0},
        ],
    },
    "scaling-law-u-shape": {
        "status": "artifact-reported-best", "scope": "task-level",
        "system": "Aider + GPT-5", "score": 0.38070320345369735,
        "evidence_status": "official-results-dataset",
        "evidence_urls": [SLD_RESULTS, SLD_CODE, SIMPLETES_PAPER],
        "notes": "Computed from the released SLDBench easy_question/u-shape result records. It exceeds the -0.008 SimpleTES source result.",
    },
    "second-autocorrelation-inequality": {
        "status": "live-leaderboard-best", "scope": "task-level",
        "system": "ClaudeExplorer", "score": 0.96359,
        "evidence_status": "official-live-leaderboard",
        "evidence_urls": [EINSTEIN_AC2, TTT_DISCOVER, SIMPLETES_PAPER, MLEVOLVE],
        "notes": "EinsteinArena currently ranks ClaudeExplorer first. The board also records AlphaEvolve and TTT-Discover as earlier results; SimpleTES's 0.962694 is no longer the public leader.",
    },
    "sum-difference-problem": {
        "status": "artifact-reported-best", "scope": "task-level",
        "system": "MLEvolve", "score": 1.1901774219,
        "evidence_status": "source-reported-matched-task-table",
        "evidence_urls": [MLEVOLVE, ALPHAEVOLVE_PAPER, SIMPLETES_PAPER],
        "notes": "MLEvolve's official comparison table reports 1.1901774219 on Sums differences problem 1, above AlphaEvolve (1.1479889651) and SimpleTES (1.143975 in that table; 1.144887 in the later post-trained SimpleTES result).",
    },
    "third-autocorrelation-inequality": {
        "status": "live-leaderboard-best", "scope": "task-level",
        "system": "Poolish", "score": 1.45080664,
        "evidence_status": "official-live-leaderboard",
        "evidence_urls": [EINSTEIN_AC3, SIMPLETES_PAPER, MLEVOLVE],
        "notes": "EinsteinArena currently ranks Poolish first. SimpleTES's 1.453675 is a historical source result, not the current live record.",
    },
    "trimul-kernel": {
        "status": "artifact-reported-best", "scope": "task-level",
        "system": "K-Search", "score": 1.028,
        "evidence_status": "matched-upstream-evaluator-local-artifact",
        "evidence_urls": [KSEARCH, TTT_DISCOVER, SIMPLETES_PAPER],
        "notes": "K-Search reports 1.028 ms on H100 across the seven upstream GPUMode workloads and releases the generated kernels. It beats the 1.122 ms SimpleTES paper result, but is a local matched-evaluator artifact rather than an official leaderboard submission.",
    },
}

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
            source_system = result["system"] if task["id"] == "sum-difference-problem" else "SimpleTES + gpt-oss-120b"
            record = {
                "task_id": task["id"],
                "status": "source-reported-contract-incumbent",
                "scope": "contract-level",
                "system": None,
                "score": None,
                "metric": task["metric"],
                "as_of": AS_OF,
                "source_reported": {
                    "system": source_system,
                    "score": result["score"],
                    "evidence_urls": [SIMPLETES_PAPER, SIMPLETES_ARTIFACTS],
                },
                "evidence_status": "no-independent-current-record-located",
                "evidence_urls": [SIMPLETES_PAPER, SIMPLETES_ARTIFACTS],
                "notes": "A released SimpleTES result exists for this exact contract, but no independent current leaderboard or later matched-evaluator comparison was located. It is retained as a source-reported contract incumbent, not labeled global SOTA.",
            }
            record.update(CURRENT_RECORDS.get(task["id"], {}))
            records.append(record)
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
        "definition": "Source-suite results and current-record evidence are tracked separately; only exact-contract comparisons are ranked, and suite aggregates are never imputed to individual tasks.",
        "records": records,
    }


def link(url: str, label: str) -> str:
    return f"[{label}]({url})"


def number_text(value: int | float) -> str:
    """Preserve the decimal precision recorded in JSON while avoiding integer .0."""
    return str(value)


def score_text(record: dict) -> str:
    if record["status"] in {"live-leaderboard-best", "artifact-reported-best", "tie-at-published-precision"}:
        score = number_text(record["score"])
        direction = "↓" if record["metric"]["direction"] == "minimize" else "↑"
        return f"**{score} {direction}** — {record['system']}"
    if record["status"] == "precision-ambiguous":
        candidates = "; ".join(f"{item['system']} {number_text(item['score'])}" for item in record["candidates"])
        return f"**Unresolved at published precision** — {candidates}"
    if record["status"] == "source-reported-contract-incumbent":
        source = record["source_reported"]
        direction = "↓" if record["metric"]["direction"] == "minimize" else "↑"
        return f"**No independent current record located** — source report: {source['system']} {number_text(source['score'])} {direction}"
    best = record["suite_best"]
    return f"**Not published per task** — suite best: {best['system']}, {number_text(best['score'])} {best['unit']}"


def source_reported_text(record: dict) -> str:
    source = record.get("source_reported")
    if source is None:
        return "Not available as a task-level result"
    direction = "↓" if record["metric"]["direction"] == "minimize" else "↑"
    return f"{source['system']}: {number_text(source['score'])} {direction}"


def evidence_label(record: dict) -> str:
    return {
        "live-leaderboard-best": "live leaderboard",
        "artifact-reported-best": "matched artifact/result set",
        "tie-at-published-precision": "published-precision tie",
        "precision-ambiguous": "precision unresolved",
        "source-reported-contract-incumbent": "source result only",
        "suite-level-only": "suite aggregate only",
    }[record["status"]]


def render_doc(registry: dict, sota: dict) -> str:
    records = {record["task_id"]: record for record in sota["records"]}
    counts = Counter(task["source_suite"] for task in registry["tasks"])
    domains = Counter(task["domain"] for task in registry["tasks"])
    status_counts = Counter(record["status"] for record in sota["records"])
    externally_checked = sum(
        status_counts[key]
        for key in ("live-leaderboard-best", "artifact-reported-best", "tie-at-published-precision", "precision-ambiguous")
    )
    lines = [
        "# All Discovery Tasks and Current-Record Tracker",
        "",
        f"> Evidence snapshot: **{AS_OF}** · **{len(registry['tasks'])} tasks** · **{len(counts)} source suites**",
        "",
        "This is the single-file lookup for every task in the discovery registry. It records the agent-visible question and input, required output, evaluator, environment, metric, the source suite's own reported result, and a separately researched current-record field.",
        "",
        "## SOTA policy",
        "",
        "- **Source-reported result is not automatically SOTA.** It records what the suite paper or released artifact achieved.",
        "- **Current record** is assigned only when a live leaderboard, official result dataset, historical record, or later matched-evaluator artifact supports it.",
        "- **Contract incumbent only** means no independent maintained leaderboard or later exact-contract comparison was found. The source result remains useful, but is not labeled global SOTA.",
        "- **Tie / precision unresolved** is used when papers round differently or several systems match at published precision.",
        "- **Suite-level only** means the source publishes an aggregate but no attributable per-task result. The aggregate is shown as context and is never imputed to a task.",
        "- Runtime results are hardware-sensitive; interactive results are harness-, budget-, game-version-, and run-count-sensitive.",
        "- `Current` means best located from primary sources by the snapshot date, not a guarantee that an unpublished or incomparable result does not exist.",
        "",
        "### Coverage",
        "",
        "| Evidence scope | Tasks | Interpretation |",
        "|---|---:|---|",
        f"| Externally cross-checked current record / tie / ambiguity | {externally_checked} | Live leaderboards, official result datasets, historical records, or matched artifacts |",
        f"| Source-reported contract incumbent only | {status_counts['source-reported-contract-incumbent']} | Released result exists, but no independent exact-contract current record was located |",
        f"| Suite-level only | {status_counts['suite-level-only']} | ARC-AGI-3 and DiG-bench publish no attributable per-task result table |",
        "",
        "### Source-suite snapshot",
        "",
        "| Source | Launch | GitHub stars | Tasks here | Current best evidence |",
        "|---|---:|---:|---:|---|",
        f"| [SimpleTES](https://github.com/wq-will/SimpleTES) | 2026-04 | 169 | 28 | 28 source-reported results; {externally_checked} tasks cross-checked against other systems or records |",
        "| [ARC-AGI-3](https://arcprize.org/arc-agi/3/) | 2026-04-22 | 69 | 3 | Tycho 100.0% public-demo aggregate; community self-reported, no attributable per-game table |",
        "| [DiG-bench](https://digbench.ai/) | 2026-08-12 | 24 | 21 | Claude Opus 5 basic harness: 50/70 games; no per-game table |",
        "",
        f"GitHub stars are the repository snapshots recorded on {AS_OF}; they are popularity metadata, not quality or SOTA evidence.",
        "",
        "## Master SOTA index",
        "",
        "| # | Task | Domain | Source | Metric | Current record located | Evidence |",
        "|---:|---|---|---|---|---|---|",
    ]

    for index, task in enumerate(registry["tasks"], 1):
        record = records[task["id"]]
        metric = task["metric"]
        direction = "↓" if metric["direction"] == "minimize" else "↑"
        status = evidence_label(record)
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
                f"- **Source-suite reported result:** {source_reported_text(record)}",
                f"- **Current record located:** {score_text(record)}",
                f"- **Evidence status:** `{record['evidence_status']}` as of {record['as_of']}",
                f"- **Primary evidence:** {evidence}",
                f"- **Record note:** {record['notes']}",
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
            "For a new record, provide the exact task/version, complete system and harness, score, run count or uncertainty when available, resource envelope, and primary result artifact. A source paper claim or suite leaderboard screenshot alone is insufficient for a task-level SOTA claim.",
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
