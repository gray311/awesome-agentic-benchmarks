#!/usr/bin/env python3
"""Validate the complete TTT-Discover and Finch task catalogues."""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TTT_PATH = ROOT / "data" / "ttt-discover-tasks.json"
FINCH_PATH = ROOT / "data" / "finch-collection-tasks.json"


def main() -> int:
    errors: list[str] = []
    ttt = json.loads(TTT_PATH.read_text(encoding="utf-8"))
    finch = json.loads(FINCH_PATH.read_text(encoding="utf-8"))

    ttt_tasks = ttt.get("tasks", [])
    if len(ttt_tasks) != 11:
        errors.append(f"TTT-Discover must contain 11 published variants, found {len(ttt_tasks)}")
    if len({task.get("id") for task in ttt_tasks}) != len(ttt_tasks):
        errors.append("TTT-Discover task IDs must be unique")
    required_ttt = {
        "id", "name", "domain", "question", "input", "output", "evaluation",
        "environment", "metric", "ttt_discover_result", "current_record",
    }
    for index, task in enumerate(ttt_tasks):
        missing = required_ttt - task.keys()
        if missing:
            errors.append(f"TTT task {index} missing fields: {sorted(missing)}")
        metric = task.get("metric", {})
        if metric.get("direction") not in {"minimize", "maximize"}:
            errors.append(f"{task.get('id')}: invalid metric direction")
        record = task.get("current_record", {})
        if record.get("as_of") != ttt.get("snapshot_date"):
            errors.append(f"{task.get('id')}: current-record date must match snapshot date")

    finch_tasks = finch.get("tasks", [])
    if len(finch_tasks) != finch.get("current_task_count") or len(finch_tasks) != 442:
        errors.append(f"Finch task count mismatch: {len(finch_tasks)}")
    if len({task.get("id") for task in finch_tasks}) != len(finch_tasks):
        errors.append("Finch catalogue IDs must be unique")
    domain_task_keys = {(task.get("domain"), task.get("task")) for task in finch_tasks}
    if len(domain_task_keys) != len(finch_tasks):
        errors.append("Finch domain/task pairs must be unique")
    row_total = sum(task.get("current_dataset_rows", 0) for task in finch_tasks)
    if row_total != finch.get("current_trajectory_count") or row_total != 217780:
        errors.append(f"Finch trajectory-row count mismatch: {row_total}")

    current_counts = Counter(task.get("domain") for task in finch_tasks)
    if dict(current_counts) != finch.get("current_group_counts"):
        errors.append("Finch current_group_counts do not match task rows")
    if sum(finch.get("paper_group_counts", {}).values()) != 371:
        errors.append("Finch paper group counts must sum to 371")
    if set(current_counts) != set(finch.get("paper_group_counts", {})):
        errors.append("Finch current and paper domain sets must match")
    if set(current_counts) != set(finch.get("domain_contracts", {})):
        errors.append("Every Finch domain must have one evaluation contract")

    membership_counts = Counter(task.get("paper_371_membership") for task in finch_tasks)
    if membership_counts["identified-in-arxiv-v1-appendix"] != 353:
        errors.append("Expected 353 task IDs in the rendered arXiv appendix tables")
    if membership_counts["paper-v1-seed-identified-by-official-manifest"] != 17:
        errors.append("Expected 14 Erdős + 3 biology seeds identified by the official manifest")
    if membership_counts["post-paper-442-expansion"] != 7:
        errors.append("Expected four math + three ALE tasks explicitly outside the paper group counts")
    if membership_counts["unresolved-paper-v1-or-expansion"] != 65:
        errors.append("Expected 65 numerical IDs spanning one omitted v1 seed and 64 additions")

    if errors:
        print(f"Discovery-collection validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        "Discovery collections are valid: 11 TTT-Discover variants and "
        "442 Finch task IDs / 217,780 trajectory rows."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
