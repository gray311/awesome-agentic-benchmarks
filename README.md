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

### AI R&D and scientific discovery

| Benchmark | Paper / Primary resources |
|---|---|
| **MLE-bench** | [Paper](https://arxiv.org/abs/2410.07095); [Code](https://github.com/openai/mle-bench); [Leaderboard](https://github.com/openai/mle-bench#leaderboard) |
| **NatureBench** | [Paper](https://arxiv.org/abs/2606.24530); [Code](https://github.com/FrontisAI/NatureBench); [Leaderboard](https://frontisai.github.io/NatureBench/) |
| **PostTrainBench** | [Paper](https://arxiv.org/abs/2603.08640); [Code](https://github.com/aisa-group/PostTrainBench); [Leaderboard](https://posttrainbench.com/) |
| **ARC-AGI-3** | [Report](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf); [Toolkit](https://github.com/arcprize/ARC-AGI); [Docs](https://docs.arcprize.org/) |
| **DiG-bench** | [Paper](https://arxiv.org/abs/2608.12593); [Code](https://github.com/discos-research/dig-bench); [Leaderboard](https://digbench.ai/) |
| **EdgeBench** | [Project](https://edge-bench.org/); [Code](https://github.com/ByteDance-Seed/EdgeBench) |
| **RSI Bench** | [Project](https://www.rsi-benchmark.com/); [Tasks](https://www.rsi-benchmark.com/tasks); [Runs](https://www.rsi-benchmark.com/runs) |
| **RSIBench** | [Dataset](https://huggingface.co/datasets/AgPerry/rsi-bench); [Code](https://github.com/reacher-z/rsi-bench) |
| **AI4AI-Bench** | [Paper](https://arxiv.org/abs/2608.20318) |
| **RE-Bench** | [Paper](https://arxiv.org/abs/2411.15114); [Code](https://github.com/METR/RE-Bench) |
| **MLR-Bench** | [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/ab8dd000d6f87f40061a73f8bca7fae4-Abstract-Datasets_and_Benchmarks_Track.html) |
| **PaperBench** | [Paper](https://arxiv.org/abs/2504.01848); [Project](https://openai.com/index/paperbench/) |
| **InferenceBench** | [Code](https://github.com/aisa-group/InferenceBench) |
| **AgentHPOBench** | [Paper](https://arxiv.org/abs/2607.29626) |
| **SciAgentArena** | [Paper](https://arxiv.org/abs/2606.12736) |
| **EarthVerse** | [Paper](https://arxiv.org/abs/2608.23525) |
| **ScienceAgentBench** | [Paper](https://arxiv.org/abs/2410.05080); [Code](https://github.com/OSU-NLP-Group/ScienceAgentBench) |
| **EXP-Bench** | [Paper](https://arxiv.org/abs/2505.24785); [Code](https://github.com/EvolvingLMMs-Lab/EXP-Bench) |

### Coding and software engineering

| Benchmark | Paper / Primary resources |
|---|---|
| **SWE-bench Verified** | [Code](https://github.com/SWE-bench/SWE-bench) |
| **SWE-bench Pro** | [Project](https://scale.com/leaderboard/swe_bench_pro_public) |
| **SWE-bench Multilingual** | [Code](https://github.com/multi-swe-bench/multi-swe-bench) |
| **SWE-bench Multimodal** | [Code](https://github.com/SWE-bench/SWE-bench) |
| **Terminal-Bench** | [Code](https://github.com/harbor-framework/terminal-bench) |
| **TerminalWorld** | [Project / Leaderboard](https://terminalworld.ai/) |
| **TUA-Bench** | [Code](https://github.com/facebookresearch/TUA-Bench) |
| **SWE Refactor Bench** | [Paper](https://arxiv.org/abs/2608.23564) |
| **NetConfArena** | [Paper](https://arxiv.org/abs/2608.23179) |
| **SWE-Lancer** | [Code](https://github.com/openai/SWELancer-Benchmark) |

### Tool use and interaction

| Benchmark | Paper / Primary resources |
|---|---|
| **tau-bench** | [Code](https://github.com/sierra-research/tau-bench) |
| **tau2-bench** | [Code](https://github.com/sierra-research/tau2-bench) |
| **BFCL** | [Code](https://github.com/ShishirPatil/gorilla) |
| **MCP-Atlas** | [Code](https://github.com/scaleapi/mcp-atlas); [Leaderboard](https://labs.scale.com/leaderboard/mcp_atlas) |
| **MCP-Bench** | [Code](https://github.com/Accenture/mcp-bench) |
| **Toolathlon** | [Project](https://toolathlon.xyz/) |
| **ACEBench** | [Results](https://github.com/Agent-Suite/AgentSuite/blob/main/ACEBench/README.md) |

### Computer use and GUI interaction

| Benchmark | Paper / Primary resources |
|---|---|
| **OSWorld** | [Code](https://github.com/xlang-ai/OSWorld) |
| **OSWorld-Verified** | [Project](https://xlang.ai/blog/osworld-verified) |
| **OSWorld 2.0** | [Code](https://github.com/xlang-ai/OSWorld-V2) |
| **WindowsWorld** | [Code](https://github.com/HITsz-TMG/WindowsWorld) |
| **MacAgentBench** | [Code](https://github.com/JetAstra/MacAgentBench) |
| **WeaveBench** | [Code](https://github.com/weavebench/WeaveBench) |
| **DeskCraft** | [Code](https://github.com/mrwwk/DeskCraft) |
| **ClawBench** | [Code](https://github.com/TIGER-AI-Lab/ClawBench) |
| **SaaS-Bench** | [Code](https://github.com/UniPat-AI/SaaS-Bench) |
| **MobileWorld** | [Code](https://github.com/Tongyi-MAI/MobileWorld) |
| **VenusBench-Mobile** | [Code](https://github.com/inclusionAI/UI-Venus/tree/VenusBench-Mobile) |
| **MemGUI-Bench** | [Code](https://github.com/lgy0404/MemGUI-Bench) |
| **MobileGym-Bench** | [Code](https://github.com/Purewhiter/mobilegym) |
| **AndroidDaily** | [Paper](https://arxiv.org/abs/2605.27761) |
| **OS-Marathon** | [Project](https://os-marathon.github.io/) |
| **ScreenSpot-Pro** | [Code](https://github.com/likaixin2000/ScreenSpot-Pro-GUI-Grounding) |
| **AgentCLUE-CUA** | [Leaderboard](https://www.cluebenchmarks.com/superclue_2025) |
| **OS-Harm** | [Code](https://github.com/tml-epfl/os-harm) |
| **RTC-Bench / RedTeamCUA** | [Code](https://github.com/OSU-NLP-Group/RedTeamCUA) |
| **OSGuard** | [Paper](https://arxiv.org/abs/2606.15034) |

### General, professional, and safety agents

| Benchmark | Paper / Primary resources |
|---|---|
| **OmniaBench** | [Code](https://github.com/scuuy/OmniaBench) |
| **AGENCYBENCH** | [Paper](https://aclanthology.org/2026.acl-long.337.pdf) |
| **GDPval-AA v2** | [Leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa) |
| **Claw-Eval-Live** | [Code](https://github.com/Claw-Eval-Live/Claw-Eval-Live) |
| **Agent3Sigma** | [Code](https://github.com/antgroup/Agent3Sigma) |
| **SkillSafetyBench** | [Paper](https://arxiv.org/abs/2605.12015); [Code](https://github.com/AI45Lab/skill-safety-bench) |
| **TRUST-Bench** | [Paper](https://arxiv.org/abs/2605.17453) |
| **AgentLAB** | [Paper](https://arxiv.org/abs/2602.16901) |
| **TAMAS** | [Paper](https://aclanthology.org/2026.acl-long.1442/); [Code](https://github.com/microsoft/TAMAS) |
| **ST-WebAgentBench** | [Project](https://research.ibm.com/publications/st-webagentbench-a-benchmark-for-evaluating-safety-and-trustworthiness-in-web-agents--1) |
| **AgentFairBench** | [Paper](https://arxiv.org/abs/2606.16723) |
| **HVTB** | [Paper](https://arxiv.org/abs/2608.22103) |
| **CatchBench** | [Paper](https://arxiv.org/abs/2608.22808) |
| **TheAgentCompany** | [Code](https://github.com/TheAgentCompany/TheAgentCompany) |
| **AgentDojo** | [Code](https://github.com/ethz-spylab/agentdojo) |
| **AgentHarm** | [Code](https://github.com/UKGovernmentBEIS/inspect_evals) |

Detailed task contracts, scores, model coverage, launch dates, and machine-readable registries are maintained in [`docs/`](docs/) and [`data/`](data/).

Contributions are welcome; see [CONTRIBUTING.md](CONTRIBUTING.md).

Licensed under the [MIT License](LICENSE).
