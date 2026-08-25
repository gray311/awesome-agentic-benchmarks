<div align="center">

# Awesome Agentic Benchmarks

### A task-level, evidence-backed map of discovery environments for autonomous agents, AI R&D, and recursive self-improvement

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Registry](https://img.shields.io/badge/registry-machine--readable-2563eb)
![Model coverage](https://img.shields.io/badge/models-GPT%20%7C%20Claude%20%7C%20GLM%20%7C%20Kimi%20%7C%20Qwen-7c3aed)
![Validation](https://img.shields.io/badge/validation-passing-16a34a)
[![License: MIT](https://img.shields.io/badge/license-MIT-f59e0b.svg)](LICENSE)

[Benchmark Catalog](#-benchmark-suite-catalog) · [2026 Frontier Tracker](docs/2026-frontier-benchmarks.md) · [Launch & Stars](docs/benchmark-release-and-stars.md) · [Discovery Tasks](docs/all-discovery-tasks.md) · [CUA & GUI](docs/cua-gui-benchmarks.md) · [Contributing](CONTRIBUTING.md)

</div>

---

> Agent benchmark scores are properties of a complete evaluation system—not a bare model:
>
> **model + scaffold + tools + environment + compute budget + evaluator**

This repository primarily tracks **executable discovery tasks** in which agents either optimize scientific, mathematical, engineering, or AI-system artifacts, or discover unfamiliar environment rules through interaction. Benchmark suites are indexed as sources of tasks; methods and agent frameworks are recorded only as systems evaluated on those tasks. The broader catalog also covers agent benchmarks for browsing, computer use, coding, post-training, and safety. It is designed as shared evaluation infrastructure for **AI4AI** and **recursive self-improvement (RSI)** research.

## 🎯 Mission: Evaluation Infrastructure for RSI

Our goal is to help advance **recursive self-improvement (RSI)** by making progress measurable, comparable, and reproducible. An AI system cannot improve itself reliably without knowing which capabilities changed, whether an apparent gain survives controlled evaluation, and what resources or scaffolding produced that gain.

The primary unit is a task such as *Cassini gravity-assist trajectory optimization* or *Erdős minimum overlap*—not a method such as SimpleTES or TTT-Discover. To support this goal, the repository collects and organizes:

- **task-level discovery datasets** with the question, agent-visible input, required artifact, objective direction, evaluator, environment, reference result, and reported discovery result;
- **benchmark suites as task sources** spanning quantum compilation, astrodynamics, scientific algorithms, AI foundations, mathematics, coding, machine learning engineering, post-training, paper reproduction, tool use, and safety;
- **evaluation methods and protocols**, including task construction, inputs and outputs, scoring rules, judges, pass criteria, baselines, uncertainty, contamination controls, and reproducibility procedures;
- **evaluation environments and resource envelopes**, such as tools, agent scaffolds, sandboxes, network access, time limits, token budgets, compute budgets, and hardware;
- **cross-model evidence** for GPT, Claude, GLM, Kimi, Qwen, and other model families, with explicit distinctions between the agent model, target model, and judge model;
- **machine-readable records** that future AI4AI systems can search, compare, validate, and use to select evaluations for their own improvement cycles.

The long-term aim is not merely to maintain a leaderboard. It is to build an open evaluation layer for the AI4AI/RSI loop:

> **propose an improvement → implement it → evaluate across dimensions → analyze regressions and trade-offs → retain verified gains → repeat**

We therefore treat every score as a result of a complete experimental configuration—not as an intrinsic property of a model—and prioritize primary sources, transparent protocols, reproducible environments, and dated evidence.

## 🔥 News

- **2026-08-25** — Expanded the paper catalog with recent discovery, RSI, safety, and computer-use benchmarks; added dated launch and GitHub-star metadata.
- **2026-08-25** — Released task-level discovery references covering 52 full contracts, 11 TTT-Discover variants, and the 442-task Finch Collection snapshot.
- **2026-08-24** — Launched the repository with evidence-backed coverage of MLE-bench, NatureBench, PostTrainBench, and GPT/Claude/GLM/Kimi/Qwen evaluations.

## 📑 Table of Contents

- [Why this repository](#-why-this-repository)
- [Mission: Evaluation Infrastructure for RSI](#-mission-evaluation-infrastructure-for-rsi)
- [Benchmark dimensions](#-benchmark-dimensions)
- [Discovery task registry](#-discovery-task-registry)
- [Launch dates and GitHub stars](#-launch-dates-and-github-stars)
- [Featured benchmark suites](#-featured-benchmark-suites)
- [2026 frontier tracker](#-2026-frontier-tracker)
- [Benchmark suite catalog](#-benchmark-suite-catalog)
  - [AI R&D and scientific discovery](#ai-rd-and-scientific-discovery)
  - [Coding and software engineering](#coding-and-software-engineering)
  - [Tool use and interaction](#tool-use-and-interaction)
  - [Computer use and GUI interaction](#computer-use-and-gui-interaction)
  - [General, professional, and safety agents](#general-professional-and-safety-agents)
- [Model-family coverage](#-model-family-coverage)
- [Machine-readable registries](#-machine-readable-registries)
- [Inclusion criteria](#-inclusion-criteria)
- [Contributing](#-contributing)
- [Related repositories](#-related-repositories)

## ✨ Why this repository

Agentic benchmarks are difficult to compare. Two results using the same underlying model can differ substantially because of the scaffold, available tools, time limit, GPU budget, feedback channel, network policy, inference configuration, or integrity rules.

Awesome Agentic Benchmarks provides:

- a task-first scientific-discovery landscape;
- machine-readable task and benchmark-suite registries for evaluation infrastructure and research agents;
- evidence-backed coverage of GPT, Claude, GLM, Kimi, and Qwen;
- dated score snapshots tied to the model, scaffold, and resource envelope;
- explicit agent-model, target-model, and judge-model roles;
- an AI4AI/RSI taxonomy based on the object and persistence of improvement;
- benchmark integrity notes covering contamination, artifact substitution, evaluator access, and reward hacking.

## 🧭 Benchmark dimensions

Dimensions describe **what the benchmark evaluates**. SFT, DPO, GRPO, RLHF, LoRA, and distillation are training methods—not top-level benchmark dimensions.

| Dimension | What it evaluates | Example benchmarks |
|---|---|---|
| **Coding & Software Engineering** | Repository editing, issue resolution, debugging, tests, and terminal work | SWE-bench, Terminal-Bench, SWE Refactor Bench |
| **Machine Learning Engineering** | Building and optimizing ML systems against a defined objective | MLE-bench, MLAgentBench, ML-Dev-Bench |
| **Post-Training** | Improving a provided base model under a bounded compute budget | PostTrainBench, RSI Bench |
| **Open-Ended AI R&D** | Proposing, implementing, and validating AI research improvements | AI4AI-Bench, RSI Bench, RE-Bench |
| **Agent & Harness Improvement** | Modifying an agent's scaffold, memory, skills, or reusable procedures and testing transfer | RSIBench, LongWoF-Bench |
| **Scientific Discovery** | Solving research problems in scientific domains | NatureBench, EarthVerse, SciAgentArena |
| **Interactive World Discovery** | Inferring unfamiliar dynamics, rules, goals, and strategies from action-conditioned feedback | ARC-AGI-3, DiG-bench, EdgeBench |
| **Paper Reproduction** | Reconstructing research code, environments, and results | PaperBench, CORE-Bench, SUPER |
| **Web Research & Browsing** | Locating and synthesizing hard-to-find information | BrowseComp, WebArena, GAIA |
| **Computer Use & GUI Interaction** | Grounding controls and completing executable workflows across desktop, browser, mobile, hybrid GUI+CLI/MCP, and safety-critical interfaces | OSWorld 2.0, WeaveBench, MobileWorld, ScreenSpot-Pro, OS-Harm |
| **Tool Use** | Selecting APIs and tools while following stateful policies | BFCL, tau2-bench, MCP-Atlas |
| **Professional Work** | Completing realistic office and knowledge-work deliverables | GDPval-AA, SpreadsheetBench 2, WorkArena |
| **Multi-Agent Coordination** | Delegation, collaboration, negotiation, and competition | MultiAgentBench, GAMA-Bench, SOTOPIA |
| **Safety & Security** | Harmful actions, permissions, prompt injection, reward hacking, and cyber capability | SkillSafetyBench, TAMAS, HVTB |
| **Evaluation Integrity** | Verifier exploitation, reward hacking, leakage, and judge reliability | HVTB, CatchBench |
| **General Agents** | Broad planning, reasoning, tool use, and long-horizon execution | OmniaBench, AGENCYBENCH, AgentBench |

See the complete definitions and classification rules in [Benchmark Dimensions](docs/benchmark-dimensions.md).

## 🔬 Discovery task registry

Task-level discovery data is maintained outside the README so this page can stay focused on papers and benchmark suites.

Use [All Discovery Tasks + SOTA](docs/all-discovery-tasks.md) for the detailed reference and [Discovery Overview](docs/discovery-tasks.md) for taxonomy and inclusion policy. Machine-readable files are linked in the registry section below.

## 🗓️ Launch dates and GitHub stars

Launch time and repository popularity are tracked separately from capability scores. Dates use the earliest verified public artifact and preserve their actual precision; GitHub stars are dated snapshots and are never treated as benchmark quality.

| Benchmark / task source | Launch | Official repository | Stars on 2026-08-25 |
|---|---:|---|---:|
| **MLE-bench** | 2024-10 | [openai/mle-bench](https://github.com/openai/mle-bench) | 1,716 |
| **NatureBench** | 2026-06 | [FrontisAI/NatureBench](https://github.com/FrontisAI/NatureBench) | 102 |
| **PostTrainBench** | 2026-03 | [aisa-group/PostTrainBench](https://github.com/aisa-group/PostTrainBench) | 532 |
| **SimpleTES** | 2026-04 | [wq-will/SimpleTES](https://github.com/wq-will/SimpleTES) | 169 |
| **ARC-AGI-3** | 2026-04-22 | [arcprize/ARC-AGI](https://github.com/arcprize/ARC-AGI) (toolkit) | 69 |
| **DiG-bench** | 2026-08-12 | [discos-research/dig-bench](https://github.com/discos-research/dig-bench) | 24 |
| **TTT-Discover** | 2026-01-22 | [test-time-training/discover](https://github.com/test-time-training/discover) | 628 |
| **Finch Collection / EFT** | 2026-06-27 | [Open-Galapagos/evolution-fine-tuning](https://github.com/Open-Galapagos/evolution-fine-tuning) | 28 |
| **EdgeBench** | 2026-07-02 | [ByteDance-Seed/EdgeBench](https://github.com/ByteDance-Seed/EdgeBench) | 432 |

See the [complete 59-benchmark launch and star table](docs/benchmark-release-and-stars.md) and its [machine-readable metadata](data/benchmark-metadata.json). Repositories shared by multiple evaluations are marked `shared-suite`; benchmarks without a verified official GitHub repository show `N/A`, not zero.

## 🌟 Featured benchmark suites

These are the first fully documented suite-level entries. Their internal evaluation units should be extracted into the task registry when executable artifacts are available.

| Benchmark | Launch | GitHub stars¹ | Primary dimension | Evaluation unit | Output | Environment | Current headline snapshot |
|---|---:|---:|---|---|---|---|---|
| [**MLE-bench**](https://github.com/openai/mle-bench) | 2024-10 | 1,716 | Machine Learning Engineering | One offline Kaggle competition | Prediction submission | 24h, A10 GPU | 64.44% Any Medal for the leading comparable entry |
| [**NatureBench**](https://github.com/FrontisAI/NatureBench) | 2026-06 | 102 | Scientific Discovery | One Nature-family scientific ML problem | Executable pipeline and predictions | 4h, task-dependent GPU | 23.3% Surpass-SOTA for the leading entry |
| [**PostTrainBench**](https://posttrainbench.com/) | 2026-03 | 532 | Post-Training | One base-model × target-benchmark run | Post-trained model checkpoint | 10h, one H100 | 41.79% weighted average for the leading listed entry, with a fallback caveat |

¹ Star snapshot: 2026-08-25. Use the complete metadata page for live badges and repository-scope caveats.

```text
MLE-bench
  Agent builds task-specific ML systems
        ↓
NatureBench
  Agent attempts to exceed published scientific ML systems
        ↓
PostTrainBench
  Agent directly changes another language model's weights
```

These benchmarks measure increasingly direct forms of AI-assisted AI development. None is, by itself, a complete recursive self-improvement benchmark: the evaluated agent does not repeatedly improve successor versions of its own improvement mechanism under a controlled causal protocol.

## 🛰️ 2026 frontier tracker

Fast-moving 2026 work is tracked separately from the stable catalog so that maturity remains visible.

| Benchmark | Dimension | Maturity | Why it matters |
|---|---|---|---|
| [**RSI Bench**](https://www.rsi-benchmark.com/) | Open-Ended AI R&D / Post-Training | Live preview | Long-horizon research tasks with controlled compute and executable verifiers; current public runs include GPT and Claude systems. |
| [**ARC-AGI-3**](https://arcprize.org/arc-agi/3) | Interactive World Discovery | Live / Released protocol | Agents discover visual-world mechanics and goals without language instructions; official semi-private frontier results remain below 1% RHAE. |
| [**DiG-bench**](https://digbench.ai/) | Interactive World Discovery | Released | 70 unknown-rule text games, including 21 public tasks; its official leaderboard covers GPT, Claude, GLM, Kimi, and Qwen. |
| [**EdgeBench**](https://edge-bench.org/) | Environment Learning | Released / extraction queue | 134 real-world tasks with 12–72+ hour learning curves; 51 task artifacts are initially released. |
| [**RSIBench**](https://huggingface.co/datasets/AgPerry/rsi-bench) | Agent/Harness Improvement | Released dataset | Counterfactual test of whether coding-agent self-modifications transfer to held-out tasks. |
| [**AI4AI-Bench**](https://arxiv.org/abs/2608.20318) | Open-Ended AI R&D | Emerging | Agents rewrite training algorithms in frozen research repositories under a B300 compute envelope. |
| [**Terminal-Bench**](https://github.com/harbor-framework/terminal-bench) | Coding / Terminal | Live, continuous | The former TB3 effort now publishes tagged continuous task sets through Harbor; a score needs an exact release tag. |
| [**TerminalWorld**](https://terminalworld.ai/) | Coding / Terminal | Live | Its human-verified leaderboard currently contains GPT, Claude, GLM, Kimi, and Qwen results in one shared environment. |
| [**EarthVerse**](https://arxiv.org/abs/2608.23525) | Scientific Discovery | Emerging | 405 reproducible Earth-science tasks with executable answer units and process rubrics. |
| [**SWE Refactor Bench**](https://arxiv.org/abs/2608.23564) | Coding | Emerging | Whole-repository migrations evaluated by audits, behavior tests, and independently generated hidden tests. |
| [**HVTB**](https://arxiv.org/abs/2608.22103) | Safety / Evaluation Integrity | Emerging | Detects reward hacking in terminal-agent evaluation rather than trusting verifier success alone. |
| [**SkillSafetyBench**](https://arxiv.org/abs/2605.12015) | Safety | Released | Tests malicious skills and local artifacts across six risk domains. |

See [2026 Frontier Agentic Benchmarks](docs/2026-frontier-benchmarks.md) for task inputs, evaluators, environments, reported scores, status definitions, and the explicit unresolved-name audit for **DeTrustAgent**.

## 📚 Benchmark suite catalog

Legend: **Detailed** = complete registry entry; **Tracked** = included in the model-coverage and verification pipeline; **Live/Preview/Emerging** = status is defined in the [2026 tracker](docs/2026-frontier-benchmarks.md); **Discovery queue** = primary artifacts still need review.

### AI R&D and scientific discovery

| Benchmark | Launch | Stars¹ | Dimension | Status | Paper / Code / Leaderboard |
|---|---|---|---|---|---|
| **MLE-bench** | 2024-10 | 1,716 | Machine Learning Engineering | Detailed | [Paper](https://arxiv.org/abs/2410.07095) · [Code](https://github.com/openai/mle-bench) · [Leaderboard](https://github.com/openai/mle-bench#leaderboard) |
| **NatureBench** | 2026-06 | 102 | Scientific Discovery | Detailed | [Paper](https://arxiv.org/abs/2606.24530) · [Code](https://github.com/FrontisAI/NatureBench) · [Leaderboard](https://frontisai.github.io/NatureBench/) |
| **PostTrainBench** | 2026-03 | 532 | Post-Training | Detailed | [Paper](https://arxiv.org/abs/2603.08640) · [Code](https://github.com/aisa-group/PostTrainBench) · [Leaderboard](https://posttrainbench.com/) |
| **ARC-AGI-3** | 2026-04-22 | 69 | Interactive World Discovery | Detailed | [Report](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf) · [Toolkit](https://github.com/arcprize/ARC-AGI) · [Docs](https://docs.arcprize.org/) |
| **DiG-bench** | 2026-08-12 | 24 | Interactive World Discovery | Detailed | [Paper](https://arxiv.org/abs/2608.12593) · [Code](https://github.com/discos-research/dig-bench) · [Leaderboard](https://digbench.ai/) |
| **EdgeBench** | 2026-07-02 | 432 | Environment Learning | Extraction queue | [Project](https://edge-bench.org/) · [Code](https://github.com/ByteDance-Seed/EdgeBench) |
| **RSI Bench** | 2026-08-07 | N/A | Open-Ended AI R&D / Post-Training | Live / Preview | [Project](https://www.rsi-benchmark.com/) · [Tasks](https://www.rsi-benchmark.com/tasks) · [Runs](https://www.rsi-benchmark.com/runs) |
| **RSIBench** | 2026 | N/A | Agent/Harness Improvement | Released dataset | [Dataset](https://huggingface.co/datasets/AgPerry/rsi-bench) · [Code](https://github.com/reacher-z/rsi-bench) |
| **AI4AI-Bench** | 2026-08-20 | N/A | Open-Ended AI R&D | Emerging | [Paper](https://arxiv.org/abs/2608.20318) |
| **RE-Bench** | 2024-11 | 156 | Open-Ended AI R&D | Tracked | [Paper](https://arxiv.org/abs/2411.15114) · [Code](https://github.com/METR/RE-Bench) |
| **MLR-Bench** | 2025 | N/A | Open-Ended AI R&D | Tracked | [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/ab8dd000d6f87f40061a73f8bca7fae4-Abstract-Datasets_and_Benchmarks_Track.html) |
| **PaperBench** | 2025-04 | N/A | Paper Reproduction | Tracked | [Paper](https://arxiv.org/abs/2504.01848) · [Project](https://openai.com/index/paperbench/) |
| **InferenceBench** | 2026-04 | 42 | AI Systems Optimization | Tracked | [Code](https://github.com/aisa-group/InferenceBench) |
| **AgentHPOBench** | 2026-07 | N/A | Machine Learning Engineering | Emerging | [Paper](https://arxiv.org/abs/2607.29626) |
| **SciAgentArena** | 2026-06 | N/A | Scientific Discovery | Emerging | [Paper](https://arxiv.org/abs/2606.12736) |
| **EarthVerse** | 2026-08-24 | N/A | Scientific Discovery | Emerging | [Paper](https://arxiv.org/abs/2608.23525) |
| **ScienceAgentBench** | 2024-10 | 161 | Scientific Discovery | Discovery queue | [Paper](https://arxiv.org/abs/2410.05080) · [Code](https://github.com/OSU-NLP-Group/ScienceAgentBench) |
| **EXP-Bench** | 2025-05 | N/A | Open-Ended AI R&D | Discovery queue | [Paper](https://arxiv.org/abs/2505.24785) · [Code](https://github.com/EvolvingLMMs-Lab/EXP-Bench) |

### Coding and software engineering

| Benchmark | Launch | Stars¹ | Scope | Status | Project |
|---|---|---|---|---|---|
| **SWE-bench Verified** | 2024-06 | 5,708 | Real GitHub issue resolution | Tracked | [Code](https://github.com/SWE-bench/SWE-bench) |
| **SWE-bench Pro** | 2025 | N/A | Harder professional repository tasks | Tracked | [Project](https://scale.com/leaderboard/swe_bench_pro_public) |
| **SWE-bench Multilingual** | 2025-02 | 359 | Repository tasks across programming languages | Tracked | [Code](https://github.com/multi-swe-bench/multi-swe-bench) |
| **SWE-bench Multimodal** | 2025 | 5,708 | UI-facing repository issues with visual context | Tracked | [Code](https://github.com/SWE-bench/SWE-bench) |
| **Terminal-Bench** | 2026-01 | 539 | Continuous long-horizon terminal tasks; TB3 lineage | Live | [Code](https://github.com/harbor-framework/terminal-bench) |
| **TerminalWorld** | 2026-05 | N/A | Reproduced real-world terminal environments | Live | [Project / Leaderboard](https://terminalworld.ai/) |
| **TUA-Bench** | 2026-06 | 46 | General-purpose terminal use | Tracked | [Code](https://github.com/facebookresearch/TUA-Bench) |
| **SWE Refactor Bench** | 2026-08-24 | N/A | Whole-repository migrations and technical-debt removal | Emerging | [Paper](https://arxiv.org/abs/2608.23564) |
| **NetConfArena** | 2026-08-24 | N/A | Closed-loop multi-device network configuration | Emerging | [Paper](https://arxiv.org/abs/2608.23179) |
| **SWE-Lancer** | 2025-02 | 1,431 | Paid freelance software-engineering tasks | Discovery queue | [Code](https://github.com/openai/SWELancer-Benchmark) |

### Tool use and interaction

| Benchmark | Launch | Stars¹ | Scope | Status | Project |
|---|---|---|---|---|---|
| **tau-bench** | 2024-06 | 1,403 | Stateful customer-service tool use | Tracked | [Code](https://github.com/sierra-research/tau-bench) |
| **tau2-bench** | 2025-06 | 1,867 | Dual-control tool-agent-user interaction | Tracked | [Code](https://github.com/sierra-research/tau2-bench) |
| **BFCL** | 2023-07 | 13,007 | Function calling and API selection | Tracked | [Code](https://github.com/ShishirPatil/gorilla) |
| **MCP-Atlas** | 2025-12 | 149 | Real MCP-server tool use | Tracked | [Code](https://github.com/scaleapi/mcp-atlas) · [Leaderboard](https://labs.scale.com/leaderboard/mcp_atlas) |
| **MCP-Bench** | 2025-08 | 502 | MCP discovery, selection, and execution | Tracked | [Code](https://github.com/Accenture/mcp-bench) |
| **Toolathlon** | 2025 | N/A | Diverse, realistic, long-horizon tool execution | Tracked | [Project](https://toolathlon.xyz/) |
| **ACEBench** | 2026-07 | 3 | Normal, special, and agent function calling | Tracked | [Results](https://github.com/Agent-Suite/AgentSuite/blob/main/ACEBench/README.md) |

### Computer use and GUI interaction

The full [Computer-Use and GUI Agent Benchmark registry](docs/cua-gui-benchmarks.md) contains **70 artifacts**, including **31 launched in 2026**. It keeps `static-grounding`, `offline-trajectory`, `interactive-episode`, `long-horizon-workflow`, `arena-preference`, and `safety-adversarial` results separate. Every row records the input question, agent-visible observation, required output, evaluator, environment, launch source, dated stars, and verified model-family evidence.

| Benchmark | Launch | Stars¹ | Platform / evaluation unit | Why it is distinct | Project |
|---|---:|---:|---|---|---|
| **OSWorld** | 2024-04 | 3,106 | Desktop · interactive episode | 369 real-computer tasks | [Code](https://github.com/xlang-ai/OSWorld) |
| **OSWorld-Verified** | 2025-07-28 | 3,106 | Desktop · interactive episode | Repaired tasks, evaluators, and verified submission protocol | [Project](https://xlang.ai/blog/osworld-verified) |
| **OSWorld 2.0** | 2026-06 | 258 | Desktop · long-horizon workflow | 108 workflows; binary and partial scoring at up to 500 steps | [Code](https://github.com/xlang-ai/OSWorld-V2) |
| **WindowsWorld** | 2026-04 | 21 | Windows · long-horizon workflow | 181 process-centric tasks; 77.9% multi-app | [Code](https://github.com/HITsz-TMG/WindowsWorld) |
| **MacAgentBench** | 2026-06 | 49 | macOS · long-horizon workflow | 676 tasks across 25 applications | [Code](https://github.com/JetAstra/MacAgentBench) |
| **WeaveBench** | 2026-06-05 | 159 | Desktop GUI+CLI · long-horizon workflow | 114 channel-non-substitutable hybrid tasks | [Code](https://github.com/weavebench/WeaveBench) |
| **DeskCraft** | 2026-06-02 | 91 | Desktop · professional workflow | 538 standard and user-interactive delivery tasks | [Code](https://github.com/mrwwk/DeskCraft) |
| **ClawBench** | 2026-04 | 585 | Live web · interactive episode | 283 tasks on production websites with write interception | [Code](https://github.com/TIGER-AI-Lab/ClawBench) |
| **SaaS-Bench** | 2026-05 | 96 | Web · professional workflow | 106 tasks on 23 self-hosted SaaS applications | [Code](https://github.com/UniPat-AI/SaaS-Bench) |
| **MobileWorld** | 2025-12-23 | 258 | Mobile GUI+MCP · long-horizon workflow | 201 tasks with cross-app and agent-user interaction | [Code](https://github.com/Tongyi-MAI/MobileWorld) |
| **VenusBench-Mobile** | 2026-04 | 1,010² | Mobile · interactive episode | User-intent tasks and environment-variation diagnostics | [Code](https://github.com/inclusionAI/UI-Venus/tree/VenusBench-Mobile) |
| **MemGUI-Bench** | 2026-02-03 | 48 | Mobile · memory workflow | Dynamic, long-horizon memory evaluation | [Code](https://github.com/lgy0404/MemGUI-Bench) |
| **MobileGym-Bench** | 2026-05 | 773 | Mobile simulation · interactive episode | 416 parameterized templates with deterministic judges | [Code](https://github.com/Purewhiter/mobilegym) |
| **AndroidDaily** | 2026-05-26 | N/A | Real Android · long-horizon workflow | 350 tasks across 94 closed-source applications | [Paper](https://arxiv.org/abs/2605.27761) |
| **OS-Marathon** | 2026-01-28 | N/A | Desktop · repetitive workflow | 242 scalable expense/transcript tasks | [Project](https://os-marathon.github.io/) |
| **ScreenSpot-Pro** | 2025-01 | 391 | Desktop · static grounding | 4,304 instructions over professional high-resolution GUIs | [Code](https://github.com/likaixin2000/ScreenSpot-Pro-GUI-Grounding) |
| **AgentCLUE-CUA** | 2026 | N/A | Cross-platform · offline trajectory | Chinese grounding, information, and agent-action sub-scores | [Leaderboard](https://www.cluebenchmarks.com/superclue_2025) |
| **OS-Harm** | 2025-06 | 71 | Desktop · safety adversarial | 150 deliberate-misuse, injection, and misbehavior tasks | [Code](https://github.com/tml-epfl/os-harm) |
| **RTC-Bench / RedTeamCUA** | 2025-05 | 60 | Desktop/web · safety adversarial | 864 indirect prompt-injection examples across three environments | [Code](https://github.com/OSU-NLP-Group/RedTeamCUA) |
| **OSGuard** | 2026-06 | N/A | Desktop · safety adversarial | Action-level safety plus OSWorld-derived invariant checking | [Paper](https://arxiv.org/abs/2606.15034) |

¹ Star snapshot: 2026-08-25. ² Shared method repository; stars do not measure the benchmark alone. See the full registry for every repository-scope caveat and the other 50 artifacts.

### General, professional, and safety agents

| Benchmark | Launch | Stars¹ | Dimension | Status | Project |
|---|---|---|---|---|---|
| **OmniaBench** | 2026-07 | 12 | General Agent | Tracked | [Code](https://github.com/scuuy/OmniaBench) |
| **AGENCYBENCH** | 2026 | N/A | General Agent | Tracked | [Paper](https://aclanthology.org/2026.acl-long.337.pdf) |
| **GDPval-AA v2** | 2026 | N/A | Professional Work | Tracked | [Leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa) |
| **Claw-Eval-Live** | 2026-04 | 44 | Enterprise Agent Workflows | Tracked | [Code](https://github.com/Claw-Eval-Live/Claw-Eval-Live) |
| **Agent3Sigma** | 2026-05 | 30 | Agent Safety | Tracked | [Code](https://github.com/antgroup/Agent3Sigma) |
| **SkillSafetyBench** | 2026-05 | 30 | Skill and Local-Artifact Safety | Released | [Paper](https://arxiv.org/abs/2605.12015) · [Code](https://github.com/AI45Lab/skill-safety-bench) |
| **TRUST-Bench** | 2026-05 | N/A | Compromised-Tool Robustness | Emerging | [Paper](https://arxiv.org/abs/2605.17453) |
| **AgentLAB** | 2026-02 | N/A | Long-Horizon Agent Security | Emerging | [Paper](https://arxiv.org/abs/2602.16901) |
| **TAMAS** | 2026 | 24 | Multi-Agent System Safety | Released | [Paper](https://aclanthology.org/2026.acl-long.1442/) · [Code](https://github.com/microsoft/TAMAS) |
| **ST-WebAgentBench** | 2026 | N/A | Web-Agent Safety and Trust | Emerging | [Project](https://research.ibm.com/publications/st-webagentbench-a-benchmark-for-evaluating-safety-and-trustworthiness-in-web-agents--1) |
| **AgentFairBench** | 2026-06 | N/A | Fairness in Stateful Agent Decisions | Emerging | [Paper](https://arxiv.org/abs/2606.16723) |
| **HVTB** | 2026-08-22 | N/A | Reward-Hacking Detection | Emerging | [Paper](https://arxiv.org/abs/2608.22103) |
| **CatchBench** | 2026-08-24 | N/A | Evaluation Auditing | Work in progress | [Paper](https://arxiv.org/abs/2608.22808) |
| **TheAgentCompany** | 2024-12 | 770 | Simulated Knowledge Work | Discovery queue | [Code](https://github.com/TheAgentCompany/TheAgentCompany) |
| **AgentDojo** | 2024-06 | 768 | Prompt-Injection Safety | Discovery queue | [Code](https://github.com/ethz-spylab/agentdojo) |
| **AgentHarm** | 2024-10 | 643 | Harmful Agent Behavior | Discovery queue | [Code](https://github.com/UKGovernmentBEIS/inspect_evals) |

¹ GitHub star snapshot: 2026-08-25. `N/A` means no verified official repository or an unavailable repository; shared-suite and toolkit caveats are listed in [Launch & Stars](docs/benchmark-release-and-stars.md).

## 🤖 Model-family coverage

The target families are **GPT, Claude, GLM, Kimi, and Qwen**. Coverage is role-aware:

- **Agent model** — drives the evaluated agent.
- **Target model** — is trained, modified, or optimized by another agent.
- **Judge model** — scores outputs but does not perform the task.

This distinction prevents false claims. For example, PostTrainBench uses Qwen3 base checkpoints as target models; that does not establish that a Qwen-powered agent completed PostTrainBench.

Benchmarks with reported results for all five target families already include:

| Benchmark | Dimension | GPT | Claude | GLM | Kimi | Qwen |
|---|---|:---:|:---:|:---:|:---:|:---:|
| NatureBench | Scientific Discovery | ✓ | ✓ | ✓ | ✓ | ✓ |
| DiG-bench | Interactive World Discovery | ✓ | ✓ | ✓ | ✓ | ✓ |
| SWE-bench Verified | Coding | ✓ | ✓ | ✓ | ✓ | ✓ |
| SWE-bench Pro | Coding | ✓ | ✓ | ✓ | ✓ | ✓ |
| Terminal-Bench | Coding | ✓ | ✓ | ✓ | ✓ | ✓ |
| TerminalWorld | Coding | ✓ | ✓ | ✓ | ✓ | ✓ |
| tau2-bench | Tool Use | ✓ | ✓ | ✓ | ✓ | ✓ |
| MCP-Atlas | Tool Use | ✓ | ✓ | ✓ | ✓ | ✓ |
| MCP-Bench | Tool Use | ✓ | ✓ | ✓ | ✓ | ✓ |
| Toolathlon | Tool Use | ✓ | ✓ | ✓ | ✓ | ✓ |
| OmniaBench | General Agent | ✓ | ✓ | ✓ | ✓ | ✓ |
| AGENCYBENCH | General Agent | ✓ | ✓ | ✓ | ✓ | ✓ |
| Agent3Sigma | Safety | ✓ | ✓ | ✓ | ✓ | ✓ |
| Claw-Eval-Live | Professional Workflows | ✓ | ✓ | ✓ | ✓ | ✓ |
| GDPval-AA v2 | Professional Work | ✓ | ✓ | ✓ | ✓ | ✓ |

The evidence source, exact model version, role, and remaining gaps are recorded in [Model Coverage](docs/model-coverage.md). A checkmark means that a result has been reported; it does **not** imply that scores produced with different scaffolds are directly comparable.

CUA/GUI coverage is currently **distributed across complementary benchmarks**, rather than supported by one trustworthy five-family apples-to-apples run. For example, [MobileWorld](docs/cua-gui-benchmarks.md#reported-model-family-coverage) reports GPT, Claude, Kimi, and Qwen; AgentCLUE-CUA and the official GLM-V evaluations add GLM evidence; OSWorld-MCP, ClawBench, AndroidWorld, WebVoyager, and UI-Vision provide further overlapping checks. The CUA registry leaves cells blank when only harness support—not an evaluated result—was found.

## 🧱 Machine-readable registries

The task-level registry is [data/discovery-tasks.json](data/discovery-tasks.json), validated against [schema/discovery-task.schema.json](schema/discovery-task.schema.json). The suite-level registry is [data/benchmarks.json](data/benchmarks.json), validated against [schema/benchmark.schema.json](schema/benchmark.schema.json). The dedicated [CUA/GUI registry](data/cua-gui-benchmarks.json) adds 70 task-contract records with its own dependency-free validator and generated [human-readable catalog](docs/cua-gui-benchmarks.md).

Each detailed task or suite entry records:

- task type and agent-visible input;
- required output artifact;
- evaluator and aggregation method;
- container, VM, hardware, time, network, and scaffold policy;
- dated score snapshots and caveats;
- integrity risks and controls;
- AI4AI/RSI relevance;
- GPT, Claude, GLM, Kimi, and Qwen evidence by model role.

```python
import json
from pathlib import Path

registry = json.loads(Path("data/benchmarks.json").read_text(encoding="utf-8"))

for benchmark in registry["benchmarks"]:
    coverage = benchmark["model_coverage"]["families"]
    tested_agents = [
        family
        for family, record in coverage.items()
        if record["agent_models"]
    ]
    print(benchmark["name"], tested_agents)
```

Validate locally:

```bash
python scripts/validate_registry.py
python scripts/validate_discovery_tasks.py
python scripts/validate_cua_gui_benchmarks.py
python scripts/render_cua_gui_benchmarks.py --check
python scripts/render_discovery_task_sota.py --check
```

## ✅ Inclusion criteria

A discovery task belongs in the primary registry when it has a concrete optimization question, an agent-mutable output artifact, an executable or inspectable evaluator, a named metric and direction, and enough environment information to attempt reproduction. A method name or paper-level claim without an extractable task remains provenance or a discovery lead.

A benchmark belongs here when the evaluated system must do at least two of the following:

- act over multiple steps rather than answer once;
- use tools, a terminal, files, APIs, a browser, or an interactive environment;
- create or modify an executable artifact;
- run experiments and respond to environment feedback;
- manage a meaningful time, token, or compute budget;
- improve another model, algorithm, scientific result, or AI-development workflow.

Static QA and ordinary single-turn code-generation benchmarks are out of scope unless they are embedded in an agentic tool-use or long-horizon workflow.

Model coverage requires evidence from an official paper, repository, leaderboard, model card, or a reproducible third-party run with released artifacts. Search snippets and marketing tables without methodology remain discovery leads.

## 🤝 Contributing

Contributions are welcome. Good first contributions include:

- adding an executable discovery task with its question, seed/input, evaluator, environment, metric, and reference result;
- adding a missing benchmark to the discovery queue;
- attaching primary-source evidence for a model-family result;
- upgrading a tracked benchmark into a detailed registry entry;
- correcting an environment, score, model role, or integrity caveat;
- contributing reproducible evaluation artifacts.

Before opening a PR:

1. Read [CONTRIBUTING.md](CONTRIBUTING.md).
2. Prefer primary sources.
3. Record the exact model, scaffold, benchmark version, budget, and date.
4. Distinguish agent, target, and judge models.
5. Run `python scripts/validate_registry.py`.
6. Run `python scripts/validate_discovery_tasks.py` when changing the task registry.
7. Run `python scripts/render_discovery_task_sota.py --check` when changing task or SOTA data.

## 🔗 Related repositories

- [Awesome RSI](https://github.com/lobehub/awesome-rsi) — research map of recursive self-improvement, harness evolution, AI R&D, and safety.
- [Awesome AI for Research](https://github.com/THU-KEG/Awesome-AI-for-Research) — papers, systems, and benchmarks across the research lifecycle.
- [Awesome Agent Evals](https://github.com/benchflow-ai/awesome-evals) — annotated resources for building and evaluating agents.
- [Awesome AI Agent Benchmarks](https://github.com/serenakeyitan/awesome-ai-agent-benchmarks) — broad benchmark index across agent dimensions.
- [Awesome AI Scientist Benchmarks](https://github.com/hflyzju/Awesome-AI-Scientist-Benchmarks) — AI-scientist and proposal-to-code benchmark list.

## 📄 License

This repository is released under the [MIT License](LICENSE). Individual benchmark papers, datasets, environments, and evaluation artifacts remain subject to their respective licenses.

---

<div align="center">

If this registry helps your research, consider contributing a benchmark, an evaluation artifact, or a model-family result.

</div>
