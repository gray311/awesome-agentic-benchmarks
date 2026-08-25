# Interactive Discovery Tasks

**Evidence snapshot:** 2026-08-25

Interactive discovery is the ability to infer an unfamiliar environment's rules, objective, and useful abstractions from action-conditioned feedback. It differs from static question answering and from artifact optimization: the agent is not given a complete problem specification and must first discover what problem it is solving.

## Task contract

Every row should make six elements explicit:

| Field | Required evidence |
|---|---|
| Observation | What the agent sees at each turn, including modality and state encoding |
| Action space | Legal state-changing actions and their arguments |
| Hidden structure | Rules, dynamics, objective, or win condition withheld from the agent |
| Feedback | State transitions, errors, scores, lives, and terminal signals |
| Budget | Steps, actions, resets, time, context, and compute |
| Evaluator | Success condition, aggregation, human baseline, and split policy |

## ARC-AGI-3

[ARC-AGI-3](https://arcprize.org/arc-agi/3) is an interactive reasoning benchmark in which agents explore novel visual environments without natural-language instructions. The agent must infer mechanics and goals, build a world model, and complete progressively harder levels.

### Verified protocol

| Property | ARC-AGI-3 contract |
|---|---|
| Input | Turn-based frames up to 64×64 using 16 colors, available actions, and interaction history |
| Actions | `RESET`, `ACTION1`–`ACTION7`; `ACTION6` accepts coordinates and `ACTION7` is undo when supported |
| Hidden information | Objective, mechanics, transition rules, and win condition |
| Terminal states | `NOT_FINISHED`, `WIN`, or `GAME_OVER` |
| Dataset | 25 public demo + 55 semi-private + 55 fully private = 135 environments |
| Metric | Relative Human Action Efficiency (RHAE) |
| Human baseline | Upper-median first-run human action count for each level |
| Level score | `(human_baseline_actions / ai_actions)^2`, capped at 1.15 |
| Aggregation | Level-index-weighted game score; total score is the mean across games |
| Official environment | [ARC-AGI Toolkit](https://github.com/arcprize/ARC-AGI) and hosted API |

The official release report places frontier systems below 1% on the semi-private set:

| Model | Official RHAE |
|---|---:|
| Anthropic Opus 4.6 (Max) | 0.50% |
| Gemini 3.1 Pro Preview | 0.40% |
| OpenAI GPT-5.4 (High) | 0.20% |
| xAI Grok-4.20 Beta | 0.10% |

These are suite-level official results, not scores for the individual public games below. GLM, Kimi, and Qwen do not yet have verified official ARC-AGI-3 rows in the sources reviewed.

### Individually verified public tasks

The official docs expose three games to anonymous users; an API key is required to list the remaining public games. We therefore itemize exactly these three and keep the other 22 public IDs in the extraction queue:

| Task | Official descriptor | Question presented to this registry |
|---|---|---|
| **ARC-AGI-3 ls20 (Agent reasoning)** | Agent reasoning | Discover the hidden mechanics and win condition, then complete the levels efficiently. |
| **ARC-AGI-3 ft09 (Elementary Logic)** | Elementary Logic | Discover the hidden mechanics and win condition, then complete the levels efficiently. |
| **ARC-AGI-3 vc33 (Orchestration)** | Orchestration | Discover the hidden mechanics and win condition, then complete the levels efficiently. |

Public games are demonstrations and development material. They must not be presented as the official generalization score. Semi-private and fully private environment content must never be copied into this repository.

### Integrity and versioning

ARC-AGI-3 is a live 2026 protocol. A reproducible result needs the game ID and version, toolkit/API version, scorecard and replay, exact prompt, action budget, model snapshot, harness policy, and split. The technical report and current docs have evolved on details such as score caps and set-difficulty expectations; record the dated protocol used rather than silently merging versions.

Primary sources: [benchmark page](https://arcprize.org/arc-agi/3), [technical report](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf), [scoring methodology](https://docs.arcprize.org/methodology), [available games](https://docs.arcprize.org/available-games), [testing policy](https://arcprize.org/policy), and [official benchmarking harness](https://github.com/arcprize/arc-agi-3-benchmarking).

## DiG-bench

[DiG-bench](https://digbench.ai/) contains 70 text-based interactive games, 21 of which are public. Each game has its own unknown transformation rules. The agent receives JSON state and legal actions, experiments, infers the rules, and applies them to beat the game within a fixed step budget.

| Property | DiG-bench contract |
|---|---|
| Input | Observation, level, lives, steps remaining, status, legal actions, and history |
| Hidden information | Transformation rules and win conditions |
| Interface | Same game state, action set, and step budget for humans and models |
| Optional feedback mode | Some games provide a creative mode for experiments that do not consume ordinary steps |
| Metric | Binary success per run; per-game win rate averaged over runs, then averaged within tier |
| Dataset | 70 games across seven tiers; 21 public and 49 private |
| Human validation | Every game was beaten by at least one external human tester on the first attempt |

### Public task IDs

| 1 | **DiG-bench P-1**, **DiG-bench P-2**, **DiG-bench P-3** |
| 2 | **DiG-bench P-4**, **DiG-bench P-5**, **DiG-bench P-6** |
| 3 | **DiG-bench P-7**, **DiG-bench P-8**, **DiG-bench P-9** |
| 4 | **DiG-bench P-10**, **DiG-bench P-11**, **DiG-bench P-12** |
| 5 | **DiG-bench P-13**, **DiG-bench P-14**, **DiG-bench P-15** |
| 6 | **DiG-bench P-16**, **DiG-bench P-17**, **DiG-bench P-18** |
| 7 | **DiG-bench P-19**, **DiG-bench P-20**, **DiG-bench P-21** |

The benchmark intentionally withholds semantic task names because discovering the rule is the task. The correct public identifiers are therefore P-1 through P-21, not inferred puzzle descriptions. The official leaderboard currently exposes all five model families tracked by this repository: GPT, Claude, GLM, Kimi, and Qwen.

### Reported model snapshot

The paper evaluates Opus 5, GPT-5.5, Kimi K3, GLM-5.2, Qwen 3.6 27B, Gemini 3.1 Pro, and two DeepSeek V4 variants on all 70 games in the basic harness. It reports exact bookends of **50/70 games won for Opus 5** and **1/70 for Qwen 3.6 27B**. Gemini 3.1 Pro wins **18/70** without rules and **69/70** when given a concise description of the rules, isolating rule discovery as the main bottleneck. Most model×game pairs have one run, so these should not be treated as low-variance estimates. Agentic harnesses were tested only on tiers 6 and 7 and did not consistently improve the matched Kimi, Gemini, or Opus conditions.

Examples of public-game discoveries disclosed by the paper include P-2's analogous two-part structure, P-9's goal-order reversal, P-13's Knights/Knaves truth condition, P-18's rate-constant controls, and P-21's creative-mode bridge experiment. These descriptions are useful for taxonomy but are spoilers; the registry keeps the agent-facing question generic.

Primary sources: [project and leaderboard](https://digbench.ai/), [paper with methods and results](https://arxiv.org/html/2608.12593), and [baseline harness](https://github.com/discos-research/dig-bench).

## Closely related sources under extraction

These suites belong in the discovery map, but their headline suite counts are not yet converted into individual registry rows until each task's executable contract is extracted:

| Source | Verified scope | Registry decision |
|---|---|---|
| [EdgeBench](https://edge-bench.org/) | 134 environment-learning tasks; 51 initially released across science/ML, systems, optimization, knowledge, formal math, and games; runs last 12–72+ hours | High-priority extraction queue. Add each task only after its workspace, feedback, budget, evaluator, and artifact are pinned. |
| [ScrambleToolBench](https://arxiv.org/abs/2608.02358) | Interactive terminal tasks with obfuscated tool schemas, mapping drift, stochastic failures, and temporal windows | Emerging task source. Await a verified code/data release and exact task inventory. |
| [FALSIFYBENCH](https://arxiv.org/abs/2606.04751) | Hidden semantic properties discovered by proposing examples and receiving confirm/disconfirm feedback; 12 LLMs evaluated | Strong 2026 rule-discovery source. Extract the released property/task inventory and turn-level evaluator before promotion. |
| [CausalGame](https://arxiv.org/abs/2607.04293) | 14 interactive causal-discovery scenarios with selection bias, measurement error, and hidden confounders; 30 agents evaluated | Strong 2026 scientific-discovery source. Extract scenario variants, survival objective, and causal-reasoning rubric separately. |
| [PhysGym](https://arxiv.org/abs/2507.15550) | Interactive physics simulations with controlled prior-knowledge levels, sequential experiments, and hypothesis/model-fidelity scoring | Important controlled-prior source; public task manifest and versioned simulator contracts remain to be extracted. |
| [DiscoveryWorld](https://allenai.github.io/discoveryworld/) | 120 simulated scientific-discovery tasks across eight topics and three difficulty levels | Historical anchor; task manifest extraction is pending. |
| [AutumnBench / WorldTest](https://openreview.net/forum?id=HuNIgYhBoy) | Reported 43 grid-world environments × three challenges | Emerging and not promoted until primary artifacts can be accessed and verified. |
| [AGI Maze](https://arxiv.org/abs/2607.00627) | Partially observed maze family testing memory and state inference | Framework lead; exact public task artifacts remain to be verified. |

BALROG, AI GameStore, NetHack-style suites, and EdgeBench games may require learning mechanics, but they also intentionally mix discovery with navigation, perception, planning, and long-context control. They remain useful broader environment-learning benchmarks rather than pure rule-discovery tests.

World-model video prediction benchmarks such as iWorld-Bench and WR-Arena are adjacent, not primary discovery tasks: they evaluate generated futures or planning representations rather than an agent learning hidden rules through a live action-feedback loop. Static induction suites such as ARC-AGI-1/2 and ConceptARC are also adjacent: they infer rules from fixed demonstrations but do not measure experimental action selection.
