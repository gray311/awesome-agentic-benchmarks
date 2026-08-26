<div align="center">

# Awesome Agentic Benchmarks

A curated list of papers and primary resources for evaluating autonomous agents, AI R&D systems, and recursive self-improvement.

[Categories](#categories) | [Papers](#papers) | [Contributing](CONTRIBUTING.md)

</div>

## Categories

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

## Papers

Stars are a **2026-08-25 snapshot** of the official benchmark repository (or a clearly marked shared toolkit); frontier results were checked on **2026-08-26**. `N/A` means that no verified official GitHub repository was available. Results are only compared within the same benchmark version, track, and harness policy; a newly released model is not labeled SOTA until a result exists. `—` means that no trustworthy single leader could be established.

### AI R&D and scientific discovery

| Benchmark | Stars | Current SOTA / frontier results | Paper / Primary resources |
|---|---:|---|---|
| **MLE-bench** | 1,716 | Famou-Agent 2.0 + Gemini-3-Pro-Preview — 64.44% (latest official board) | [Paper](https://arxiv.org/abs/2410.07095); [Code](https://github.com/openai/mle-bench); [Leaderboard](https://www.mlebench.com/) |
| **NatureBench** | 102 | Opus 5 + Claude Code — 23.3% Surpass-SOTA | [Paper](https://arxiv.org/abs/2606.24530); [Code](https://github.com/FrontisAI/NatureBench); [Leaderboard](https://frontisai.github.io/NatureBench/) |
| **PostTrainBench** | 532 | Fable 5 + Claude Code Max — 41.79% (GPQA uses Opus 4.8 fallback); GPT-5.6 Sol run flagged | [Paper](https://arxiv.org/abs/2603.08640); [Code](https://github.com/aisa-group/PostTrainBench); [Leaderboard](https://posttrainbench.com/) |
| **ARC-AGI-3** | 69 | Opus 5 — 30.2% verified track; [Tycho](https://arcprize.org/leaderboard/community) — 100% public-demo track | [Report](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf); [Toolkit](https://github.com/arcprize/ARC-AGI); [Leaderboard](https://arcprize.org/arc-agi/3/leaderboard) |
| **DiG-bench** | 24 | Opus 5 + Prime Agent | [Paper](https://arxiv.org/abs/2608.12593); [Code](https://github.com/discos-research/dig-bench); [Leaderboard](https://digbench.ai/) |
| **EdgeBench** | 432 | Claude Opus 4.8 — 43.6 at 12h (release board) | [Project / Leaderboard](https://edge-bench.org/); [Code](https://github.com/ByteDance-Seed/EdgeBench) |
| **RSI Bench** | N/A | — (task-dependent) | [Project](https://www.rsi-benchmark.com/); [Tasks](https://www.rsi-benchmark.com/tasks); [Runs](https://www.rsi-benchmark.com/runs) |
| **RSIBench** | N/A | — | [Dataset](https://huggingface.co/datasets/AgPerry/rsi-bench); [Code](https://github.com/reacher-z/rsi-bench) |
| **AI4AI-Bench** | N/A | — | [Paper](https://arxiv.org/abs/2608.20318) |
| **RE-Bench** | 156 | — | [Paper](https://arxiv.org/abs/2411.15114); [Code](https://github.com/METR/RE-Bench) |
| **MLR-Bench** | N/A | MARS (paper result) | [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/ab8dd000d6f87f40061a73f8bca7fae4-Abstract-Datasets_and_Benchmarks_Track.html) |
| **PaperBench** | N/A | — | [Paper](https://arxiv.org/abs/2504.01848); [Project](https://openai.com/index/paperbench/) |
| **InferenceBench** | 42 | — | [Code](https://github.com/aisa-group/InferenceBench) |
| **AgentHPOBench** | N/A | — | [Paper](https://arxiv.org/abs/2607.29626) |
| **SciAgentArena** | N/A | — | [Paper](https://arxiv.org/abs/2606.12736) |
| **EarthVerse** | N/A | — | [Paper](https://arxiv.org/abs/2608.23525) |
| **ScienceAgentBench** | 161 | GPT-4o (paper result) | [Paper](https://arxiv.org/abs/2410.05080); [Code](https://github.com/OSU-NLP-Group/ScienceAgentBench) |
| **EXP-Bench** | N/A | — | [Paper](https://arxiv.org/abs/2505.24785); [Code](https://github.com/EvolvingLMMs-Lab/EXP-Bench) |

### Coding and software engineering

| Benchmark | Stars | Current SOTA / frontier results | Paper / Primary resources |
|---|---:|---|---|
| **SWE-bench Verified** | 5,708 | **Claude Opus 5 — 97.0%**; GPT-5.6 Sol Max — 96.2%; Claude Fable 5 Max — 95.0% (Vals, 2026-08-19) | [Code](https://github.com/SWE-bench/SWE-bench); [Vals leaderboard](https://www.vals.ai/benchmarks/swebench) |
| **SWE-bench Pro** | N/A | **Claude Fable 5 — 80.0%** vendor track; GPT-5.6 Sol — 64.6%; GPT-5.4 xHigh — 59.1% standardized Scale track | [Project / Leaderboard](https://scale.com/leaderboard/swe_bench_pro_public) |
| **SWE-bench Multilingual** | 359 | **Claude Opus 5 — 89.5%** | [Code](https://github.com/multi-swe-bench/multi-swe-bench); [Leaderboard](https://www.swebench.com/) |
| **SWE-bench Multimodal** | 5,708 | **Claude Opus 5 — 59.4%** | [Code](https://github.com/SWE-bench/SWE-bench); [Leaderboard](https://www.swebench.com/) |
| **Terminal-Bench** | 539 | **Opus 5 Max + mini-SWE-agent — 42.7%**; GPT-5.6 Sol Max + Codex — 34.6%; Fable 5 Max + Claude Code — 34.1% (v3.0) | [Code](https://github.com/harbor-framework/terminal-bench); [Leaderboard](https://www.frontierbench.ai/) |
| **TerminalWorld** | N/A | Claude Opus 4.7 + Terminus-2 — 62.5% (board last updated 2026-05-21) | [Project / Leaderboard](https://terminalworld.ai/) |
| **TUA-Bench** | 46 | Claude Code + Claude Opus 4.8 Max — 65.8% (release result) | [Code](https://github.com/facebookresearch/TUA-Bench); [Leaderboard](https://tuabench.ai/) |
| **SWE Refactor Bench** | N/A | — | [Paper](https://arxiv.org/abs/2608.23564) |
| **NetConfArena** | N/A | — | [Paper](https://arxiv.org/abs/2608.23179) |
| **SWE-Lancer** | 1,431 | — | [Code](https://github.com/openai/SWELancer-Benchmark) |

### Tool use and interaction

| Benchmark | Stars | Current SOTA / frontier results | Paper / Primary resources |
|---|---:|---|---|
| **tau-bench** | 1,403 | — | [Code](https://github.com/sierra-research/tau-bench) |
| **tau2-bench** | 1,867 | GLM-5.2 — 99.1% (Aug 2026 public snapshot) | [Code](https://github.com/sierra-research/tau2-bench) |
| **BFCL** | 13,007 | Claude Opus 4.5 (FC) — 77.47% (official V4 board last updated 2026-04-12) | [Code](https://github.com/ShishirPatil/gorilla); [Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard) |
| **MCP-Atlas** | 149 | Muse Spark 1.1 — 88.1%; Opus 5 — 85.8%; Fable 5 — 83.3%; GPT-5.6 Sol — 81.8% | [Code](https://github.com/scaleapi/mcp-atlas); [Leaderboard](https://labs.scale.com/leaderboard/mcp_atlas) |
| **MCP-Bench** | 502 | — | [Code](https://github.com/Accenture/mcp-bench) |
| **Toolathlon** | N/A | Opus 5 — 80.6% (Aug 23 mirror); Muse Spark 1.1 — 75.6% (Aug 22 mirror); GPT-5.6 Sol — 58.0% | [Project](https://toolathlon.xyz/) |
| **ACEBench** | 3 | — | [Results](https://github.com/Agent-Suite/AgentSuite/blob/main/ACEBench/README.md) |

### Computer use and GUI interaction

| Benchmark | Stars | Current SOTA / frontier results | Paper / Primary resources |
|---|---:|---|---|
| **OSWorld** | 3,106 | Original protocol; current submissions use OSWorld-Verified | [Code](https://github.com/xlang-ai/OSWorld); [Leaderboard](https://os-world.github.io/) |
| **OSWorld-Verified** | 3,106¹ | **Qwen3.8 Max Preview — 86.1%**; Claude Fable 5 — 85.0%; GPT-5.6 Sol — 83.0% (2026-08-25 public snapshot) | [Project](https://xlang.ai/blog/osworld-verified); [Leaderboard](https://os-world.github.io/) |
| **OSWorld 2.0** | 258 | Claude Opus 4.8 + batched actions — 20.6% binary / 54.8% partial credit (full 108-task board) | [Code](https://github.com/xlang-ai/OSWorld-V2); [Project](https://osworld-v2.xlang.ai/) |
| **WindowsWorld** | 21 | — | [Code](https://github.com/HITsz-TMG/WindowsWorld) |
| **MacAgentBench** | 49 | Claude Opus 4.6 + OpenClaw | [Code](https://github.com/JetAstra/MacAgentBench) |
| **WeaveBench** | 159 | LongHorizon-Harness + Qwen3.7-Plus + Claude Code executor — 80.7% pass rate (full 114 tasks) | [Code](https://github.com/weavebench/WeaveBench); [Leaderboard](https://weavebench.github.io/) |
| **DeskCraft** | 91 | Kimi K2.6 — 33.8% standard; GPT-5.4 — 27.6% interactive (split-dependent) | [Code](https://github.com/mrwwk/DeskCraft); [Project](https://mrwwk.github.io/DeskCraft/) |
| **ClawBench** | 585 | — | [Code](https://github.com/TIGER-AI-Lab/ClawBench) |
| **SaaS-Bench** | 96 | Claude Opus 4.6 — 1.9% resolved (paper result) | [Code](https://github.com/UniPat-AI/SaaS-Bench) |
| **MobileWorld** | 258 | Qwen-UI-Agent — 82.1% | [Code](https://github.com/Tongyi-MAI/MobileWorld); [Leaderboard](https://tongyi-mai.github.io/MobileWorld/) |
| **VenusBench-Mobile** | 1,010¹ | — | [Code](https://github.com/inclusionAI/UI-Venus/tree/VenusBench-Mobile) |
| **MemGUI-Bench** | 48 | Kimi K2.6 (board last updated 2026-06) | [Code](https://github.com/lgy0404/MemGUI-Bench) |
| **MobileGym-Bench** | 773 | Gemini 3.1 Pro — 58.8% | [Code](https://github.com/Purewhiter/mobilegym); [Leaderboard](https://mobilegym.dev/) |
| **AndroidDaily** | N/A | Qwen-UI-Agent — 97.5% | [Paper](https://arxiv.org/abs/2605.27761) |
| **OS-Marathon** | N/A | — | [Project](https://os-marathon.github.io/) |
| **ScreenSpot-Pro** | 391 | — | [Code](https://github.com/likaixin2000/ScreenSpot-Pro-GUI-Grounding) |
| **AgentCLUE-CUA** | N/A | Qwen3-VL-235B-A22B-Thinking — 87.37 | [Leaderboard](https://www.cluebenchmarks.com/superclue_2025) |
| **OS-Harm** | 71 | No single SOTA (safety/utility trade-off) | [Code](https://github.com/tml-epfl/os-harm) |
| **RTC-Bench / RedTeamCUA** | 60 | No single SOTA (attack/defense metrics) | [Code](https://github.com/OSU-NLP-Group/RedTeamCUA) |
| **OSGuard** | N/A | No single SOTA (safety/utility trade-off) | [Paper](https://arxiv.org/abs/2606.15034) |

### General, professional, and safety agents

| Benchmark | Stars | Current SOTA / frontier results | Paper / Primary resources |
|---|---:|---|---|
| **OmniaBench** | 12 | Claude Sonnet 5 — 58.54%; GPT-5.6 Sol — 57.14% | [Code](https://github.com/scuuy/OmniaBench) |
| **AGENCYBENCH** | N/A | — | [Paper](https://aclanthology.org/2026.acl-long.337.pdf) |
| **GDPval-AA v2** | N/A | Claude Opus 5 Max — 1,835 Elo | [Leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa) |
| **Claw-Eval-Live** | 44 | Claude Opus 4.6 — 83.6% (latest released board) | [Code](https://github.com/Claw-Eval-Live/Claw-Eval-Live); [Leaderboard](https://claw-eval-live.github.io/#/leaderboard) |
| **Agent3Sigma** | 30 | Claude Opus 4.6 — 85.1 (latest released board) | [Code / Leaderboard](https://github.com/antgroup/Agent3Sigma) |
| **SkillSafetyBench** | 30 | No single SOTA (capability/safety trade-off) | [Paper](https://arxiv.org/abs/2605.12015); [Code](https://github.com/AI45Lab/skill-safety-bench) |
| **TRUST-Bench** | N/A | No single SOTA (robustness trade-off) | [Paper](https://arxiv.org/abs/2605.17453) |
| **AgentLAB** | N/A | No single SOTA (security metrics) | [Paper](https://arxiv.org/abs/2602.16901) |
| **TAMAS** | 24 | No single SOTA (multi-agent safety) | [Paper](https://aclanthology.org/2026.acl-long.1442/); [Code](https://github.com/microsoft/TAMAS) |
| **ST-WebAgentBench** | N/A | No single SOTA (safety/trust dimensions) | [Project](https://research.ibm.com/publications/st-webagentbench-a-benchmark-for-evaluating-safety-and-trustworthiness-in-web-agents--1) |
| **AgentFairBench** | N/A | No single SOTA (fairness/utility trade-off) | [Paper](https://arxiv.org/abs/2606.16723) |
| **HVTB** | N/A | No single SOTA (reward-hacking detection) | [Paper](https://arxiv.org/abs/2608.22103) |
| **CatchBench** | N/A | No single SOTA (evaluation auditing) | [Paper](https://arxiv.org/abs/2608.22808) |
| **TheAgentCompany** | 770 | DeepSeek-V3.2 — 42.9% (latest public snapshot) | [Code](https://github.com/TheAgentCompany/TheAgentCompany) |
| **AgentDojo** | 768 | No single SOTA (utility/security frontier) | [Code](https://github.com/ethz-spylab/agentdojo) |
| **AgentHarm** | 643¹ | No single SOTA (harm/refusal metrics) | [Code](https://github.com/UKGovernmentBEIS/inspect_evals) |

¹ Stars belong to a shared suite, toolkit, or method repository rather than a benchmark-only repository.

Detailed task contracts, scores, model coverage, launch dates, and machine-readable registries are maintained in [`docs/`](docs/) and [`data/`](data/).

Contributions are welcome; see [CONTRIBUTING.md](CONTRIBUTING.md).

Licensed under the [MIT License](LICENSE).
