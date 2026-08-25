# Discovery Task Registry

**Task evidence snapshot:** 2026-08-25

This is the primary discovery layer of the repository. The unit of collection is an **executable discovery task**, not the method or agent that attempted it. It now covers both fully specified artifact-optimization tasks and environments whose rules or objectives must be discovered through interaction.

> **Task:** “Find a lower-cost Cassini trajectory under this simulator and these constraints.”  
> **Not a task:** “Use SimpleTES to improve science.”

SimpleTES, TTT-Discover, SkyDiscover, AlphaEvolve, and other systems belong in provenance and result fields. They become a source suite only when they release reusable task instructions, starting artifacts, environments, and evaluators.

## Required task record

| Field | Meaning |
|---|---|
| **Question** | The scientific or engineering objective shown to the discovery agent. |
| **Input** | Data, seed program, constraints, visible examples, simulator state, and feedback channel. |
| **Output** | Program, construction, model, trajectory, kernel, policy, or other artifact being optimized. |
| **Evaluator** | How feasibility is checked and how the objective is recomputed. |
| **Environment** | Language, dependencies, data, simulator, hardware, timeout, and isolation policy. |
| **Metric** | Named quantity, units, direction, aggregation, and precision. |
| **Reference** | Previous method/system and score under the same task contract. |
| **Reported result** | Evaluated system, score, artifact version, and evidence source. |
| **Integrity** | Leakage, evaluator access, simulator mismatch, numerical precision, and reward-hacking risks. |

The machine-readable form is [data/discovery-tasks.json](../data/discovery-tasks.json), validated against [schema/discovery-task.schema.json](../schema/discovery-task.schema.json).

## Two discovery modes

| Mode | What is hidden | Example tasks |
|---|---|---|
| **Artifact optimization** | A better solution is unknown, but the objective and evaluator are specified | Cassini trajectory, GPU kernels, circle packing |
| **Interactive rule discovery** | The environment's dynamics, transformation rules, objective, or win condition | ARC-AGI-3 and DiG-bench games |

The second mode is documented in depth in [Interactive Discovery Tasks](interactive-discovery-tasks.md). A registry row may have no model result yet; that means the task contract is verified but a matched run has not been recorded.

## SimpleTES as a task source

[SimpleTES](https://github.com/wq-will/SimpleTES) is recorded as both:

1. a **source suite** that currently exposes 28 task packages; and
2. an **evaluated discovery system** that produced the reported candidate results.

The source reports `gpt-oss-20b` as the generator for the comparison summarized here. Matched runs using GPT, Claude, GLM, Kimi, and Qwen agents have not yet been recorded for these 28 task contracts; those cells should remain unknown rather than inferred from other benchmarks.

The shared task contract is concrete:

```text
instruction shown to the model
        +
editable seed program
        +
fixed executable evaluator
        ↓
candidate program or construction
        ↓
isolated subprocess → constraint validation → recomputed objective
```

According to the official [task catalogue](https://github.com/wq-will/SimpleTES/blob/main/datasets/README.md), the evaluator applies a timeout and memory cap, validates hard constraints, and recomputes the score rather than trusting a self-reported value. Each row below is therefore cataloged separately, even though the tasks were evaluated by one discovery framework.

## Interactive discovery task index

The suite inventories and private splits are larger than the list below. We itemize only public task IDs that can be verified from official sources: three anonymous ARC-AGI-3 games and all 21 public DiG-bench games.

| Discovery task | Modality | Metric | Registry status |
|---|---|---|---|
| **ARC-AGI-3 ls20 (Agent reasoning)** | Visual grid | RHAE ↑ | Public demo; per-game score pending |
| **ARC-AGI-3 ft09 (Elementary Logic)** | Visual grid | RHAE ↑ | Public demo; per-game score pending |
| **ARC-AGI-3 vc33 (Orchestration)** | Visual grid | RHAE ↑ | Public demo; per-game score pending |
| **DiG-bench P-1 (tier 1)** | Text/JSON | Win rate ↑ | Public task; score pending |
| **DiG-bench P-2 (tier 1)** | Text/JSON | Win rate ↑ | Public task; score pending |
| **DiG-bench P-3 (tier 1)** | Text/JSON | Win rate ↑ | Public task; score pending |
| **DiG-bench P-4 (tier 2)** | Text/JSON | Win rate ↑ | Public task; score pending |
| **DiG-bench P-5 (tier 2)** | Text/JSON | Win rate ↑ | Public task; score pending |
| **DiG-bench P-6 (tier 2)** | Text/JSON | Win rate ↑ | Public task; score pending |
| **DiG-bench P-7 (tier 3)** | Text/JSON | Win rate ↑ | Public task; score pending |
| **DiG-bench P-8 (tier 3)** | Text/JSON | Win rate ↑ | Public task; score pending |
| **DiG-bench P-9 (tier 3)** | Text/JSON | Win rate ↑ | Public task; score pending |
| **DiG-bench P-10 (tier 4)** | Text/JSON | Win rate ↑ | Public task; score pending |
| **DiG-bench P-11 (tier 4)** | Text/JSON | Win rate ↑ | Public task; score pending |
| **DiG-bench P-12 (tier 4)** | Text/JSON | Win rate ↑ | Public task; score pending |
| **DiG-bench P-13 (tier 5)** | Text/JSON | Win rate ↑ | Public task; score pending |
| **DiG-bench P-14 (tier 5)** | Text/JSON | Win rate ↑ | Public task; score pending |
| **DiG-bench P-15 (tier 5)** | Text/JSON | Win rate ↑ | Public task; score pending |
| **DiG-bench P-16 (tier 6)** | Text/JSON | Win rate ↑ | Public task; score pending |
| **DiG-bench P-17 (tier 6)** | Text/JSON | Win rate ↑ | Public task; score pending |
| **DiG-bench P-18 (tier 6)** | Text/JSON | Win rate ↑ | Public task; score pending |
| **DiG-bench P-19 (tier 7)** | Text/JSON | Win rate ↑ | Public task; score pending |
| **DiG-bench P-20 (tier 7)** | Text/JSON | Win rate ↑ | Public task; score pending |
| **DiG-bench P-21 (tier 7)** | Text/JSON | Win rate ↑ | Public task; score pending |

See the [interactive task guide](interactive-discovery-tasks.md) for input/action schemas, hidden information, budgets, evaluation formulas, official aggregate model scores, split restrictions, and the extraction queue.

## Task families: question, evaluator, and environment

| Domain | Task question pattern | Output | Evaluator | Environment |
|---|---|---|---|---|
| **Quantum compilation** | Minimize routing overhead or scheduled execution time subject to hardware constraints | Rust/Python compilation policy | Compile fixed circuits, validate legal operations, aggregate SWAP count or simulator time | Rust toolchain for superconducting routing; Python task environment for zoned neutral atoms |
| **Astrodynamics** | Minimize propulsive cost for a historical gravity-assist mission | Trajectory optimizer and feasible mission parameters | Validate mission constraints and recompute cost in the fixed simulator | Python, astrodynamics dependencies, and NAIF ephemeris kernels |
| **Scientific algorithms** | Improve runtime, forecasting error, or biological reconstruction quality | C++/Python scientific program and predictions | Correctness or held-out-data gate followed by runtime/error/composite score | C++/Eigen or task-specific Python environments; ZAPBench requires GPU and dataset |
| **AI foundations** | Optimize GPU kernels or infer extrapolating scaling laws | GPU kernel or scaling-law program | Correctness-gated profiling or held-out extrapolation R² | H100/H200 profiling server for kernels; Python and task data for scaling laws |
| **Mathematics discovery** | Find a feasible extremal or combinatorial construction | Function, sequence, set, matrix, or geometric construction | Recheck every hard constraint and recompute the objective | Python; most released tasks list no external setup |

## SimpleTES task-level results

Scores below reproduce the supplied comparison table and are labeled **source-reported**, not independently certified by this repository. `↓` means minimize and `↑` means maximize.

### Quantum compilation

| Discovery task | Metric | Reference | Reported SimpleTES | Outcome |
|---|---|---:|---:|---|
| **Superconducting qubit routing** | Added SWAPs ↓ | LightSABRE: 20,063 | 15,147 | Improved |
| **Zoned neutral-atom compilation** | Execution time ↓ | ZAC: 29,187.7 | 19,507.5 | Improved |

### Astrodynamics

| Discovery task | Metric | Reference | Reported SimpleTES | Outcome |
|---|---|---:|---:|---|
| **Mariner 10 gravity-assist trajectory** | Propulsive cost ↓ | Historical sequence: 0.424147 | 0.326993 | Improved |
| **Voyager 2 gravity-assist trajectory** | Propulsive cost ↓ | Historical sequence: 3.503798 | 3.430214 | Improved |
| **Galileo gravity-assist trajectory** | Propulsive cost ↓ | Historical sequence: 0.823681 | 0.795108 | Improved |
| **Cassini gravity-assist trajectory** | Propulsive cost ↓ | Historical sequence: 1.066682 | 0.820129 | Improved |
| **Rosetta gravity-assist trajectory** | Propulsive cost ↓ | Historical sequence: 1.736837 | 1.552968 | Improved |

### Scientific algorithms

| Discovery task | Metric | Reference | Reported SimpleTES | Outcome |
|---|---|---:|---:|---|
| **LASSO regularization path** | Runtime (ms) ↓ | glmnet: 4,139.4 | 2,502.3 | Improved |
| **ZAPBench whole-brain forecasting (H=1)** | Test MAE ↓ | ERA: 0.0174 | 0.0165 | Improved |
| **ZAPBench whole-brain forecasting (H=4)** | Test MAE ↓ | ERA: 0.0221 | 0.0211 | Improved |
| **ZAPBench whole-brain forecasting (H=8)** | Test MAE ↓ | ERA: 0.0244 | 0.0230 | Improved |
| **ZAPBench whole-brain forecasting (H=16)** | Test MAE ↓ | ERA: 0.0267 | 0.0251 | Improved |
| **ZAPBench whole-brain forecasting (H=32)** | Test MAE ↓ | ERA: 0.0283 | 0.0259 | Improved |
| **Single-cell RNA-seq denoising** | Denoising score ↑ | TTT-Discover: 0.73 | 0.74 | Improved |

### AI foundations

| Discovery task | Metric | Reference | Reported SimpleTES | Outcome |
|---|---|---:|---:|---|
| **TriMul GPU kernel** | Runtime (ms) ↓ | Human expert: 1.140 | 1.122 | Improved |
| **Asymmetric matrix multiplication** | Runtime (ms) ↓ | CUDAAgent: 0.747 | 0.440 | Improved |
| **Batched cumulative sum** | Runtime (ms) ↓ | NVIDIA CUB: 0.147 | 0.104 | Improved |
| **Scaling-law discovery: parallel** | Extrapolation R² ↑ | SLD Agent (GPT-5): 1.000 | 1.000 | Matched |
| **Scaling-law discovery: domain mix** | Extrapolation R² ↑ | SLD Agent (Gemini-2.5-Flash): 0.991 | 0.991 | Matched |
| **Scaling-law discovery: learning rate and batch size** | Extrapolation R² ↑ | SLD Agent (o4-mini): 0.611 | 0.712 | Improved |
| **Scaling-law discovery: U-shape** | Extrapolation R² ↑ | Goose + GPT-5: −0.232 | −0.008 | Improved |

### Mathematics discovery

| Discovery task | Metric | Reference | Reported SimpleTES | Outcome |
|---|---|---:|---:|---|
| **Erdős minimum overlap** | Overlap ↓ | Together AI: 0.380871 | 0.380868 | Reported improvement; certification caveat |
| **Second autocorrelation inequality** | Bound ↑ | Together AI: 0.961206 | 0.962694 | Improved |
| **Third autocorrelation inequality** | Bound ↓ | Together AI: 1.454555 | 1.453675 | Improved |
| **Sum-Difference problem** | Ratio ↑ | AlphaEvolve V2: 1.121936 | 1.143975 | Improved |
| **Circle packing in a unit square (n=26)** | Sum of radii ↑ | AlphaEvolve V2: 2.635983 | 2.635983 | Matched at shown precision |
| **Circle packing in a unit square (n=32)** | Sum of radii ↑ | AlphaEvolve V2: 2.939572 | 2.939572 | Matched at shown precision |
| **Hadamard maximum determinant (n=29)** | Normalized determinant ↑ | Orrick: 0.935673 | 0.935673 | Matched at shown precision |

## Integrity note: Erdős minimum overlap

The task is valuable, but the record claim illustrates why we store task artifacts and evaluator versions rather than only headline numbers. The supplied table reports `0.380868`, while other SimpleTES revisions discuss `0.380856`; subsequent independent work reported normalization and exact-feasibility concerns. The [Optimization Problems reference page](https://teorth.github.io/optimizationproblems/constants/1b.html) currently lists the SimpleTES bound as `0.380868`.

Until an artifact is replayed with exact feasibility and a frozen objective, this registry treats the number as **source-reported**, not independently certified.

## Where methods belong

| Name | Registry role | Why |
|---|---|---|
| **SimpleTES** | Source suite + evaluated system | Releases executable tasks and also reports results from its search method. |
| **TTT-Discover** | Evaluated system / task source when artifacts exist | Its `0.73` result is the reference for the single-cell task; the method itself is not a task. |
| **SkyDiscover** | Candidate source suite | Promote its individual problems only after extracting question, input, evaluator, environment, and artifacts. |
| **EFT** | Training method | Record as agent/training configuration attached to a task result, not as a benchmark or discovery task. |
| **AlphaEvolve / Together AI / CUDAAgent / SLD Agent** | Reference systems | Appear in result provenance for the tasks they attempted. |

## Next task-source extraction queue

The next expansion should extract individual executable problems—rather than add framework names—from:

- TTT-Discover;
- SkyDiscover;
- AlphaEvolve and AlphaEvolve V2;
- AI4AI-Bench's ten frozen training-algorithm repositories;
- NatureBench's scientific ML problem packages;
- AgentHPOBench's 30 ML optimization tasks; and
- EarthVerse's reproducible Earth-science events.

A task is promoted only when its objective, inputs, output artifact, evaluator, and environment can be identified from primary artifacts.
