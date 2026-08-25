# All Discovery Tasks and Current-Record Tracker

> Evidence snapshot: **2026-08-25** · **52 full-contract registry tasks** · **11 TTT-Discover variants** · **442 current Finch task IDs**

This is the single-file lookup for every task in the discovery registry. It records the agent-visible question and input, required output, evaluator, environment, metric, the source suite's own reported result, and a separately researched current-record field.

## SOTA policy

- **Source-reported result is not automatically SOTA.** It records what the suite paper or released artifact achieved.
- **Current record** is assigned only when a live leaderboard, official result dataset, historical record, or later matched-evaluator artifact supports it.
- **Contract incumbent only** means no independent maintained leaderboard or later exact-contract comparison was found. The source result remains useful, but is not labeled global SOTA.
- **Tie / precision unresolved** is used when papers round differently or several systems match at published precision.
- **Suite-level only** means the source publishes an aggregate but no attributable per-task result. The aggregate is shown as context and is never imputed to a task.
- Runtime results are hardware-sensitive; interactive results are harness-, budget-, game-version-, and run-count-sensitive.
- `Current` means best located from primary sources by the snapshot date, not a guarantee that an unpublished or incomparable result does not exist.

### Coverage

| Evidence scope | Tasks | Interpretation |
|---|---:|---|
| Externally cross-checked current record / tie / ambiguity | 12 | Live leaderboards, official result datasets, historical records, or matched artifacts |
| Source-reported contract incumbent only | 16 | Released result exists, but no independent exact-contract current record was located |
| Suite-level only | 24 | ARC-AGI-3 and DiG-bench publish no attributable per-task result table |

### Source-suite snapshot

| Source | Launch | GitHub stars | Tasks here | Current best evidence |
|---|---:|---:|---:|---|
| [SimpleTES](https://github.com/wq-will/SimpleTES) | 2026-04 | 169 | 28 | 28 source-reported results; 12 tasks cross-checked against other systems or records |
| [ARC-AGI-3](https://arcprize.org/arc-agi/3/) | 2026-04-22 | 69 | 3 | Tycho 100.0% public-demo aggregate; community self-reported, no attributable per-game table |
| [DiG-bench](https://digbench.ai/) | 2026-08-12 | 24 | 21 | Claude Opus 5 basic harness: 50/70 games; no per-game table |

GitHub stars are the repository snapshots recorded on 2026-08-25; they are popularity metadata, not quality or SOTA evidence.

## Master SOTA index

| # | Discovery task | Domain | Source | SOTA method / status | Model / backbone | Result | Link |
|---:|---|---|---|---|---|---|---|
| 1 | [Asymmetric matrix multiplication](#asymmetric-matrix-multiplication) | ai-foundations | SimpleTES | SimpleTES (source incumbent; global SOTA unverified) | gpt-oss-120b | 0.44 ↓ (source incumbent; SOTA unverified) | [evidence](https://arxiv.org/html/2604.19341) |
| 2 | [Batched cumulative sum](#batched-cumulative-sum) | ai-foundations | SimpleTES | SimpleTES (source incumbent; global SOTA unverified) | gpt-oss-120b | 0.104 ↓ (source incumbent; SOTA unverified) | [evidence](https://arxiv.org/html/2604.19341) |
| 3 | [Cassini gravity-assist trajectory](#cassini-trajectory) | astrodynamics | SimpleTES | SimpleTES (source incumbent; global SOTA unverified) | gpt-oss-120b | 0.820129 ↓ (source incumbent; SOTA unverified) | [evidence](https://arxiv.org/html/2604.19341) |
| 4 | [Circle packing in a unit square (n=26)](#circle-packing-n26) | mathematics-discovery | SimpleTES | AlphaEvolve (live-board tie) | Not disclosed for leaderboard row | 2.6359830849 ↑ (current record) | [evidence](https://einsteinarena.com/problems/circle-packing) |
| 5 | [Circle packing in a unit square (n=32)](#circle-packing-n32) | mathematics-discovery | SimpleTES | nanodiscover (EFT) | Qwen3-8B / Finch-8B | 2.939573 ↑ (tie) | [evidence](https://arxiv.org/html/2606.29082) |
| 6 | [Erdős minimum overlap](#erdos-minimum-overlap) | mathematics-discovery | SimpleTES | CodexProLong | Not disclosed by leaderboard | 0.38085857 ↓ (current record) | [evidence](https://einsteinarena.com/problems/erdos-min-overlap) |
| 7 | [Galileo gravity-assist trajectory](#galileo-trajectory) | astrodynamics | SimpleTES | SimpleTES (source incumbent; global SOTA unverified) | gpt-oss-120b | 0.795108 ↓ (source incumbent; SOTA unverified) | [evidence](https://arxiv.org/html/2604.19341) |
| 8 | [Hadamard maximum determinant (n=29)](#hadamard-determinant-n29) | mathematics-discovery | SimpleTES | Orrick et al. construction; matched by SimpleTES | Human construction / gpt-oss-120b match | 0.935673 ↑ (tie) | [evidence](https://maths-people.anu.edu.au/~brent/maxdet/order29/) |
| 9 | [LASSO regularization path](#lasso-regularization-path) | scientific-algorithms | SimpleTES | SimpleTES (source incumbent; global SOTA unverified) | gpt-oss-120b | 2502.3 ↓ (source incumbent; SOTA unverified) | [evidence](https://arxiv.org/html/2604.19341) |
| 10 | [Mariner 10 gravity-assist trajectory](#mariner-10-trajectory) | astrodynamics | SimpleTES | SimpleTES (source incumbent; global SOTA unverified) | gpt-oss-120b | 0.326993 ↓ (source incumbent; SOTA unverified) | [evidence](https://arxiv.org/html/2604.19341) |
| 11 | [Rosetta gravity-assist trajectory](#rosetta-trajectory) | astrodynamics | SimpleTES | SimpleTES (source incumbent; global SOTA unverified) | gpt-oss-120b | 1.552968 ↓ (source incumbent; SOTA unverified) | [evidence](https://arxiv.org/html/2604.19341) |
| 12 | [Scaling-law discovery: domain mix](#scaling-law-domain-mix) | ai-foundations | SimpleTES | SLDAgent | Gemini-3-Pro-Preview | 0.993529 ↑ (current record) | [evidence](https://huggingface.co/datasets/pkuHaowei/scaling_law_discovery_results) |
| 13 | [Scaling-law discovery: learning rate and batch size](#scaling-law-lr-bsz) | ai-foundations | SimpleTES | SLDAgent | GPT-5 | 0.847918 ↑ (current record) | [evidence](https://huggingface.co/datasets/pkuHaowei/scaling_law_discovery_results) |
| 14 | [Scaling-law discovery: parallel](#scaling-law-parallel) | ai-foundations | SimpleTES | Unresolved: SLDAgent vs SimpleTES | Claude Sonnet 4.5 / gpt-oss-120b | Unresolved at published precision (0.999971 vs 1.0) | [evidence](https://huggingface.co/datasets/pkuHaowei/scaling_law_discovery_results) |
| 15 | [Scaling-law discovery: U-shape](#scaling-law-u-shape) | ai-foundations | SimpleTES | Aider | GPT-5 | 0.38070320345369735 ↑ (current record) | [evidence](https://huggingface.co/datasets/pkuHaowei/scaling_law_discovery_results) |
| 16 | [Second autocorrelation inequality](#second-autocorrelation-inequality) | mathematics-discovery | SimpleTES | ClaudeExplorer | Not disclosed by leaderboard | 0.96359 ↑ (current record) | [evidence](https://einsteinarena.com/problems/second-autocorrelation-inequality) |
| 17 | [Single-cell RNA-seq denoising](#single-cell-rna-denoising) | scientific-algorithms | SimpleTES | SimpleTES (source incumbent; global SOTA unverified) | gpt-oss-120b | 0.74 ↑ (source incumbent; SOTA unverified) | [evidence](https://arxiv.org/html/2604.19341) |
| 18 | [Sum-Difference problem](#sum-difference-problem) | mathematics-discovery | SimpleTES | MLEvolve | Gemini-3.1-Pro-preview | 1.1901774219 ↑ (current record) | [evidence](https://github.com/InternScience/MLEvolve) |
| 19 | [Superconducting qubit routing](#superconducting-qubit-routing) | quantum-compilation | SimpleTES | SimpleTES (source incumbent; global SOTA unverified) | gpt-oss-120b | 15147 ↓ (source incumbent; SOTA unverified) | [evidence](https://arxiv.org/html/2604.19341) |
| 20 | [Third autocorrelation inequality](#third-autocorrelation-inequality) | mathematics-discovery | SimpleTES | Poolish | Not disclosed by leaderboard | 1.45080664 ↓ (current record) | [evidence](https://einsteinarena.com/problems/third-autocorrelation-inequality) |
| 21 | [TriMul GPU kernel](#trimul-kernel) | ai-foundations | SimpleTES | K-Search | GPT-5.2 (released GPUMode default) | 1.028 ↓ (current record) | [evidence](https://github.com/caoshiyi/K-Search) |
| 22 | [Voyager 2 gravity-assist trajectory](#voyager-2-trajectory) | astrodynamics | SimpleTES | SimpleTES (source incumbent; global SOTA unverified) | gpt-oss-120b | 3.430214 ↓ (source incumbent; SOTA unverified) | [evidence](https://arxiv.org/html/2604.19341) |
| 23 | [ZAPBench whole-brain forecasting (H=1)](#zapbench-h1) | scientific-algorithms | SimpleTES | SimpleTES (source incumbent; global SOTA unverified) | gpt-oss-120b | 0.0165 ↓ (source incumbent; SOTA unverified) | [evidence](https://arxiv.org/html/2604.19341) |
| 24 | [ZAPBench whole-brain forecasting (H=4)](#zapbench-h4) | scientific-algorithms | SimpleTES | SimpleTES (source incumbent; global SOTA unverified) | gpt-oss-120b | 0.0211 ↓ (source incumbent; SOTA unverified) | [evidence](https://arxiv.org/html/2604.19341) |
| 25 | [ZAPBench whole-brain forecasting (H=8)](#zapbench-h8) | scientific-algorithms | SimpleTES | SimpleTES (source incumbent; global SOTA unverified) | gpt-oss-120b | 0.023 ↓ (source incumbent; SOTA unverified) | [evidence](https://arxiv.org/html/2604.19341) |
| 26 | [ZAPBench whole-brain forecasting (H=16)](#zapbench-h16) | scientific-algorithms | SimpleTES | SimpleTES (source incumbent; global SOTA unverified) | gpt-oss-120b | 0.0251 ↓ (source incumbent; SOTA unverified) | [evidence](https://arxiv.org/html/2604.19341) |
| 27 | [ZAPBench whole-brain forecasting (H=32)](#zapbench-h32) | scientific-algorithms | SimpleTES | SimpleTES (source incumbent; global SOTA unverified) | gpt-oss-120b | 0.0259 ↓ (source incumbent; SOTA unverified) | [evidence](https://arxiv.org/html/2604.19341) |
| 28 | [Zoned neutral-atom compilation](#zoned-neutral-atom-compilation) | quantum-compilation | SimpleTES | SimpleTES (source incumbent; global SOTA unverified) | gpt-oss-120b | 19507.5 ↓ (source incumbent; SOTA unverified) | [evidence](https://arxiv.org/html/2604.19341) |
| 29 | [ARC-AGI-3 ls20 (Agent reasoning)](#arc-agi-3-ls20) | interactive-world-discovery | ARC-AGI-3 | No per-task SOTA published (suite aggregate: Tycho) | Not disclosed | No per-task result; suite 100.0 percent | [evidence](https://arcprize.org/leaderboard/community) |
| 30 | [ARC-AGI-3 ft09 (Elementary Logic)](#arc-agi-3-ft09) | interactive-world-discovery | ARC-AGI-3 | No per-task SOTA published (suite aggregate: Tycho) | Not disclosed | No per-task result; suite 100.0 percent | [evidence](https://arcprize.org/leaderboard/community) |
| 31 | [ARC-AGI-3 vc33 (Orchestration)](#arc-agi-3-vc33) | interactive-world-discovery | ARC-AGI-3 | No per-task SOTA published (suite aggregate: Tycho) | Not disclosed | No per-task result; suite 100.0 percent | [evidence](https://arcprize.org/leaderboard/community) |
| 32 | [DiG-bench P-1 (tier 1)](#dig-bench-p-1) | interactive-world-discovery | DiG-bench | No per-task SOTA published (suite aggregate: basic harness) | Claude Opus 5 | No per-task result; suite 50 games out of 70 | [evidence](https://arxiv.org/html/2608.12593) |
| 33 | [DiG-bench P-2 (tier 1)](#dig-bench-p-2) | interactive-world-discovery | DiG-bench | No per-task SOTA published (suite aggregate: basic harness) | Claude Opus 5 | No per-task result; suite 50 games out of 70 | [evidence](https://arxiv.org/html/2608.12593) |
| 34 | [DiG-bench P-3 (tier 1)](#dig-bench-p-3) | interactive-world-discovery | DiG-bench | No per-task SOTA published (suite aggregate: basic harness) | Claude Opus 5 | No per-task result; suite 50 games out of 70 | [evidence](https://arxiv.org/html/2608.12593) |
| 35 | [DiG-bench P-4 (tier 2)](#dig-bench-p-4) | interactive-world-discovery | DiG-bench | No per-task SOTA published (suite aggregate: basic harness) | Claude Opus 5 | No per-task result; suite 50 games out of 70 | [evidence](https://arxiv.org/html/2608.12593) |
| 36 | [DiG-bench P-5 (tier 2)](#dig-bench-p-5) | interactive-world-discovery | DiG-bench | No per-task SOTA published (suite aggregate: basic harness) | Claude Opus 5 | No per-task result; suite 50 games out of 70 | [evidence](https://arxiv.org/html/2608.12593) |
| 37 | [DiG-bench P-6 (tier 2)](#dig-bench-p-6) | interactive-world-discovery | DiG-bench | No per-task SOTA published (suite aggregate: basic harness) | Claude Opus 5 | No per-task result; suite 50 games out of 70 | [evidence](https://arxiv.org/html/2608.12593) |
| 38 | [DiG-bench P-7 (tier 3)](#dig-bench-p-7) | interactive-world-discovery | DiG-bench | No per-task SOTA published (suite aggregate: basic harness) | Claude Opus 5 | No per-task result; suite 50 games out of 70 | [evidence](https://arxiv.org/html/2608.12593) |
| 39 | [DiG-bench P-8 (tier 3)](#dig-bench-p-8) | interactive-world-discovery | DiG-bench | No per-task SOTA published (suite aggregate: basic harness) | Claude Opus 5 | No per-task result; suite 50 games out of 70 | [evidence](https://arxiv.org/html/2608.12593) |
| 40 | [DiG-bench P-9 (tier 3)](#dig-bench-p-9) | interactive-world-discovery | DiG-bench | No per-task SOTA published (suite aggregate: basic harness) | Claude Opus 5 | No per-task result; suite 50 games out of 70 | [evidence](https://arxiv.org/html/2608.12593) |
| 41 | [DiG-bench P-10 (tier 4)](#dig-bench-p-10) | interactive-world-discovery | DiG-bench | No per-task SOTA published (suite aggregate: basic harness) | Claude Opus 5 | No per-task result; suite 50 games out of 70 | [evidence](https://arxiv.org/html/2608.12593) |
| 42 | [DiG-bench P-11 (tier 4)](#dig-bench-p-11) | interactive-world-discovery | DiG-bench | No per-task SOTA published (suite aggregate: basic harness) | Claude Opus 5 | No per-task result; suite 50 games out of 70 | [evidence](https://arxiv.org/html/2608.12593) |
| 43 | [DiG-bench P-12 (tier 4)](#dig-bench-p-12) | interactive-world-discovery | DiG-bench | No per-task SOTA published (suite aggregate: basic harness) | Claude Opus 5 | No per-task result; suite 50 games out of 70 | [evidence](https://arxiv.org/html/2608.12593) |
| 44 | [DiG-bench P-13 (tier 5)](#dig-bench-p-13) | interactive-world-discovery | DiG-bench | No per-task SOTA published (suite aggregate: basic harness) | Claude Opus 5 | No per-task result; suite 50 games out of 70 | [evidence](https://arxiv.org/html/2608.12593) |
| 45 | [DiG-bench P-14 (tier 5)](#dig-bench-p-14) | interactive-world-discovery | DiG-bench | No per-task SOTA published (suite aggregate: basic harness) | Claude Opus 5 | No per-task result; suite 50 games out of 70 | [evidence](https://arxiv.org/html/2608.12593) |
| 46 | [DiG-bench P-15 (tier 5)](#dig-bench-p-15) | interactive-world-discovery | DiG-bench | No per-task SOTA published (suite aggregate: basic harness) | Claude Opus 5 | No per-task result; suite 50 games out of 70 | [evidence](https://arxiv.org/html/2608.12593) |
| 47 | [DiG-bench P-16 (tier 6)](#dig-bench-p-16) | interactive-world-discovery | DiG-bench | No per-task SOTA published (suite aggregate: basic harness) | Claude Opus 5 | No per-task result; suite 50 games out of 70 | [evidence](https://arxiv.org/html/2608.12593) |
| 48 | [DiG-bench P-17 (tier 6)](#dig-bench-p-17) | interactive-world-discovery | DiG-bench | No per-task SOTA published (suite aggregate: basic harness) | Claude Opus 5 | No per-task result; suite 50 games out of 70 | [evidence](https://arxiv.org/html/2608.12593) |
| 49 | [DiG-bench P-18 (tier 6)](#dig-bench-p-18) | interactive-world-discovery | DiG-bench | No per-task SOTA published (suite aggregate: basic harness) | Claude Opus 5 | No per-task result; suite 50 games out of 70 | [evidence](https://arxiv.org/html/2608.12593) |
| 50 | [DiG-bench P-19 (tier 7)](#dig-bench-p-19) | interactive-world-discovery | DiG-bench | No per-task SOTA published (suite aggregate: basic harness) | Claude Opus 5 | No per-task result; suite 50 games out of 70 | [evidence](https://arxiv.org/html/2608.12593) |
| 51 | [DiG-bench P-20 (tier 7)](#dig-bench-p-20) | interactive-world-discovery | DiG-bench | No per-task SOTA published (suite aggregate: basic harness) | Claude Opus 5 | No per-task result; suite 50 games out of 70 | [evidence](https://arxiv.org/html/2608.12593) |
| 52 | [DiG-bench P-21 (tier 7)](#dig-bench-p-21) | interactive-world-discovery | DiG-bench | No per-task SOTA published (suite aggregate: basic harness) | Claude Opus 5 | No per-task result; suite 50 games out of 70 | [evidence](https://arxiv.org/html/2608.12593) |

## Complete TTT-Discover and Finch task catalogues

> **11 TTT-Discover published task variants** + **442 current Finch Collection task IDs**. These are catalogue entries, not additional unique benchmark claims: TTT-Discover is an evaluated system, and Finch is a trajectory collection assembled from upstream benchmarks.

This section repairs an earlier source bias: TTT-Discover and Finch were previously shown only as comparison systems on a few SimpleTES rows. Their own published/evolving task sets are now enumerated.

### TTT-Discover: every published attempted task

Launch: **2026-01-22** · repository stars: **628** (snapshot 2026-08-25) · model: **OpenAI gpt-oss-120b** · [paper](https://arxiv.org/abs/2601.16175) · [code](https://github.com/test-time-training/discover) · [project page](https://test-time-training.github.io/discover/)

The paper says it reports every attempted problem. Hardware- and dataset-specific evaluator contracts are kept as separate variants, giving 3 mathematics + 4 TriMul hardware + 2 AtCoder + 2 biology = 11.

| # | Task | Domain | SOTA method / status | Model / backbone | Result | Link |
|---:|---|---|---|---|---|---|
| 1 | [Erdős minimum overlap](#ttt-discover-erdos-minimum-overlap) | Mathematics discovery | CodexProLong | Not disclosed by leaderboard | 0.38085857 ↓ (live-leaderboard-best) | [evidence](https://einsteinarena.com/problems/erdos-min-overlap) |
| 2 | [First autocorrelation inequality (AC1)](#ttt-discover-first-autocorrelation-inequality) | Mathematics discovery | CodexProLong | Not disclosed by leaderboard | 1.50274365 ↓ (live-leaderboard-best) | [evidence](https://einsteinarena.com/problems/first-autocorrelation-inequality) |
| 3 | [Second autocorrelation inequality (AC2)](#ttt-discover-second-autocorrelation-inequality) | Mathematics discovery | ClaudeExplorer | Not disclosed by leaderboard | 0.96359 ↑ (live-leaderboard-best) | [evidence](https://einsteinarena.com/problems/second-autocorrelation-inequality) |
| 4 | [GPUMode TriMul — A100](#ttt-discover-trimul-a100) | GPU kernel engineering | TTT-Discover (source result; later SOTA unverified) | OpenAI gpt-oss-120b | 2198 ↓ (source result) | [evidence](https://test-time-training.github.io/discover/) |
| 5 | [GPUMode TriMul — H100](#ttt-discover-trimul-h100) | GPU kernel engineering | K-Search | GPT-5.2 (released GPUMode default) | 1028 ↓ (matched-evaluator-artifact) | [evidence](https://github.com/caoshiyi/K-Search) |
| 6 | [GPUMode TriMul — B200](#ttt-discover-trimul-b200) | GPU kernel engineering | TTT-Discover (source result; later SOTA unverified) | OpenAI gpt-oss-120b | 905 ↓ (source result) | [evidence](https://test-time-training.github.io/discover/) |
| 7 | [GPUMode TriMul — MI300X](#ttt-discover-trimul-mi300x) | GPU kernel engineering | TTT-Discover (source result; later SOTA unverified) | OpenAI gpt-oss-120b | 1596 ↓ (source result) | [evidence](https://test-time-training.github.io/discover/) |
| 8 | [AtCoder Heuristic Contest 039 — Purifying Machine](#ttt-discover-ahc039) | Algorithm engineering | TTT-Discover | OpenAI gpt-oss-120b | 567062 ↑ (paper-reported-sota) | [evidence](https://test-time-training.github.io/discover/) |
| 9 | [AtCoder Heuristic Contest 058 — Scheduling](#ttt-discover-ahc058) | Algorithm engineering | TTT-Discover | OpenAI gpt-oss-120b | 848414228 ↑ (paper-reported-sota) | [evidence](https://test-time-training.github.io/discover/) |
| 10 | [Single-cell RNA-seq denoising — PBMC](#ttt-discover-scrna-pbmc) | Biological discovery | TTT-Discover / SimpleTES | gpt-oss-120b | 0.71 ↑ (tie-at-published-precision) | [evidence](https://arxiv.org/abs/2604.19341) |
| 11 | [Single-cell RNA-seq denoising — Tabula Muris Senis Lung](#ttt-discover-scrna-tabula) | Biological discovery | SimpleTES | gpt-oss-120b | 0.74 ↑ (matched-evaluator-paper-result) | [evidence](https://arxiv.org/abs/2604.19341) |

#### TTT-Discover task contracts

<a id="ttt-discover-erdos-minimum-overlap"></a>

##### Erdős minimum overlap

- **Question:** Construct a normalized nonnegative function that minimizes the largest overlap with a translated copy.
- **Agent input:** The mathematical problem, an executable scorer, and the evolving archive/history of candidate constructions.
- **Required output:** A candidate construction encoded by executable program/state data.
- **Evaluation:** The released deterministic verifier evaluates the maximum translated overlap under the task normalization.
- **Environment:** TTT-Discover mathematics environment; Python/JAX execution with evaluator feedback and Tinker-based test-time RL.
- **Metric:** maximum overlap · minimize ↓ · normalized overlap
- **TTT-Discover result:** 0.380876
- **Current SOTA method / status:** CodexProLong
- **Model / backbone:** Not disclosed by leaderboard
- **Current result:** 0.38085857 ↓ (live-leaderboard-best)
- **Primary evidence:** [result source](https://einsteinarena.com/problems/erdos-min-overlap)
- **Current-record status:** `live-leaderboard-best` as of 2026-08-25

<a id="ttt-discover-first-autocorrelation-inequality"></a>

##### First autocorrelation inequality (AC1)

- **Question:** Find a nonnegative function that minimizes the upper-bound constant in the first autocorrelation inequality.
- **Agent input:** The inequality, discretization, executable convolution scorer, and candidate-search feedback.
- **Required output:** A nonnegative discretized function or program that generates it.
- **Evaluation:** The verifier computes the normalized maximum autoconvolution value; lower is better.
- **Environment:** TTT-Discover mathematics environment; Python/JAX execution with evaluator feedback and Tinker-based test-time RL.
- **Metric:** AC1 upper-bound constant · minimize ↓ · normalized constant
- **TTT-Discover result:** 1.50287
- **Current SOTA method / status:** CodexProLong
- **Model / backbone:** Not disclosed by leaderboard
- **Current result:** 1.50274365 ↓ (live-leaderboard-best)
- **Primary evidence:** [result source](https://einsteinarena.com/problems/first-autocorrelation-inequality)
- **Current-record status:** `live-leaderboard-best` as of 2026-08-25

<a id="ttt-discover-second-autocorrelation-inequality"></a>

##### Second autocorrelation inequality (AC2)

- **Question:** Construct a function that maximizes the lower-bound constant in the second autocorrelation inequality.
- **Agent input:** The inequality, discretization, executable scorer, and candidate-search feedback.
- **Required output:** A candidate discretized function or generating program.
- **Evaluation:** The released verifier evaluates the task's normalized lower-bound constant; higher is better.
- **Environment:** TTT-Discover mathematics environment; Python/JAX execution with evaluator feedback and Tinker-based test-time RL.
- **Metric:** AC2 lower-bound constant · maximize ↑ · normalized constant
- **TTT-Discover result:** 0.9591
- **Current SOTA method / status:** ClaudeExplorer
- **Model / backbone:** Not disclosed by leaderboard
- **Current result:** 0.96359 ↑ (live-leaderboard-best)
- **Primary evidence:** [result source](https://einsteinarena.com/problems/second-autocorrelation-inequality)
- **Current-record status:** `live-leaderboard-best` as of 2026-08-25

<a id="ttt-discover-trimul-a100"></a>

##### GPUMode TriMul — A100

- **Question:** Implement a correct high-performance triangular-multiplication kernel for the supplied AlphaFold-style workload on NVIDIA A100.
- **Agent input:** Reference PyTorch operator, tensor shapes/dtypes, correctness tests, benchmark harness, and runtime feedback.
- **Required output:** Executable Triton/Python kernel implementation.
- **Evaluation:** GPUMode first checks numerical correctness and then measures latency on A100; lower runtime is better.
- **Environment:** GPUMode TriMul harness on NVIDIA A100; hardware-specific results are not interchangeable.
- **Metric:** execution time · minimize ↓ · microseconds
- **TTT-Discover result:** 2198
- **Current SOTA method / status:** TTT-Discover (source result; later SOTA unverified)
- **Model / backbone:** OpenAI gpt-oss-120b
- **Current result:** 2198 ↓ (source result)
- **Primary evidence:** [result source](https://test-time-training.github.io/discover/)
- **Current-record status:** `official-result-only` as of 2026-08-25

<a id="ttt-discover-trimul-h100"></a>

##### GPUMode TriMul — H100

- **Question:** Implement a correct high-performance triangular-multiplication kernel for the supplied AlphaFold-style workload on NVIDIA H100.
- **Agent input:** Reference PyTorch operator, tensor shapes/dtypes, correctness tests, benchmark harness, and runtime feedback.
- **Required output:** Executable Triton/Python kernel implementation.
- **Evaluation:** GPUMode first checks numerical correctness and then measures latency on H100; lower runtime is better.
- **Environment:** GPUMode TriMul harness on NVIDIA H100; hardware-specific results are not interchangeable.
- **Metric:** execution time · minimize ↓ · microseconds
- **TTT-Discover result:** 1161
- **Current SOTA method / status:** K-Search
- **Model / backbone:** GPT-5.2 (released GPUMode default)
- **Current result:** 1028 ↓ (matched-evaluator-artifact)
- **Primary evidence:** [result source](https://github.com/caoshiyi/K-Search)
- **Current-record status:** `matched-evaluator-artifact` as of 2026-08-25

<a id="ttt-discover-trimul-b200"></a>

##### GPUMode TriMul — B200

- **Question:** Implement a correct high-performance triangular-multiplication kernel for the supplied AlphaFold-style workload on NVIDIA B200.
- **Agent input:** Reference PyTorch operator, tensor shapes/dtypes, correctness tests, benchmark harness, and runtime feedback.
- **Required output:** Executable Triton/Python kernel implementation.
- **Evaluation:** GPUMode first checks numerical correctness and then measures latency on B200; lower runtime is better.
- **Environment:** GPUMode TriMul harness on NVIDIA B200; the published kernel was trained with H100 reward and evaluated on B200.
- **Metric:** execution time · minimize ↓ · microseconds
- **TTT-Discover result:** 905
- **Current SOTA method / status:** TTT-Discover (source result; later SOTA unverified)
- **Model / backbone:** OpenAI gpt-oss-120b
- **Current result:** 905 ↓ (source result)
- **Primary evidence:** [result source](https://test-time-training.github.io/discover/)
- **Current-record status:** `official-result-only` as of 2026-08-25

<a id="ttt-discover-trimul-mi300x"></a>

##### GPUMode TriMul — MI300X

- **Question:** Implement a correct high-performance triangular-multiplication kernel for the supplied AlphaFold-style workload on AMD MI300X.
- **Agent input:** Reference operator, tensor shapes/dtypes, correctness tests, benchmark harness, and runtime feedback.
- **Required output:** Executable GPU kernel implementation compatible with the competition harness.
- **Evaluation:** GPUMode first checks numerical correctness and then measures latency on MI300X; lower runtime is better.
- **Environment:** GPUMode TriMul harness on AMD MI300X; the published kernel was trained with H100 reward and evaluated on MI300X.
- **Metric:** execution time · minimize ↓ · microseconds
- **TTT-Discover result:** 1596
- **Current SOTA method / status:** TTT-Discover (source result; later SOTA unverified)
- **Model / backbone:** OpenAI gpt-oss-120b
- **Current result:** 1596 ↓ (source result)
- **Primary evidence:** [result source](https://test-time-training.github.io/discover/)
- **Current-record status:** `official-result-only` as of 2026-08-25

<a id="ttt-discover-ahc039"></a>

##### AtCoder Heuristic Contest 039 — Purifying Machine

- **Question:** Write a solver that places and combines rectangular purification operations to maximize the AHC039 judge score.
- **Agent input:** Contest statement, instances, starter solver, time limit, and repeated judge feedback.
- **Required output:** A complete contest solver accepted by the AHC039 judge.
- **Evaluation:** The official AtCoder/ALE-Bench scorer computes the contest score across the evaluation instances; higher is better.
- **Environment:** AtCoder-compatible C++ solver environment and heuristic-contest judge used by the released reproduction.
- **Metric:** AHC039 judge score · maximize ↑ · points
- **TTT-Discover result:** 567062
- **Current SOTA method / status:** TTT-Discover
- **Model / backbone:** OpenAI gpt-oss-120b
- **Current result:** 567062 ↑ (paper-reported-sota)
- **Primary evidence:** [result source](https://test-time-training.github.io/discover/)
- **Current-record status:** `paper-reported-sota` as of 2026-08-25

<a id="ttt-discover-ahc058"></a>

##### AtCoder Heuristic Contest 058 — Scheduling

- **Question:** Write a scheduling solver that maximizes the AHC058 judge score under the contest constraints.
- **Agent input:** Contest statement, instances, starter solver, time limit, and repeated judge feedback.
- **Required output:** A complete contest solver accepted by the AHC058 judge.
- **Evaluation:** The official AtCoder/ALE-Bench scorer computes the contest score across the evaluation instances; higher is better.
- **Environment:** AtCoder-compatible C++ solver environment and heuristic-contest judge used by the released reproduction.
- **Metric:** AHC058 judge score · maximize ↑ · points
- **TTT-Discover result:** 848414228
- **Current SOTA method / status:** TTT-Discover
- **Model / backbone:** OpenAI gpt-oss-120b
- **Current result:** 848414228 ↑ (paper-reported-sota)
- **Primary evidence:** [result source](https://test-time-training.github.io/discover/)
- **Current-record status:** `paper-reported-sota` as of 2026-08-25

<a id="ttt-discover-scrna-pbmc"></a>

##### Single-cell RNA-seq denoising — PBMC

- **Question:** Discover a denoising transformation that reconstructs held-out PBMC single-cell RNA counts.
- **Agent input:** Training data and a starter denoising program; PBMC is held out for final evaluation.
- **Required output:** Executable Python denoising algorithm producing the required matrix predictions.
- **Evaluation:** The OpenProblems-derived evaluator averages normalized MSE and Poisson components; higher is better.
- **Environment:** Python scientific-computing environment with OpenProblems v1.0.0-compatible data/evaluator.
- **Metric:** denoising score · maximize ↑ · mean normalized score
- **TTT-Discover result:** 0.71
- **Current SOTA method / status:** TTT-Discover / SimpleTES
- **Model / backbone:** gpt-oss-120b
- **Current result:** 0.71 ↑ (tie-at-published-precision)
- **Primary evidence:** [result source](https://arxiv.org/abs/2604.19341)
- **Current-record status:** `tie-at-published-precision` as of 2026-08-25

<a id="ttt-discover-scrna-tabula"></a>

##### Single-cell RNA-seq denoising — Tabula Muris Senis Lung

- **Question:** Discover a denoising transformation that reconstructs held-out Tabula Muris Senis Lung single-cell RNA counts.
- **Agent input:** Training data and a starter denoising program; Tabula is held out for final evaluation.
- **Required output:** Executable Python denoising algorithm producing the required matrix predictions.
- **Evaluation:** The OpenProblems-derived evaluator averages normalized MSE and Poisson components; higher is better.
- **Environment:** Python scientific-computing environment with OpenProblems v1.0.0-compatible data/evaluator.
- **Metric:** denoising score · maximize ↑ · mean normalized score
- **TTT-Discover result:** 0.73
- **Current SOTA method / status:** SimpleTES
- **Model / backbone:** gpt-oss-120b
- **Current result:** 0.74 ↑ (matched-evaluator-paper-result)
- **Primary evidence:** [result source](https://arxiv.org/abs/2604.19341)
- **Current-record status:** `matched-evaluator-paper-result` as of 2026-08-25

### Finch Collection: current 442-task dataset snapshot

Paper launch: **2026-06-27** · repository stars: **28** (snapshot 2026-08-25) · [paper](https://arxiv.org/abs/2606.29082) · [code](https://github.com/Open-Galapagos/evolution-fine-tuning) · [dataset](https://huggingface.co/datasets/minnesotanlp/Finch-Collection)

The paper freezes **371 tasks / 156,731 trajectories**. The official dataset card and scanned Parquet revision now contain **442 tasks / 217,780 trajectories**. The official dataset card reports a 71-task expansion from 371 to 442. arXiv v1 identifies 370 task IDs: its summary says 47 numerical tasks, but Appendix Table 12 lists only 46. Therefore 65 current numerical IDs cannot be split into the one omitted v1 seed plus 64 additions from public artifacts alone; they are explicitly marked unresolved rather than guessed.

Finch is not itself the evaluator or the current SOTA for every row. Each task retains its upstream benchmark/evaluator; `current_dataset_rows` is trajectory coverage, not a score.
Because the released collection has no 442-row SOTA/model table, every Finch row below says so explicitly and links to the dataset provenance instead of guessing a winner from trajectory logs.

#### Group counts and evaluator contracts

| Task group | Paper v1 | Current dataset | Agent question / evaluation contract |
|---|---:|---:|---|
| Competitive Programming | 172 | 172 | Write or improve a complete solver for a Frontier-CS optimization, constructive, or interactive programming problem. Evaluator: Task-specific deterministic or interactive judge; objectives include score, query count, cost, makespan, or construction quality. |
| Constructive Search | 2 | 2 | Improve a program that searches for a high-quality construction or function minimum. Evaluator: OpenEvolve task evaluator checks constraints and computes the objective. |
| GPU Kernel Optimization | 4 | 4 | Implement a faster correct GPU kernel for the specified workload. Evaluator: GPUMode checks correctness and benchmarks latency on the named hardware contract. |
| Heuristic Optimization | 35 | 38 | Improve a solver for an AtCoder Heuristic Contest problem. Evaluator: ALE-Bench executes the official AtCoder-compatible scorer across its task instances. |
| Mathematical Discovery | 28 | 32 | Discover a better mathematical construction for an open-ended extremal problem. Evaluator: A deterministic task-specific verifier checks validity and computes the continuous extremal objective. |
| Numerical Algorithm Optimization | 47 | 111 | Optimize a general-purpose numerical routine without changing its required behavior. Evaluator: AlgoTune first checks numerical correctness against the reference and then measures speedup/runtime. |
| SR - Bio Pop Growth | 24 | 24 | Discover a symbolic equation that explains a biological population-growth dataset. Evaluator: LLM-SRBench evaluates predictive fit and task validity with its deterministic data split. |
| SR - Chem Reaction | 12 | 12 | Discover a symbolic equation that explains a chemical-reaction kinetics dataset. Evaluator: LLM-SRBench evaluates predictive fit and task validity with its deterministic data split. |
| SR - Physics Oscillation | 44 | 44 | Discover a symbolic equation that explains a physical-oscillation dataset. Evaluator: LLM-SRBench evaluates predictive fit and task validity with its deterministic data split. |
| Single-cell RNA Denoising | 3 | 3 | Improve an executable denoising method for single-cell RNA-seq counts. Evaluator: OpenProblems-derived evaluator combines normalized reconstruction metrics including MSE and Poisson score. |

#### All current Finch task IDs

Membership labels distinguish IDs explicitly recoverable from arXiv v1 from the expanded dataset. `unresolved-paper-v1-or-expansion` is deliberate: the paper says 47 numerical tasks but prints 46 IDs, while the current dataset has 65 additional numerical IDs. One is the omitted paper seed and 64 are post-paper additions; no public artifact identifies which one.

##### Competitive Programming

- **Question:** Write or improve a complete solver for a Frontier-CS optimization, constructive, or interactive programming problem.
- **Input:** Problem statement, starter program, instances or judge interface, execution feedback, and prior search history.
- **Output:** A complete C++ solver accepted and scored by the Frontier-CS judge.
- **Evaluation:** Task-specific deterministic or interactive judge; objectives include score, query count, cost, makespan, or construction quality.
- **Environment:** Frontier-CS algorithmic judge served through Docker; C++ compilation and task-specific limits.
- **Metric family:** Task-specific Frontier-CS judge objective.

| # | Task ID | Upstream source | Paper/expansion status | Trajectories | SOTA method / status | Model | Link | Published description |
|---:|---|---|---|---:|---|---|---|---|
| 1 | `frontier_cs_0` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 532 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Minimize the bounding-rectangle area for a polyomino-packing instance allowing rotations and reflections. |
| 2 | `frontier_cs_1` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 432 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Treasure-packing constructive optimization. |
| 3 | `frontier_cs_10` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 540 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Tree-distance computation problem. |
| 4 | `frontier_cs_101` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 151 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “Circuit” constructive problem. |
| 5 | `frontier_cs_104` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 166 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Interactive “dishonest-student attendance” problem. |
| 6 | `frontier_cs_106` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 178 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Recover a hidden bipartite graph. |
| 7 | `frontier_cs_107` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 159 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Guess a number’s divisor count using interactive queries. |
| 8 | `frontier_cs_108` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 154 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Open a ring lock by aligning arcs with the fewest interactive operations. |
| 9 | `frontier_cs_109` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 167 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Find the longest knight’s tour on a chess sub-board. |
| 10 | `frontier_cs_11` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 457 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Find a palindromic path in a graph or grid. |
| 11 | `frontier_cs_110` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 185 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Fill an 8×148{\times}14 digit grid to maximize the number of 8-directional readable numerals. |
| 12 | `frontier_cs_111` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 163 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Construct a set whose pairwise XORs are all distinct. |
| 13 | `frontier_cs_112` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 147 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “SphereSpread” constructive problem. |
| 14 | `frontier_cs_113` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 160 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Constructive ball-distribution between three baskets. |
| 15 | `frontier_cs_117` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 149 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “Line” constructive problem. |
| 16 | `frontier_cs_119` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 162 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Constructive operator-insertion puzzle. |
| 17 | `frontier_cs_120` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 154 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “Da Bai” interactive problem. |
| 18 | `frontier_cs_121` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 160 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | DNA-matching constructive problem. |
| 19 | `frontier_cs_122` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 144 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Discover a hidden editor’s line width via interactive queries. |
| 20 | `frontier_cs_123` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 171 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Recover a hidden integer through set-membership queries. |
| 21 | `frontier_cs_124` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 159 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “AveragePermutation” constructive problem. |
| 22 | `frontier_cs_125` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 163 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Discover a hidden mineral pair via device queries. |
| 23 | `frontier_cs_127` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 155 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Locate a hidden diamond inside a box through interactive probes. |
| 24 | `frontier_cs_13` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 536 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Detonate a grid robot in ≤3000\leq 3000 steps using interactive cell-marking queries. |
| 25 | `frontier_cs_132` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 169 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Locate a hidden chairman on a graph using a movable robot. |
| 26 | `frontier_cs_133` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 172 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Maximize the brush-stroke area covered by a set of line segments. |
| 27 | `frontier_cs_134` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 170 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Interactive number-guessing variant. |
| 28 | `frontier_cs_135` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 163 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Adversarial interactive problem requiring non-standard strategy. |
| 29 | `frontier_cs_137` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 166 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “Kangaroos” constructive problem. |
| 30 | `frontier_cs_138` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 177 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “Fabulous Fungus Frenzy” constructive problem. |
| 31 | `frontier_cs_14` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 511 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Determine the length of a hidden cycle through interactive queries. |
| 32 | `frontier_cs_140` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 163 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Interactive mineral-deposit identification problem. |
| 33 | `frontier_cs_141` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 180 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “Bakery Survey” constructive problem. |
| 34 | `frontier_cs_142` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 169 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “Ball Game” constructive problem. |
| 35 | `frontier_cs_143` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 191 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Interactive Texas-Hold’em training problem. |
| 36 | `frontier_cs_144` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 171 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Interactively find the median of a hidden array. |
| 37 | `frontier_cs_145` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 172 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Meituan Cup “Number Loop” constructive problem. |
| 38 | `frontier_cs_147` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 162 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | 10000×1000010000{\times}10000 ad-rectangle placement (AHC001-style). |
| 39 | `frontier_cs_148` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 171 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | 50×5050{\times}50 tile-path score maximization (AHC002-style). |
| 40 | `frontier_cs_149` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 158 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Online shortest-path queries on a grid with unknown edge weights. |
| 41 | `frontier_cs_15` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 482 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Minimize lexicographic permutation order using ≤4​n\leq 4n cut-and-swap operations. |
| 42 | `frontier_cs_150` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 177 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Recover a torus-matrix matching given cyclic substrings. |
| 43 | `frontier_cs_151` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 176 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Patrol-route minimization on weighted road grid (AHC005-style). |
| 44 | `frontier_cs_152` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 171 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Select 50 of 1000 orders on a cyclic delivery route (AHC006-style). |
| 45 | `frontier_cs_153` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 173 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Online MST under edge-length uncertainty (AHC003-style). |
| 46 | `frontier_cs_154` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 159 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Pet herding on a 30×3030{\times}30 grid via partitions (AHC008-style). |
| 47 | `frontier_cs_155` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 172 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Robust action-sequence design under stochastic execution (AHC004-style). |
| 48 | `frontier_cs_156` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 117 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Toy-train loop-line track-laying (AHC009-style). |
| 49 | `frontier_cs_157` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 138 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Sliding-tile puzzle to form a target spanning tree (AHC011-style). |
| 50 | `frontier_cs_158` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 165 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Cut a circular cake with ≤K\leq K lines to match a strawberry-count target (AHC012-style). |
| 51 | `frontier_cs_159` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 76 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | RectJoin grid-puzzle constructive problem (AHC014-style). |
| 52 | `frontier_cs_16` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 508 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Identify a hidden chord on a circle through queries. |
| 53 | `frontier_cs_160` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 177 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Tilt-controlled candy-clustering on a 10×1010{\times}10 box (AHC015-style). |
| 54 | `frontier_cs_161` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 175 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Planar-graph TV-network construction (AHC010-style). |
| 55 | `frontier_cs_162` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 167 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Pyramid-ball reorder via adjacent swaps (AHC021-style). |
| 56 | `frontier_cs_163` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 163 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Map-tile coloring/compression preserving adjacencies (AHC024-style). |
| 57 | `frontier_cs_164` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 177 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Cardboard-box carry-out with minimum lifting energy (AHC026-style). |
| 58 | `frontier_cs_165` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 165 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Keyboard-layout design for lucky-string typing. |
| 59 | `frontier_cs_166` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 165 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Dump-truck ground leveling on an N×NN{\times}N grid (AHC034-style). |
| 60 | `frontier_cs_167` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 150 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Rectilinear-polygon mackerel/sardine separation (AHC039-style). |
| 61 | `frontier_cs_168` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 173 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Rooted-tree beauty maximization. |
| 62 | `frontier_cs_169` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 168 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Setsubun-themed Oni/Fuku push-board game. |
| 63 | `frontier_cs_17` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 509 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Interactive permutation-recovery variant. |
| 64 | `frontier_cs_170` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 169 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Cleaning-duty assignment under per-employee targets. |
| 65 | `frontier_cs_171` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 160 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Skating-rink block-placement order-of-visit problem (AHC046-style). |
| 66 | `frontier_cs_174` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 185 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | 3-coloring of a given graph. |
| 67 | `frontier_cs_175` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 182 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | 3-SAT instance (Frontier-CS variant). |
| 68 | `frontier_cs_176` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 187 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | 3-SAT instance (different size class). |
| 69 | `frontier_cs_177` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 188 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | 3-coloring instance (different size class). |
| 70 | `frontier_cs_178` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 177 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | 3-SAT instance (third size class). |
| 71 | `frontier_cs_179` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 163 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Subset-sum instance. |
| 72 | `frontier_cs_180` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 174 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Graph-isomorphism instance. |
| 73 | `frontier_cs_181` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 192 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Binary-QAP instance. |
| 74 | `frontier_cs_182` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 169 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Vertex-cover challenge. |
| 75 | `frontier_cs_183` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 172 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Maximum-independent-set challenge. |
| 76 | `frontier_cs_184` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 168 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Maximum-independent-set challenge (different instance). |
| 77 | `frontier_cs_185` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 170 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Maximum-clique challenge. |
| 78 | `frontier_cs_186` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 174 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Graph-coloring challenge. |
| 79 | `frontier_cs_187` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 167 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Clique-cover challenge. |
| 80 | `frontier_cs_188` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 181 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Approximate longest-common-subsequence challenge. |
| 81 | `frontier_cs_189` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 165 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Approximate edit-distance challenge. |
| 82 | `frontier_cs_192` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 178 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Max-cut instance. |
| 83 | `frontier_cs_193` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 174 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Max-2-SAT instance. |
| 84 | `frontier_cs_2` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 509 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Construct a permutation satisfying problem-specific constraints. |
| 85 | `frontier_cs_203` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 141 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “Chameleon” constructive problem. |
| 86 | `frontier_cs_205` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 117 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Constrained sequence-transformation problem. |
| 87 | `frontier_cs_207` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 159 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Cost-bounded sorting variant. |
| 88 | `frontier_cs_209` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 135 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Recover hidden item weights via comparison queries. |
| 89 | `frontier_cs_210` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 167 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Joint fighter scheduling and base-strike planning. |
| 90 | `frontier_cs_211` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 140 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “Communication Robots” constructive problem. |
| 91 | `frontier_cs_212` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 155 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “I Wanna Cross the Grid” constructive problem. |
| 92 | `frontier_cs_213` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 127 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “moqueve” sequence-shift problem. |
| 93 | `frontier_cs_214` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 144 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “requese” sequence-reversal problem. |
| 94 | `frontier_cs_217` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 149 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “Super Dango Maker” constructive problem. |
| 95 | `frontier_cs_22` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 525 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Hard variant of the A+B problem (high-precision / large-input). |
| 96 | `frontier_cs_220` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 166 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “Playing Around the Table” constructive problem. |
| 97 | `frontier_cs_222` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 141 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “Hedgehog” graph-construction problem. |
| 98 | `frontier_cs_225` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 122 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Permutation-set merging problem. |
| 99 | `frontier_cs_227` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 160 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | 4-way partition maximizing the combined LIS++LDS++LIS++LDS lengths. |
| 100 | `frontier_cs_228` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 152 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Count {0,1}\{0,1\}-string substrings where #​0=(#​1)2\#0=(\#1)^{2}. |
| 101 | `frontier_cs_229` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 164 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Maximize LIS after ≤10\leq 10 interval shifts. |
| 102 | `frontier_cs_23` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 542 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Transform sequence AA into BB via constrained operations. |
| 103 | `frontier_cs_231` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 139 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “Differentiating Games” constructive problem. |
| 104 | `frontier_cs_233` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 167 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “Snake” constructive problem. |
| 105 | `frontier_cs_239` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 138 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Add minimum edges to a 0→n0{\to}n chain so every v<uv{<}u has a ≤3\leq 3-edge path. |
| 106 | `frontier_cs_24` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 513 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Construct an “almost monochromatic” permutation. |
| 107 | `frontier_cs_241` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 157 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Construct an AND/OR Boolean expression matching a given truth table. |
| 108 | `frontier_cs_243` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 162 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Locate a hidden position on a grid map via interactive queries. |
| 109 | `frontier_cs_245` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 135 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “Asesino” constructive problem. |
| 110 | `frontier_cs_247` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 137 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Transform AA into BB via swap-and-adjust ops (Ai,Aj)→(Aj−1,Ai+1)(A_{i},A_{j})\to(A_{j}{-}1,A_{i}{+}1). |
| 111 | `frontier_cs_248` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 143 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “Drone Delivery” constructive problem. |
| 112 | `frontier_cs_249` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 181 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “X-OR” constructive problem. |
| 113 | `frontier_cs_25` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 518 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Decide graph connectivity using only neighborhood queries. |
| 114 | `frontier_cs_252` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 141 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “Hotel” constructive problem. |
| 115 | `frontier_cs_253` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 155 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “Roads” constructive problem. |
| 116 | `frontier_cs_254` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 143 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “Pepe Racing” constructive problem. |
| 117 | `frontier_cs_255` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 176 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “Magnets” constructive problem. |
| 118 | `frontier_cs_256` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 152 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “Palindromic Paths” constructive problem. |
| 119 | `frontier_cs_257` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 161 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “Omkar and Modes” constructive problem. |
| 120 | `frontier_cs_258` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 169 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Network-synchronization dual-anomaly detection. |
| 121 | `frontier_cs_26` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 518 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Custom comparison-sort variant (“OgreSort”). |
| 122 | `frontier_cs_27` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 520 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Place the maximum number of points in an n×mn{\times}m grid with no axis-parallel rectangle of any 4 of them. |
| 123 | `frontier_cs_28` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 535 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “Hacking the Project” constructive problem. |
| 124 | `frontier_cs_3` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 520 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Recover a hidden cyclic permutation via lamp-toggle queries with adjacency feedback. |
| 125 | `frontier_cs_30` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 523 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Locate a hidden mole on a tree via interactive vertex queries. |
| 126 | `frontier_cs_33` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 477 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Modified-version of an interactive permutation problem. |
| 127 | `frontier_cs_35` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 523 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Identify the unique element in a doubled array via comparison queries. |
| 128 | `frontier_cs_36` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 489 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “Hack!” constructive challenge. |
| 129 | `frontier_cs_4` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 519 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Identify the kk-th smallest element of a hidden matrix through interactive queries. |
| 130 | `frontier_cs_40` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 542 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Recover a hidden balanced-bracket sequence interactively. |
| 131 | `frontier_cs_41` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 511 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Construct a strictly increasing sequence whose consecutive GCDs are also strictly increasing. |
| 132 | `frontier_cs_42` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 551 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Pack nn unit squares allowing arbitrary rotation in the smallest enclosing square. |
| 133 | `frontier_cs_43` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 527 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Larger-scale Sokoban-style puzzle (40k cells). |
| 134 | `frontier_cs_44` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 528 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Tour problem with carrot-pickup constraints. |
| 135 | `frontier_cs_45` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 538 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Balanced partitioning of DIMACS10 graphs minimizing edge cut. |
| 136 | `frontier_cs_46` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 459 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Classical job-shop scheduling on JSPLIB instances. |
| 137 | `frontier_cs_47` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 432 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | 2D rectangle knapsack with 90∘ rotations allowed. |
| 138 | `frontier_cs_48` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 532 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Pack nn unit spheres inside the smallest enclosing cube. |
| 139 | `frontier_cs_5` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 537 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Construct or approximate a Hamiltonian path on a given graph instance. |
| 140 | `frontier_cs_50` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 524 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Minimum-cost weighted set cover. |
| 141 | `frontier_cs_52` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 534 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Game-state constructive problem (“Geemu”). |
| 142 | `frontier_cs_53` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 452 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Hard interactive variant “G2. Inter Active”. |
| 143 | `frontier_cs_54` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 505 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Interactive centroid-guessing on a tree. |
| 144 | `frontier_cs_57` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 542 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Identify a rooted tree using path-sum queries. |
| 145 | `frontier_cs_58` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 478 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Inverse-counting path-construction problem. |
| 146 | `frontier_cs_59` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 539 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Restore an array using a limited number of shuffles. |
| 147 | `frontier_cs_6` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 486 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Constructive world-map design. |
| 148 | `frontier_cs_60` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 537 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Detect a hidden disk’s center and radius via line-segment light probes. |
| 149 | `frontier_cs_61` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 141 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “Let’s Go! New Adventure” constructive problem. |
| 150 | `frontier_cs_62` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 175 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Constructive ball-moving puzzle. |
| 151 | `frontier_cs_63` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 155 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “Space Thief” constructive problem. |
| 152 | `frontier_cs_64` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 134 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Subset-sum closest to a target value. |
| 153 | `frontier_cs_68` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 154 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Interactive pen-ink-selection problem. |
| 154 | `frontier_cs_69` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 153 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Maximize the number of distinct substrings (“magic words”) in a string. |
| 155 | `frontier_cs_7` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 509 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Combinatorial construction problem (“Build a Computer”). |
| 156 | `frontier_cs_70` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 177 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “Treasure Hunt” constructive problem. |
| 157 | `frontier_cs_72` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 136 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | On a 6×66{\times}6 Rush-Hour puzzle, maximize the minimum steps required for any solution. |
| 158 | `frontier_cs_73` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 170 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “Inversion” constructive problem. |
| 159 | `frontier_cs_75` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 152 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “Black and White” constructive problem. |
| 160 | `frontier_cs_77` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 181 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Minimize wrong guesses across 10,000 interactive prediction rounds. |
| 161 | `frontier_cs_79` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 165 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “H. Hack” constructive problem. |
| 162 | `frontier_cs_8` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 505 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “The Empress” constructive optimization problem. |
| 163 | `frontier_cs_80` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 171 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “Indiana Jones” interactive cave-traversal problem. |
| 164 | `frontier_cs_81` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 124 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Recover a hidden string written on a stone slate. |
| 165 | `frontier_cs_82` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 160 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Recover a hidden permutation in ≤4269\leq 4269 bitwise-OR queries. |
| 166 | `frontier_cs_83` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 169 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | For a completely multiplicative f⁡(⋅)f(\cdot), minimize maxk⁡\|∑i≤kf⁡(i)\|\max_{k}\|\sum_{i\leq k}f(i)\|. |
| 167 | `frontier_cs_85` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 181 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “Maze” constructive problem. |
| 168 | `frontier_cs_86` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 130 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Recover a hidden tree via queries. |
| 169 | `frontier_cs_87` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 174 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Graph-coloring decision/optimization. |
| 170 | `frontier_cs_89` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 153 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Reconstruct a tree using Steiner-set membership queries. |
| 171 | `frontier_cs_9` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 547 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Sort a tree-labeled permutation to identity using minimum-matching swaps. |
| 172 | `frontier_cs_93` | Frontier-CS | `identified-in-arxiv-v1-appendix` | 166 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | “Greedy” constructive problem. |

##### Constructive Search

- **Question:** Improve a program that searches for a high-quality construction or function minimum.
- **Input:** Objective function, constraints, starter program, and deterministic evaluator feedback.
- **Output:** Executable Python program defining the candidate construction/search strategy.
- **Evaluation:** OpenEvolve task evaluator checks constraints and computes the objective.
- **Environment:** Python OpenEvolve example environment with task-specific dependencies.
- **Metric family:** Task-specific construction or minimization objective.

| # | Task ID | Upstream source | Paper/expansion status | Trajectories | SOTA method / status | Model | Link | Published description |
|---:|---|---|---|---:|---|---|---|---|
| 173 | `function_minimization` | OpenEvolve constructive search | `identified-in-arxiv-v1-appendix` | 1036 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Black-box minimization of f⁡(x,y)=sin⁡(x)​cos⁡(y)+sin⁡(x​y)+(x2+y2)/20f(x,y)=\sin(x)\cos(y)+\sin(xy)+(x^{2}{+}y^{2})/20 on [−5,5]2[-5,5]^{2}; evolve a random-search seed into an adaptive optimizer. |
| 174 | `k_module_problem` | OpenEvolve constructive search | `identified-in-arxiv-v1-appendix` | 149 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Discover the correct 4-component pipeline configuration (54=6255^{4}{=}625 possibilities) when the only feedback per query is the count of correctly placed modules (deceptive landscape). |

##### GPU Kernel Optimization

- **Question:** Implement a faster correct GPU kernel for the specified workload.
- **Input:** Reference operator, tensor contracts, starter kernel, correctness tests, hardware target, and runtime feedback.
- **Output:** Executable Triton/Python GPU kernel.
- **Evaluation:** GPUMode checks correctness and benchmarks latency on the named hardware contract.
- **Environment:** Task-specific GPU hardware and GPUMode benchmark harness; scores are hardware-sensitive.
- **Metric family:** Correctness-gated execution time.

| # | Task ID | Upstream source | Paper/expansion status | Trajectories | SOTA method / status | Model | Link | Published description |
|---:|---|---|---|---:|---|---|---|---|
| 175 | `grayscale` | GPUMode | `identified-in-arxiv-v1-appendix` | 482 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Triton/PyTorch kernel for RGB→\tograyscale image conversion on H100/H200 GPUs. |
| 176 | `mla_decode` | GPUMode | `identified-in-arxiv-v1-appendix` | 61 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Triton kernel for DeepSeek-V2/V3 multi-head latent-attention decoding. |
| 177 | `trimul` | GPUMode | `identified-in-arxiv-v1-appendix` | 208 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Triton kernel for the AlphaFold-3 triangle multiplicative update. |
| 178 | `vecadd` | GPUMode | `identified-in-arxiv-v1-appendix` | 337 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Triton/PyTorch kernel for FP16 vector addition on H100/H200 GPUs. |

##### Heuristic Optimization

- **Question:** Improve a solver for an AtCoder Heuristic Contest problem.
- **Input:** Contest statement, starter C++ solver, instances, score feedback, and search history.
- **Output:** A complete C++ contest solver.
- **Evaluation:** ALE-Bench executes the official AtCoder-compatible scorer across its task instances.
- **Environment:** ALE-Bench/AtCoder-compatible C++ build and sandbox with contest-specific time limits.
- **Metric family:** Task-specific AtCoder judge score.

| # | Task ID | Upstream source | Paper/expansion status | Trajectories | SOTA method / status | Model | Link | Published description |
|---:|---|---|---|---:|---|---|---|---|
| 179 | `ahc001` | ALE-Bench | `identified-in-arxiv-v1-appendix` | 840 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Place axis-parallel rectangular ads on a 10000×1000010000{\times}10000 canvas, each containing a fixed query point and matching a target area; maximize the sum of advertiser-satisfaction scores. |
| 180 | `ahc002` | ALE-Bench | `identified-in-arxiv-v1-appendix` | 798 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | From start cell on a 50×5050{\times}50 tiled grid, walk a self-avoiding path (no tile reused); maximize the sum of cell scores along the path. |
| 181 | `ahc003` | ALE-Bench | `identified-in-arxiv-v1-appendix` | 839 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | On a 30×3030{\times}30 grid graph with unknown edge lengths, answer 1000 online shortest-path queries while learning edge lengths from noisy feedback. |
| 182 | `ahc004` | ALE-Bench | `identified-in-arxiv-v1-appendix` | 918 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Pack given strings as horizontal/vertical cyclic substrings of an N×NN{\times}N matrix; maximize the number of strings covered while minimizing matrix usage. |
| 183 | `ahc005` | ALE-Bench | `identified-in-arxiv-v1-appendix` | 831 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | On an N×NN{\times}N obstacle map with weighted road squares, design a closed walk from the start so that every road square is line-of-sight visible; minimize total travel time. |
| 184 | `ahc006` | ALE-Bench | `identified-in-arxiv-v1-appendix` | 879 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Out of 1000 delivery orders on an 801×801801{\times}801 grid, select 50 and produce a closed tour from the office that visits each pickup before its drop-off; minimize tour length. |
| 185 | `ahc007` | ALE-Bench | `identified-in-arxiv-v1-appendix` | 847 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Online Steiner-MST: edges of an embedded graph arrive one by one with revealed length ∈[di,3​di]\in[d_{i},3d_{i}]; decide on the fly whether to include each edge to ultimately span all terminals at minimum cost. |
| 186 | `ahc008` | ALE-Bench | `identified-in-arxiv-v1-appendix` | 386 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Control MM humans on a 30×3030{\times}30 grid for 300 turns, placing fences to isolate NN pets into pet-free regions; maximize the per-human area-isolation reward. |
| 187 | `ahc009` | ALE-Bench | `identified-in-arxiv-v1-appendix` | 680 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Output a single fixed action sequence ∈{U,D,L,R}∗\in\{U,D,L,R\}^{*} that, under random execution slippage, maximizes the probability of reaching the goal in a 20×2020{\times}20 walled maze. |
| 188 | `ahc010` | ALE-Bench | `identified-in-arxiv-v1-appendix` | 642 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Rotate 30×3030{\times}30 railroad-pattern tiles to form one closed loop of maximum total length. |
| 189 | `ahc011` | ALE-Bench | `identified-in-arxiv-v1-appendix` | 299 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Slide tiles on an N×NN{\times}N board so the line patterns form one large connected tree; maximize tree size while staying within the move budget. |
| 190 | `ahc012` | ALE-Bench | `identified-in-arxiv-v1-appendix` | 701 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Cut a circular cake of radius 10410^{4} with at most KK straight lines so that the strawberry counts in resulting pieces match a target multiset. |
| 191 | `ahc014` | ALE-Bench | `identified-in-arxiv-v1-appendix` | 514 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | In the RectJoin grid game, place dots and draw axis-aligned/diagonal rectangles repeatedly; maximize the weighted score of placed dots. |
| 192 | `ahc015` | ALE-Bench | `identified-in-arxiv-v1-appendix` | 486 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | In a 10×1010{\times}10 box where 100 candies of three flavors fall in a known order to random empty cells, choose a tilt direction before each candy to maximize same-flavor connected-component sizes. |
| 193 | `ahc016` | ALE-Bench | `identified-in-arxiv-v1-appendix` | 199 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Given target MM and noise rate ε\varepsilon, design MM reference graphs G0,…,GM−1G_{0},\dots,G_{M-1} that remain pairwise distinguishable after random edge flipping and label permutation. |
| 194 | `ahc017` | ALE-Bench | `identified-in-arxiv-v1-appendix` | 720 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Schedule the one-time repair of each edge of a planar weighted graph across DD days (at most KK repairs/day); minimize the total inflation in shortest-path distances during repairs. |
| 195 | `ahc019` | ALE-Bench | `identified-in-arxiv-v1-appendix` | 726 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Combine polycube blocks into a single 3D object whose front and right silhouettes match two given 2D monochrome targets. |
| 196 | `ahc020` | ALE-Bench | `identified-in-arxiv-v1-appendix` | 576 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Choose a connected subgraph and per-vertex broadcast power on a planar graph with weighted edges so that all KK residents are covered; minimize total power+edge cost. |
| 197 | `ahc021` | ALE-Bench | `identified-in-arxiv-v1-appendix` | 664 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Reorder balls in an NN-tier pyramid via adjacent swaps so that the value at each position is at least its parent; minimize swap count. |
| 198 | `ahc024` | ALE-Bench | `identified-in-arxiv-v1-appendix` | 277 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Re-tile an n×nn{\times}n multi-ward city map onto a smaller grid while preserving every ward’s connectivity and inter-ward adjacency; minimize the resulting grid size. |
| 199 | `ahc025` | ALE-Bench | `identified-in-arxiv-v1-appendix` | 382 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Using only balance-scale comparisons of item subsets, partition NN items of unknown weight into DD groups of equal total weight within QQ queries. |
| 200 | `ahc026` | ALE-Bench | `identified-in-arxiv-v1-appendix` | 307 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Carry out nn uniquely-numbered boxes from mm stacks in ascending order using up to 5000 stack-relocation moves; minimize total move cost. |
| 201 | `ahc027` | ALE-Bench | `identified-in-arxiv-v1-appendix` | 121 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Design a closed cleaning route on an N×NN{\times}N walled grid; minimize the steady-state average dirtiness across cells with cell-specific dirt-accumulation rates. |
| 202 | `ahc028` | ALE-Bench | `identified-in-arxiv-v1-appendix` | 606 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Given an N×NN{\times}N keyboard with letters in cells and MM target words to type, output a finger trajectory whose visited letters contain every target word as a contiguous substring; minimize total moves. |
| 203 | `ahc030` | ALE-Bench | `identified-in-arxiv-v1-appendix` | 686 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | On an N×NN{\times}N island hiding MM polyomino oil-fields of known shape, locate every field via interactive cell/region drilling queries with noisy feedback. |
| 204 | `ahc031` | ALE-Bench | `identified-in-arxiv-v1-appendix` | 660 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Partition a W×WW{\times}W hall into NN axis-aligned rectangles per day for DD days, each rectangle satisfying a daily area request; minimize unmet-area + cross-day partition-change penalties. |
| 205 | `ahc032` | ALE-Bench | `identified-in-arxiv-v1-appendix` | 552 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | On an N×NN{\times}N integer board, repeatedly press 3×33{\times}3 stamps from MM stamp templates (mod 109+710^{9}{+}7); maximize the final cell-sum. |
| 206 | `ahc033` | ALE-Bench | `post-paper-442-expansion` | 647 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 207 | `ahc034` | ALE-Bench | `identified-in-arxiv-v1-appendix` | 637 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Drive a dump truck on an N×NN{\times}N height-grid (total height zero), loading and unloading dirt to flatten the field; minimize total transport cost. |
| 208 | `ahc035` | ALE-Bench | `identified-in-arxiv-v1-appendix` | 594 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Over a sequence of crossing rounds, schedule pairings of 2​N​(N−1)2N(N{-}1) multi-trait seeds to evolve a high-quality final population. |
| 209 | `ahc038` | ALE-Bench | `post-paper-442-expansion` | 587 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 210 | `ahc039` | ALE-Bench | `identified-in-arxiv-v1-appendix` | 96 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Construct a rectilinear polygon in the plane that encloses as many mackerels and excludes as many sardines as possible, subject to a perimeter budget. |
| 211 | `ahc040` | ALE-Bench | `post-paper-442-expansion` | 609 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 212 | `ahc041` | ALE-Bench | `identified-in-arxiv-v1-appendix` | 629 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Partition a planar graph into rooted trees so that the weighted sum ∑v(hv+1)​Av\sum_{v}(h_{v}{+}1)A_{v} over depths and beauty values is maximized. |
| 213 | `ahc042` | ALE-Bench | `identified-in-arxiv-v1-appendix` | 574 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | On an N×NN{\times}N board with Oni and Fukunokami tokens, repeatedly push entire rows/columns to drive Oni off the board while keeping as many Fukunokami as possible. |
| 214 | `ahc044` | ALE-Bench | `identified-in-arxiv-v1-appendix` | 689 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Choose a per-employee finite-state-automaton transition (ai,bi)(a_{i},b_{i}) so that, after a long simulated week sequence, employee ii’s cleaning count converges to a target TiT_{i}. |
| 215 | `ahc045` | ALE-Bench | `identified-in-arxiv-v1-appendix` | 774 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Cluster NN cities into tour groups of fixed sizes when each city’s coordinates are only known up to a rectangular range, using a limited number of true-distance queries. |
| 216 | `ahc046` | ALE-Bench | `identified-in-arxiv-v1-appendix` | 101 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | On an N×NN{\times}N skating rink, visit target squares in order using Move, Slide, and block-placement actions; minimize total action count. |

##### Mathematical Discovery

- **Question:** Discover a better mathematical construction for an open-ended extremal problem.
- **Input:** Problem statement, executable verifier, starter construction/program, and iterative score feedback.
- **Output:** Executable code or structured data defining a candidate construction.
- **Evaluation:** A deterministic task-specific verifier checks validity and computes the continuous extremal objective.
- **Environment:** Python/JAX mathematical-search environments vendored with SkyDiscover/OpenEvolve.
- **Metric family:** Task-specific extremal bound, ratio, distance, determinant, or packing objective.

| # | Task ID | Upstream source | Paper/expansion status | Trajectories | SOTA method / status | Model | Link | Published description |
|---:|---|---|---|---:|---|---|---|---|
| 217 | `circle_packing` | AlphaEvolve-style mathematical discovery set | `post-paper-442-expansion` | 487 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 218 | `circle_packing_rect` | AlphaEvolve-style mathematical discovery set | `identified-in-arxiv-v1-appendix` | 625 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Pack equal-radius circles inside an axis-aligned rectangle without overlap; maximize the common radius under boundary and non-overlap constraints. |
| 219 | `erdos_106_square_packing` | Erdős problem variants | `paper-v1-seed-identified-by-official-manifest` | 691 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 220 | `erdos_1097_3ap_diffs_n40` | Erdős problem variants | `paper-v1-seed-identified-by-official-manifest` | 492 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 221 | `erdos_43_sidon_pair` | Erdős problem variants | `paper-v1-seed-identified-by-official-manifest` | 601 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 222 | `erdos_440_lcm_density` | Erdős problem variants | `paper-v1-seed-identified-by-official-manifest` | 850 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 223 | `erdos_480_newman_density` | Erdős problem variants | `paper-v1-seed-identified-by-official-manifest` | 981 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 224 | `erdos_507_heilbronn_disk_n12` | Erdős problem variants | `paper-v1-seed-identified-by-official-manifest` | 541 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 225 | `erdos_654_no_four_concyclic_distances` | Erdős problem variants | `paper-v1-seed-identified-by-official-manifest` | 356 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 226 | `erdos_659_4subset_3dist_construction` | Erdős problem variants | `paper-v1-seed-identified-by-official-manifest` | 790 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 227 | `erdos_705_unit_distance_high_girth` | Erdős problem variants | `paper-v1-seed-identified-by-official-manifest` | 658 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 228 | `erdos_difference_bases_N121` | Erdős problem variants | `paper-v1-seed-identified-by-official-manifest` | 520 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 229 | `erdos_flat_polynomials_n32` | Erdős problem variants | `paper-v1-seed-identified-by-official-manifest` | 609 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 230 | `erdos_isosceles_free_grid` | Erdős problem variants | `paper-v1-seed-identified-by-official-manifest` | 449 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 231 | `erdos_min_overlap` | AlphaEvolve-style mathematical discovery set | `identified-in-arxiv-v1-appendix` | 522 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Construct a witness function (step function on [−1,1][-1,1]) that gives a constructive upper bound on Erdős’s minimum-overlap constant M⁡(n)M(n). |
| 232 | `erdos_no_5_on_sphere_n8` | Erdős problem variants | `paper-v1-seed-identified-by-official-manifest` | 146 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 233 | `erdos_no_5_on_sphere_n9` | Erdős problem variants | `paper-v1-seed-identified-by-official-manifest` | 193 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 234 | `first_autocorr_ineq` | AlphaEvolve-style mathematical discovery set | `identified-in-arxiv-v1-appendix` | 367 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | First autocorrelation inequality: minimize ∥f∗f∥∞\lVert f*f\rVert_{\infty} over functions f≥0f\geq 0 supported on [−1/4,1/4][-1/4,1/4] with ∫f=1\int f=1. |
| 235 | `heilbronn_convex_13` | AlphaEvolve-style mathematical discovery set | `identified-in-arxiv-v1-appendix` | 990 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Heilbronn-on-a-convex-region variant with n=13n{=}13 points: maximize the minimum convex-hull area over all subsets of k>3k>3 points. |
| 236 | `heilbronn_convex_14` | AlphaEvolve-style mathematical discovery set | `identified-in-arxiv-v1-appendix` | 599 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Heilbronn-on-a-convex-region variant with n=14n{=}14 points (otherwise as above). |
| 237 | `heilbronn_triangle` | AlphaEvolve-style mathematical discovery set | `identified-in-arxiv-v1-appendix` | 576 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Place nn points in the unit square [0,1]2[0,1]^{2}; maximize the area of the smallest triangle formed by any three points. |
| 238 | `hexagon_packing_11` | AlphaEvolve-style mathematical discovery set | `identified-in-arxiv-v1-appendix` | 192 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Pack n=11n{=}11 unit regular hexagons inside the smallest enclosing regular hexagon. |
| 239 | `hexagon_packing_12` | AlphaEvolve-style mathematical discovery set | `identified-in-arxiv-v1-appendix` | 219 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Pack n=12n{=}12 unit regular hexagons inside the smallest enclosing regular hexagon. |
| 240 | `kissing_number` | AlphaEvolve-style mathematical discovery set | `post-paper-442-expansion` | 269 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 241 | `matmul` | AlphaEvolve-style mathematical discovery set | `post-paper-442-expansion` | 2 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 242 | `minimizing_max_min_dist_2` | AlphaEvolve-style mathematical discovery set | `identified-in-arxiv-v1-appendix` | 1492 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Place points in [0,1]2[0,1]^{2} so that the ratio of minimum to maximum pairwise distance is as close to 1 as possible (uniform 2D point distribution). |
| 243 | `minimizing_max_min_dist_3` | AlphaEvolve-style mathematical discovery set | `identified-in-arxiv-v1-appendix` | 1264 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Same as above but for points in [0,1]3[0,1]^{3} (uniform 3D point distribution). |
| 244 | `second_autocorr_ineq` | AlphaEvolve-style mathematical discovery set | `identified-in-arxiv-v1-appendix` | 692 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Second autocorrelation inequality: extremal ∥f∗f∥\lVert f*f\rVert under prescribed support and mass constraints. |
| 245 | `signal_processing` | AlphaEvolve-style mathematical discovery set | `identified-in-arxiv-v1-appendix` | 761 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Design a causal real-time filter for a noisy non-stationary time series, balancing fidelity, smoothness, lag, and false-trend detection. |
| 246 | `sums_diffs_finite_sets` | AlphaEvolve-style mathematical discovery set | `identified-in-arxiv-v1-appendix` | 225 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Construct a finite set A⊂ℤA\subset\mathbb{Z} minimizing the ratio between sumset and difference-set cardinalities (additive combinatorics). |
| 247 | `third_autocorr_ineq` | AlphaEvolve-style mathematical discovery set | `identified-in-arxiv-v1-appendix` | 430 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Third autocorrelation inequality: tighten the upper bound on the third autocorrelation constant arising in additive combinatorics. |
| 248 | `uncertainty_ineq` | AlphaEvolve-style mathematical discovery set | `post-paper-442-expansion` | 53 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |

##### Numerical Algorithm Optimization

- **Question:** Optimize a general-purpose numerical routine without changing its required behavior.
- **Input:** Reference routine, starter implementation, correctness tests, benchmark cases, and runtime feedback.
- **Output:** An executable Python implementation of the routine.
- **Evaluation:** AlgoTune first checks numerical correctness against the reference and then measures speedup/runtime.
- **Environment:** Python scientific-computing environment with task-specific NumPy/SciPy and benchmark dependencies.
- **Metric family:** Correctness-gated speedup or runtime.

| # | Task ID | Upstream source | Paper/expansion status | Trajectories | SOTA method / status | Model | Link | Published description |
|---:|---|---|---|---:|---|---|---|---|
| 249 | `aes_gcm_encryption` | AlgoTune | `identified-in-arxiv-v1-appendix` | 1297 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Speed up AES-GCM authenticated encryption against a cryptography-library reference. |
| 250 | `affine_transform_2d` | AlgoTune | `identified-in-arxiv-v1-appendix` | 191 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Speed up 2D affine image warping with cubic-spline interpolation against a SciPy reference. |
| 251 | `aircraft_wing_design` | AlgoTune | `identified-in-arxiv-v1-appendix` | 396 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Speed up the geometric-programming aircraft-wing design problem (drag minimization under aerodynamic constraints). |
| 252 | `articulation_points` | AlgoTune | `identified-in-arxiv-v1-appendix` | 1323 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Find all articulation points in an undirected graph (cut vertices whose removal disconnects the graph). |
| 253 | `base64_encoding` | AlgoTune | `identified-in-arxiv-v1-appendix` | 1374 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Speed up Base64 encoding of binary data against a base64 stdlib reference. |
| 254 | `battery_scheduling` | AlgoTune | `identified-in-arxiv-v1-appendix` | 453 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Convex battery charge/discharge scheduling under price, capacity, and ramp constraints (CVXPY reference). |
| 255 | `btsp` | AlgoTune | `unresolved-paper-v1-or-expansion` | 269 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 256 | `chacha_encryption` | AlgoTune | `identified-in-arxiv-v1-appendix` | 1305 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Speed up ChaCha20 stream-cipher encryption against a cryptography-library reference. |
| 257 | `channel_capacity` | AlgoTune | `identified-in-arxiv-v1-appendix` | 1189 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Compute the channel capacity of a discrete memoryless channel by maximizing mutual information (CVXPY reference). |
| 258 | `chebyshev_center` | AlgoTune | `identified-in-arxiv-v1-appendix` | 1323 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Find the center of the largest inscribed ball of a polyhedron P={x∣ai⊤​x≤bi}P=\{x\mid a_{i}^{\top}x\leq b_{i}\} via an LP. |
| 259 | `cholesky_factorization` | AlgoTune | `identified-in-arxiv-v1-appendix` | 1277 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Speed up dense Cholesky factorization of a symmetric positive-definite matrix. |
| 260 | `clustering_outliers` | AlgoTune | `identified-in-arxiv-v1-appendix` | 1239 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Outlier-robust clustering of points in multidimensional space (HDBSCAN-style reference). |
| 261 | `communicability` | AlgoTune | `identified-in-arxiv-v1-appendix` | 1073 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Compute communicability C⁡(u,v)C(u,v) between all node pairs in an undirected graph (NetworkX reference). |
| 262 | `convex_hull` | AlgoTune | `identified-in-arxiv-v1-appendix` | 1243 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Compute the convex hull of a 2D point set (smallest convex polygon containing all points). |
| 263 | `convolve2d_full_fill` | AlgoTune | `identified-in-arxiv-v1-appendix` | 173 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Speed up 2D convolution with full-output, fill boundary against scipy.signal.convolve2d. |
| 264 | `convolve_1d` | AlgoTune | `identified-in-arxiv-v1-appendix` | 1050 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Speed up 1D convolution over a list of array pairs against a SciPy reference. |
| 265 | `correlate_1d` | AlgoTune | `identified-in-arxiv-v1-appendix` | 1288 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Speed up 1D cross-correlation over a list of array pairs against a SciPy reference. |
| 266 | `count_connected_components` | AlgoTune | `identified-in-arxiv-v1-appendix` | 1166 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Count connected components of an undirected edge-list graph. |
| 267 | `count_riemann_zeta_zeros` | AlgoTune | `identified-in-arxiv-v1-appendix` | 1260 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Count nontrivial zeros of the Riemann zeta function with imaginary part in (0,t](0,t]. |
| 268 | `cumulative_simpson_1d` | AlgoTune | `identified-in-arxiv-v1-appendix` | 1274 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Cumulative integral of a 1D function via Simpson’s rule (SciPy reference). |
| 269 | `cumulative_simpson_multid` | AlgoTune | `identified-in-arxiv-v1-appendix` | 1257 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Cumulative integral along the last axis of a multidimensional array via Simpson’s rule. |
| 270 | `dct_type_I_scipy_fftpack` | AlgoTune | `identified-in-arxiv-v1-appendix` | 293 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Speed up Type-I Discrete Cosine Transform against scipy.fftpack. |
| 271 | `delaunay` | AlgoTune | `identified-in-arxiv-v1-appendix` | 259 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Compute Delaunay triangulation of a 2D point set (SciPy reference). |
| 272 | `dijkstra_from_indices` | AlgoTune | `identified-in-arxiv-v1-appendix` | 270 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Shortest paths from a subset of source nodes to all others on a weighted undirected CSR graph. |
| 273 | `dst_type_II_scipy_fftpack` | AlgoTune | `identified-in-arxiv-v1-appendix` | 275 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Speed up Type-II Discrete Sine Transform on a 2D array against scipy.fftpack. |
| 274 | `dynamic_assortment_planning` | AlgoTune | `identified-in-arxiv-v1-appendix` | 247 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Dynamic assortment planning over TT periods with NN products under per-product capacities; maximize expected revenue. |
| 275 | `earth_movers_distance` | AlgoTune | `identified-in-arxiv-v1-appendix` | 484 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Solve the optimal-transport problem between two histograms with a given cost matrix (POT reference). |
| 276 | `edge_expansion` | AlgoTune | `identified-in-arxiv-v1-appendix` | 482 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Compute the edge expansion ∂S/\|S\|\partial S/\|S\| for a node subset SS in a directed graph. |
| 277 | `eigenvalues_complex` | AlgoTune | `identified-in-arxiv-v1-appendix` | 484 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Eigenvalues of a real square matrix that may have complex eigenvalues (LAPACK reference). |
| 278 | `eigenvalues_real` | AlgoTune | `identified-in-arxiv-v1-appendix` | 494 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Eigenvalues of a symmetric real matrix (LAPACK reference). |
| 279 | `eigenvectors_complex` | AlgoTune | `identified-in-arxiv-v1-appendix` | 188 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Eigenpairs of a real square matrix (complex eigenvalues/eigenvectors). |
| 280 | `eigenvectors_real` | AlgoTune | `identified-in-arxiv-v1-appendix` | 488 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Eigenpairs of a real symmetric matrix (orthonormal eigenvectors). |
| 281 | `elementwise_integration` | AlgoTune | `identified-in-arxiv-v1-appendix` | 469 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Elementwise definite integration of Wright’s Bessel function across an array of arguments. |
| 282 | `fft_cmplx_scipy_fftpack` | AlgoTune | `identified-in-arxiv-v1-appendix` | 181 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | NN-dimensional complex FFT of a complex matrix against scipy.fftpack. |
| 283 | `fft_convolution` | AlgoTune | `identified-in-arxiv-v1-appendix` | 179 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | FFT-based convolution of two signals (overlap-add / circular-FFT reference). |
| 284 | `fft_real_scipy_fftpack` | AlgoTune | `identified-in-arxiv-v1-appendix` | 480 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | NN-dimensional FFT of a real-valued matrix against scipy.fftpack. |
| 285 | `firls` | AlgoTune | `identified-in-arxiv-v1-appendix` | 386 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Design a least-squares FIR filter for given frequency-band edges (SciPy firls reference). |
| 286 | `generalized_eigenvalues_complex` | AlgoTune | `identified-in-arxiv-v1-appendix` | 262 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Generalized eigenvalues of (A,B)(A,B) where A,BA,B are real and the spectrum may be complex. |
| 287 | `generalized_eigenvalues_real` | AlgoTune | `identified-in-arxiv-v1-appendix` | 287 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Generalized eigenvalues of (A,B)(A,B) with real spectrum (symmetric/positive-definite case). |
| 288 | `generalized_eigenvectors_complex` | AlgoTune | `identified-in-arxiv-v1-appendix` | 191 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Generalized eigenpairs of (A,B)(A,B) with complex spectrum. |
| 289 | `generalized_eigenvectors_real` | AlgoTune | `identified-in-arxiv-v1-appendix` | 270 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Generalized eigenpairs of (A,B)(A,B) with real spectrum. |
| 290 | `graph_global_efficiency` | AlgoTune | `identified-in-arxiv-v1-appendix` | 281 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Average inverse shortest-path length over all node pairs of an undirected graph (NetworkX reference). |
| 291 | `graph_isomorphism` | AlgoTune | `identified-in-arxiv-v1-appendix` | 274 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Find a node mapping between two isomorphic undirected graphs (NetworkX VF2 reference). |
| 292 | `graph_laplacian` | AlgoTune | `identified-in-arxiv-v1-appendix` | 202 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Compute the combinatorial or symmetric-normalized Laplacian of a sparse undirected graph. |
| 293 | `group_lasso` | AlgoTune | `identified-in-arxiv-v1-appendix` | 144 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Logistic regression with group-lasso penalty over JJ feature groups (CVXPY reference). |
| 294 | `gzip_compression` | AlgoTune | `identified-in-arxiv-v1-appendix` | 287 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Speed up Gzip compression of binary data against the gzip stdlib reference. |
| 295 | `kcenters` | AlgoTune | `unresolved-paper-v1-or-expansion` | 37 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 296 | `kd_tree` | AlgoTune | `unresolved-paper-v1-or-expansion` | 128 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 297 | `kernel_density_estimation` | AlgoTune | `unresolved-paper-v1-or-expansion` | 129 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 298 | `kmeans` | AlgoTune | `unresolved-paper-v1-or-expansion` | 105 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 299 | `ks_test_2samp` | AlgoTune | `unresolved-paper-v1-or-expansion` | 160 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 300 | `l0_pruning` | AlgoTune | `unresolved-paper-v1-or-expansion` | 198 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 301 | `l1_pruning` | AlgoTune | `unresolved-paper-v1-or-expansion` | 193 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 302 | `lasso` | AlgoTune | `unresolved-paper-v1-or-expansion` | 140 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 303 | `least_squares` | AlgoTune | `unresolved-paper-v1-or-expansion` | 130 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 304 | `linear_system_solver` | AlgoTune | `unresolved-paper-v1-or-expansion` | 200 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 305 | `lp_box` | AlgoTune | `unresolved-paper-v1-or-expansion` | 170 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 306 | `lp_centering` | AlgoTune | `unresolved-paper-v1-or-expansion` | 166 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 307 | `lqr` | AlgoTune | `unresolved-paper-v1-or-expansion` | 24 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 308 | `lti_simulation` | AlgoTune | `unresolved-paper-v1-or-expansion` | 156 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 309 | `lu_factorization` | AlgoTune | `identified-in-arxiv-v1-appendix` | 164 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Speed up dense LU factorization with partial pivoting against a LAPACK reference. |
| 310 | `markowitz` | AlgoTune | `unresolved-paper-v1-or-expansion` | 174 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 311 | `matrix_exponential` | AlgoTune | `unresolved-paper-v1-or-expansion` | 196 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 312 | `matrix_exponential_sparse` | AlgoTune | `unresolved-paper-v1-or-expansion` | 187 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 313 | `matrix_multiplication` | AlgoTune | `unresolved-paper-v1-or-expansion` | 199 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 314 | `min_weight_assignment` | AlgoTune | `unresolved-paper-v1-or-expansion` | 178 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 315 | `minimum_spanning_tree` | AlgoTune | `unresolved-paper-v1-or-expansion` | 197 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 316 | `multi_dim_knapsack` | AlgoTune | `unresolved-paper-v1-or-expansion` | 113 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 317 | `ode_brusselator` | AlgoTune | `unresolved-paper-v1-or-expansion` | 150 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 318 | `ode_hires` | AlgoTune | `unresolved-paper-v1-or-expansion` | 95 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 319 | `ode_hodgkinhuxley` | AlgoTune | `unresolved-paper-v1-or-expansion` | 12 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 320 | `ode_lorenz96_nonchaotic` | AlgoTune | `unresolved-paper-v1-or-expansion` | 129 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 321 | `ode_lotkavolterra` | AlgoTune | `unresolved-paper-v1-or-expansion` | 161 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 322 | `ode_seirs` | AlgoTune | `unresolved-paper-v1-or-expansion` | 149 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 323 | `ode_stiff_robertson` | AlgoTune | `unresolved-paper-v1-or-expansion` | 148 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 324 | `ode_stiff_vanderpol` | AlgoTune | `unresolved-paper-v1-or-expansion` | 16 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 325 | `odr` | AlgoTune | `unresolved-paper-v1-or-expansion` | 173 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 326 | `optimal_advertising` | AlgoTune | `unresolved-paper-v1-or-expansion` | 18 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 327 | `outer_product` | AlgoTune | `unresolved-paper-v1-or-expansion` | 199 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 328 | `pagerank` | AlgoTune | `unresolved-paper-v1-or-expansion` | 134 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 329 | `polynomial_mixed` | AlgoTune | `unresolved-paper-v1-or-expansion` | 184 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 330 | `power_control` | AlgoTune | `unresolved-paper-v1-or-expansion` | 86 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 331 | `procrustes` | AlgoTune | `unresolved-paper-v1-or-expansion` | 104 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 332 | `qp` | AlgoTune | `unresolved-paper-v1-or-expansion` | 174 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 333 | `qr_factorization` | AlgoTune | `unresolved-paper-v1-or-expansion` | 161 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 334 | `quantile_regression` | AlgoTune | `unresolved-paper-v1-or-expansion` | 164 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 335 | `queuing` | AlgoTune | `unresolved-paper-v1-or-expansion` | 106 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 336 | `qz_factorization` | AlgoTune | `unresolved-paper-v1-or-expansion` | 67 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 337 | `randomized_svd` | AlgoTune | `unresolved-paper-v1-or-expansion` | 179 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 338 | `rbf_interpolation` | AlgoTune | `unresolved-paper-v1-or-expansion` | 80 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 339 | `rocket_landing_optimization` | AlgoTune | `unresolved-paper-v1-or-expansion` | 19 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 340 | `rotate_2d` | AlgoTune | `unresolved-paper-v1-or-expansion` | 200 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 341 | `sha256_hashing` | AlgoTune | `unresolved-paper-v1-or-expansion` | 199 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 342 | `shift_2d` | AlgoTune | `unresolved-paper-v1-or-expansion` | 197 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 343 | `shortest_path_dijkstra` | AlgoTune | `unresolved-paper-v1-or-expansion` | 196 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 344 | `sinkhorn` | AlgoTune | `unresolved-paper-v1-or-expansion` | 168 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 345 | `sparse_lowest_eigenvalues_posdef` | AlgoTune | `unresolved-paper-v1-or-expansion` | 200 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 346 | `sparse_lowest_eigenvectors_posdef` | AlgoTune | `unresolved-paper-v1-or-expansion` | 162 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 347 | `sparse_pca` | AlgoTune | `unresolved-paper-v1-or-expansion` | 7 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 348 | `stable_matching` | AlgoTune | `unresolved-paper-v1-or-expansion` | 144 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 349 | `svd` | AlgoTune | `unresolved-paper-v1-or-expansion` | 2 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 350 | `svm` | AlgoTune | `unresolved-paper-v1-or-expansion` | 170 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 351 | `toeplitz_solver` | AlgoTune | `unresolved-paper-v1-or-expansion` | 195 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 352 | `two_eigenvalues_around_0` | AlgoTune | `unresolved-paper-v1-or-expansion` | 166 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 353 | `unit_simplex_projection` | AlgoTune | `unresolved-paper-v1-or-expansion` | 195 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 354 | `upfirdn1d` | AlgoTune | `unresolved-paper-v1-or-expansion` | 181 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 355 | `vectorized_newton` | AlgoTune | `unresolved-paper-v1-or-expansion` | 186 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 356 | `voronoi_diagram` | AlgoTune | `unresolved-paper-v1-or-expansion` | 112 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 357 | `wasserstein_dist` | AlgoTune | `unresolved-paper-v1-or-expansion` | 200 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 358 | `water_filling` | AlgoTune | `unresolved-paper-v1-or-expansion` | 196 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 359 | `zoom_2d` | AlgoTune | `unresolved-paper-v1-or-expansion` | 196 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |

##### SR - Bio Pop Growth

- **Question:** Discover a symbolic equation that explains a biological population-growth dataset.
- **Input:** Observed variables/data, allowed operators, starter expression/program, and fit feedback.
- **Output:** Executable symbolic-regression program or equation.
- **Evaluation:** LLM-SRBench evaluates predictive fit and task validity with its deterministic data split.
- **Environment:** Python symbolic-regression environment with the BPG dataset and evaluator.
- **Metric family:** Task-specific symbolic-regression fit objective.

| # | Task ID | Upstream source | Paper/expansion status | Trajectories | SOTA method / status | Model | Link | Published description |
|---:|---|---|---|---:|---|---|---|---|
| 360 | `symbolic_regression_bio_pop_growth_BPG0` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1178 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: 0.954​(1−P/96.9)​P+0.954​P0.333\displaystyle 0.954\,(1-P/96.9)\,P+0.954\,P^{0.333}. |
| 361 | `symbolic_regression_bio_pop_growth_BPG1` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1176 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: 0.316​P​e−0.0541​t+0.316​P2/(9.87​P+1)\displaystyle 0.316\,P\,e^{-0.0541t}+0.316\,P^{2}/(9.87\,P+1). |
| 362 | `symbolic_regression_bio_pop_growth_BPG10` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1164 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: 0.101​P0.333+0.101​P\displaystyle 0.101\,P^{0.333}+0.101\,P. |
| 363 | `symbolic_regression_bio_pop_growth_BPG11` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1172 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: 0.712​(1−P/68.9)​P+0.712​P0.333+0.712​P​e−0.0346​t\displaystyle 0.712\,(1-P/68.9)\,P+0.712\,P^{0.333}+0.712\,P\,e^{-0.0346t}. |
| 364 | `symbolic_regression_bio_pop_growth_BPG12` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1166 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: 0.877​P​sin⁡(0.567​t)+0.701​(1−P/65.8)​P\displaystyle 0.877\,P\sin(0.567\,t)+0.701\,(1-P/65.8)\,P. |
| 365 | `symbolic_regression_bio_pop_growth_BPG13` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1171 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: 0.201​(−1+P/5.64)​(1−P/10.2)​P+0.201​P+0.201​P/(1+e−5.64​(−0.634+P))\displaystyle 0.201\,(-1+P/5.64)(1-P/10.2)\,P+0.201\,P+0.201\,P/(1+e^{-5.64(-0.634+P)}). |
| 366 | `symbolic_regression_bio_pop_growth_BPG14` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1161 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: 0.114​(1−P/40.7)​P+0.114​(1−e−0.0837​P)​P+0.114​P​e−0.0837​t\displaystyle 0.114\,(1-P/40.7)\,P+0.114\,(1-e^{-0.0837P})\,P+0.114\,P\,e^{-0.0837t}. |
| 367 | `symbolic_regression_bio_pop_growth_BPG15` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1167 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: 0.487​P0.333+0.487​P​e−0.0858​t\displaystyle 0.487\,P^{0.333}+0.487\,P\,e^{-0.0858t}. |
| 368 | `symbolic_regression_bio_pop_growth_BPG16` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1169 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: 0.868​(−1+P/6.06)​(1−P/14.2)​P+0.868​P0.333+0.868​P\displaystyle 0.868\,(-1+P/6.06)(1-P/14.2)\,P+0.868\,P^{0.333}+0.868\,P. |
| 369 | `symbolic_regression_bio_pop_growth_BPG17` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1171 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: 0.769​(−1+P/8.67)​(1−P/14.3)​P+0.769​P0.333\displaystyle 0.769\,(-1+P/8.67)(1-P/14.3)\,P+0.769\,P^{0.333}. |
| 370 | `symbolic_regression_bio_pop_growth_BPG18` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1163 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: 0.477​P​sin⁡(0.776​t)+0.445​(1−P/51.1)​P+0.445​P\displaystyle 0.477\,P\sin(0.776\,t)+0.445\,(1-P/51.1)\,P+0.445\,P. |
| 371 | `symbolic_regression_bio_pop_growth_BPG19` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1175 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: 0.421​(1−P/84.4)​P+0.421​P/t2.59\displaystyle 0.421\,(1-P/84.4)\,P+0.421\,P/t^{2.59}. |
| 372 | `symbolic_regression_bio_pop_growth_BPG2` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1169 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: 0.257​P​sin⁡(0.722​t)+0.115​P​e−0.0304​t\displaystyle 0.257\,P\sin(0.722\,t)+0.115\,P\,e^{-0.0304t}. |
| 373 | `symbolic_regression_bio_pop_growth_BPG20` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1166 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: 0.139​(−1+P/8.04)​(1−P/70)​P+0.139​(1−P/70)​P+0.139​P/(1+e−8.04​(−0.589+P))\displaystyle 0.139\,(-1+P/8.04)(1-P/70)\,P+0.139\,(1-P/70)\,P+0.139\,P/(1+e^{-8.04(-0.589+P)}). |
| 374 | `symbolic_regression_bio_pop_growth_BPG21` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1168 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: 0.14​(−1+P/4.53)​(1−P/78.5)​P+0.14​P/t4.53\displaystyle 0.14\,(-1+P/4.53)(1-P/78.5)\,P+0.14\,P/t^{4.53}. |
| 375 | `symbolic_regression_bio_pop_growth_BPG22` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1171 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: 0.118​(1−e−0.0272​P)​P+0.118​P​e−0.0272​t\displaystyle 0.118\,(1-e^{-0.0272P})\,P+0.118\,P\,e^{-0.0272t}. |
| 376 | `symbolic_regression_bio_pop_growth_BPG23` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1169 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: 0.598​(1−P/32.9)​P+0.598​(1−e−0.0768​P)​P\displaystyle 0.598\,(1-P/32.9)\,P+0.598\,(1-e^{-0.0768P})\,P. |
| 377 | `symbolic_regression_bio_pop_growth_BPG3` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1161 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: 0.845​(−1+P/5.12)​(1−P/34.4)​P+0.845​(1−e−0.0969​P)​P\displaystyle 0.845\,(-1+P/5.12)(1-P/34.4)\,P+0.845\,(1-e^{-0.0969P})\,P. |
| 378 | `symbolic_regression_bio_pop_growth_BPG4` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1166 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: 0.173​(1−P/48.5)​P+0.173​P/(1+e−1.52​(−0.924+P))\displaystyle 0.173\,(1-P/48.5)\,P+0.173\,P/(1+e^{-1.52(-0.924+P)}). |
| 379 | `symbolic_regression_bio_pop_growth_BPG5` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1169 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: 0.92​(1−P/84)​P+0.92​P2/(7.53​P+1)\displaystyle 0.92\,(1-P/84)\,P+0.92\,P^{2}/(7.53\,P+1). |
| 380 | `symbolic_regression_bio_pop_growth_BPG6` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1161 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: −6.22⋅1.41P+0.858(1−P/79.2)P+0.858P0.333+0.858P\displaystyle-6.22\cdot 1.41\,P+0.858\,(1-P/79.2)\,P+0.858\,P^{0.333}+0.858\,P. |
| 381 | `symbolic_regression_bio_pop_growth_BPG7` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1162 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: 0.721​(−1+P/6.65)​(1−P/13.5)​P+0.721​(1−P/13.5)​P+0.721​P0.333\displaystyle 0.721\,(-1+P/6.65)(1-P/13.5)\,P+0.721\,(1-P/13.5)\,P+0.721\,P^{0.333}. |
| 382 | `symbolic_regression_bio_pop_growth_BPG8` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1166 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: 0.991​(1−P/39)​P+0.991​P0.333+0.991​P\displaystyle 0.991\,(1-P/39)\,P+0.991\,P^{0.333}+0.991\,P. |
| 383 | `symbolic_regression_bio_pop_growth_BPG9` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1173 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: 0.17​(−1+P/1.05)​(1−P/10.2)​P+0.17​(1−P/10.2)​P+0.17​(1−e−0.0971​P)​P\displaystyle 0.17\,(-1+P/1.05)(1-P/10.2)\,P+0.17\,(1-P/10.2)\,P+0.17\,(1-e^{-0.0971P})\,P. |

##### SR - Chem Reaction

- **Question:** Discover a symbolic equation that explains a chemical-reaction kinetics dataset.
- **Input:** Observed variables/data, allowed operators, starter expression/program, and fit feedback.
- **Output:** Executable symbolic-regression program or equation.
- **Evaluation:** LLM-SRBench evaluates predictive fit and task validity with its deterministic data split.
- **Environment:** Python symbolic-regression environment with the CRK dataset and evaluator.
- **Metric family:** Task-specific symbolic-regression fit objective.

| # | Task ID | Upstream source | Paper/expansion status | Trajectories | SOTA method / status | Model | Link | Published description |
|---:|---|---|---|---:|---|---|---|---|
| 384 | `symbolic_regression_chem_react_CRK0` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1174 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: −0.19​A2+0.19​A2/(0.75​A4+1)\displaystyle-0.19\,A^{2}+0.19\,A^{2}/(0.75\,A^{4}+1). |
| 385 | `symbolic_regression_chem_react_CRK1` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1157 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: −0.773​A2−0.773​A+0.773​cos⁡(log⁡(A+1))\displaystyle-0.773\,A^{2}-0.773\,A+0.773\,\cos(\log(A+1)). |
| 386 | `symbolic_regression_chem_react_CRK10` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1162 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: −0.175​A2+0.175​sin⁡(log⁡(A+1))\displaystyle-0.175\,A^{2}+0.175\,\sin(\log(A+1)). |
| 387 | `symbolic_regression_chem_react_CRK11` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1169 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: −0.882​A2+0.882​sin⁡(A)\displaystyle-0.882\,A^{2}+0.882\,\sin(\sqrt{A}). |
| 388 | `symbolic_regression_chem_react_CRK2` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1160 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: −0.195​A+0.195​cos⁡(log⁡(A+1))\displaystyle-0.195\,A+0.195\,\cos(\log(A+1)). |
| 389 | `symbolic_regression_chem_react_CRK3` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1159 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: −0.548​A2−0.548​A​e−0.548​t+0.548​cos⁡(log⁡(A+1))\displaystyle-0.548\,A^{2}-0.548\,A\,e^{-0.548t}+0.548\,\cos(\log(A+1)). |
| 390 | `symbolic_regression_chem_react_CRK4` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1167 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: −0.115​A2+0.115​A​log⁡(0.257​t+1)\displaystyle-0.115\,A^{2}+0.115\,A\,\log(0.257\,t+1). |
| 391 | `symbolic_regression_chem_react_CRK5` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1164 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: −0.325​A+0.325​A0.333\displaystyle-0.325\,\sqrt{A}+0.325\,A^{0.333}. |
| 392 | `symbolic_regression_chem_react_CRK6` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1160 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: −0.447​A​e−0.447​t+0.447​sin⁡(A)\displaystyle-0.447\,A\,e^{-0.447t}+0.447\,\sin(\sqrt{A}). |
| 393 | `symbolic_regression_chem_react_CRK7` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1164 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: −0.732​A​e−0.732​t+0.732​cos⁡(log⁡(A+1))\displaystyle-0.732\,A\,e^{-0.732t}+0.732\,\cos(\log(A+1)). |
| 394 | `symbolic_regression_chem_react_CRK8` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1177 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: −0.679​A2−0.679​A+0.679​sin⁡(log⁡(A+1))\displaystyle-0.679\,A^{2}-0.679\,A+0.679\,\sin(\log(A+1)). |
| 395 | `symbolic_regression_chem_react_CRK9` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1162 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: −0.26​A+0.26​cos⁡(log⁡(A+1))\displaystyle-0.26\,\sqrt{A}+0.26\,\cos(\log(A+1)). |

##### SR - Physics Oscillation

- **Question:** Discover a symbolic equation that explains a physical-oscillation dataset.
- **Input:** Observed variables/data, allowed operators, starter expression/program, and fit feedback.
- **Output:** Executable symbolic-regression program or equation.
- **Evaluation:** LLM-SRBench evaluates predictive fit and task validity with its deterministic data split.
- **Environment:** Python symbolic-regression environment with the PO dataset and evaluator.
- **Metric family:** Task-specific symbolic-regression fit objective.

| # | Task ID | Upstream source | Paper/expansion status | Trajectories | SOTA method / status | Model | Link | Published description |
|---:|---|---|---|---:|---|---|---|---|
| 396 | `symbolic_regression_phys_osc_PO0` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1171 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: F0​sin⁡t−β​sin⁡v−ω02​x3−ω02​x​e−\|x\|\displaystyle F_{0}\sin t-\beta\sin v-\omega_{0}^{2}x^{3}-\omega_{0}^{2}x\,e^{-\|x\|}. |
| 397 | `symbolic_regression_phys_osc_PO1` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1173 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: F0​sin⁡t−ω02​x−ω02​x​e−\|x\|\displaystyle F_{0}\sin t-\omega_{0}^{2}x-\omega_{0}^{2}x\,e^{-\|x\|}. |
| 398 | `symbolic_regression_phys_osc_PO10` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1170 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: F0​sin⁡t−ω02​(γ​t+1)​x−ω02​x3−ω02​x\displaystyle F_{0}\sin t-\omega_{0}^{2}(\gamma t+1)x-\omega_{0}^{2}x^{3}-\omega_{0}^{2}x. |
| 399 | `symbolic_regression_phys_osc_PO11` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1168 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: −β​sin⁡v−ω02​(γ​t+1)​x−ω02​x3\displaystyle-\beta\sin v-\omega_{0}^{2}(\gamma t+1)x-\omega_{0}^{2}x^{3}. |
| 400 | `symbolic_regression_phys_osc_PO12` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1160 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: F0​sin⁡t−α​v3−β​\|v\|0.333−ω02​(γ​t+1)​x−ω02​x\displaystyle F_{0}\sin t-\alpha v^{3}-\beta\|v\|^{0.333}-\omega_{0}^{2}(\gamma t+1)x-\omega_{0}^{2}x. |
| 401 | `symbolic_regression_phys_osc_PO13` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1167 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: F0​sin⁡t−μ⁡(1−x2)​v−ω02​(γ​\|v\|0.333+1)​x\displaystyle F_{0}\sin t-\mu(1-x^{2})v-\omega_{0}^{2}(\gamma\|v\|^{0.333}+1)x. |
| 402 | `symbolic_regression_phys_osc_PO14` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1149 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: F0​sin⁡t−β​log⁡(\|v\|+1)−β​sin⁡v−2​β​v−μ⁡(1−x2)​v\displaystyle F_{0}\sin t-\beta\log(\|v\|+1)-\beta\sin v-2\beta v-\mu(1-x^{2})v. |
| 403 | `symbolic_regression_phys_osc_PO15` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1151 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: F0​sin⁡t−ω02​(γ​\|v\|0.333+1)​x−ω02​x−ω02​x​e−\|x\|\displaystyle F_{0}\sin t-\omega_{0}^{2}(\gamma\|v\|^{0.333}+1)x-\omega_{0}^{2}x-\omega_{0}^{2}x\,e^{-\|x\|}. |
| 404 | `symbolic_regression_phys_osc_PO16` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1166 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: F0​sin⁡t−β​sin⁡(x)​v−β​sin⁡v−ω02​x3\displaystyle F_{0}\sin t-\beta\sin(x)\,v-\beta\sin v-\omega_{0}^{2}x^{3}. |
| 405 | `symbolic_regression_phys_osc_PO17` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1170 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: F0​sin⁡t−β​sin⁡(x)​v−2​β​v−ω02​x\displaystyle F_{0}\sin t-\beta\sin(x)\,v-2\beta v-\omega_{0}^{2}x. |
| 406 | `symbolic_regression_phys_osc_PO18` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1161 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: −β​sin⁡(x)​v−ω02​x\displaystyle-\beta\sin(x)\,v-\omega_{0}^{2}x. |
| 407 | `symbolic_regression_phys_osc_PO19` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1154 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: −2​β​v−ω02​x​e−\|x\|\displaystyle-2\beta v-\omega_{0}^{2}x\,e^{-\|x\|}. |
| 408 | `symbolic_regression_phys_osc_PO2` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1161 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: −α​v3−μ⁡(1−x2)​v−ω02​x−ω02​x​e−\|x\|\displaystyle-\alpha v^{3}-\mu(1-x^{2})v-\omega_{0}^{2}x-\omega_{0}^{2}x\,e^{-\|x\|}. |
| 409 | `symbolic_regression_phys_osc_PO20` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1158 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: −α​v3−β​log⁡(\|v\|+1)−2​β​v−μ⁡(1−v2)​v−ω02​(γ​\|v\|0.333+1)​x\displaystyle-\alpha v^{3}-\beta\log(\|v\|+1)-2\beta v-\mu(1-v^{2})v-\omega_{0}^{2}(\gamma\|v\|^{0.333}+1)x. |
| 410 | `symbolic_regression_phys_osc_PO21` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1165 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: F0​sin⁡t−β​sin⁡(x)​v\displaystyle F_{0}\sin t-\beta\sin(x)\,v. |
| 411 | `symbolic_regression_phys_osc_PO22` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1165 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: −2​β​v−β​e−\|x\|​v−μ⁡(1−x2)​v−ω02​x3\displaystyle-2\beta v-\beta e^{-\|x\|}v-\mu(1-x^{2})v-\omega_{0}^{2}x^{3}. |
| 412 | `symbolic_regression_phys_osc_PO23` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1161 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: F0​sin⁡t−β​log⁡(\|v\|+1)−ω02​x​e−\|x\|\displaystyle F_{0}\sin t-\beta\log(\|v\|+1)-\omega_{0}^{2}x\,e^{-\|x\|}. |
| 413 | `symbolic_regression_phys_osc_PO24` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1161 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: F0​sin⁡t−α​v3−β​log⁡(\|v\|+1)\displaystyle F_{0}\sin t-\alpha v^{3}-\beta\log(\|v\|+1). |
| 414 | `symbolic_regression_phys_osc_PO25` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1166 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: F0​sin⁡t−β​sin⁡v\displaystyle F_{0}\sin t-\beta\sin v. |
| 415 | `symbolic_regression_phys_osc_PO26` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1159 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: F0​sin⁡t−β​log⁡(\|v\|+1)−2​β​v−ω02​x3\displaystyle F_{0}\sin t-\beta\log(\|v\|+1)-2\beta v-\omega_{0}^{2}x^{3}. |
| 416 | `symbolic_regression_phys_osc_PO27` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1151 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: F0​sin⁡t−α​v3−2​β​v−β​e−\|v\|​v\displaystyle F_{0}\sin t-\alpha v^{3}-2\beta v-\beta e^{-\|v\|}v. |
| 417 | `symbolic_regression_phys_osc_PO28` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1164 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: −2​β​v−ω02​(γ​\|v\|0.333+1)​x−ω02​x3−ω02​x\displaystyle-2\beta v-\omega_{0}^{2}(\gamma\|v\|^{0.333}+1)x-\omega_{0}^{2}x^{3}-\omega_{0}^{2}x. |
| 418 | `symbolic_regression_phys_osc_PO29` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1163 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: −μ⁡(1−x2)​v−ω02​(γ​t+1)​x−ω02​x3\displaystyle-\mu(1-x^{2})v-\omega_{0}^{2}(\gamma t+1)x-\omega_{0}^{2}x^{3}. |
| 419 | `symbolic_regression_phys_osc_PO3` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1172 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: F0​sin⁡t−β​sin⁡v−2​β​v\displaystyle F_{0}\sin t-\beta\sin v-2\beta v. |
| 420 | `symbolic_regression_phys_osc_PO30` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1156 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: −α​v3−β​sin⁡(x)​v−β​sin⁡v−ω02​x3\displaystyle-\alpha v^{3}-\beta\sin(x)\,v-\beta\sin v-\omega_{0}^{2}x^{3}. |
| 421 | `symbolic_regression_phys_osc_PO31` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1155 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: −ω02​(γ​\|v\|0.333+1)​x−ω02​x3\displaystyle-\omega_{0}^{2}(\gamma\|v\|^{0.333}+1)x-\omega_{0}^{2}x^{3}. |
| 422 | `symbolic_regression_phys_osc_PO32` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1154 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: F0​sin⁡t−α​v3−β​e−\|v\|​v−ω02​x3\displaystyle F_{0}\sin t-\alpha v^{3}-\beta e^{-\|v\|}v-\omega_{0}^{2}x^{3}. |
| 423 | `symbolic_regression_phys_osc_PO33` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1178 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: −2​β​v−μ⁡(1−v2)​v−ω02​(γ​t+1)​x−ω02​x\displaystyle-2\beta v-\mu(1-v^{2})v-\omega_{0}^{2}(\gamma t+1)x-\omega_{0}^{2}x. |
| 424 | `symbolic_regression_phys_osc_PO34` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1160 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: −2​β​v−μ⁡(1−v2)​v−ω02​(γ​\|v\|0.333+1)​x\displaystyle-2\beta v-\mu(1-v^{2})v-\omega_{0}^{2}(\gamma\|v\|^{0.333}+1)x. |
| 425 | `symbolic_regression_phys_osc_PO35` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1166 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: F0​sin⁡t−β​sin⁡v−ω02​(γ​\|v\|0.333+1)​x\displaystyle F_{0}\sin t-\beta\sin v-\omega_{0}^{2}(\gamma\|v\|^{0.333}+1)x. |
| 426 | `symbolic_regression_phys_osc_PO36` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1170 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: F0​sin⁡t−β​e−\|x\|​v\displaystyle F_{0}\sin t-\beta e^{-\|x\|}v. |
| 427 | `symbolic_regression_phys_osc_PO37` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1172 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: F0​sin⁡t−α​v3−2​β​v−ω02​(γ​t+1)​x\displaystyle F_{0}\sin t-\alpha v^{3}-2\beta v-\omega_{0}^{2}(\gamma t+1)x. |
| 428 | `symbolic_regression_phys_osc_PO38` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1160 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: −β​sin⁡v−μ⁡(1−x2)​v−ω02​x​e−\|x\|\displaystyle-\beta\sin v-\mu(1-x^{2})v-\omega_{0}^{2}x\,e^{-\|x\|}. |
| 429 | `symbolic_regression_phys_osc_PO39` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1175 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: F0​sin⁡t−α​v3−β​e−\|x\|​v−μ⁡(1−v2)​v\displaystyle F_{0}\sin t-\alpha v^{3}-\beta e^{-\|x\|}v-\mu(1-v^{2})v. |
| 430 | `symbolic_regression_phys_osc_PO4` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1166 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: F0​sin⁡t−α​v3−ω02​(γ​\|v\|0.333+1)​x−ω02​x\displaystyle F_{0}\sin t-\alpha v^{3}-\omega_{0}^{2}(\gamma\|v\|^{0.333}+1)x-\omega_{0}^{2}x. |
| 431 | `symbolic_regression_phys_osc_PO40` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1155 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: F0​sin⁡t−β​\|v\|0.333−ω02​(γ​\|v\|0.333+1)​x−ω02​x3−ω02​x\displaystyle F_{0}\sin t-\beta\|v\|^{0.333}-\omega_{0}^{2}(\gamma\|v\|^{0.333}+1)x-\omega_{0}^{2}x^{3}-\omega_{0}^{2}x. |
| 432 | `symbolic_regression_phys_osc_PO41` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1166 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: −μ⁡(1−x2)​v−ω02​x​e−\|x\|\displaystyle-\mu(1-x^{2})v-\omega_{0}^{2}x\,e^{-\|x\|}. |
| 433 | `symbolic_regression_phys_osc_PO42` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1173 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: F0​sin⁡t−α​v3−β​sin⁡(x)​v−2​β​v\displaystyle F_{0}\sin t-\alpha v^{3}-\beta\sin(x)\,v-2\beta v. |
| 434 | `symbolic_regression_phys_osc_PO43` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1163 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: F0​sin⁡t−β​sin⁡(x)​v−2​β​v−μ⁡(1−x2)​v−ω02​x​e−\|x\|\displaystyle F_{0}\sin t-\beta\sin(x)\,v-2\beta v-\mu(1-x^{2})v-\omega_{0}^{2}x\,e^{-\|x\|}. |
| 435 | `symbolic_regression_phys_osc_PO5` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1165 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: −β​sin⁡v−2​β​v−ω02​(γ​\|v\|0.333+1)​x−ω02​x3−ω02​x\displaystyle-\beta\sin v-2\beta v-\omega_{0}^{2}(\gamma\|v\|^{0.333}+1)x-\omega_{0}^{2}x^{3}-\omega_{0}^{2}x. |
| 436 | `symbolic_regression_phys_osc_PO6` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1167 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: −β​log⁡(\|v\|+1)−2​β​v−ω02​x3\displaystyle-\beta\log(\|v\|+1)-2\beta v-\omega_{0}^{2}x^{3}. |
| 437 | `symbolic_regression_phys_osc_PO7` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1171 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: −α​v3−β​\|v\|0.333−ω02​x3\displaystyle-\alpha v^{3}-\beta\|v\|^{0.333}-\omega_{0}^{2}x^{3}. |
| 438 | `symbolic_regression_phys_osc_PO8` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1169 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: −β​\|v\|0.333−ω02​x3\displaystyle-\beta\|v\|^{0.333}-\omega_{0}^{2}x^{3}. |
| 439 | `symbolic_regression_phys_osc_PO9` | LLM-SRBench | `identified-in-arxiv-v1-appendix` | 1163 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | Ground-truth: F0​sin⁡t−μ⁡(1−x2)​v−ω02​(γ​\|v\|0.333+1)​x−ω02​x\displaystyle F_{0}\sin t-\mu(1-x^{2})v-\omega_{0}^{2}(\gamma\|v\|^{0.333}+1)x-\omega_{0}^{2}x. |

##### Single-cell RNA Denoising

- **Question:** Improve an executable denoising method for single-cell RNA-seq counts.
- **Input:** Training dataset, starter denoising program, evaluator feedback, and held-out dataset contract.
- **Output:** Executable Python denoising algorithm and predicted matrix.
- **Evaluation:** OpenProblems-derived evaluator combines normalized reconstruction metrics including MSE and Poisson score.
- **Environment:** Python scientific-computing environment with OpenProblems v1.0.0-compatible data/evaluator.
- **Metric family:** Mean normalized denoising score.

| # | Task ID | Upstream source | Paper/expansion status | Trajectories | SOTA method / status | Model | Link | Published description |
|---:|---|---|---|---:|---|---|---|---|
| 440 | `biology_denoising_pancreas` | OpenProblems single-cell denoising | `paper-v1-seed-identified-by-official-manifest` | 174 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 441 | `biology_denoising_pbmc` | OpenProblems single-cell denoising | `paper-v1-seed-identified-by-official-manifest` | 166 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |
| 442 | `biology_denoising_tabula` | OpenProblems single-cell denoising | `paper-v1-seed-identified-by-official-manifest` | 163 | Not published per task in Finch; consult upstream evaluator | — | [Finch provenance](https://huggingface.co/datasets/minnesotanlp/Finch-Collection) | No per-task description in arXiv v1; use the upstream evaluator artifact. |


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
- **Source-suite reported result:** SimpleTES + gpt-oss-120b: 0.44 ↓
- **Current SOTA method / status:** SimpleTES (source incumbent; global SOTA unverified)
- **Model / backbone:** gpt-oss-120b
- **Current record located:** **No independent current record located** — source report: SimpleTES + gpt-oss-120b 0.44 ↓
- **Evidence status:** `no-independent-current-record-located` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **Record note:** A released SimpleTES result exists for this exact contract, but no independent current leaderboard or later matched-evaluator comparison was located. It is retained as a source-reported contract incumbent, not labeled global SOTA.
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
- **Source-suite reported result:** SimpleTES + gpt-oss-120b: 0.104 ↓
- **Current SOTA method / status:** SimpleTES (source incumbent; global SOTA unverified)
- **Model / backbone:** gpt-oss-120b
- **Current record located:** **No independent current record located** — source report: SimpleTES + gpt-oss-120b 0.104 ↓
- **Evidence status:** `no-independent-current-record-located` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **Record note:** A released SimpleTES result exists for this exact contract, but no independent current leaderboard or later matched-evaluator comparison was located. It is retained as a source-reported contract incumbent, not labeled global SOTA.
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
- **Source-suite reported result:** SimpleTES + gpt-oss-120b: 0.820129 ↓
- **Current SOTA method / status:** SimpleTES (source incumbent; global SOTA unverified)
- **Model / backbone:** gpt-oss-120b
- **Current record located:** **No independent current record located** — source report: SimpleTES + gpt-oss-120b 0.820129 ↓
- **Evidence status:** `no-independent-current-record-located` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **Record note:** A released SimpleTES result exists for this exact contract, but no independent current leaderboard or later matched-evaluator comparison was located. It is retained as a source-reported contract incumbent, not labeled global SOTA.
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
- **Source-suite reported result:** SimpleTES + gpt-oss-120b: 2.635983 ↑
- **Current SOTA method / status:** AlphaEvolve (live-board tie)
- **Model / backbone:** Not disclosed for leaderboard row
- **Current record located:** **2.6359830849 ↑** — AlphaEvolve (tied on the live board)
- **Evidence status:** `official-live-leaderboard` as of 2026-08-25
- **Primary evidence:** [source 1](https://einsteinarena.com/problems/circle-packing) · [source 2](https://arxiv.org/abs/2511.02864) · [source 3](https://arxiv.org/html/2604.19341) · [source 4](https://github.com/InternScience/MLEvolve)
- **Record note:** EinsteinArena lists AlphaEvolve first at 2.6359830849, with several agents tied at displayed precision. SimpleTES reports 2.635983 and MLEvolve 2.6359830395; neither should be presented as the unique current record.
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
- **Source-suite reported result:** SimpleTES + gpt-oss-120b: 2.939572 ↑
- **Current SOTA method / status:** nanodiscover (EFT)
- **Model / backbone:** Qwen3-8B / Finch-8B
- **Current record located:** **2.939573 ↑** — nanodiscover + Qwen3-8B / Finch-8B (EFT), tied at published precision
- **Evidence status:** `cross-paper-tie-at-published-precision` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2606.29082) · [source 2](https://arxiv.org/html/2604.19341) · [source 3](https://arxiv.org/abs/2511.02864)
- **Record note:** EFT Table 6 reports 2.939573 for both nanodiscover + Qwen3-8B and nanodiscover + Finch-8B, above the 2.939572 SimpleTES source result at displayed precision. The two 2.939573 entries are tied only at published precision; full-precision artifacts are needed to order them.
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
- **Source-suite reported result:** SimpleTES + gpt-oss-120b: 0.380868 ↓
- **Current SOTA method / status:** CodexProLong
- **Model / backbone:** Not disclosed by leaderboard
- **Current record located:** **0.38085857 ↓** — CodexProLong
- **Evidence status:** `official-live-leaderboard-with-certification-caveat` as of 2026-08-25
- **Primary evidence:** [source 1](https://einsteinarena.com/problems/erdos-min-overlap) · [source 2](https://github.com/bzanghi/erdos-minimum-overlap-bochner/blob/main/MINIMUM_OVERLAP_STATE_2026-07-25b.md) · [source 3](https://test-time-training.github.io/discover/) · [source 4](https://arxiv.org/html/2604.19341)
- **Record note:** EinsteinArena's live leader is CodexProLong. The independent certification note verifies a slightly older 0.3808590566148069 construction and explains why a widely cited lower SimpleTES number was affected by normalization; leaderboard rank and rigorous certification are therefore reported separately.
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
- **Source-suite reported result:** SimpleTES + gpt-oss-120b: 0.795108 ↓
- **Current SOTA method / status:** SimpleTES (source incumbent; global SOTA unverified)
- **Model / backbone:** gpt-oss-120b
- **Current record located:** **No independent current record located** — source report: SimpleTES + gpt-oss-120b 0.795108 ↓
- **Evidence status:** `no-independent-current-record-located` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **Record note:** A released SimpleTES result exists for this exact contract, but no independent current leaderboard or later matched-evaluator comparison was located. It is retained as a source-reported contract incumbent, not labeled global SOTA.
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
- **Source-suite reported result:** SimpleTES + gpt-oss-120b: 0.935673 ↑
- **Current SOTA method / status:** Orrick et al. construction; matched by SimpleTES
- **Model / backbone:** Human construction / gpt-oss-120b match
- **Current record located:** **0.935673 ↑** — Orrick et al. human record (matched by SimpleTES)
- **Evidence status:** `historical-record-matched-by-agent` as of 2026-08-25
- **Primary evidence:** [source 1](https://maths-people.anu.edu.au/~brent/maxdet/order29/) · [source 2](https://arxiv.org/html/2604.19341)
- **Record note:** The order-29 construction predates SimpleTES. SimpleTES matches the normalized determinant at published precision; it did not originate the record.
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
- **Source-suite reported result:** SimpleTES + gpt-oss-120b: 2502.3 ↓
- **Current SOTA method / status:** SimpleTES (source incumbent; global SOTA unverified)
- **Model / backbone:** gpt-oss-120b
- **Current record located:** **No independent current record located** — source report: SimpleTES + gpt-oss-120b 2502.3 ↓
- **Evidence status:** `no-independent-current-record-located` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **Record note:** A released SimpleTES result exists for this exact contract, but no independent current leaderboard or later matched-evaluator comparison was located. It is retained as a source-reported contract incumbent, not labeled global SOTA.
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
- **Source-suite reported result:** SimpleTES + gpt-oss-120b: 0.326993 ↓
- **Current SOTA method / status:** SimpleTES (source incumbent; global SOTA unverified)
- **Model / backbone:** gpt-oss-120b
- **Current record located:** **No independent current record located** — source report: SimpleTES + gpt-oss-120b 0.326993 ↓
- **Evidence status:** `no-independent-current-record-located` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **Record note:** A released SimpleTES result exists for this exact contract, but no independent current leaderboard or later matched-evaluator comparison was located. It is retained as a source-reported contract incumbent, not labeled global SOTA.
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
- **Source-suite reported result:** SimpleTES + gpt-oss-120b: 1.552968 ↓
- **Current SOTA method / status:** SimpleTES (source incumbent; global SOTA unverified)
- **Model / backbone:** gpt-oss-120b
- **Current record located:** **No independent current record located** — source report: SimpleTES + gpt-oss-120b 1.552968 ↓
- **Evidence status:** `no-independent-current-record-located` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **Record note:** A released SimpleTES result exists for this exact contract, but no independent current leaderboard or later matched-evaluator comparison was located. It is retained as a source-reported contract incumbent, not labeled global SOTA.
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
- **Source-suite reported result:** SimpleTES + gpt-oss-120b: 0.991 ↑
- **Current SOTA method / status:** SLDAgent
- **Model / backbone:** Gemini-3-Pro-Preview
- **Current record located:** **0.993529 ↑** — SLDAgent + Gemini-3-Pro-Preview
- **Evidence status:** `official-results-dataset` as of 2026-08-25
- **Primary evidence:** [source 1](https://huggingface.co/datasets/pkuHaowei/scaling_law_discovery_results) · [source 2](https://github.com/linhaowei1/SLD) · [source 3](https://arxiv.org/html/2604.19341)
- **Record note:** Computed from the released SLDBench result records for the domain_mixture split. It exceeds the 0.991 SimpleTES source result under the matched split metric.
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
- **Source-suite reported result:** SimpleTES + gpt-oss-120b: 0.712 ↑
- **Current SOTA method / status:** SLDAgent
- **Model / backbone:** GPT-5
- **Current record located:** **0.847918 ↑** — SLDAgent + GPT-5
- **Evidence status:** `official-results-dataset` as of 2026-08-25
- **Primary evidence:** [source 1](https://huggingface.co/datasets/pkuHaowei/scaling_law_discovery_results) · [source 2](https://github.com/linhaowei1/SLD) · [source 3](https://arxiv.org/html/2604.19341)
- **Record note:** Computed from the released SLDBench result records for the lr_bsz split. It exceeds the 0.712 SimpleTES source result.
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
- **Source-suite reported result:** SimpleTES + gpt-oss-120b: 1.0 ↑
- **Current SOTA method / status:** Unresolved: SLDAgent vs SimpleTES
- **Model / backbone:** Claude Sonnet 4.5 / gpt-oss-120b
- **Current record located:** **Unresolved at published precision** — SLDAgent + Claude Sonnet 4.5 0.999971; SimpleTES + gpt-oss-120b (rounded) 1.0
- **Evidence status:** `incomparable-published-precision` as of 2026-08-25
- **Primary evidence:** [source 1](https://huggingface.co/datasets/pkuHaowei/scaling_law_discovery_results) · [source 2](https://github.com/linhaowei1/SLD) · [source 3](https://arxiv.org/html/2604.19341)
- **Record note:** The official SLDBench result dataset has SLDAgent + Claude Sonnet 4.5 at 0.999971, while SimpleTES reports 1.000 only to three decimals. The rounded number cannot establish a strict win or tie, so no unique current record is assigned.
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
- **Source-suite reported result:** SimpleTES + gpt-oss-120b: -0.008 ↑
- **Current SOTA method / status:** Aider
- **Model / backbone:** GPT-5
- **Current record located:** **0.38070320345369735 ↑** — Aider + GPT-5
- **Evidence status:** `official-results-dataset` as of 2026-08-25
- **Primary evidence:** [source 1](https://huggingface.co/datasets/pkuHaowei/scaling_law_discovery_results) · [source 2](https://github.com/linhaowei1/SLD) · [source 3](https://arxiv.org/html/2604.19341)
- **Record note:** Computed from the released SLDBench easy_question/u-shape result records. It exceeds the -0.008 SimpleTES source result.
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
- **Source-suite reported result:** SimpleTES + gpt-oss-120b: 0.962694 ↑
- **Current SOTA method / status:** ClaudeExplorer
- **Model / backbone:** Not disclosed by leaderboard
- **Current record located:** **0.96359 ↑** — ClaudeExplorer
- **Evidence status:** `official-live-leaderboard` as of 2026-08-25
- **Primary evidence:** [source 1](https://einsteinarena.com/problems/second-autocorrelation-inequality) · [source 2](https://test-time-training.github.io/discover/) · [source 3](https://arxiv.org/html/2604.19341) · [source 4](https://github.com/InternScience/MLEvolve)
- **Record note:** EinsteinArena currently ranks ClaudeExplorer first. The board also records AlphaEvolve and TTT-Discover as earlier results; SimpleTES's 0.962694 is no longer the public leader.
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
- **Source-suite reported result:** SimpleTES + gpt-oss-120b: 0.74 ↑
- **Current SOTA method / status:** SimpleTES (source incumbent; global SOTA unverified)
- **Model / backbone:** gpt-oss-120b
- **Current record located:** **No independent current record located** — source report: SimpleTES + gpt-oss-120b 0.74 ↑
- **Evidence status:** `no-independent-current-record-located` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **Record note:** A released SimpleTES result exists for this exact contract, but no independent current leaderboard or later matched-evaluator comparison was located. It is retained as a source-reported contract incumbent, not labeled global SOTA.
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
- **Source-suite reported result:** SimpleTES + trajectory-level post-trained gpt-oss-120b: 1.144887 ↑
- **Current SOTA method / status:** MLEvolve
- **Model / backbone:** Gemini-3.1-Pro-preview
- **Current record located:** **1.1901774219 ↑** — MLEvolve
- **Evidence status:** `source-reported-matched-task-table` as of 2026-08-25
- **Primary evidence:** [source 1](https://github.com/InternScience/MLEvolve) · [source 2](https://arxiv.org/abs/2511.02864) · [source 3](https://arxiv.org/html/2604.19341)
- **Record note:** MLEvolve's official comparison table reports 1.1901774219 on Sums differences problem 1, above AlphaEvolve (1.1479889651) and SimpleTES (1.143975 in that table; 1.144887 in the later post-trained SimpleTES result).
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
- **Source-suite reported result:** SimpleTES + gpt-oss-120b: 15147 ↓
- **Current SOTA method / status:** SimpleTES (source incumbent; global SOTA unverified)
- **Model / backbone:** gpt-oss-120b
- **Current record located:** **No independent current record located** — source report: SimpleTES + gpt-oss-120b 15147 ↓
- **Evidence status:** `no-independent-current-record-located` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **Record note:** A released SimpleTES result exists for this exact contract, but no independent current leaderboard or later matched-evaluator comparison was located. It is retained as a source-reported contract incumbent, not labeled global SOTA.
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
- **Source-suite reported result:** SimpleTES + gpt-oss-120b: 1.453675 ↓
- **Current SOTA method / status:** Poolish
- **Model / backbone:** Not disclosed by leaderboard
- **Current record located:** **1.45080664 ↓** — Poolish
- **Evidence status:** `official-live-leaderboard` as of 2026-08-25
- **Primary evidence:** [source 1](https://einsteinarena.com/problems/third-autocorrelation-inequality) · [source 2](https://arxiv.org/html/2604.19341) · [source 3](https://github.com/InternScience/MLEvolve)
- **Record note:** EinsteinArena currently ranks Poolish first. SimpleTES's 1.453675 is a historical source result, not the current live record.
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
- **Source-suite reported result:** SimpleTES + gpt-oss-120b: 1.122 ↓
- **Current SOTA method / status:** K-Search
- **Model / backbone:** GPT-5.2 (released GPUMode default)
- **Current record located:** **1.028 ↓** — K-Search
- **Evidence status:** `matched-upstream-evaluator-local-artifact` as of 2026-08-25
- **Primary evidence:** [source 1](https://github.com/caoshiyi/K-Search) · [source 2](https://test-time-training.github.io/discover/) · [source 3](https://arxiv.org/html/2604.19341)
- **Record note:** K-Search reports 1.028 ms on H100 across the seven upstream GPUMode workloads and releases the generated kernels. It beats the 1.122 ms SimpleTES paper result, but is a local matched-evaluator artifact rather than an official leaderboard submission.
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
- **Source-suite reported result:** SimpleTES + gpt-oss-120b: 3.430214 ↓
- **Current SOTA method / status:** SimpleTES (source incumbent; global SOTA unverified)
- **Model / backbone:** gpt-oss-120b
- **Current record located:** **No independent current record located** — source report: SimpleTES + gpt-oss-120b 3.430214 ↓
- **Evidence status:** `no-independent-current-record-located` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **Record note:** A released SimpleTES result exists for this exact contract, but no independent current leaderboard or later matched-evaluator comparison was located. It is retained as a source-reported contract incumbent, not labeled global SOTA.
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
- **Source-suite reported result:** SimpleTES + gpt-oss-120b: 0.0165 ↓
- **Current SOTA method / status:** SimpleTES (source incumbent; global SOTA unverified)
- **Model / backbone:** gpt-oss-120b
- **Current record located:** **No independent current record located** — source report: SimpleTES + gpt-oss-120b 0.0165 ↓
- **Evidence status:** `no-independent-current-record-located` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **Record note:** A released SimpleTES result exists for this exact contract, but no independent current leaderboard or later matched-evaluator comparison was located. It is retained as a source-reported contract incumbent, not labeled global SOTA.
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
- **Source-suite reported result:** SimpleTES + gpt-oss-120b: 0.0211 ↓
- **Current SOTA method / status:** SimpleTES (source incumbent; global SOTA unverified)
- **Model / backbone:** gpt-oss-120b
- **Current record located:** **No independent current record located** — source report: SimpleTES + gpt-oss-120b 0.0211 ↓
- **Evidence status:** `no-independent-current-record-located` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **Record note:** A released SimpleTES result exists for this exact contract, but no independent current leaderboard or later matched-evaluator comparison was located. It is retained as a source-reported contract incumbent, not labeled global SOTA.
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
- **Source-suite reported result:** SimpleTES + gpt-oss-120b: 0.023 ↓
- **Current SOTA method / status:** SimpleTES (source incumbent; global SOTA unverified)
- **Model / backbone:** gpt-oss-120b
- **Current record located:** **No independent current record located** — source report: SimpleTES + gpt-oss-120b 0.023 ↓
- **Evidence status:** `no-independent-current-record-located` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **Record note:** A released SimpleTES result exists for this exact contract, but no independent current leaderboard or later matched-evaluator comparison was located. It is retained as a source-reported contract incumbent, not labeled global SOTA.
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
- **Source-suite reported result:** SimpleTES + gpt-oss-120b: 0.0251 ↓
- **Current SOTA method / status:** SimpleTES (source incumbent; global SOTA unverified)
- **Model / backbone:** gpt-oss-120b
- **Current record located:** **No independent current record located** — source report: SimpleTES + gpt-oss-120b 0.0251 ↓
- **Evidence status:** `no-independent-current-record-located` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **Record note:** A released SimpleTES result exists for this exact contract, but no independent current leaderboard or later matched-evaluator comparison was located. It is retained as a source-reported contract incumbent, not labeled global SOTA.
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
- **Source-suite reported result:** SimpleTES + gpt-oss-120b: 0.0259 ↓
- **Current SOTA method / status:** SimpleTES (source incumbent; global SOTA unverified)
- **Model / backbone:** gpt-oss-120b
- **Current record located:** **No independent current record located** — source report: SimpleTES + gpt-oss-120b 0.0259 ↓
- **Evidence status:** `no-independent-current-record-located` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **Record note:** A released SimpleTES result exists for this exact contract, but no independent current leaderboard or later matched-evaluator comparison was located. It is retained as a source-reported contract incumbent, not labeled global SOTA.
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
- **Source-suite reported result:** SimpleTES + gpt-oss-120b: 19507.5 ↓
- **Current SOTA method / status:** SimpleTES (source incumbent; global SOTA unverified)
- **Model / backbone:** gpt-oss-120b
- **Current record located:** **No independent current record located** — source report: SimpleTES + gpt-oss-120b 19507.5 ↓
- **Evidence status:** `no-independent-current-record-located` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2604.19341) · [source 2](https://github.com/wq-will/SimpleTES/tree/main/best_results)
- **Record note:** A released SimpleTES result exists for this exact contract, but no independent current leaderboard or later matched-evaluator comparison was located. It is retained as a source-reported contract incumbent, not labeled global SOTA.
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
- **Source-suite reported result:** Not available as a task-level result
- **Current SOTA method / status:** No per-task SOTA published (suite aggregate: Tycho)
- **Model / backbone:** Not disclosed
- **Current record located:** **Not published per task** — suite best: Tycho, 100.0 percent
- **Evidence status:** `community-self-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arcprize.org/leaderboard/community) · [source 2](https://arcprize.org/scorecards/08b98aa0-5df0-42c0-b501-856f553a21e9) · [source 3](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)
- **Record note:** The official community page reports Tycho at 100.0% on the public-demo suite, but labels community results self-reported and does not expose an attributable per-game breakdown. The suite score must not be copied into this task row.
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
- **Source-suite reported result:** Not available as a task-level result
- **Current SOTA method / status:** No per-task SOTA published (suite aggregate: Tycho)
- **Model / backbone:** Not disclosed
- **Current record located:** **Not published per task** — suite best: Tycho, 100.0 percent
- **Evidence status:** `community-self-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arcprize.org/leaderboard/community) · [source 2](https://arcprize.org/scorecards/08b98aa0-5df0-42c0-b501-856f553a21e9) · [source 3](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf) · [source 4](https://arcprize.org/replay/591e7e51-5004-4510-9e03-eca2b2d81edb?frame=19)
- **Record note:** The official community page reports Tycho at 100.0% on the public-demo suite, but labels community results self-reported and does not expose an attributable per-game breakdown. The suite score must not be copied into this task row. A public ft09 replay reaches 100%, but its model and harness fields are blank.
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
- **Source-suite reported result:** Not available as a task-level result
- **Current SOTA method / status:** No per-task SOTA published (suite aggregate: Tycho)
- **Model / backbone:** Not disclosed
- **Current record located:** **Not published per task** — suite best: Tycho, 100.0 percent
- **Evidence status:** `community-self-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arcprize.org/leaderboard/community) · [source 2](https://arcprize.org/scorecards/08b98aa0-5df0-42c0-b501-856f553a21e9) · [source 3](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf)
- **Record note:** The official community page reports Tycho at 100.0% on the public-demo suite, but labels community results self-reported and does not expose an attributable per-game breakdown. The suite score must not be copied into this task row.
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
- **Source-suite reported result:** Not available as a task-level result
- **Current SOTA method / status:** No per-task SOTA published (suite aggregate: basic harness)
- **Model / backbone:** Claude Opus 5
- **Current record located:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **Record note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
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
- **Source-suite reported result:** Not available as a task-level result
- **Current SOTA method / status:** No per-task SOTA published (suite aggregate: basic harness)
- **Model / backbone:** Claude Opus 5
- **Current record located:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **Record note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
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
- **Source-suite reported result:** Not available as a task-level result
- **Current SOTA method / status:** No per-task SOTA published (suite aggregate: basic harness)
- **Model / backbone:** Claude Opus 5
- **Current record located:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **Record note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
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
- **Source-suite reported result:** Not available as a task-level result
- **Current SOTA method / status:** No per-task SOTA published (suite aggregate: basic harness)
- **Model / backbone:** Claude Opus 5
- **Current record located:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **Record note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
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
- **Source-suite reported result:** Not available as a task-level result
- **Current SOTA method / status:** No per-task SOTA published (suite aggregate: basic harness)
- **Model / backbone:** Claude Opus 5
- **Current record located:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **Record note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
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
- **Source-suite reported result:** Not available as a task-level result
- **Current SOTA method / status:** No per-task SOTA published (suite aggregate: basic harness)
- **Model / backbone:** Claude Opus 5
- **Current record located:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **Record note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
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
- **Source-suite reported result:** Not available as a task-level result
- **Current SOTA method / status:** No per-task SOTA published (suite aggregate: basic harness)
- **Model / backbone:** Claude Opus 5
- **Current record located:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **Record note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
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
- **Source-suite reported result:** Not available as a task-level result
- **Current SOTA method / status:** No per-task SOTA published (suite aggregate: basic harness)
- **Model / backbone:** Claude Opus 5
- **Current record located:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **Record note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
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
- **Source-suite reported result:** Not available as a task-level result
- **Current SOTA method / status:** No per-task SOTA published (suite aggregate: basic harness)
- **Model / backbone:** Claude Opus 5
- **Current record located:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **Record note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
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
- **Source-suite reported result:** Not available as a task-level result
- **Current SOTA method / status:** No per-task SOTA published (suite aggregate: basic harness)
- **Model / backbone:** Claude Opus 5
- **Current record located:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **Record note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
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
- **Source-suite reported result:** Not available as a task-level result
- **Current SOTA method / status:** No per-task SOTA published (suite aggregate: basic harness)
- **Model / backbone:** Claude Opus 5
- **Current record located:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **Record note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
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
- **Source-suite reported result:** Not available as a task-level result
- **Current SOTA method / status:** No per-task SOTA published (suite aggregate: basic harness)
- **Model / backbone:** Claude Opus 5
- **Current record located:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **Record note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
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
- **Source-suite reported result:** Not available as a task-level result
- **Current SOTA method / status:** No per-task SOTA published (suite aggregate: basic harness)
- **Model / backbone:** Claude Opus 5
- **Current record located:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **Record note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
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
- **Source-suite reported result:** Not available as a task-level result
- **Current SOTA method / status:** No per-task SOTA published (suite aggregate: basic harness)
- **Model / backbone:** Claude Opus 5
- **Current record located:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **Record note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
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
- **Source-suite reported result:** Not available as a task-level result
- **Current SOTA method / status:** No per-task SOTA published (suite aggregate: basic harness)
- **Model / backbone:** Claude Opus 5
- **Current record located:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **Record note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
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
- **Source-suite reported result:** Not available as a task-level result
- **Current SOTA method / status:** No per-task SOTA published (suite aggregate: basic harness)
- **Model / backbone:** Claude Opus 5
- **Current record located:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **Record note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
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
- **Source-suite reported result:** Not available as a task-level result
- **Current SOTA method / status:** No per-task SOTA published (suite aggregate: basic harness)
- **Model / backbone:** Claude Opus 5
- **Current record located:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **Record note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
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
- **Source-suite reported result:** Not available as a task-level result
- **Current SOTA method / status:** No per-task SOTA published (suite aggregate: basic harness)
- **Model / backbone:** Claude Opus 5
- **Current record located:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **Record note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
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
- **Source-suite reported result:** Not available as a task-level result
- **Current SOTA method / status:** No per-task SOTA published (suite aggregate: basic harness)
- **Model / backbone:** Claude Opus 5
- **Current record located:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **Record note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
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
- **Source-suite reported result:** Not available as a task-level result
- **Current SOTA method / status:** No per-task SOTA published (suite aggregate: basic harness)
- **Model / backbone:** Claude Opus 5
- **Current record located:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **Record note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
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
- **Source-suite reported result:** Not available as a task-level result
- **Current SOTA method / status:** No per-task SOTA published (suite aggregate: basic harness)
- **Model / backbone:** Claude Opus 5
- **Current record located:** **Not published per task** — suite best: Claude Opus 5, basic harness, 50 games out of 70
- **Evidence status:** `source-reported-no-task-breakdown` as of 2026-08-25
- **Primary evidence:** [source 1](https://arxiv.org/html/2608.12593) · [source 2](https://digbench.ai/)
- **Record note:** The paper publishes a 50/70 suite-level best but no official per-game result table for P-1 through P-21. Human solvability is a reference, not a model SOTA.
- **Integrity note:** P-series task is public and may be used for development, so report public-versus-private evaluation separately. Pin the game, server, harness, model, prompt, context policy, run count, and step budget.

## Maintenance

The machine-readable SOTA snapshot is [`data/discovery-task-sota.json`](../data/discovery-task-sota.json). Regenerate both artifacts after changing the task registry:

```bash
python scripts/render_discovery_task_sota.py
python scripts/render_discovery_task_sota.py --check
```

For a new record, provide the exact task/version, complete system and harness, score, run count or uncertainty when available, resource envelope, and primary result artifact. A source paper claim or suite leaderboard screenshot alone is insufficient for a task-level SOTA claim.
