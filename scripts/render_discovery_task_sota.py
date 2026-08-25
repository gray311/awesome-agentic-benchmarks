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
README_PATH = ROOT / "README.md"
TTT_TASK_PATH = ROOT / "data" / "ttt-discover-tasks.json"
FINCH_TASK_PATH = ROOT / "data" / "finch-collection-tasks.json"
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
        "method": "AlphaEvolve (live-board tie)",
        "model": "Not disclosed for leaderboard row",
        "primary_result_url": EINSTEIN_CIRCLE,
        "evidence_status": "official-live-leaderboard",
        "evidence_urls": [EINSTEIN_CIRCLE, ALPHAEVOLVE_PAPER, SIMPLETES_PAPER, MLEVOLVE],
        "notes": "EinsteinArena lists AlphaEvolve first at 2.6359830849, with several agents tied at displayed precision. SimpleTES reports 2.635983 and MLEvolve 2.6359830395; neither should be presented as the unique current record.",
    },
    "circle-packing-n32": {
        "status": "tie-at-published-precision", "scope": "task-level",
        "system": "nanodiscover + Qwen3-8B / Finch-8B (EFT), tied at published precision", "score": 2.939573,
        "method": "nanodiscover (EFT)",
        "model": "Qwen3-8B / Finch-8B",
        "primary_result_url": EFT_PAPER,
        "evidence_status": "cross-paper-tie-at-published-precision",
        "evidence_urls": [EFT_PAPER, SIMPLETES_PAPER, ALPHAEVOLVE_PAPER],
        "notes": "EFT Table 6 reports 2.939573 for both nanodiscover + Qwen3-8B and nanodiscover + Finch-8B, above the 2.939572 SimpleTES source result at displayed precision. The two 2.939573 entries are tied only at published precision; full-precision artifacts are needed to order them.",
    },
    "erdos-minimum-overlap": {
        "status": "live-leaderboard-best", "scope": "task-level",
        "system": "CodexProLong", "score": 0.38085857,
        "method": "CodexProLong",
        "model": "Not disclosed by leaderboard",
        "primary_result_url": EINSTEIN_ERDOS,
        "evidence_status": "official-live-leaderboard-with-certification-caveat",
        "evidence_urls": [EINSTEIN_ERDOS, ERDOS_CERTIFICATION, TTT_DISCOVER, SIMPLETES_PAPER],
        "notes": "EinsteinArena's live leader is CodexProLong. The independent certification note verifies a slightly older 0.3808590566148069 construction and explains why a widely cited lower SimpleTES number was affected by normalization; leaderboard rank and rigorous certification are therefore reported separately.",
    },
    "hadamard-determinant-n29": {
        "status": "tie-at-published-precision", "scope": "task-level",
        "system": "Orrick et al. human record (matched by SimpleTES)", "score": 0.935673,
        "method": "Orrick et al. construction; matched by SimpleTES",
        "model": "Human construction / gpt-oss-120b match",
        "primary_result_url": HADAMARD_29,
        "evidence_status": "historical-record-matched-by-agent",
        "evidence_urls": [HADAMARD_29, SIMPLETES_PAPER],
        "notes": "The order-29 construction predates SimpleTES. SimpleTES matches the normalized determinant at published precision; it did not originate the record.",
    },
    "scaling-law-domain-mix": {
        "status": "artifact-reported-best", "scope": "task-level",
        "system": "SLDAgent + Gemini-3-Pro-Preview", "score": 0.993529,
        "method": "SLDAgent",
        "model": "Gemini-3-Pro-Preview",
        "primary_result_url": SLD_RESULTS,
        "evidence_status": "official-results-dataset",
        "evidence_urls": [SLD_RESULTS, SLD_CODE, SIMPLETES_PAPER],
        "notes": "Computed from the released SLDBench result records for the domain_mixture split. It exceeds the 0.991 SimpleTES source result under the matched split metric.",
    },
    "scaling-law-lr-bsz": {
        "status": "artifact-reported-best", "scope": "task-level",
        "system": "SLDAgent + GPT-5", "score": 0.847918,
        "method": "SLDAgent",
        "model": "GPT-5",
        "primary_result_url": SLD_RESULTS,
        "evidence_status": "official-results-dataset",
        "evidence_urls": [SLD_RESULTS, SLD_CODE, SIMPLETES_PAPER],
        "notes": "Computed from the released SLDBench result records for the lr_bsz split. It exceeds the 0.712 SimpleTES source result.",
    },
    "scaling-law-parallel": {
        "status": "precision-ambiguous", "scope": "task-level", "system": None, "score": None,
        "method": "Unresolved: SLDAgent vs SimpleTES",
        "model": "Claude Sonnet 4.5 / gpt-oss-120b",
        "primary_result_url": SLD_RESULTS,
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
        "method": "Aider",
        "model": "GPT-5",
        "primary_result_url": SLD_RESULTS,
        "evidence_status": "official-results-dataset",
        "evidence_urls": [SLD_RESULTS, SLD_CODE, SIMPLETES_PAPER],
        "notes": "Computed from the released SLDBench easy_question/u-shape result records. It exceeds the -0.008 SimpleTES source result.",
    },
    "second-autocorrelation-inequality": {
        "status": "live-leaderboard-best", "scope": "task-level",
        "system": "ClaudeExplorer", "score": 0.96359,
        "method": "ClaudeExplorer",
        "model": "Not disclosed by leaderboard",
        "primary_result_url": EINSTEIN_AC2,
        "evidence_status": "official-live-leaderboard",
        "evidence_urls": [EINSTEIN_AC2, TTT_DISCOVER, SIMPLETES_PAPER, MLEVOLVE],
        "notes": "EinsteinArena currently ranks ClaudeExplorer first. The board also records AlphaEvolve and TTT-Discover as earlier results; SimpleTES's 0.962694 is no longer the public leader.",
    },
    "sum-difference-problem": {
        "status": "artifact-reported-best", "scope": "task-level",
        "system": "MLEvolve", "score": 1.1901774219,
        "method": "MLEvolve",
        "model": "Gemini-3.1-Pro-preview",
        "primary_result_url": MLEVOLVE,
        "evidence_status": "source-reported-matched-task-table",
        "evidence_urls": [MLEVOLVE, ALPHAEVOLVE_PAPER, SIMPLETES_PAPER],
        "notes": "MLEvolve's official comparison table reports 1.1901774219 on Sums differences problem 1, above AlphaEvolve (1.1479889651) and SimpleTES (1.143975 in that table; 1.144887 in the later post-trained SimpleTES result).",
    },
    "third-autocorrelation-inequality": {
        "status": "live-leaderboard-best", "scope": "task-level",
        "system": "Poolish", "score": 1.45080664,
        "method": "Poolish",
        "model": "Not disclosed by leaderboard",
        "primary_result_url": EINSTEIN_AC3,
        "evidence_status": "official-live-leaderboard",
        "evidence_urls": [EINSTEIN_AC3, SIMPLETES_PAPER, MLEVOLVE],
        "notes": "EinsteinArena currently ranks Poolish first. SimpleTES's 1.453675 is a historical source result, not the current live record.",
    },
    "trimul-kernel": {
        "status": "artifact-reported-best", "scope": "task-level",
        "system": "K-Search", "score": 1.028,
        "method": "K-Search",
        "model": "GPT-5.2 (released GPUMode default)",
        "primary_result_url": KSEARCH,
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
                "method": "SimpleTES (source incumbent; global SOTA unverified)",
                "model": "gpt-oss-120b",
                "primary_result_url": SIMPLETES_PAPER,
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
                    "method": "No per-task SOTA published (suite aggregate: Tycho)",
                    "model": "Not disclosed",
                    "primary_result_url": ARC_BOARD,
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
                    "method": "No per-task SOTA published (suite aggregate: basic harness)",
                    "model": "Claude Opus 5",
                    "primary_result_url": DIG_PAPER,
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


def result_cell(record: dict) -> str:
    """Render only the result/status, keeping method and model in separate columns."""
    direction = "↓" if record["metric"]["direction"] == "minimize" else "↑"
    if record["status"] in {"live-leaderboard-best", "artifact-reported-best", "tie-at-published-precision"}:
        qualifier = "tie" if record["status"] == "tie-at-published-precision" else "current record"
        return f"{number_text(record['score'])} {direction} ({qualifier})"
    if record["status"] == "precision-ambiguous":
        candidates = " vs ".join(number_text(item["score"]) for item in record["candidates"])
        return f"Unresolved at published precision ({candidates})"
    if record["status"] == "source-reported-contract-incumbent":
        source = record["source_reported"]
        return f"{number_text(source['score'])} {direction} (source incumbent; SOTA unverified)"
    best = record["suite_best"]
    return f"No per-task result; suite {number_text(best['score'])} {best['unit']}"


def source_reported_text(record: dict) -> str:
    source = record.get("source_reported")
    if source is None:
        return "Not available as a task-level result"
    direction = "↓" if record["metric"]["direction"] == "minimize" else "↑"
    return f"{source['system']}: {number_text(source['score'])} {direction}"


def cell(value: object) -> str:
    """Render a compact Markdown-table cell without changing source data."""
    return str(value).replace("|", "\\|").replace("\n", " ")


def sota_table_lines(registry: dict, sota: dict, *, readme: bool = False) -> list[str]:
    """Build the task-first SOTA table shared by README and the detailed reference."""
    records = {record["task_id"]: record for record in sota["records"]}
    lines = [
        "| # | Discovery task | Domain | Source | SOTA method / status | Model / backbone | Result | Link |",
        "|---:|---|---|---|---|---|---|---|",
    ]
    for index, task in enumerate(registry["tasks"], 1):
        record = records[task["id"]]
        anchor = f"docs/all-discovery-tasks.md#{task['id']}" if readme else f"#{task['id']}"
        lines.append(
            f"| {index} | [{cell(task['name'])}]({anchor}) | {cell(task['domain'])} | "
            f"{SUITE_LABELS[task['source_suite']]} | {cell(record['method'])} | {cell(record['model'])} | "
            f"{cell(result_cell(record))} | [evidence]({record['primary_result_url']}) |"
        )
    return lines


README_TABLE_START = "<!-- DISCOVERY_SOTA_TABLE:START -->"
README_TABLE_END = "<!-- DISCOVERY_SOTA_TABLE:END -->"


def render_readme(readme: str, registry: dict, sota: dict) -> str:
    """Replace only the generated README table, preserving every hand-written section."""
    if README_TABLE_START not in readme or README_TABLE_END not in readme:
        raise ValueError("README discovery SOTA table markers are missing")
    before, remainder = readme.split(README_TABLE_START, 1)
    _, after = remainder.split(README_TABLE_END, 1)
    generated = "\n".join(sota_table_lines(registry, sota, readme=True))
    return f"{before}{README_TABLE_START}\n{generated}\n{README_TABLE_END}{after}"


def ttt_record_fields(task: dict, ttt: dict) -> tuple[str, str, str, str]:
    """Separate method, model, result, and evidence for a TTT-Discover task variant."""
    record = task["current_record"]
    system = record.get("system")
    url = record.get("url", ttt["project_page"])
    direction = "↓" if task["metric"]["direction"] == "minimize" else "↑"
    if system is None:
        return (
            "TTT-Discover (source result; later SOTA unverified)",
            ttt["model"],
            f"{task['ttt_discover_result']} {direction} (source result)",
            url,
        )
    model = {
        "K-Search": "GPT-5.2 (released GPUMode default)",
        "TTT-Discover": ttt["model"],
        "TTT-Discover / SimpleTES": "gpt-oss-120b",
        "SimpleTES": "gpt-oss-120b",
    }.get(system, "Not disclosed by leaderboard")
    return system, model, f"{record['score']} {direction} ({record['status']})", url


def render_collection_catalogue(ttt: dict, finch: dict) -> list[str]:
    lines = [
        "## Complete TTT-Discover and Finch task catalogues",
        "",
        f"> **{len(ttt['tasks'])} TTT-Discover published task variants** + "
        f"**{len(finch['tasks'])} current Finch Collection task IDs**. These are catalogue entries, not "
        "additional unique benchmark claims: TTT-Discover is an evaluated system, and Finch is a trajectory "
        "collection assembled from upstream benchmarks.",
        "",
        "This section repairs an earlier source bias: TTT-Discover and Finch were previously shown only as "
        "comparison systems on a few SimpleTES rows. Their own published/evolving task sets are now enumerated.",
        "",
        "### TTT-Discover: every published attempted task",
        "",
        f"Launch: **{ttt['launch_date']}** · repository stars: **{ttt['repository_stars']['count']}** "
        f"(snapshot {ttt['repository_stars']['as_of']}) · model: **{ttt['model']}** · "
        f"[paper]({ttt['paper']}) · [code]({ttt['repository']}) · [project page]({ttt['project_page']})",
        "",
        "The paper says it reports every attempted problem. Hardware- and dataset-specific evaluator contracts "
        "are kept as separate variants, giving 3 mathematics + 4 TriMul hardware + 2 AtCoder + 2 biology = 11.",
        "",
        "| # | Task | Domain | SOTA method / status | Model / backbone | Result | Link |",
        "|---:|---|---|---|---|---|---|",
    ]
    for index, task in enumerate(ttt["tasks"], 1):
        method, model, result, url = ttt_record_fields(task, ttt)
        lines.append(
            f"| {index} | [{cell(task['name'])}](#{task['id']}) | {cell(task['domain'])} | "
            f"{cell(method)} | {cell(model)} | {cell(result)} | [evidence]({url}) |"
        )

    lines.extend(["", "#### TTT-Discover task contracts", ""])
    for task in ttt["tasks"]:
        metric = task["metric"]
        direction = "minimize ↓" if metric["direction"] == "minimize" else "maximize ↑"
        method, model, result, url = ttt_record_fields(task, ttt)
        lines.extend(
            [
                f"<a id=\"{task['id']}\"></a>",
                "",
                f"##### {task['name']}",
                "",
                f"- **Question:** {task['question']}",
                f"- **Agent input:** {task['input']}",
                f"- **Required output:** {task['output']}",
                f"- **Evaluation:** {task['evaluation']}",
                f"- **Environment:** {task['environment']}",
                f"- **Metric:** {metric['name']} · {direction} · {metric['unit']}",
                f"- **TTT-Discover result:** {task['ttt_discover_result']}",
                f"- **Current SOTA method / status:** {method}",
                f"- **Model / backbone:** {model}",
                f"- **Current result:** {result}",
                f"- **Primary evidence:** [result source]({url})",
                f"- **Current-record status:** `{task['current_record']['status']}` as of {task['current_record']['as_of']}",
                "",
            ]
        )

    lines.extend(
        [
            "### Finch Collection: current 442-task dataset snapshot",
            "",
            f"Paper launch: **{finch['paper_launch_date']}** · repository stars: "
            f"**{finch['repository_stars']['count']}** (snapshot {finch['repository_stars']['as_of']}) · "
            f"[paper]({finch['paper']}) · [code]({finch['repository']}) · [dataset]({finch['dataset']})",
            "",
            f"The paper freezes **{finch['paper_task_count']} tasks / {finch['paper_trajectory_count']:,} trajectories**. "
            f"The official dataset card and scanned Parquet revision now contain **{finch['current_task_count']} tasks / "
            f"{finch['current_trajectory_count']:,} trajectories**. {finch['version_note']}",
            "",
            "Finch is not itself the evaluator or the current SOTA for every row. Each task retains its upstream "
            "benchmark/evaluator; `current_dataset_rows` is trajectory coverage, not a score.",
            "Because the released collection has no 442-row SOTA/model table, every Finch row below says so explicitly "
            "and links to the dataset provenance instead of guessing a winner from trajectory logs.",
            "",
            "#### Group counts and evaluator contracts",
            "",
            "| Task group | Paper v1 | Current dataset | Agent question / evaluation contract |",
            "|---|---:|---:|---|",
        ]
    )
    for domain in finch["current_group_counts"]:
        contract = finch["domain_contracts"][domain]
        lines.append(
            f"| {cell(domain)} | {finch['paper_group_counts'][domain]} | "
            f"{finch['current_group_counts'][domain]} | {cell(contract['question'])} "
            f"Evaluator: {cell(contract['evaluation'])} |"
        )

    lines.extend(
        [
            "",
            "#### All current Finch task IDs",
            "",
            "Membership labels distinguish IDs explicitly recoverable from arXiv v1 from the expanded dataset. "
            "`unresolved-paper-v1-or-expansion` is deliberate: the paper says 47 numerical tasks but prints 46 IDs, "
            "while the current dataset has 65 additional numerical IDs. One is the omitted paper seed and 64 are "
            "post-paper additions; no public artifact identifies which one.",
            "",
        ]
    )
    current_domain = None
    running = 0
    for task in finch["tasks"]:
        if task["domain"] != current_domain:
            current_domain = task["domain"]
            contract = finch["domain_contracts"][current_domain]
            lines.extend(
                [
                    f"##### {current_domain}",
                    "",
                    f"- **Question:** {contract['question']}",
                    f"- **Input:** {contract['input']}",
                    f"- **Output:** {contract['output']}",
                    f"- **Evaluation:** {contract['evaluation']}",
                    f"- **Environment:** {contract['environment']}",
                    f"- **Metric family:** {contract['metric']}",
                    "",
                    "| # | Task ID | Upstream source | Paper/expansion status | Trajectories | SOTA method / status | Model | Link | Published description |",
                    "|---:|---|---|---|---:|---|---|---|---|",
                ]
            )
        running += 1
        description = task.get("paper_description", "No per-task description in arXiv v1; use the upstream evaluator artifact.")
        lines.append(
            f"| {running} | `{cell(task['task'])}` | {cell(task['upstream_benchmark'])} | "
            f"`{task['paper_371_membership']}` | {task['current_dataset_rows']} | "
            f"Not published per task in Finch; consult upstream evaluator | — | "
            f"[Finch provenance]({finch['dataset']}) | {cell(description)} |"
        )
        if running == len(finch["tasks"]) or finch["tasks"][running]["domain"] != current_domain:
            lines.append("")
    return lines


def render_doc(registry: dict, sota: dict, ttt: dict, finch: dict) -> str:
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
        f"> Evidence snapshot: **{AS_OF}** · **{len(registry['tasks'])} full-contract registry tasks** · "
        f"**{len(ttt['tasks'])} TTT-Discover variants** · **{len(finch['tasks'])} current Finch task IDs**",
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
    ]
    lines.extend(sota_table_lines(registry, sota))

    lines.extend([""] + render_collection_catalogue(ttt, finch) + ["", "## Full task contracts", ""])
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
                f"- **Current SOTA method / status:** {record['method']}",
                f"- **Model / backbone:** {record['model']}",
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
    ttt = json.loads(TTT_TASK_PATH.read_text(encoding="utf-8"))
    finch = json.loads(FINCH_TASK_PATH.read_text(encoding="utf-8"))
    sota = build_sota(registry)
    readme = README_PATH.read_text(encoding="utf-8")
    expected = {
        SOTA_PATH: serialize_sota(sota),
        DOC_PATH: render_doc(registry, sota, ttt, finch),
        README_PATH: render_readme(readme, registry, sota),
    }

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
