# All Discovery Tasks and Current SOTA

> Evidence snapshot: **2026-08-25** · **52 tasks** · **3 source suites**

This is the single-file lookup for every task in the discovery registry. It records the agent-visible question and input, required output, evaluator, environment, metric, and the best result that could be traced to the exact task contract.

## SOTA policy

- **Task-level current best** means a result was located for that exact evaluator and task version. It may still be source-reported rather than independently reproduced.
- **Suite-level only** means the source publishes an aggregate but no attributable per-task result. The aggregate is shown as context and is never imputed to a task.
- Runtime results are hardware-sensitive; interactive results are harness-, budget-, game-version-, and run-count-sensitive.
- `Current` means best located from primary sources by the snapshot date, not a guarantee that an unpublished or incomparable result does not exist.

### Coverage

| Evidence scope | Tasks | Interpretation |
|---|---:|---|
| Task-level current best | 28 | SimpleTES result and released artifact located |
| Suite-level only | 24 | ARC-AGI-3 (3) and DiG-bench (21) publish no attributable per-task result table |

### Source-suite snapshot

| Source | Launch | GitHub stars | Tasks here | Current best evidence |
|---|---:|---:|---:|---|
| [SimpleTES](https://github.com/wq-will/SimpleTES) | 2026-04 | 169 | 28 | 28 task-level source-reported best results; current paper uses gpt-oss-120b |
| [ARC-AGI-3](https://arcprize.org/arc-agi/3/) | 2026-04-22 | 69 | 3 | Tycho 100.0% public-demo aggregate; community self-reported, no attributable per-game table |
| [DiG-bench](https://digbench.ai/) | 2026-08-12 | 24 | 21 | Claude Opus 5 basic harness: 50/70 games; no per-game table |

GitHub stars are the repository snapshots recorded on 2026-08-25; they are popularity metadata, not quality or SOTA evidence.

## Master SOTA index

| # | Task | Domain | Source | Metric | Current SOTA | Evidence |
|---:|---|---|---|---|---|---|
| 1 | [Asymmetric matrix multiplication](#asymmetric-matrix-multiplication) | ai-foundations | SimpleTES | runtime (↓) | **0.44 ↓** — SimpleTES + gpt-oss-120b | task-level, source-reported |
| 2 | [Batched cumulative sum](#batched-cumulative-sum) | ai-foundations | SimpleTES | runtime (↓) | **0.104 ↓** — SimpleTES + gpt-oss-120b | task-level, source-reported |
| 3 | [Cassini gravity-assist trajectory](#cassini-trajectory) | astrodynamics | SimpleTES | propulsive cost (↓) | **0.820129 ↓** — SimpleTES + gpt-oss-120b | task-level, source-reported |
| 4 | [Circle packing in a unit square (n=26)](#circle-packing-n26) | mathematics-discovery | SimpleTES | sum of radii (↑) | **2.635983 ↑** — SimpleTES + gpt-oss-120b | task-level, source-reported |
| 5 | [Circle packing in a unit square (n=32)](#circle-packing-n32) | mathematics-discovery | SimpleTES | sum of radii (↑) | **2.939572 ↑** — SimpleTES + gpt-oss-120b | task-level, source-reported |
| 6 | [Erdős minimum overlap](#erdos-minimum-overlap) | mathematics-discovery | SimpleTES | overlap (↓) | **0.380868 ↓** — SimpleTES + gpt-oss-120b | task-level, source-reported |
| 7 | [Galileo gravity-assist trajectory](#galileo-trajectory) | astrodynamics | SimpleTES | propulsive cost (↓) | **0.795108 ↓** — SimpleTES + gpt-oss-120b | task-level, source-reported |
| 8 | [Hadamard maximum determinant (n=29)](#hadamard-determinant-n29) | mathematics-discovery | SimpleTES | normalized determinant (↑) | **0.935673 ↑** — SimpleTES + gpt-oss-120b | task-level, source-reported |
| 9 | [LASSO regularization path](#lasso-regularization-path) | scientific-algorithms | SimpleTES | runtime (↓) | **2502.3 ↓** — SimpleTES + gpt-oss-120b | task-level, source-reported |
| 10 | [Mariner 10 gravity-assist trajectory](#mariner-10-trajectory) | astrodynamics | SimpleTES | propulsive cost (↓) | **0.326993 ↓** — SimpleTES + gpt-oss-120b | task-level, source-reported |
| 11 | [Rosetta gravity-assist trajectory](#rosetta-trajectory) | astrodynamics | SimpleTES | propulsive cost (↓) | **1.552968 ↓** — SimpleTES + gpt-oss-120b | task-level, source-reported |
| 12 | [Scaling-law discovery: domain mix](#scaling-law-domain-mix) | ai-foundations | SimpleTES | extrapolation R2 (↑) | **0.991 ↑** — SimpleTES + gpt-oss-120b | task-level, source-reported |
| 13 | [Scaling-law discovery: learning rate and batch size](#scaling-law-lr-bsz) | ai-foundations | SimpleTES | extrapolation R2 (↑) | **0.712 ↑** — SimpleTES + gpt-oss-120b | task-level, source-reported |
| 14 | [Scaling-law discovery: parallel](#scaling-law-parallel) | ai-foundations | SimpleTES | extrapolation R2 (↑) | **1.0 ↑** — SimpleTES + gpt-oss-120b | task-level, source-reported |
| 15 | [Scaling-law discovery: U-shape](#scaling-law-u-shape) | ai-foundations | SimpleTES | extrapolation R2 (↑) | **-0.008 ↑** — SimpleTES + gpt-oss-120b | task-level, source-reported |
| 16 | [Second autocorrelation inequality](#second-autocorrelation-inequality) | mathematics-discovery | SimpleTES | bound (↑) | **0.962694 ↑** — SimpleTES + gpt-oss-120b | task-level, source-reported |
| 17 | [Single-cell RNA-seq denoising](#single-cell-rna-denoising) | scientific-algorithms | SimpleTES | denoising score (↑) | **0.74 ↑** — SimpleTES + gpt-oss-120b | task-level, source-reported |
| 18 | [Sum-Difference problem](#sum-difference-problem) | mathematics-discovery | SimpleTES | ratio (↑) | **1.144887 ↑** — SimpleTES + trajectory-level post-trained gpt-oss-120b | task-level, source-reported |
| 19 | [Superconducting qubit routing](#superconducting-qubit-routing) | quantum-compilation | SimpleTES | added SWAPs (↓) | **15147 ↓** — SimpleTES + gpt-oss-120b | task-level, source-reported |
| 20 | [Third autocorrelation inequality](#third-autocorrelation-inequality) | mathematics-discovery | SimpleTES | bound (↓) | **1.453675 ↓** — SimpleTES + gpt-oss-120b | task-level, source-reported |
| 21 | [TriMul GPU kernel](#trimul-kernel) | ai-foundations | SimpleTES | runtime (↓) | **1.122 ↓** — SimpleTES + gpt-oss-120b | task-level, source-reported |
| 22 | [Voyager 2 gravity-assist trajectory](#voyager-2-trajectory) | astrodynamics | SimpleTES | propulsive cost (↓) | **3.430214 ↓** — SimpleTES + gpt-oss-120b | task-level, source-reported |
| 23 | [ZAPBench whole-brain forecasting (H=1)](#zapbench-h1) | scientific-algorithms | SimpleTES | test MAE (↓) | **0.0165 ↓** — SimpleTES + gpt-oss-120b | task-level, source-reported |
| 24 | [ZAPBench whole-brain forecasting (H=4)](#zapbench-h4) | scientific-algorithms | SimpleTES | test MAE (↓) | **0.0211 ↓** — SimpleTES + gpt-oss-120b | task-level, source-reported |
| 25 | [ZAPBench whole-brain forecasting (H=8)](#zapbench-h8) | scientific-algorithms | SimpleTES | test MAE (↓) | **0.023 ↓** — SimpleTES + gpt-oss-120b | task-level, source-reported |
| 26 | [ZAPBench whole-brain forecasting (H=16)](#zapbench-h16) | scientific-algorithms | SimpleTES | test MAE (↓) | **0.0251 ↓** — SimpleTES + gpt-oss-120b | task-level, source-reported |
| 27 | [ZAPBench whole-brain forecasting (H=32)](#zapbench-h32) | scientific-algorithms | SimpleTES | test MAE (↓) | **0.0259 ↓** — SimpleTES + gpt-oss-120b | task-level, source-reported |
| 28 | [Zoned neutral-atom compilation](#zoned-neutral-atom-compilation) | quantum-compilation | SimpleTES | execution time (↓) | **19507.5 ↓** — SimpleTES + gpt-oss-120b | task-level, source-reported |
| 29 | [ARC-AGI-3 ls20 (Agent reasoning)](#arc-agi-3-ls20) | interactive-world-discovery | ARC-AGI-3 | Relative Human Action Efficiency (RHAE) (↑) | **Not published per task** — suite best: Tycho, 100.0 percent | suite-level only |
| 30 | [ARC-AGI-3 ft09 (Elementary Logic)](#arc-agi-3-ft09) | interactive-world-discovery | ARC-AGI-3 | Relative Human Action Efficiency (RHAE) (↑) | **Not published per task** — suite best: Tycho, 100.0 percent | suite-level only |
| 31 | [ARC-AGI-3 vc33 (Orchestration)](#arc-agi-3-vc33) | interactive-world-discovery | ARC-AGI-3 | Relative Human Action Efficiency (RHAE) (↑) | **Not published per task** — suite best: Tycho, 100.0 percent | suite-level only |
| 32 | [DiG-bench P-1 (tier 1)](#dig-bench-p-1) | interactive-world-discovery | DiG-bench | win rate (↑) | **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70 | suite-level only |
| 33 | [DiG-bench P-2 (tier 1)](#dig-bench-p-2) | interactive-world-discovery | DiG-bench | win rate (↑) | **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70 | suite-level only |
| 34 | [DiG-bench P-3 (tier 1)](#dig-bench-p-3) | interactive-world-discovery | DiG-bench | win rate (↑) | **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70 | suite-level only |
| 35 | [DiG-bench P-4 (tier 2)](#dig-bench-p-4) | interactive-world-discovery | DiG-bench | win rate (↑) | **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70 | suite-level only |
| 36 | [DiG-bench P-5 (tier 2)](#dig-bench-p-5) | interactive-world-discovery | DiG-bench | win rate (↑) | **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70 | suite-level only |
| 37 | [DiG-bench P-6 (tier 2)](#dig-bench-p-6) | interactive-world-discovery | DiG-bench | win rate (↑) | **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70 | suite-level only |
| 38 | [DiG-bench P-7 (tier 3)](#dig-bench-p-7) | interactive-world-discovery | DiG-bench | win rate (↑) | **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70 | suite-level only |
| 39 | [DiG-bench P-8 (tier 3)](#dig-bench-p-8) | interactive-world-discovery | DiG-bench | win rate (↑) | **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70 | suite-level only |
| 40 | [DiG-bench P-9 (tier 3)](#dig-bench-p-9) | interactive-world-discovery | DiG-bench | win rate (↑) | **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70 | suite-level only |
| 41 | [DiG-bench P-10 (tier 4)](#dig-bench-p-10) | interactive-world-discovery | DiG-bench | win rate (↑) | **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70 | suite-level only |
| 42 | [DiG-bench P-11 (tier 4)](#dig-bench-p-11) | interactive-world-discovery | DiG-bench | win rate (↑) | **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70 | suite-level only |
| 43 | [DiG-bench P-12 (tier 4)](#dig-bench-p-12) | interactive-world-discovery | DiG-bench | win rate (↑) | **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70 | suite-level only |
| 44 | [DiG-bench P-13 (tier 5)](#dig-bench-p-13) | interactive-world-discovery | DiG-bench | win rate (↑) | **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70 | suite-level only |
| 45 | [DiG-bench P-14 (tier 5)](#dig-bench-p-14) | interactive-world-discovery | DiG-bench | win rate (↑) | **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70 | suite-level only |
| 46 | [DiG-bench P-15 (tier 5)](#dig-bench-p-15) | interactive-world-discovery | DiG-bench | win rate (↑) | **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70 | suite-level only |
| 47 | [DiG-bench P-16 (tier 6)](#dig-bench-p-16) | interactive-world-discovery | DiG-bench | win rate (↑) | **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70 | suite-level only |
| 48 | [DiG-bench P-17 (tier 6)](#dig-bench-p-17) | interactive-world-discovery | DiG-bench | win rate (↑) | **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70 | suite-level only |
| 49 | [DiG-bench P-18 (tier 6)](#dig-bench-p-18) | interactive-world-discovery | DiG-bench | win rate (↑) | **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70 | suite-level only |
| 50 | [DiG-bench P-19 (tier 7)](#dig-bench-p-19) | interactive-world-discovery | DiG-bench | win rate (↑) | **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70 | suite-level only |
| 51 | [DiG-bench P-20 (tier 7)](#dig-bench-p-20) | interactive-world-discovery | DiG-bench | win rate (↑) | **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70 | suite-level only |
| 52 | [DiG-bench P-21 (tier 7)](#dig-bench-p-21) | interactive-world-discovery | DiG-bench | win rate (↑) | **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70 | suite-level only |

## Full task contracts

## Ai Foundations

<a id="asymmetric-matrix-multiplication"></a>

### Asymmetric matrix multiplication

- **ID / source:** `asymmetric-matrix-multiplication` · SimpleTES
- **Question:** Implement a faster asymmetric matrix-multiplication GPU kernel without changing numerical semantics.
- **Agent input:** A seed Triton/CUDA kernel, fixed tensor shapes and dtypes, correctness tests, and a profiling harness.
- **Required output:** GPU kernel source
- **Evaluation:** Correctness-gated execution followed by runtime profiling on the fixed benchmark workload.
- **Environment:** Triton/CUDA with a GPU profiling server; headline result uses H200.
- **Metric:** runtime · minimize ↓ · ms
- **Prior reference:** CUDAAgent: 0.747
- **Current SOTA:** **0.44 ↓** — SimpleTES + gpt-oss-120b
- **Evidence status:** `source-reported-current-best` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **SOTA note:** Best result located under the released task evaluator. This is a source-reported record, not an independent global certification.
- **Integrity note:** Runtime depends on hardware and profiler configuration; scores are source-reported and require matched-device replay.

<a id="batched-cumulative-sum"></a>

### Batched cumulative sum

- **ID / source:** `batched-cumulative-sum` · SimpleTES
- **Question:** Implement a faster batched prefix-sum GPU kernel while preserving output correctness.
- **Agent input:** A seed GPU kernel, fixed tensors, correctness tests, and a profiling harness.
- **Required output:** GPU kernel source
- **Evaluation:** Correctness-gated execution followed by runtime profiling on the fixed benchmark workload.
- **Environment:** Triton/CUDA with a GPU profiling server; headline result uses H200.
- **Metric:** runtime · minimize ↓ · ms
- **Prior reference:** NVIDIA CUB: 0.147
- **Current SOTA:** **0.104 ↓** — SimpleTES + gpt-oss-120b
- **Evidence status:** `source-reported-current-best` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **SOTA note:** Best result located under the released task evaluator. This is a source-reported record, not an independent global certification.
- **Integrity note:** Runtime depends on hardware and profiler configuration; scores are source-reported and require matched-device replay.

## Astrodynamics

<a id="cassini-trajectory"></a>

### Cassini gravity-assist trajectory

- **ID / source:** `cassini-trajectory` · SimpleTES
- **Question:** Find a feasible Cassini gravity-assist trajectory with lower total propulsive cost.
- **Agent input:** Mission window, body sequence/search variables, orbital constraints, a seed optimizer, and NAIF ephemeris kernels.
- **Required output:** Trajectory-design program and feasible mission parameters
- **Evaluation:** The mission simulator validates feasibility and computes the fixed propulsive-cost objective.
- **Environment:** Python task environment with astrodynamics dependencies and NAIF kernels.
- **Metric:** propulsive cost · minimize ↓ · normalized mission objective
- **Prior reference:** Historical sequence: 1.066682
- **Current SOTA:** **0.820129 ↓** — SimpleTES + gpt-oss-120b
- **Evidence status:** `source-reported-current-best` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **SOTA note:** Best result located under the released task evaluator. This is a source-reported record, not an independent global certification.
- **Integrity note:** Comparison is meaningful only under the same mission windows, simulator, constraints, and cost normalization.

## Mathematics Discovery

<a id="circle-packing-n26"></a>

### Circle packing in a unit square (n=26)

- **ID / source:** `circle-packing-n26` · SimpleTES
- **Question:** Place 26 non-overlapping circles inside a unit square to maximize the sum of their radii.
- **Agent input:** A Python seed construction, geometric constraints, and an executable feasibility checker.
- **Required output:** Circle centers and radii
- **Evaluation:** Recompute boundary and non-overlap constraints, then sum all feasible radii.
- **Environment:** Python; no external task setup listed.
- **Metric:** sum of radii · maximize ↑ · unit-square length
- **Prior reference:** AlphaEvolve V2: 2.635983
- **Current SOTA:** **2.635983 ↑** — SimpleTES + gpt-oss-120b
- **Evidence status:** `source-reported-current-best` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **SOTA note:** Best result located under the released task evaluator. This is a source-reported record, not an independent global certification.
- **Integrity note:** Rounded values match; full-precision artifacts are required to establish equality or a strict improvement.

<a id="circle-packing-n32"></a>

### Circle packing in a unit square (n=32)

- **ID / source:** `circle-packing-n32` · SimpleTES
- **Question:** Place 32 non-overlapping circles inside a unit square to maximize the sum of their radii.
- **Agent input:** A Python seed construction, geometric constraints, and an executable feasibility checker.
- **Required output:** Circle centers and radii
- **Evaluation:** Recompute boundary and non-overlap constraints, then sum all feasible radii.
- **Environment:** Python; no external task setup listed.
- **Metric:** sum of radii · maximize ↑ · unit-square length
- **Prior reference:** AlphaEvolve V2: 2.939572
- **Current SOTA:** **2.939572 ↑** — SimpleTES + gpt-oss-120b
- **Evidence status:** `source-reported-current-best` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **SOTA note:** Best result located under the released task evaluator. This is a source-reported record, not an independent global certification.
- **Integrity note:** Rounded values match; full-precision artifacts are required to establish equality or a strict improvement.

<a id="erdos-minimum-overlap"></a>

### Erdős minimum overlap

- **ID / source:** `erdos-minimum-overlap` · SimpleTES
- **Question:** Construct a feasible step function with unit mass that minimizes its worst translated one-sided overlap.
- **Agent input:** A discretized Python construction, integral and range constraints, and a fixed overlap evaluator.
- **Required output:** Step-function construction
- **Evaluation:** Validate range and mass constraints and recompute the supremum of the translated overlap objective.
- **Environment:** Python; no external task setup listed.
- **Metric:** overlap · minimize ↓ · dimensionless bound
- **Prior reference:** Together AI: 0.380871
- **Current SOTA:** **0.380868 ↓** — SimpleTES + gpt-oss-120b
- **Evidence status:** `source-reported-current-best` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **SOTA note:** Best result located under the released task evaluator. This is a source-reported record, not an independent global certification.
- **Integrity note:** This row preserves the rounded comparison table supplied for the task. Other SimpleTES versions report 0.380856, and later independent analysis raised normalization/certification issues; cite the exact artifact and recompute at full precision before claiming a record.

## Astrodynamics

<a id="galileo-trajectory"></a>

### Galileo gravity-assist trajectory

- **ID / source:** `galileo-trajectory` · SimpleTES
- **Question:** Find a feasible Galileo gravity-assist trajectory with lower total propulsive cost.
- **Agent input:** Mission window, body sequence/search variables, orbital constraints, a seed optimizer, and NAIF ephemeris kernels.
- **Required output:** Trajectory-design program and feasible mission parameters
- **Evaluation:** The mission simulator validates feasibility and computes the fixed propulsive-cost objective.
- **Environment:** Python task environment with astrodynamics dependencies and NAIF kernels.
- **Metric:** propulsive cost · minimize ↓ · normalized mission objective
- **Prior reference:** Historical sequence: 0.823681
- **Current SOTA:** **0.795108 ↓** — SimpleTES + gpt-oss-120b
- **Evidence status:** `source-reported-current-best` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **SOTA note:** Best result located under the released task evaluator. This is a source-reported record, not an independent global certification.
- **Integrity note:** Comparison is meaningful only under the same mission windows, simulator, constraints, and cost normalization.

## Mathematics Discovery

<a id="hadamard-determinant-n29"></a>

### Hadamard maximum determinant (n=29)

- **ID / source:** `hadamard-determinant-n29` · SimpleTES
- **Question:** Construct a plus-or-minus-one matrix of order 29 with maximum normalized determinant.
- **Agent input:** A Python seed construction, discrete matrix constraints, and a determinant evaluator.
- **Required output:** 29 by 29 sign matrix
- **Evaluation:** Validate every entry and recompute the determinant under the task's normalization.
- **Environment:** Python; no external task setup listed.
- **Metric:** normalized determinant · maximize ↑ · dimensionless
- **Prior reference:** Orrick: 0.935673
- **Current SOTA:** **0.935673 ↑** — SimpleTES + gpt-oss-120b
- **Evidence status:** `source-reported-current-best` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **SOTA note:** Best result located under the released task evaluator. This is a source-reported record, not an independent global certification.
- **Integrity note:** Rounded values match; use exact determinant arithmetic and the released matrix to verify equality.

## Scientific Algorithms

<a id="lasso-regularization-path"></a>

### LASSO regularization path

- **ID / source:** `lasso-regularization-path` · SimpleTES
- **Question:** Implement a faster solver for the complete LASSO regularization path while retaining solution accuracy.
- **Agent input:** A seed solver, fixed datasets and regularization path, accuracy checks, and a timing harness.
- **Required output:** C++ solver program
- **Evaluation:** Accuracy-gated execution followed by aggregate runtime measurement over the fixed workload.
- **Environment:** C++ invoked through Python with g++ and Eigen.
- **Metric:** runtime · minimize ↓ · ms
- **Prior reference:** glmnet: 4139.4
- **Current SOTA:** **2502.3 ↓** — SimpleTES + gpt-oss-120b
- **Evidence status:** `source-reported-current-best` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **SOTA note:** Best result located under the released task evaluator. This is a source-reported record, not an independent global certification.
- **Integrity note:** Runtime comparison requires identical CPU, compiler flags, datasets, tolerance, warmup, and thread policy.

## Astrodynamics

<a id="mariner-10-trajectory"></a>

### Mariner 10 gravity-assist trajectory

- **ID / source:** `mariner-10-trajectory` · SimpleTES
- **Question:** Find a feasible Mariner 10 gravity-assist trajectory with lower total propulsive cost.
- **Agent input:** Mission window, body sequence/search variables, orbital constraints, a seed optimizer, and NAIF ephemeris kernels.
- **Required output:** Trajectory-design program and feasible mission parameters
- **Evaluation:** The mission simulator validates feasibility and computes the fixed propulsive-cost objective.
- **Environment:** Python task environment with astrodynamics dependencies and NAIF kernels.
- **Metric:** propulsive cost · minimize ↓ · normalized mission objective
- **Prior reference:** Historical sequence: 0.424147
- **Current SOTA:** **0.326993 ↓** — SimpleTES + gpt-oss-120b
- **Evidence status:** `source-reported-current-best` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **SOTA note:** Best result located under the released task evaluator. This is a source-reported record, not an independent global certification.
- **Integrity note:** Comparison is meaningful only under the same mission windows, simulator, constraints, and cost normalization.

<a id="rosetta-trajectory"></a>

### Rosetta gravity-assist trajectory

- **ID / source:** `rosetta-trajectory` · SimpleTES
- **Question:** Find a feasible Rosetta gravity-assist trajectory with lower total propulsive cost.
- **Agent input:** Mission window, body sequence/search variables, orbital constraints, a seed optimizer, and NAIF ephemeris kernels.
- **Required output:** Trajectory-design program and feasible mission parameters
- **Evaluation:** The mission simulator validates feasibility and computes the fixed propulsive-cost objective.
- **Environment:** Python task environment with astrodynamics dependencies and NAIF kernels.
- **Metric:** propulsive cost · minimize ↓ · normalized mission objective
- **Prior reference:** Historical sequence: 1.736837
- **Current SOTA:** **1.552968 ↓** — SimpleTES + gpt-oss-120b
- **Evidence status:** `source-reported-current-best` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **SOTA note:** Best result located under the released task evaluator. This is a source-reported record, not an independent global certification.
- **Integrity note:** Comparison is meaningful only under the same mission windows, simulator, constraints, and cost normalization.

## Ai Foundations

<a id="scaling-law-domain-mix"></a>

### Scaling-law discovery: domain mix

- **ID / source:** `scaling-law-domain-mix` · SimpleTES
- **Question:** Discover a scaling-law program that extrapolates performance across training-domain mixtures.
- **Agent input:** Observed training runs, a seed symbolic/numerical predictor, a held-out extrapolation split, and fixed fitting code.
- **Required output:** Scaling-law prediction program
- **Evaluation:** Fit on visible observations and compute R2 on the fixed held-out extrapolation split.
- **Environment:** Python with the task dataset and Hugging Face cache.
- **Metric:** extrapolation R2 · maximize ↑ · coefficient of determination
- **Prior reference:** SLD Agent (Gemini-2.5-Flash): 0.991
- **Current SOTA:** **0.991 ↑** — SimpleTES + gpt-oss-120b
- **Evidence status:** `source-reported-current-best` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **SOTA note:** Best result located under the released task evaluator. This is a source-reported record, not an independent global certification.
- **Integrity note:** Rounded values match; the exact split, preprocessing, and full-precision predictions are required for comparison.

<a id="scaling-law-lr-bsz"></a>

### Scaling-law discovery: learning rate and batch size

- **ID / source:** `scaling-law-lr-bsz` · SimpleTES
- **Question:** Discover a scaling-law program that extrapolates across learning-rate and batch-size choices.
- **Agent input:** Observed training runs, a seed symbolic/numerical predictor, a held-out extrapolation split, and fixed fitting code.
- **Required output:** Scaling-law prediction program
- **Evaluation:** Fit on visible observations and compute R2 on the fixed held-out extrapolation split.
- **Environment:** Python with the task dataset and Hugging Face cache.
- **Metric:** extrapolation R2 · maximize ↑ · coefficient of determination
- **Prior reference:** SLD Agent (o4-mini): 0.611
- **Current SOTA:** **0.712 ↑** — SimpleTES + gpt-oss-120b
- **Evidence status:** `source-reported-current-best` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **SOTA note:** Best result located under the released task evaluator. This is a source-reported record, not an independent global certification.
- **Integrity note:** The exact split, preprocessing, and full-precision predictions are required for comparison.

<a id="scaling-law-parallel"></a>

### Scaling-law discovery: parallel

- **ID / source:** `scaling-law-parallel` · SimpleTES
- **Question:** Discover a scaling-law program that extrapolates performance on the parallel-compute split.
- **Agent input:** Observed training runs, a seed symbolic/numerical predictor, a held-out extrapolation split, and fixed fitting code.
- **Required output:** Scaling-law prediction program
- **Evaluation:** Fit on visible observations and compute R2 on the fixed held-out extrapolation split.
- **Environment:** Python with the task dataset and Hugging Face cache.
- **Metric:** extrapolation R2 · maximize ↑ · coefficient of determination
- **Prior reference:** SLD Agent (GPT-5): 1.0
- **Current SOTA:** **1.0 ↑** — SimpleTES + gpt-oss-120b
- **Evidence status:** `source-reported-current-best` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **SOTA note:** Best result located under the released task evaluator. This is a source-reported record, not an independent global certification.
- **Integrity note:** Rounded values match; the exact split, preprocessing, and full-precision predictions are required for comparison.

<a id="scaling-law-u-shape"></a>

### Scaling-law discovery: U-shape

- **ID / source:** `scaling-law-u-shape` · SimpleTES
- **Question:** Discover a scaling-law program that extrapolates the U-shaped performance regime.
- **Agent input:** Observed training runs, a seed symbolic/numerical predictor, a held-out extrapolation split, and fixed fitting code.
- **Required output:** Scaling-law prediction program
- **Evaluation:** Fit on visible observations and compute R2 on the fixed held-out extrapolation split.
- **Environment:** Python with the task dataset and Hugging Face cache.
- **Metric:** extrapolation R2 · maximize ↑ · coefficient of determination
- **Prior reference:** Goose + GPT-5: -0.232
- **Current SOTA:** **-0.008 ↑** — SimpleTES + gpt-oss-120b
- **Evidence status:** `source-reported-current-best` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **SOTA note:** Best result located under the released task evaluator. This is a source-reported record, not an independent global certification.
- **Integrity note:** The exact split, preprocessing, and full-precision predictions are required for comparison.

## Mathematics Discovery

<a id="second-autocorrelation-inequality"></a>

### Second autocorrelation inequality

- **ID / source:** `second-autocorrelation-inequality` · SimpleTES
- **Question:** Construct a feasible function or sequence that improves the second autocorrelation-inequality bound.
- **Agent input:** A discretized Python construction, inequality constraints, and a fixed bound evaluator.
- **Required output:** Mathematical construction
- **Evaluation:** Validate construction constraints and recompute the bound from the submitted artifact.
- **Environment:** Python; no external task setup listed.
- **Metric:** bound · maximize ↑ · dimensionless
- **Prior reference:** Together AI: 0.961206
- **Current SOTA:** **0.962694 ↑** — SimpleTES + gpt-oss-120b
- **Evidence status:** `source-reported-current-best` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **SOTA note:** Best result located under the released task evaluator. This is a source-reported record, not an independent global certification.
- **Integrity note:** Source-reported rounded score; full-precision construction and independent feasibility checks are required for a record claim.

## Scientific Algorithms

<a id="single-cell-rna-denoising"></a>

### Single-cell RNA-seq denoising

- **ID / source:** `single-cell-rna-denoising` · SimpleTES
- **Question:** Discover a denoising policy that reconstructs held-out single-cell gene-expression measurements more accurately.
- **Agent input:** OpenProblems/Tabula Muris data, a seed Python denoising program, visible training data, and held-out evaluation data.
- **Required output:** Denoising program and reconstructed expression matrix
- **Evaluation:** Run the submitted policy on the fixed data split and compute the OpenProblems denoising score.
- **Environment:** Python in a bundled task environment with the biological dataset.
- **Metric:** denoising score · maximize ↑ · OpenProblems composite score
- **Prior reference:** TTT-Discover: 0.73
- **Current SOTA:** **0.74 ↑** — SimpleTES + gpt-oss-120b
- **Evidence status:** `source-reported-current-best` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **SOTA note:** Best result located under the released task evaluator. This is a source-reported record, not an independent global certification.
- **Integrity note:** The data split, preprocessing, allowed retraining, and metric implementation must be frozen for comparison.

## Mathematics Discovery

<a id="sum-difference-problem"></a>

### Sum-Difference problem

- **ID / source:** `sum-difference-problem` · SimpleTES
- **Question:** Construct a set with a larger sumset-to-difference-set objective ratio under the fixed task definition.
- **Agent input:** A Python seed construction, discrete constraints, and an exact set-operation evaluator.
- **Required output:** Combinatorial set construction
- **Evaluation:** Validate the construction and recompute the objective from its sumset and difference set.
- **Environment:** Python; no external task setup listed.
- **Metric:** ratio · maximize ↑ · dimensionless
- **Prior reference:** AlphaEvolve V2: 1.121936
- **Current SOTA:** **1.144887 ↑** — SimpleTES + trajectory-level post-trained gpt-oss-120b
- **Evidence status:** `source-reported-current-best` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **SOTA note:** Best result located under the released task evaluator. This is a source-reported record, not an independent global certification.
- **Integrity note:** The current paper reports 1.143975 for the training-free run and 1.144887 after trajectory-level post-training. Verify the released set and exact objective independently.

## Quantum Compilation

<a id="superconducting-qubit-routing"></a>

### Superconducting qubit routing

- **ID / source:** `superconducting-qubit-routing` · SimpleTES
- **Question:** Route two-qubit gates onto a superconducting-device coupling graph while adding as few SWAP gates as possible.
- **Agent input:** Quantum circuits, target coupling graphs, a Rust seed routing policy, and a fixed compiler/evaluator.
- **Required output:** Rust qubit-routing policy
- **Evaluation:** Compile the fixed circuit corpus, validate legal routing, and aggregate added SWAP counts.
- **Environment:** Rust toolchain with the task's quantum-circuit corpus and compiler harness.
- **Metric:** added SWAPs · minimize ↓ · aggregate gate count
- **Prior reference:** LightSABRE: 20063
- **Current SOTA:** **15147 ↓** — SimpleTES + gpt-oss-120b
- **Evidence status:** `source-reported-current-best` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **SOTA note:** Best result located under the released task evaluator. This is a source-reported record, not an independent global certification.
- **Integrity note:** Circuit corpus, device topology, compiler version, seed policy, and aggregation must match.

## Mathematics Discovery

<a id="third-autocorrelation-inequality"></a>

### Third autocorrelation inequality

- **ID / source:** `third-autocorrelation-inequality` · SimpleTES
- **Question:** Construct a feasible function or sequence that improves the third autocorrelation-inequality bound.
- **Agent input:** A discretized Python construction, inequality constraints, and a fixed bound evaluator.
- **Required output:** Mathematical construction
- **Evaluation:** Validate construction constraints and recompute the bound from the submitted artifact.
- **Environment:** Python; no external task setup listed.
- **Metric:** bound · minimize ↓ · dimensionless
- **Prior reference:** Together AI: 1.454555
- **Current SOTA:** **1.453675 ↓** — SimpleTES + gpt-oss-120b
- **Evidence status:** `source-reported-current-best` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **SOTA note:** Best result located under the released task evaluator. This is a source-reported record, not an independent global certification.
- **Integrity note:** Source-reported rounded score; full-precision construction and independent feasibility checks are required for a record claim.

## Ai Foundations

<a id="trimul-kernel"></a>

### TriMul GPU kernel

- **ID / source:** `trimul-kernel` · SimpleTES
- **Question:** Implement a faster triangular matrix-multiplication GPU kernel without changing numerical semantics.
- **Agent input:** A seed Triton kernel, fixed tensor shapes and dtypes, correctness tests, and a profiling harness.
- **Required output:** Triton kernel source
- **Evaluation:** Correctness-gated execution followed by runtime profiling on the fixed benchmark workload.
- **Environment:** Triton with a GPU profiling server; headline result uses H100.
- **Metric:** runtime · minimize ↓ · ms
- **Prior reference:** Human expert: 1.14
- **Current SOTA:** **1.122 ↓** — SimpleTES + gpt-oss-120b
- **Evidence status:** `source-reported-current-best` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **SOTA note:** Best result located under the released task evaluator. This is a source-reported record, not an independent global certification.
- **Integrity note:** Runtime depends on hardware and profiler configuration; scores are source-reported and require matched-device replay.

## Astrodynamics

<a id="voyager-2-trajectory"></a>

### Voyager 2 gravity-assist trajectory

- **ID / source:** `voyager-2-trajectory` · SimpleTES
- **Question:** Find a feasible Voyager 2 gravity-assist trajectory with lower total propulsive cost.
- **Agent input:** Mission window, body sequence/search variables, orbital constraints, a seed optimizer, and NAIF ephemeris kernels.
- **Required output:** Trajectory-design program and feasible mission parameters
- **Evaluation:** The mission simulator validates feasibility and computes the fixed propulsive-cost objective.
- **Environment:** Python task environment with astrodynamics dependencies and NAIF kernels.
- **Metric:** propulsive cost · minimize ↓ · normalized mission objective
- **Prior reference:** Historical sequence: 3.503798
- **Current SOTA:** **3.430214 ↓** — SimpleTES + gpt-oss-120b
- **Evidence status:** `source-reported-current-best` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **SOTA note:** Best result located under the released task evaluator. This is a source-reported record, not an independent global certification.
- **Integrity note:** Comparison is meaningful only under the same mission windows, simulator, constraints, and cost normalization.

## Scientific Algorithms

<a id="zapbench-h1"></a>

### ZAPBench whole-brain forecasting (H=1)

- **ID / source:** `zapbench-h1` · SimpleTES
- **Question:** Forecast whole-brain neural activity one step ahead with lower held-out error.
- **Agent input:** ZAPBench time-series data, a seed forecasting program, visible context, and a fixed held-out split.
- **Required output:** Python forecasting program and predictions
- **Evaluation:** Run the forecaster on the fixed H=1 test split and compute mean absolute error.
- **Environment:** Python task environment with GPU and ZAPBench dataset.
- **Metric:** test MAE · minimize ↓ · normalized activity
- **Prior reference:** ERA: 0.0174
- **Current SOTA:** **0.0165 ↓** — SimpleTES + gpt-oss-120b
- **Evidence status:** `source-reported-current-best` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **SOTA note:** Best result located under the released task evaluator. This is a source-reported record, not an independent global certification.
- **Integrity note:** Forecast split, normalization, horizon semantics, and use of future information must be identical.

<a id="zapbench-h4"></a>

### ZAPBench whole-brain forecasting (H=4)

- **ID / source:** `zapbench-h4` · SimpleTES
- **Question:** Forecast whole-brain neural activity four steps ahead with lower held-out error.
- **Agent input:** ZAPBench time-series data, a seed forecasting program, visible context, and a fixed held-out split.
- **Required output:** Python forecasting program and predictions
- **Evaluation:** Run the forecaster on the fixed H=4 test split and compute mean absolute error.
- **Environment:** Python task environment with GPU and ZAPBench dataset.
- **Metric:** test MAE · minimize ↓ · normalized activity
- **Prior reference:** ERA: 0.0221
- **Current SOTA:** **0.0211 ↓** — SimpleTES + gpt-oss-120b
- **Evidence status:** `source-reported-current-best` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **SOTA note:** Best result located under the released task evaluator. This is a source-reported record, not an independent global certification.
- **Integrity note:** Forecast split, normalization, horizon semantics, and use of future information must be identical.

<a id="zapbench-h8"></a>

### ZAPBench whole-brain forecasting (H=8)

- **ID / source:** `zapbench-h8` · SimpleTES
- **Question:** Forecast whole-brain neural activity eight steps ahead with lower held-out error.
- **Agent input:** ZAPBench time-series data, a seed forecasting program, visible context, and a fixed held-out split.
- **Required output:** Python forecasting program and predictions
- **Evaluation:** Run the forecaster on the fixed H=8 test split and compute mean absolute error.
- **Environment:** Python task environment with GPU and ZAPBench dataset.
- **Metric:** test MAE · minimize ↓ · normalized activity
- **Prior reference:** ERA: 0.0244
- **Current SOTA:** **0.023 ↓** — SimpleTES + gpt-oss-120b
- **Evidence status:** `source-reported-current-best` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **SOTA note:** Best result located under the released task evaluator. This is a source-reported record, not an independent global certification.
- **Integrity note:** Forecast split, normalization, horizon semantics, and use of future information must be identical.

<a id="zapbench-h16"></a>

### ZAPBench whole-brain forecasting (H=16)

- **ID / source:** `zapbench-h16` · SimpleTES
- **Question:** Forecast whole-brain neural activity sixteen steps ahead with lower held-out error.
- **Agent input:** ZAPBench time-series data, a seed forecasting program, visible context, and a fixed held-out split.
- **Required output:** Python forecasting program and predictions
- **Evaluation:** Run the forecaster on the fixed H=16 test split and compute mean absolute error.
- **Environment:** Python task environment with GPU and ZAPBench dataset.
- **Metric:** test MAE · minimize ↓ · normalized activity
- **Prior reference:** ERA: 0.0267
- **Current SOTA:** **0.0251 ↓** — SimpleTES + gpt-oss-120b
- **Evidence status:** `source-reported-current-best` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **SOTA note:** Best result located under the released task evaluator. This is a source-reported record, not an independent global certification.
- **Integrity note:** Forecast split, normalization, horizon semantics, and use of future information must be identical.

<a id="zapbench-h32"></a>

### ZAPBench whole-brain forecasting (H=32)

- **ID / source:** `zapbench-h32` · SimpleTES
- **Question:** Forecast whole-brain neural activity thirty-two steps ahead with lower held-out error.
- **Agent input:** ZAPBench time-series data, a seed forecasting program, visible context, and a fixed held-out split.
- **Required output:** Python forecasting program and predictions
- **Evaluation:** Run the forecaster on the fixed H=32 test split and compute mean absolute error.
- **Environment:** Python task environment with GPU and ZAPBench dataset.
- **Metric:** test MAE · minimize ↓ · normalized activity
- **Prior reference:** ERA: 0.0283
- **Current SOTA:** **0.0259 ↓** — SimpleTES + gpt-oss-120b
- **Evidence status:** `source-reported-current-best` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **SOTA note:** Best result located under the released task evaluator. This is a source-reported record, not an independent global certification.
- **Integrity note:** Forecast split, normalization, horizon semantics, and use of future information must be identical.

## Quantum Compilation

<a id="zoned-neutral-atom-compilation"></a>

### Zoned neutral-atom compilation

- **ID / source:** `zoned-neutral-atom-compilation` · SimpleTES
- **Question:** Compile circuits for a zoned neutral-atom architecture while minimizing aggregate execution time.
- **Agent input:** Quantum circuits, architecture constraints, a Python seed compilation policy, and a fixed simulator.
- **Required output:** Python compilation policy
- **Evaluation:** Validate legal movement and gate scheduling, simulate every circuit, and aggregate execution time.
- **Environment:** Python in the task-specific zoned-neutral-atom environment.
- **Metric:** execution time · minimize ↓ · geometric-mean simulator time
- **Prior reference:** ZAC: 29187.7
- **Current SOTA:** **19507.5 ↓** — SimpleTES + gpt-oss-120b
- **Evidence status:** `source-reported-current-best` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **SOTA note:** Best result located under the released task evaluator. This is a source-reported record, not an independent global certification.
- **Integrity note:** Circuit corpus, architecture parameters, simulator version, and aggregation must match.

## Interactive World Discovery

<a id="arc-agi-3-ls20"></a>

### ARC-AGI-3 ls20 (Agent reasoning)

- **ID / source:** `arc-agi-3-ls20` · ARC-AGI-3
- **Question:** Without natural-language instructions, discover ls20's hidden mechanics and win condition through interaction, then complete its levels efficiently.
- **Agent input:** A turn-based grid frame of at most 64x64 cells using 16 colors, the currently available actions, and the accumulated frame/action history; the objective and mechanics are withheld.
- **Required output:** An action trace that reaches WIN across the game's levels
- **Evaluation:** For each completed level, square human-baseline actions divided by agent actions, cap at 1.15, take a level-index-weighted game score, then average games for an aggregate benchmark score.
- **Environment:** Official ARC-AGI Toolkit/API; deterministic turn-based environment; RESET, ACTION1-ACTION7, with ACTION6 accepting coordinates and ACTION7 serving as undo when available.
- **Metric:** Relative Human Action Efficiency (RHAE) · maximize ↑ · percent
- **Prior reference:** Human first-attempt upper-median baseline: 100
- **Current SOTA:** **Not published per task** — suite best: Tycho, 100.0 percent
- **Evidence status:** `community-self-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arcprize.org/leaderboard/community) · [source 2](https://arcprize.org/scorecards/08b98aa0-5df0-42c0-b501-856f553a21e9) · [source 3](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)
- **SOTA note:** The official community page reports Tycho at 100.0% on the public-demo suite, but labels community results self-reported and does not expose an attributable per-game breakdown. The suite score must not be copied into this task row.
- **Integrity note:** This is a public demonstration environment, not a valid stand-alone measure of ARC-AGI-3 progress. Record the exact game version, scorecard, replay, prompt, action budget, and toolkit/API version; do not expose private environments.

<a id="arc-agi-3-ft09"></a>

### ARC-AGI-3 ft09 (Elementary Logic)

- **ID / source:** `arc-agi-3-ft09` · ARC-AGI-3
- **Question:** Without natural-language instructions, discover ft09's hidden mechanics and win condition through interaction, then complete its levels efficiently.
- **Agent input:** A turn-based grid frame of at most 64x64 cells using 16 colors, the currently available actions, and the accumulated frame/action history; the objective and mechanics are withheld.
- **Required output:** An action trace that reaches WIN across the game's levels
- **Evaluation:** For each completed level, square human-baseline actions divided by agent actions, cap at 1.15, take a level-index-weighted game score, then average games for an aggregate benchmark score.
- **Environment:** Official ARC-AGI Toolkit/API; deterministic turn-based environment; RESET, ACTION1-ACTION7, with ACTION6 accepting coordinates and ACTION7 serving as undo when available.
- **Metric:** Relative Human Action Efficiency (RHAE) · maximize ↑ · percent
- **Prior reference:** Human first-attempt upper-median baseline: 100
- **Current SOTA:** **Not published per task** — suite best: Tycho, 100.0 percent
- **Evidence status:** `community-self-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arcprize.org/leaderboard/community) · [source 2](https://arcprize.org/scorecards/08b98aa0-5df0-42c0-b501-856f553a21e9) · [source 3](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf) · [source 4](https://arcprize.org/replay/591e7e51-5004-4510-9e03-eca2b2d81edb?frame=19)
- **SOTA note:** The official community page reports Tycho at 100.0% on the public-demo suite, but labels community results self-reported and does not expose an attributable per-game breakdown. The suite score must not be copied into this task row. A public ft09 replay reaches 100%, but its model and harness fields are blank.
- **Integrity note:** This is a public demonstration environment, not a valid stand-alone measure of ARC-AGI-3 progress. Record the exact game version, scorecard, replay, prompt, action budget, and toolkit/API version; do not expose private environments.

<a id="arc-agi-3-vc33"></a>

### ARC-AGI-3 vc33 (Orchestration)

- **ID / source:** `arc-agi-3-vc33` · ARC-AGI-3
- **Question:** Without natural-language instructions, discover vc33's hidden mechanics and win condition through interaction, then complete its levels efficiently.
- **Agent input:** A turn-based grid frame of at most 64x64 cells using 16 colors, the currently available actions, and the accumulated frame/action history; the objective and mechanics are withheld.
- **Required output:** An action trace that reaches WIN across the game's levels
- **Evaluation:** For each completed level, square human-baseline actions divided by agent actions, cap at 1.15, take a level-index-weighted game score, then average games for an aggregate benchmark score.
- **Environment:** Official ARC-AGI Toolkit/API; deterministic turn-based environment; RESET, ACTION1-ACTION7, with ACTION6 accepting coordinates and ACTION7 serving as undo when available.
- **Metric:** Relative Human Action Efficiency (RHAE) · maximize ↑ · percent
- **Prior reference:** Human first-attempt upper-median baseline: 100
- **Current SOTA:** **Not published per task** — suite best: Tycho, 100.0 percent
- **Evidence status:** `community-self-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arcprize.org/leaderboard/community) · [source 2](https://arcprize.org/scorecards/08b98aa0-5df0-42c0-b501-856f553a21e9) · [source 3](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)
- **SOTA note:** The official community page reports Tycho at 100.0% on the public-demo suite, but labels community results self-reported and does not expose an attributable per-game breakdown. The suite score must not be copied into this task row.
- **Integrity note:** This is a public demonstration environment, not a valid stand-alone measure of ARC-AGI-3 progress. Record the exact game version, scorecard, replay, prompt, action budget, and toolkit/API version; do not expose private environments.

<a id="dig-bench-p-1"></a>

### DiG-bench P-1 (tier 1)

- **ID / source:** `dig-bench-p-1` · DiG-bench
- **Question:** Discover P-1's unknown transformation rules and win conditions through experimentation, then apply the learned rules to beat its challenges within the step budget.
- **Agent input:** A JSON game state containing the observation, level, lives, steps remaining, status, legal actions, and interaction history; no semantic description of the hidden rules.
- **Required output:** A legal action sequence that wins the game
- **Evaluation:** Score each run by whether the game is beaten within its fixed step budget; average wins over repeated runs for the game, then average games within the difficulty tier.
- **Environment:** Official text-game server exposed through the DiG-bench API or MCP and a declared model harness; humans and models receive identical states, actions, and step budgets. Some games offer a declared creative mode for unmetered experiments.
- **Metric:** win rate · maximize ↑ · fraction of runs
- **Prior reference:** No matched task-level reference published
- **Current SOTA:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **SOTA note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
- **Integrity note:** P-series task is public and may be used for development, so report public-versus-private evaluation separately. Pin the game, server, harness, model, prompt, context policy, run count, and step budget.

<a id="dig-bench-p-2"></a>

### DiG-bench P-2 (tier 1)

- **ID / source:** `dig-bench-p-2` · DiG-bench
- **Question:** Discover P-2's unknown transformation rules and win conditions through experimentation, then apply the learned rules to beat its challenges within the step budget.
- **Agent input:** A JSON game state containing the observation, level, lives, steps remaining, status, legal actions, and interaction history; no semantic description of the hidden rules.
- **Required output:** A legal action sequence that wins the game
- **Evaluation:** Score each run by whether the game is beaten within its fixed step budget; average wins over repeated runs for the game, then average games within the difficulty tier.
- **Environment:** Official text-game server exposed through the DiG-bench API or MCP and a declared model harness; humans and models receive identical states, actions, and step budgets. Some games offer a declared creative mode for unmetered experiments.
- **Metric:** win rate · maximize ↑ · fraction of runs
- **Prior reference:** No matched task-level reference published
- **Current SOTA:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **SOTA note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
- **Integrity note:** P-series task is public and may be used for development, so report public-versus-private evaluation separately. Pin the game, server, harness, model, prompt, context policy, run count, and step budget.

<a id="dig-bench-p-3"></a>

### DiG-bench P-3 (tier 1)

- **ID / source:** `dig-bench-p-3` · DiG-bench
- **Question:** Discover P-3's unknown transformation rules and win conditions through experimentation, then apply the learned rules to beat its challenges within the step budget.
- **Agent input:** A JSON game state containing the observation, level, lives, steps remaining, status, legal actions, and interaction history; no semantic description of the hidden rules.
- **Required output:** A legal action sequence that wins the game
- **Evaluation:** Score each run by whether the game is beaten within its fixed step budget; average wins over repeated runs for the game, then average games within the difficulty tier.
- **Environment:** Official text-game server exposed through the DiG-bench API or MCP and a declared model harness; humans and models receive identical states, actions, and step budgets. Some games offer a declared creative mode for unmetered experiments.
- **Metric:** win rate · maximize ↑ · fraction of runs
- **Prior reference:** No matched task-level reference published
- **Current SOTA:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **SOTA note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
- **Integrity note:** P-series task is public and may be used for development, so report public-versus-private evaluation separately. Pin the game, server, harness, model, prompt, context policy, run count, and step budget.

<a id="dig-bench-p-4"></a>

### DiG-bench P-4 (tier 2)

- **ID / source:** `dig-bench-p-4` · DiG-bench
- **Question:** Discover P-4's unknown transformation rules and win conditions through experimentation, then apply the learned rules to beat its challenges within the step budget.
- **Agent input:** A JSON game state containing the observation, level, lives, steps remaining, status, legal actions, and interaction history; no semantic description of the hidden rules.
- **Required output:** A legal action sequence that wins the game
- **Evaluation:** Score each run by whether the game is beaten within its fixed step budget; average wins over repeated runs for the game, then average games within the difficulty tier.
- **Environment:** Official text-game server exposed through the DiG-bench API or MCP and a declared model harness; humans and models receive identical states, actions, and step budgets. Some games offer a declared creative mode for unmetered experiments.
- **Metric:** win rate · maximize ↑ · fraction of runs
- **Prior reference:** No matched task-level reference published
- **Current SOTA:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **SOTA note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
- **Integrity note:** P-series task is public and may be used for development, so report public-versus-private evaluation separately. Pin the game, server, harness, model, prompt, context policy, run count, and step budget.

<a id="dig-bench-p-5"></a>

### DiG-bench P-5 (tier 2)

- **ID / source:** `dig-bench-p-5` · DiG-bench
- **Question:** Discover P-5's unknown transformation rules and win conditions through experimentation, then apply the learned rules to beat its challenges within the step budget.
- **Agent input:** A JSON game state containing the observation, level, lives, steps remaining, status, legal actions, and interaction history; no semantic description of the hidden rules.
- **Required output:** A legal action sequence that wins the game
- **Evaluation:** Score each run by whether the game is beaten within its fixed step budget; average wins over repeated runs for the game, then average games within the difficulty tier.
- **Environment:** Official text-game server exposed through the DiG-bench API or MCP and a declared model harness; humans and models receive identical states, actions, and step budgets. Some games offer a declared creative mode for unmetered experiments.
- **Metric:** win rate · maximize ↑ · fraction of runs
- **Prior reference:** No matched task-level reference published
- **Current SOTA:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **SOTA note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
- **Integrity note:** P-series task is public and may be used for development, so report public-versus-private evaluation separately. Pin the game, server, harness, model, prompt, context policy, run count, and step budget.

<a id="dig-bench-p-6"></a>

### DiG-bench P-6 (tier 2)

- **ID / source:** `dig-bench-p-6` · DiG-bench
- **Question:** Discover P-6's unknown transformation rules and win conditions through experimentation, then apply the learned rules to beat its challenges within the step budget.
- **Agent input:** A JSON game state containing the observation, level, lives, steps remaining, status, legal actions, and interaction history; no semantic description of the hidden rules.
- **Required output:** A legal action sequence that wins the game
- **Evaluation:** Score each run by whether the game is beaten within its fixed step budget; average wins over repeated runs for the game, then average games within the difficulty tier.
- **Environment:** Official text-game server exposed through the DiG-bench API or MCP and a declared model harness; humans and models receive identical states, actions, and step budgets. Some games offer a declared creative mode for unmetered experiments.
- **Metric:** win rate · maximize ↑ · fraction of runs
- **Prior reference:** No matched task-level reference published
- **Current SOTA:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **SOTA note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
- **Integrity note:** P-series task is public and may be used for development, so report public-versus-private evaluation separately. Pin the game, server, harness, model, prompt, context policy, run count, and step budget.

<a id="dig-bench-p-7"></a>

### DiG-bench P-7 (tier 3)

- **ID / source:** `dig-bench-p-7` · DiG-bench
- **Question:** Discover P-7's unknown transformation rules and win conditions through experimentation, then apply the learned rules to beat its challenges within the step budget.
- **Agent input:** A JSON game state containing the observation, level, lives, steps remaining, status, legal actions, and interaction history; no semantic description of the hidden rules.
- **Required output:** A legal action sequence that wins the game
- **Evaluation:** Score each run by whether the game is beaten within its fixed step budget; average wins over repeated runs for the game, then average games within the difficulty tier.
- **Environment:** Official text-game server exposed through the DiG-bench API or MCP and a declared model harness; humans and models receive identical states, actions, and step budgets. Some games offer a declared creative mode for unmetered experiments.
- **Metric:** win rate · maximize ↑ · fraction of runs
- **Prior reference:** No matched task-level reference published
- **Current SOTA:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **SOTA note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
- **Integrity note:** P-series task is public and may be used for development, so report public-versus-private evaluation separately. Pin the game, server, harness, model, prompt, context policy, run count, and step budget.

<a id="dig-bench-p-8"></a>

### DiG-bench P-8 (tier 3)

- **ID / source:** `dig-bench-p-8` · DiG-bench
- **Question:** Discover P-8's unknown transformation rules and win conditions through experimentation, then apply the learned rules to beat its challenges within the step budget.
- **Agent input:** A JSON game state containing the observation, level, lives, steps remaining, status, legal actions, and interaction history; no semantic description of the hidden rules.
- **Required output:** A legal action sequence that wins the game
- **Evaluation:** Score each run by whether the game is beaten within its fixed step budget; average wins over repeated runs for the game, then average games within the difficulty tier.
- **Environment:** Official text-game server exposed through the DiG-bench API or MCP and a declared model harness; humans and models receive identical states, actions, and step budgets. Some games offer a declared creative mode for unmetered experiments.
- **Metric:** win rate · maximize ↑ · fraction of runs
- **Prior reference:** No matched task-level reference published
- **Current SOTA:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **SOTA note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
- **Integrity note:** P-series task is public and may be used for development, so report public-versus-private evaluation separately. Pin the game, server, harness, model, prompt, context policy, run count, and step budget.

<a id="dig-bench-p-9"></a>

### DiG-bench P-9 (tier 3)

- **ID / source:** `dig-bench-p-9` · DiG-bench
- **Question:** Discover P-9's unknown transformation rules and win conditions through experimentation, then apply the learned rules to beat its challenges within the step budget.
- **Agent input:** A JSON game state containing the observation, level, lives, steps remaining, status, legal actions, and interaction history; no semantic description of the hidden rules.
- **Required output:** A legal action sequence that wins the game
- **Evaluation:** Score each run by whether the game is beaten within its fixed step budget; average wins over repeated runs for the game, then average games within the difficulty tier.
- **Environment:** Official text-game server exposed through the DiG-bench API or MCP and a declared model harness; humans and models receive identical states, actions, and step budgets. Some games offer a declared creative mode for unmetered experiments.
- **Metric:** win rate · maximize ↑ · fraction of runs
- **Prior reference:** No matched task-level reference published
- **Current SOTA:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **SOTA note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
- **Integrity note:** P-series task is public and may be used for development, so report public-versus-private evaluation separately. Pin the game, server, harness, model, prompt, context policy, run count, and step budget.

<a id="dig-bench-p-10"></a>

### DiG-bench P-10 (tier 4)

- **ID / source:** `dig-bench-p-10` · DiG-bench
- **Question:** Discover P-10's unknown transformation rules and win conditions through experimentation, then apply the learned rules to beat its challenges within the step budget.
- **Agent input:** A JSON game state containing the observation, level, lives, steps remaining, status, legal actions, and interaction history; no semantic description of the hidden rules.
- **Required output:** A legal action sequence that wins the game
- **Evaluation:** Score each run by whether the game is beaten within its fixed step budget; average wins over repeated runs for the game, then average games within the difficulty tier.
- **Environment:** Official text-game server exposed through the DiG-bench API or MCP and a declared model harness; humans and models receive identical states, actions, and step budgets. Some games offer a declared creative mode for unmetered experiments.
- **Metric:** win rate · maximize ↑ · fraction of runs
- **Prior reference:** No matched task-level reference published
- **Current SOTA:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **SOTA note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
- **Integrity note:** P-series task is public and may be used for development, so report public-versus-private evaluation separately. Pin the game, server, harness, model, prompt, context policy, run count, and step budget.

<a id="dig-bench-p-11"></a>

### DiG-bench P-11 (tier 4)

- **ID / source:** `dig-bench-p-11` · DiG-bench
- **Question:** Discover P-11's unknown transformation rules and win conditions through experimentation, then apply the learned rules to beat its challenges within the step budget.
- **Agent input:** A JSON game state containing the observation, level, lives, steps remaining, status, legal actions, and interaction history; no semantic description of the hidden rules.
- **Required output:** A legal action sequence that wins the game
- **Evaluation:** Score each run by whether the game is beaten within its fixed step budget; average wins over repeated runs for the game, then average games within the difficulty tier.
- **Environment:** Official text-game server exposed through the DiG-bench API or MCP and a declared model harness; humans and models receive identical states, actions, and step budgets. Some games offer a declared creative mode for unmetered experiments.
- **Metric:** win rate · maximize ↑ · fraction of runs
- **Prior reference:** No matched task-level reference published
- **Current SOTA:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **SOTA note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
- **Integrity note:** P-series task is public and may be used for development, so report public-versus-private evaluation separately. Pin the game, server, harness, model, prompt, context policy, run count, and step budget.

<a id="dig-bench-p-12"></a>

### DiG-bench P-12 (tier 4)

- **ID / source:** `dig-bench-p-12` · DiG-bench
- **Question:** Discover P-12's unknown transformation rules and win conditions through experimentation, then apply the learned rules to beat its challenges within the step budget.
- **Agent input:** A JSON game state containing the observation, level, lives, steps remaining, status, legal actions, and interaction history; no semantic description of the hidden rules.
- **Required output:** A legal action sequence that wins the game
- **Evaluation:** Score each run by whether the game is beaten within its fixed step budget; average wins over repeated runs for the game, then average games within the difficulty tier.
- **Environment:** Official text-game server exposed through the DiG-bench API or MCP and a declared model harness; humans and models receive identical states, actions, and step budgets. Some games offer a declared creative mode for unmetered experiments.
- **Metric:** win rate · maximize ↑ · fraction of runs
- **Prior reference:** No matched task-level reference published
- **Current SOTA:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **SOTA note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
- **Integrity note:** P-series task is public and may be used for development, so report public-versus-private evaluation separately. Pin the game, server, harness, model, prompt, context policy, run count, and step budget.

<a id="dig-bench-p-13"></a>

### DiG-bench P-13 (tier 5)

- **ID / source:** `dig-bench-p-13` · DiG-bench
- **Question:** Discover P-13's unknown transformation rules and win conditions through experimentation, then apply the learned rules to beat its challenges within the step budget.
- **Agent input:** A JSON game state containing the observation, level, lives, steps remaining, status, legal actions, and interaction history; no semantic description of the hidden rules.
- **Required output:** A legal action sequence that wins the game
- **Evaluation:** Score each run by whether the game is beaten within its fixed step budget; average wins over repeated runs for the game, then average games within the difficulty tier.
- **Environment:** Official text-game server exposed through the DiG-bench API or MCP and a declared model harness; humans and models receive identical states, actions, and step budgets. Some games offer a declared creative mode for unmetered experiments.
- **Metric:** win rate · maximize ↑ · fraction of runs
- **Prior reference:** No matched task-level reference published
- **Current SOTA:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **SOTA note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
- **Integrity note:** P-series task is public and may be used for development, so report public-versus-private evaluation separately. Pin the game, server, harness, model, prompt, context policy, run count, and step budget.

<a id="dig-bench-p-14"></a>

### DiG-bench P-14 (tier 5)

- **ID / source:** `dig-bench-p-14` · DiG-bench
- **Question:** Discover P-14's unknown transformation rules and win conditions through experimentation, then apply the learned rules to beat its challenges within the step budget.
- **Agent input:** A JSON game state containing the observation, level, lives, steps remaining, status, legal actions, and interaction history; no semantic description of the hidden rules.
- **Required output:** A legal action sequence that wins the game
- **Evaluation:** Score each run by whether the game is beaten within its fixed step budget; average wins over repeated runs for the game, then average games within the difficulty tier.
- **Environment:** Official text-game server exposed through the DiG-bench API or MCP and a declared model harness; humans and models receive identical states, actions, and step budgets. Some games offer a declared creative mode for unmetered experiments.
- **Metric:** win rate · maximize ↑ · fraction of runs
- **Prior reference:** No matched task-level reference published
- **Current SOTA:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **SOTA note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
- **Integrity note:** P-series task is public and may be used for development, so report public-versus-private evaluation separately. Pin the game, server, harness, model, prompt, context policy, run count, and step budget.

<a id="dig-bench-p-15"></a>

### DiG-bench P-15 (tier 5)

- **ID / source:** `dig-bench-p-15` · DiG-bench
- **Question:** Discover P-15's unknown transformation rules and win conditions through experimentation, then apply the learned rules to beat its challenges within the step budget.
- **Agent input:** A JSON game state containing the observation, level, lives, steps remaining, status, legal actions, and interaction history; no semantic description of the hidden rules.
- **Required output:** A legal action sequence that wins the game
- **Evaluation:** Score each run by whether the game is beaten within its fixed step budget; average wins over repeated runs for the game, then average games within the difficulty tier.
- **Environment:** Official text-game server exposed through the DiG-bench API or MCP and a declared model harness; humans and models receive identical states, actions, and step budgets. Some games offer a declared creative mode for unmetered experiments.
- **Metric:** win rate · maximize ↑ · fraction of runs
- **Prior reference:** No matched task-level reference published
- **Current SOTA:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **SOTA note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
- **Integrity note:** P-series task is public and may be used for development, so report public-versus-private evaluation separately. Pin the game, server, harness, model, prompt, context policy, run count, and step budget.

<a id="dig-bench-p-16"></a>

### DiG-bench P-16 (tier 6)

- **ID / source:** `dig-bench-p-16` · DiG-bench
- **Question:** Discover P-16's unknown transformation rules and win conditions through experimentation, then apply the learned rules to beat its challenges within the step budget.
- **Agent input:** A JSON game state containing the observation, level, lives, steps remaining, status, legal actions, and interaction history; no semantic description of the hidden rules.
- **Required output:** A legal action sequence that wins the game
- **Evaluation:** Score each run by whether the game is beaten within its fixed step budget; average wins over repeated runs for the game, then average games within the difficulty tier.
- **Environment:** Official text-game server exposed through the DiG-bench API or MCP and a declared model harness; humans and models receive identical states, actions, and step budgets. Some games offer a declared creative mode for unmetered experiments.
- **Metric:** win rate · maximize ↑ · fraction of runs
- **Prior reference:** No matched task-level reference published
- **Current SOTA:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **SOTA note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
- **Integrity note:** P-series task is public and may be used for development, so report public-versus-private evaluation separately. Pin the game, server, harness, model, prompt, context policy, run count, and step budget.

<a id="dig-bench-p-17"></a>

### DiG-bench P-17 (tier 6)

- **ID / source:** `dig-bench-p-17` · DiG-bench
- **Question:** Discover P-17's unknown transformation rules and win conditions through experimentation, then apply the learned rules to beat its challenges within the step budget.
- **Agent input:** A JSON game state containing the observation, level, lives, steps remaining, status, legal actions, and interaction history; no semantic description of the hidden rules.
- **Required output:** A legal action sequence that wins the game
- **Evaluation:** Score each run by whether the game is beaten within its fixed step budget; average wins over repeated runs for the game, then average games within the difficulty tier.
- **Environment:** Official text-game server exposed through the DiG-bench API or MCP and a declared model harness; humans and models receive identical states, actions, and step budgets. Some games offer a declared creative mode for unmetered experiments.
- **Metric:** win rate · maximize ↑ · fraction of runs
- **Prior reference:** No matched task-level reference published
- **Current SOTA:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **SOTA note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
- **Integrity note:** P-series task is public and may be used for development, so report public-versus-private evaluation separately. Pin the game, server, harness, model, prompt, context policy, run count, and step budget.

<a id="dig-bench-p-18"></a>

### DiG-bench P-18 (tier 6)

- **ID / source:** `dig-bench-p-18` · DiG-bench
- **Question:** Discover P-18's unknown transformation rules and win conditions through experimentation, then apply the learned rules to beat its challenges within the step budget.
- **Agent input:** A JSON game state containing the observation, level, lives, steps remaining, status, legal actions, and interaction history; no semantic description of the hidden rules.
- **Required output:** A legal action sequence that wins the game
- **Evaluation:** Score each run by whether the game is beaten within its fixed step budget; average wins over repeated runs for the game, then average games within the difficulty tier.
- **Environment:** Official text-game server exposed through the DiG-bench API or MCP and a declared model harness; humans and models receive identical states, actions, and step budgets. Some games offer a declared creative mode for unmetered experiments.
- **Metric:** win rate · maximize ↑ · fraction of runs
- **Prior reference:** No matched task-level reference published
- **Current SOTA:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **SOTA note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
- **Integrity note:** P-series task is public and may be used for development, so report public-versus-private evaluation separately. Pin the game, server, harness, model, prompt, context policy, run count, and step budget.

<a id="dig-bench-p-19"></a>

### DiG-bench P-19 (tier 7)

- **ID / source:** `dig-bench-p-19` · DiG-bench
- **Question:** Discover P-19's unknown transformation rules and win conditions through experimentation, then apply the learned rules to beat its challenges within the step budget.
- **Agent input:** A JSON game state containing the observation, level, lives, steps remaining, status, legal actions, and interaction history; no semantic description of the hidden rules.
- **Required output:** A legal action sequence that wins the game
- **Evaluation:** Score each run by whether the game is beaten within its fixed step budget; average wins over repeated runs for the game, then average games within the difficulty tier.
- **Environment:** Official text-game server exposed through the DiG-bench API or MCP and a declared model harness; humans and models receive identical states, actions, and step budgets. Some games offer a declared creative mode for unmetered experiments.
- **Metric:** win rate · maximize ↑ · fraction of runs
- **Prior reference:** No matched task-level reference published
- **Current SOTA:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **SOTA note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
- **Integrity note:** P-series task is public and may be used for development, so report public-versus-private evaluation separately. Pin the game, server, harness, model, prompt, context policy, run count, and step budget.

<a id="dig-bench-p-20"></a>

### DiG-bench P-20 (tier 7)

- **ID / source:** `dig-bench-p-20` · DiG-bench
- **Question:** Discover P-20's unknown transformation rules and win conditions through experimentation, then apply the learned rules to beat its challenges within the step budget.
- **Agent input:** A JSON game state containing the observation, level, lives, steps remaining, status, legal actions, and interaction history; no semantic description of the hidden rules.
- **Required output:** A legal action sequence that wins the game
- **Evaluation:** Score each run by whether the game is beaten within its fixed step budget; average wins over repeated runs for the game, then average games within the difficulty tier.
- **Environment:** Official text-game server exposed through the DiG-bench API or MCP and a declared model harness; humans and models receive identical states, actions, and step budgets. Some games offer a declared creative mode for unmetered experiments.
- **Metric:** win rate · maximize ↑ · fraction of runs
- **Prior reference:** No matched task-level reference published
- **Current SOTA:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **SOTA note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
- **Integrity note:** P-series task is public and may be used for development, so report public-versus-private evaluation separately. Pin the game, server, harness, model, prompt, context policy, run count, and step budget.

<a id="dig-bench-p-21"></a>

### DiG-bench P-21 (tier 7)

- **ID / source:** `dig-bench-p-21` · DiG-bench
- **Question:** Discover P-21's unknown transformation rules and win conditions through experimentation, then apply the learned rules to beat its challenges within the step budget.
- **Agent input:** A JSON game state containing the observation, level, lives, steps remaining, status, legal actions, and interaction history; no semantic description of the hidden rules.
- **Required output:** A legal action sequence that wins the game
- **Evaluation:** Score each run by whether the game is beaten within its fixed step budget; average wins over repeated runs for the game, then average games within the difficulty tier.
- **Environment:** Official text-game server exposed through the DiG-bench API or MCP and a declared model harness; humans and models receive identical states, actions, and step budgets. Some games offer a declared creative mode for unmetered experiments.
- **Metric:** win rate · maximize ↑ · fraction of runs
- **Prior reference:** No matched task-level reference published
- **Current SOTA:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **SOTA note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
- **Integrity note:** P-series task is public and may be used for development, so report public-versus-private evaluation separately. Pin the game, server, harness, model, prompt, context policy, run count, and step budget.

## Maintenance

The machine-readable SOTA snapshot is [`data/discovery-task-sota.json`](../data/discovery-task-sota.json). Regenerate both artifacts after changing the task registry:

```bash
python scripts/render_discovery_task_sota.py
python scripts/render_discovery_task_sota.py --check
```

For a new record, provide the exact task/version, complete system and harness, score, run count or uncertainty when available, resource envelope, and primary result artifact. A suite leaderboard screenshot alone is insufficient for a task-level SOTA claim.
