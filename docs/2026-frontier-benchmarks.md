# 2026 Frontier Agentic Benchmarks

**Evidence snapshot:** 2026-08-25 (America/Chicago)

This page is a dated frontier tracker for **task sources and benchmark suites**. The primary catalog unit is the executable problem in the [Discovery Task Registry](discovery-tasks.md), not the discovery method. This page prevents a new preprint, a live suite, and a reproducible release from being presented as if they had the same maturity.

For example, SimpleTES packages/adapts 28 executable contracts and evaluates them, but it is not automatically their original source: GPUMode, SLDBench, ZAPBench, KernelBench, OpenProblems, established mathematical problems, and several SimpleTES-authored evaluator contracts all appear in per-task provenance.

## Status vocabulary

| Status | Meaning |
|---|---|
| **Released** | Public task artifacts and an executable or otherwise inspectable evaluation protocol are available. |
| **Live** | An active benchmark or leaderboard publishes tasks and runs, and may continue to change. |
| **Preview** | The organizers describe the project as provisional, are still collecting tasks, or have not frozen a release. |
| **Emerging** | A recent paper or preprint defines a benchmark, but its artifacts or independent reproducibility have not yet been fully audited here. |
| **Work in progress** | The authors explicitly present the evaluation as incomplete or subject to material protocol changes. |
| **Unresolved lead** | The name has been reported, but no matching primary source has been located. It is not counted as a verified benchmark. |

`Released` does not mean that every score is comparable. Model, scaffold, tools, compute, task version, and evaluator still define the result.

## Requested-name audit

### Terminal-Bench 3 (TB3)

**Classification:** Preview lineage → continuous benchmark.

The former TB3 project URL now resolves to the continuous [Terminal-Bench repository](https://github.com/harbor-framework/terminal-bench). The maintained project publishes tagged task-set releases through Harbor rather than presenting “TB3” as a single stable, frozen benchmark version. Evaluations run terminal tasks in isolated environments; the agent receives task instructions and a terminal, while task-specific tests or verifiers score the resulting environment state. Official leaderboard runs use the Harbor harness, with Modal used for hosted execution.

Catalog rule: cite the exact task-set tag and harness version. Do not report a bare “TB3 score” without a release identifier.

### RSI Bench: two different 2026 projects

| Project | Status | What the agent receives | Evaluation and environment | Reported evidence |
|---|---|---|---|---|
| [**RSI Bench**](https://www.rsi-benchmark.com/) | **Live / Preview** | A starting research environment, objective, compute budget, and verifier; current task families cover post-training, alignment, agent-swarm optimization, and data curation | Long-horizon AI R&D runs are compared with a baseline under task-specific verifiers; the project emphasizes reliability, efficiency, generality, and idea quality | The `agent-swarm-optimization` page reports four attempts per model on one H100 at 2h/6h budgets; the best listed reward is 0.818 for Claude Opus 5 and 0.448 for GPT-5.6 Sol. These are task-specific, not overall benchmark scores. |
| [**RSIBench: A Counterfactual Test of Recursive Self-Improvement in Coding Agents**](https://huggingface.co/datasets/AgPerry/rsi-bench) | **Released dataset** | A natural-language patch request, repository files, and visible tests; hidden tests are withheld | 300 self-contained Python patch/test tasks split 200/50/50. An agent may propose changes to its own harness on training tasks; validation gates the changes and held-out tests measure lift. Reward is the fraction of hidden tests passed | Dataset card reports a 0.4675 no-op floor and 0.9993 oracle score. These are controls, not frontier-model scores. [Code](https://github.com/reacher-z/rsi-bench). |

The two projects are not interchangeable. The first measures open-ended AI R&D in live environments; the second tests whether a coding agent's self-modification transfers to held-out tasks.

### DeTrustAgent

**Classification:** Unresolved lead.

As of the snapshot date, an exact-name search did not locate a matching paper, official repository, dataset, or benchmark page. It is therefore not silently replaced with the older **TrustAgent** benchmark and is not counted in the catalog. A source URL, alternate spelling, or paper title is needed before inclusion.

The closest verified 2026 safety benchmarks by topic are [SkillSafetyBench](https://arxiv.org/abs/2605.12015), [TRUST-Bench](https://arxiv.org/abs/2605.17453), [AgentLAB](https://arxiv.org/abs/2602.16901), [TAMAS](https://aclanthology.org/2026.acl-long.1442/), and [ST-WebAgentBench](https://research.ibm.com/publications/st-webagentbench-a-benchmark-for-evaluating-safety-and-trustworthiness-in-web-agents--1).

## AI4AI, RSI, and scientific discovery

| Benchmark | Date / status | Question or task input | Evaluation method and environment | Reported model evidence |
|---|---|---|---|---|
| [**AI4AI-Bench**](https://arxiv.org/abs/2608.20318) | 2026-08-20 · **Emerging** | One of 10 frozen research repositories representing 10 training-algorithm families; the agent rewrites the training algorithm | Four-hour development budget on one NVIDIA B300, followed by a from-scratch rerun of up to 12 hours with a fixed hidden evaluator. Normalized utility uses 0 for uninformative, 0.1 for the original algorithm, and 1.0 for the estimated optimum | 29 configurations of six systems: reported mean 0.166 and best 0.250. Consult the paper for per-system scaffold details. |
| [**RSI Bench**](https://www.rsi-benchmark.com/tasks) | 2026-08-07 · **Live / Preview** | Open-ended AI R&D objective plus starting environment, resources, and verifier | Task-specific executable verifier and controlled compute budget; live runs currently include GPT-5.6-sol and Claude Opus systems | No single aggregate score yet. See the task-specific 0.818 vs 0.448 example above. |
| [**RSIBench (coding self-improvement)**](https://huggingface.co/datasets/AgPerry/rsi-bench) | 2026 · **Released dataset** | Python repository patch tasks with visible tests | Hidden-test pass fraction before and after validation-gated harness self-modification; held-out test split and contamination canary | 0.4675 no-op floor; 0.9993 oracle. Frontier-agent matrix still needed. |
| [**AgentHPOBench**](https://arxiv.org/abs/2607.29626) | 2026-07-31 · **Emerging** | Initial ML configuration, metrics, logs, and a sequence of allowed hyperparameter interventions | 30 executable ML tasks across seven categories; compares 12 agents with conventional HPO baselines over sequential experiments | Paper-level comparative results available; cross-model scores have not yet been normalized here. |
| [**SciAgentArena**](https://arxiv.org/abs/2606.12736) | 2026-06 · **Emerging** | Interactive scientific-research tasks requiring multi-step tool and reasoning actions | Approximately 200 tasks in an agent-agnostic environment with stepwise verification rather than answer-only judging | Model table awaits primary-artifact audit. |
| [**NatureBench**](https://github.com/FrontisAI/NatureBench) | 2026-06 · **Released** | A scientific ML problem package derived from a Nature-family paper | Task-dependent executable pipelines, held-out predictions, and comparison with the published SOTA under a four-hour budget | Official results cover GPT, Claude, GLM, Kimi, and Qwen families; leading listed Surpass-SOTA rate in our detailed snapshot is 23.3%. |
| [**EarthVerse**](https://arxiv.org/abs/2608.23525) | 2026-08-24 · **Emerging** | Reproducible Earth-science event packages spanning 19 hazard families | 405 tasks from 199 documented events; executable answer units plus process rubrics. Reports answer accuracy and strict high-confidence success | Across 25 systems, paper reports best mean answer accuracy of 84.65% and best Strict@95 of 34.81%. |
| [**LongWoF-Bench**](https://arxiv.org/abs/2608.23200) | 2026-08-24 · **Emerging** | 778 machine-verifiable tasks across code, environment synthesis, mathematics, and rule following | Verified trajectories are externalized as reusable “Genes”; evaluation tests whether persistent artifacts improve later task performance | On a 252-task subset, Gene reportedly exceeds Skill by 8.7–15.5 points across seven models; Claude Opus solves 39 more tasks with 9.9% fewer tokens. This measures externalized adaptation, not weight-level RSI. |

## Interactive discovery and environment learning

| Benchmark | Date / status | Question or task input | Evaluation method and environment | Reported model evidence |
|---|---|---|---|---|
| [**ARC-AGI-3**](https://arcprize.org/arc-agi/3) | 2026-04 · **Live / Released protocol** | A 16-color grid frame and legal actions, with no language description of the mechanics, objective, or win condition | 135 environments: 25 public demos, 55 semi-private, and 55 fully private. RHAE compares completed-level action efficiency with first-run humans and averages weighted game scores | Official semi-private scores: Opus 4.6 0.50%, Gemini 3.1 Pro Preview 0.40%, GPT-5.4 0.20%, Grok-4.20 Beta 0.10%. No verified GLM, Kimi, or Qwen official row yet. |
| [**DiG-bench**](https://digbench.ai/) | 2026-08-12 · **Released** | JSON text-game state and legal actions; the agent must discover each game's unique hidden rules and win condition | 70 games in seven tiers, 21 public. Success is a win within a fixed step budget; per-game repeated-run win rates are averaged within tier | The official basic leaderboard includes GPT-5.5, Opus 5, GLM-5.2, Kimi K3, and Qwen 3.6 27B; agentic configurations include GPT, Claude, and Kimi systems. |
| [**EdgeBench**](https://edge-bench.org/) | 2026-07-02 · **Released / task extraction in progress** | Long-running real-world workspaces across science, systems, optimization, knowledge, formal math, and games | 134 tasks with 12–72+ hour feedback-driven runs; 51 initially released. Best-so-far task curves and aggregate learning curves measure improvement over interaction time | 402 curves per model are reported. One documented GPT-5.5 gravitational-wave run improves from 42.8 to 67.0 over 247 scored attempts in 12 hours. |
| [**ScrambleToolBench**](https://arxiv.org/abs/2608.02358) | 2026-08-03 · **Emerging** | Obfuscated terminal commands whose behavior must be inferred by trial and error | Tests stable discovery plus mapping drift, stochastic failures, and temporal windows; exact public task inventory awaits artifact verification | The paper reports aggregate completion collapsing from 93% in stable conditions to 3% under combined dynamic challenges. |
| [**FALSIFYBENCH**](https://arxiv.org/abs/2606.04751) | 2026-06-03 · **Emerging** | Iteratively proposed examples receive confirm/disconfirm feedback for a hidden semantic property | Wason-style rule-discovery games score hypothesis-driven induction and turn-level falsification behavior | Twelve LLMs are evaluated; the paper reports that no model approaches optimal performance and negative testing is the strongest success factor. |
| [**CausalGame**](https://arxiv.org/abs/2607.04293) | 2026-07-05 · **Emerging** | Agents design interventions, collect observations, and write a causal solution and explanation in worlds with hidden biases | 14 interactive scenarios cover selection bias, measurement error, and hidden confounding; survival and causal-reasoning rubrics are separate | Across 30 agents, the best reaches 68.0% survival versus 78–85% analytical optima, while only 5–7% of sessions receive causal-reasoning credit. |

## Coding, terminal, computer, and mobile agents

| Benchmark | Date / status | Question or task input | Evaluation method and environment | Reported model evidence |
|---|---|---|---|---|
| [**Terminal-Bench**](https://github.com/harbor-framework/terminal-bench) | Continuous · **Live** | Natural-language task instruction plus an isolated terminal environment | Task-specific executable tests through Harbor; releases are tagged and oracle runs are repeated. Hosted official execution uses Modal | Multiple provider results exist, but scores must be attached to a task-set tag, agent scaffold, and resource policy. |
| [**TerminalWorld**](https://terminalworld.ai/) | 2026-05 · **Live** | Reproduced real-world software environments and terminal tasks | 5,035 reproduced environments, 1,530 with test suites, and a 200-task human-verified subset; executable tests score completion | On the displayed 200-task leaderboard: Claude Opus 4.7 62.5, Kimi K2.6 57.5, GLM 5.1 57.0, Qwen3.6-Max-Preview 54.0, and GPT-5.5 53.5. |
| [**TUA-Bench**](https://tuabench.ai/) | 2026-06 · **Released** | 120 terminal workflows in five families, including document editing, email, live web, and scientific/engineering work | Deterministic setup and execution-based scoring in general computer-use environments | Project reports 65.8% for the strongest cited Claude Code + Claude Opus 4.8 configuration. |
| [**SWE Refactor Bench**](https://arxiv.org/abs/2608.23564) | 2026-08-24 · **Emerging** | 20 whole-repository migrations across four technical-debt categories | Three-stage evaluation: migration audit, behavior tests, and targeted hidden tests independently generated by six coding agents | 520 runs across eight frontier models and 26 configurations; 28/520 pass every stage. Reported best is Claude Opus 5 at 47/100. |
| [**NetConfArena**](https://arxiv.org/abs/2608.23179) | 2026-08-24 · **Emerging** | Natural-language multi-device network configuration and repair tasks | Closed-loop emulated networks with hidden executable tests; 480 instances from 96 templates and 3,840 trajectories | Per-model evidence awaits artifact audit. |
| [**MobilePA-Bench**](https://arxiv.org/abs/2608.23035) | 2026-08-24 · **Emerging** | Stateful personal-assistant tasks across 13 mobile domains and 212 tools | Executable mobile sandbox with evidence-based verification; explicitly tests subagents, memory, and reusable skills | Per-model evidence awaits artifact audit. |

## Safety, trust, robustness, and benchmark integrity

| Benchmark | Date / status | Threat or task input | Evaluation method and environment | Reported evidence |
|---|---|---|---|---|
| [**SkillSafetyBench**](https://arxiv.org/abs/2605.12015) | 2026-05 · **Released** | Adversarial agent-skill packages and local artifacts across 47 tasks | 155 cases, six risk domains, 30 safety categories, and a per-case rule verifier | Designed for skill-facing attacks rather than ordinary prompt-only jailbreaks. [Code](https://github.com/AI45Lab/skill-safety-bench). |
| [**TRUST-Bench**](https://arxiv.org/abs/2605.17453) | 2026-05 · **Emerging** | Tool-use episodes containing hidden-trigger compromised tools, paired with benign controls | 1,970 episodes; GuardedJoint combines useful behavior on controls with resistance to compromised tools | VISTA-Guard reports 84.2 in-distribution and 56.9 balanced OOD under the paper's metric. |
| [**AgentLAB**](https://arxiv.org/abs/2602.16901) | 2026-02 · **Emerging** | Long-horizon attack scenarios: intent hijack, tool chaining, task injection, objective drift, and memory poisoning | 644 cases in 28 realistic agent environments across 10 risk categories | Cross-model table awaits primary-artifact extraction. |
| [**TAMAS**](https://aclanthology.org/2026.acl-long.1442/) | ACL 2026 · **Released** | 300 adversarial instances across five scenarios and six attack types, plus 100 harmless tasks | 211 tools in AutoGen and CrewAI environments; Effective Robustness Score balances attack resistance and benign utility | Paper evaluates 10 backbone LLMs. [Code](https://github.com/microsoft/TAMAS). |
| [**ST-WebAgentBench**](https://research.ibm.com/publications/st-webagentbench-a-benchmark-for-evaluating-safety-and-trustworthiness-in-web-agents--1) | ICLR 2026 · **Emerging** | 375 web-agent tasks governed by 3,057 safety and trust policies | Six safety/trust dimensions, three difficulty tiers, and the CuP policy-compliance metric | Per-model result and artifact extraction is pending; benchmark protocol is verified from the official IBM publication page. |
| [**AgentFairBench**](https://arxiv.org/abs/2606.16723) | 2026-06 · **Emerging** | Stateful hiring, lending, and medical-triage workflows with counterfactual demographic variants | Measures outcome and process disparity; includes live held-out cases and contamination canaries | Cross-model scores have not yet been normalized here. |
| [**HVTB**](https://arxiv.org/abs/2608.22103) | 2026-08-22 · **Emerging** | Terminal-Bench-style tasks containing detectable opportunities for reward hacking | Hack-Verifiable Terminal Bench embeds known hacks and automatically distinguishes legitimate success from verifier exploitation | Useful as an RSI integrity benchmark; per-model results await artifact audit. |
| [**CatchBench**](https://arxiv.org/abs/2608.22808) | 2026-08-24 · **Work in progress** | Evaluation submissions shown to auditors under PRE, LIVE, and POST information states | Seven audit contracts; initial study covers 72 entrants, 11 LLM judges, nine families, 1,187 configurations, and 1,162 runs | Tracks evaluator reliability and leakage sensitivity rather than agent capability alone. |

## Frontier inbox: not yet promoted

The following very recent 2026 papers are relevant leads but require a deeper artifact and model-table audit before entering the main tables:

- [K-Bench](https://arxiv.org/abs/2608.21601) — real scientific-agent requests.
- [GameXpert-Bench](https://arxiv.org/abs/2608.21833) — game-agent expertise.
- [BC-Bench](https://arxiv.org/abs/2608.20851) — agent benchmark lead awaiting classification.
- [DreamBench-SWE](https://arxiv.org/abs/2608.20664) — software-engineering benchmark lead.
- [Trust-Memevo](https://arxiv.org/abs/2602.03224) — safety of agent memory under test-time evolution.
- [Manager Coercion Benchmark](https://arxiv.org/abs/2607.15434) — escalating coercion behavior across model families.

Being listed in the frontier inbox means “found and queued,” not “verified and recommended.”

## Evidence policy for fast-moving 2026 work

For each promoted benchmark, we aim to record:

1. the exact task version and publication date;
2. the agent-visible question, files, state, and feedback;
3. the required output or environment-state change;
4. the evaluator, aggregation method, hidden tests, judges, and uncertainty;
5. the container, VM, tools, network, hardware, time, token, and compute policy;
6. the model's role: **agent**, **target**, or **judge**;
7. score evidence tied to the complete evaluation configuration; and
8. contamination, reward-hacking, evaluator-access, and artifact-substitution risks.

This is intentionally stricter than copying a paper's benchmark name and headline number.
