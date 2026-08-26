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
| **General Agents** | Broad planning, reasoning, tool use, and long-horizon execution | OmniaBench, AgencyBench, AgentBench |

## Papers

Stars are a **2026-08-25 snapshot** of the official benchmark repository (or a clearly marked shared toolkit); frontier results were checked on **2026-08-26**. `N/A` means that no verified official GitHub repository was available. Results are only compared within the same benchmark version, track, and harness policy; a newly released model is not labeled SOTA until a result exists. `Official board` means a benchmark-owner leaderboard, `method-reported` means a paper or agent repository result not yet on that board, and `vendor-reported` means a model-provider evaluation that may use a different harness. `—` means that no trustworthy single leader could be established.

### AI R&D and scientific discovery

| Benchmark | Stars | Current SOTA / frontier results | Paper / Primary resources |
|---|---:|---|---|
| **MLE-bench** | 1,716 | Famou-Agent 2.0 + Gemini-3-Pro-Preview — 64.44% (latest official board) | [Paper](https://arxiv.org/abs/2410.07095); [Code](https://github.com/openai/mle-bench); [Leaderboard](https://www.mlebench.com/) |
| **NatureBench** | 102 | Opus 5 + Claude Code / AIBuildAI 2.5 — 23.3% Surpass-SOTA (tied; Opus ranks first on secondary metrics) | [Paper](https://arxiv.org/abs/2606.24530); [Code](https://github.com/FrontisAI/NatureBench); [Leaderboard](https://frontisai.github.io/NatureBench/) |
| **PostTrainBench** | 532 | Fable 5 + Claude Code Max — 41.79% (GPQA uses Opus 4.8 fallback); GPT-5.6 Sol run flagged | [Paper](https://arxiv.org/abs/2603.08640); [Code](https://github.com/aisa-group/PostTrainBench); [Leaderboard](https://posttrainbench.com/) |
| **ARC-AGI-3** | 69 | Opus 5 — 30.2% verified track; [Tycho](https://arcprize.org/leaderboard/community) — 100% public-demo track | [Report](https://arcprize.org/media/ARC_AGI_3_Technical_Report.pdf); [Toolkit](https://github.com/arcprize/ARC-AGI); [Leaderboard](https://arcprize.org/arc-agi/3/leaderboard) |
| **DiG-bench** | 24 | Opus 5 + Prime Agent | [Paper](https://arxiv.org/abs/2608.12593); [Code](https://github.com/discos-research/dig-bench); [Leaderboard](https://digbench.ai/) |
| **EdgeBench** | 432 | Claude Opus 4.8 — 44.2 at 12h (current official repository table; 51-task public subset) | [Project](https://edge-bench.org/); [Code / Results](https://github.com/ByteDance-Seed/EdgeBench#open-source-subset-51-tasks) |
| **RSI Bench** | N/A | No global aggregate; official runs are ranked within each task | [Project](https://www.rsi-benchmark.com/); [Tasks](https://www.rsi-benchmark.com/tasks); [Runs](https://www.rsi-benchmark.com/runs) |
| **RSIBench** | N/A | Results pending; benchmark reports six independent test scores and forbids a global rank | [Dataset](https://huggingface.co/datasets/AgPerry/rsi-bench); [Code](https://github.com/reacher-z/rsi-bench); [Results](https://harness-rsibench.com/) |
| **AI4AI-Bench** | N/A | **Claude Opus 5 + Claude Code (medium) — 0.288 mean normalized score**; system-level mean 0.250 | [Paper](https://arxiv.org/abs/2608.20318) |
| **RE-Bench** | 156 | Claude 3.5 Sonnet (New) — 43.5% normalized score at 2 h (paper baseline) | [Paper](https://arxiv.org/abs/2411.15114); [Code](https://github.com/METR/RE-Bench) |
| **MLR-Bench** | N/A | Claude 3.7 Sonnet + Claude Code — 4.70 ± 1.22 overall end-to-end research score (paper result) | [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/ab8dd000d6f87f40061a73f8bca7fae4-Abstract-Datasets_and_Benchmarks_Track.html); [Project](https://chchenhui.github.io/mlrbench/) |
| **PaperBench** | N/A | **Qwen3.8-Max + BasicAgent — 93.0%** (provider-reported, three 12 h runs); original independently comparable paper leader: Claude 3.5 Sonnet + open scaffold — 21.0% | [Paper](https://arxiv.org/abs/2504.01848); [Project](https://openai.com/index/paperbench/); [Qwen model card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) |
| **InferenceBench** | 42 | **Claude Sonnet 4.6 — 8.08× aggregate speedup** (agent track); SMAC3 non-agent search — 11.53× | [Code / Leaderboard](https://github.com/aisa-group/InferenceBench) |
| **AgentHPOBench** | N/A | Claude Sonnet 4.6 — 0.407 MBNS / 76.7% baseline win rate; 0.472 MBNS with larger budget (paper result) | [Paper](https://arxiv.org/abs/2607.29626); [Code](https://github.com/OpenMOSS/AgentHPOBench) |
| **SciAgentArena** | N/A | No single overall leader; paper frontiers are task-family specific (ToolUniverse, Claude Code + ToolUniverse, and CACTUS among category leaders) | [Paper](https://arxiv.org/abs/2606.12736); [Project](https://sciagentarena.github.io/) |
| **EarthVerse** | N/A | **Claude Fable 5 + Claude Code — 84.97 Core / 84.65% unit accuracy**; GPT-5.6 Sol + Codex — 34.81% Strict@95 | [Paper / Results](https://arxiv.org/html/2608.23525v1) |
| **ScienceAgentBench** | 161 | **SAB Self-Debug + o3 (medium) — 33.3% verified accuracy** (paused official HAL board) | [Paper](https://arxiv.org/abs/2410.05080); [Code](https://github.com/OSU-NLP-Group/ScienceAgentBench); [Leaderboard](https://hal.cs.princeton.edu/scienceagentbench) |
| **EXP-Bench** | N/A | **OpenHands + o3-mini — 1.4% All✓ / 0.5% All·E✓** (paper result; ranked first by All·E✓ with conclusion-score tiebreak) | [Paper](https://arxiv.org/abs/2505.24785); [Code](https://github.com/EvolvingLMMs-Lab/EXP-Bench) |

### Coding and software engineering

| Benchmark | Stars | Current SOTA / frontier results | Paper / Primary resources |
|---|---:|---|---|
| **SWE-bench Verified** | 5,708 | **Claude Opus 5 — 97.0%**; GPT-5.6 Sol Max — 96.2%; Claude Fable 5 Max — 95.0% (Vals, 2026-08-19) | [Code](https://github.com/SWE-bench/SWE-bench); [Vals leaderboard](https://www.vals.ai/benchmarks/swebench) |
| **SWE-bench Pro** | N/A | Official standardized public board: **Muse Spark 1.1 + mini-SWE-agent — 61.5%**; vendor-reported, non-comparable harness: Claude Fable 5 — 80.0%, GPT-5.6 Sol — 64.6% | [Scale leaderboard](https://labs.scale.com/leaderboard/swe_bench_pro_public); [OpenAI model-card evaluation](https://openai.com/index/gpt-5-6/) |
| **Multi-SWE-bench** | 359 | No official aggregate; paper frontier is per-language, with MopenHands + Claude 3.7 Sonnet leading most reported language tracks | [Paper](https://arxiv.org/abs/2504.02605); [Code](https://github.com/multi-swe-bench/multi-swe-bench) |
| **SWE-bench Multilingual** | 5,708¹ | **Gemini 3 Flash + mini-SWE-agent — 72.70%** (official board) | [Benchmark](https://www.swebench.com/multilingual.html); [Code](https://github.com/SWE-bench/SWE-bench); [Leaderboard](https://www.swebench.com/) |
| **SWE-bench Multimodal** | 5,708¹ | **GUIRepair + o3 — 35.98%; Codefuse Pycfuse SVR + o3 — 35.98%** (tied official board) | [Code](https://github.com/SWE-bench/SWE-bench); [Leaderboard](https://www.swebench.com/) |
| **Terminal-Bench** | 539 | **Opus 5 Max + mini-SWE-agent — 42.7%**; GPT-5.6 Sol Max + Codex — 34.6%; Fable 5 Max + Claude Code — 34.1% (v3.0) | [Code](https://github.com/harbor-framework/terminal-bench); [Leaderboard](https://www.frontierbench.ai/) |
| **TerminalWorld** | N/A | Claude Opus 4.7 + Terminus-2 — 62.5% (board last updated 2026-05-21) | [Project / Leaderboard](https://terminalworld.ai/) |
| **TUA-Bench** | 46 | Claude Code + Claude Opus 4.8 Max — 65.8% (release result) | [Code](https://github.com/facebookresearch/TUA-Bench); [Leaderboard](https://tuabench.ai/) |
| **SWE Refactor Bench** | N/A | **Claude Opus 5 — 47.0 / 100 composite** (paper result; 20 whole-repository migrations) | [Paper](https://arxiv.org/abs/2608.23564) |
| **NetConfArena** | N/A | **DeepSeek-V4-Pro + ReAct (thinking off) — 0.961 test-case score / 85.2% task pass rate** | [Paper / Results](https://arxiv.org/html/2608.23179v1); [Code](https://github.com/liujona/NetConfArena) |
| **SWE-Lancer** | 1,431 | **GPT-5.1-Codex-Max (xhigh) — 79.9% IC SWE** (OpenAI-reported); archived official Diamond board: o1 — 28.4% | [OpenAI evaluation](https://openai.com/index/gpt-5-1-codex-max/); [Code](https://github.com/openai/SWELancer-Benchmark); [Archived leaderboard](https://swelancer.github.io/leaderboard/) |

### Tool use and interaction

| Benchmark | Stars | Current SOTA / frontier results | Paper / Primary resources |
|---|---:|---|---|
| **tau-bench** | 1,403 | Track-specific: Claude Opus 4.6 — 91.9% Retail; Claude Sonnet 4.5 — 70.0% Airline (public reported results; no official overall aggregate) | [Code](https://github.com/sierra-research/tau-bench); [Leaderboard](https://taubench.com/) |
| **tau2-bench** | 1,867 | **Qwen3.5-397B-A17B — 87.9% Pass¹** (official τ² text board) | [Code](https://github.com/sierra-research/tau2-bench); [Leaderboard](https://taubench.com/) |
| **BFCL** | 13,007 | Claude Opus 4.5 (FC) — 77.47% (official V4 board last updated 2026-04-12) | [Code](https://github.com/ShishirPatil/gorilla); [Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard) |
| **MCP-Atlas** | 149 | Muse Spark 1.1 — 88.1%; Opus 5 — 85.8%; Fable 5 — 83.3%; GPT-5.6 Sol — 81.8% | [Code](https://github.com/scaleapi/mcp-atlas); [Leaderboard](https://labs.scale.com/leaderboard/mcp_atlas) |
| **MCP-Bench** | 502 | **GPT-5 — 0.749 overall score** (official repository leaderboard) | [Code / Leaderboard](https://github.com/Accenture/mcp-bench) |
| **Toolathlon** | N/A | No official comparable live board; vendor-reported common evaluation: Claude Mythos 5 / Mythos Preview — 61.7%, GPT-5.6 Sol — 58.0% | [Project](https://toolathlon.xyz/); [Code](https://github.com/hkust-nlp/Toolathlon); [OpenAI model-card evaluation](https://openai.com/index/gpt-5-6/) |
| **ACEBench** | 3 | No canonical single aggregate exposed by AgentSuite; 30-model audited trajectories are released across normal, special, and agent task families | [Results](https://github.com/Agent-Suite/AgentSuite/blob/main/ACEBench/README.md); [Trajectories](https://huggingface.co/datasets/AgentSuite/ACEBench-trajectories) |

### Computer use and GUI interaction

| Benchmark | Stars | Current SOTA / frontier results | Paper / Primary resources |
|---|---:|---|---|
| **OSWorld** | 3,106 | Original protocol; current submissions use OSWorld-Verified | [Code](https://github.com/xlang-ai/OSWorld); [Leaderboard](https://os-world.github.io/) |
| **OSWorld-Verified** | 3,106¹ | Method-reported: **Ouroboros + Opus 5 — 90.69%**; official verified sheet: Intelligence-Indeed Agent — 90.19%, Fable 5 — 85.96%, Opus 5 — 83.39% | [Project](https://xlang.ai/blog/osworld-verified); [Official results sheet](https://osworld-v1.xlang.ai/static/data/osworld_verified_results.xlsx); [Ouroboros paper](https://arxiv.org/abs/2608.08311) |
| **OSWorld 2.0** | 258 | Vendor-reported partial credit: **GPT-5.6 Sol — 62.6%**; official release board: Opus 4.8 + batched actions — 20.6% binary / 54.8% partial (108 tasks) | [Code](https://github.com/xlang-ai/OSWorld-V2); [Project](https://osworld-v2.xlang.ai/); [OpenAI result](https://openai.com/index/gpt-5-6/) |
| **WindowsWorld** | 21 | Gemini 3 Flash Preview (screenshot + accessibility tree) — 20.44% final success (paper result) | [Paper](https://arxiv.org/abs/2604.27776); [Code](https://github.com/HITsz-TMG/WindowsWorld) |
| **MacAgentBench** | 49 | Claude Opus 4.6 + OpenClaw — 73.7% Pass@1 (official repository snapshot) | [Code / Results](https://github.com/JetAstra/MacAgentBench) |
| **WeaveBench** | 159 | Method-reported: **LongHorizon-Harness + Qwen3.7-Plus + Claude Code executor — 80.7%** (114 tasks); official live board: Opus 4.7 + Claude Code — 41.2% | [Code](https://github.com/weavebench/WeaveBench); [Official leaderboard](https://weavebench.github.io/); [LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness) |
| **DeskCraft** | 91 | Kimi K2.6 — 33.8% standard; GPT-5.4 — 27.6% interactive (split-dependent) | [Code](https://github.com/mrwwk/DeskCraft); [Project](https://mrwwk.github.io/DeskCraft/) |
| **ClawBench** | 585 | **Claude Opus 4.7 + Hermes — 44.6% reward / 54.6% lenient pass rate** (V2 official snapshot); V1 leader: Opus 4.6 — 61.4% | [Code](https://github.com/TIGER-AI-Lab/ClawBench); [Results](https://huggingface.co/datasets/TIGER-Lab/ClawBench/blob/main/leaderboard/results.csv) |
| **SaaS-Bench** | 96 | **Claude Opus 4.7 — 3.8% resolved / 43.9% checkpoint score** (paper result) | [Paper](https://arxiv.org/abs/2605.15777); [Code](https://github.com/UniPat-AI/SaaS-Bench) |
| **MobileWorld** | 258 | Method-reported: **Qwen-UI-Agent — 82.1%** (GUI-only, 50-step setting) | [Code](https://github.com/Tongyi-MAI/MobileWorld); [Leaderboard](https://tongyi-mai.github.io/MobileWorld/); [Qwen-UI-Agent](https://github.com/Tongyi-MAI/Qwen-UI-Agent) |
| **VenusBench-Mobile** | 1,010¹ | **Gemini 3 Pro planner + UI-Venus-72B executor — 36.9% success rate** (official 149-task board) | [Code](https://github.com/inclusionAI/UI-Venus/tree/VenusBench-Mobile); [Leaderboard](https://ui-venus.github.io/VenusBench-Mobile-Leaderboard/) |
| **MemGUI-Bench** | 48 | Official board ranks Kimi K2.6 first — 39.1 p@1 / 68.8 p@3 / 45.5 IRR (updated 2026-06) | [Code](https://github.com/lgy0404/MemGUI-Bench); [Leaderboard](https://memgui-bench.github.io/) |
| **MobileGym-Bench** | 773 | Gemini 3.1 Pro — 58.8% | [Code](https://github.com/Purewhiter/mobilegym); [Leaderboard](https://mobilegym.dev/) |
| **AndroidDaily** | N/A | Method-reported: Qwen-UI-Agent — 97.5% | [Paper](https://arxiv.org/abs/2605.27761); [Qwen-UI-Agent](https://github.com/Tongyi-MAI/Qwen-UI-Agent) |
| **OS-Marathon** | N/A | AgentS2.5 + GPT-5 + FCWD — 37.5% web / 25.0% spreadsheet SWA@200 on Expense L1–2 (paper result; 0% binary SR) | [Paper / Results](https://arxiv.org/html/2601.20650v1); [Project](https://os-marathon.github.io/) |
| **ScreenSpot-Pro** | 391 | **Claude Mythos Preview — 92.8% with Python tools / 79.5% without tools** (adaptive thinking, max effort; system-card result) | [Code](https://github.com/likaixin2000/ScreenSpot-Pro-GUI-Grounding); [System card](https://www-cdn.anthropic.com/8b8380204f74670be75e81c820ca8dda846ab289.pdf) |
| **AgentCLUE-CUA** | N/A | Qwen3-VL-235B-A22B-Thinking — 87.37 (official snapshot dated 2025-10-30) | [Leaderboard](https://www.cluebenchmarks.com/superclue_2025) |
| **OS-Harm** | 71 | Safety frontier (lower unsafe rate): GPT-4.1 — 21% average unsafe execution; category minima differ (paper results) | [Paper](https://arxiv.org/abs/2506.14866); [Code](https://github.com/tml-epfl/os-harm) |
| **RTC-Bench / RedTeamCUA** | 60 | Safety frontier in the paper: **OpenAI Operator — 7.6% attack success rate** (lowest); Claude 4 Opus CUA reaches 48% ASR in end-to-end attacks | [Paper](https://arxiv.org/abs/2505.21936); [Code](https://github.com/OSU-NLP-Group/RedTeamCUA) |
| **OSGuard** | N/A | Gemini 3 Pro Preview guardrail — 80% action accuracy / 0.80 macro-F1; guarded execution — 62% safe success / 33% unsafe completion | [Paper / Results](https://arxiv.org/html/2606.15034v1) |

### General, professional, and safety agents

| Benchmark | Stars | Current SOTA / frontier results | Paper / Primary resources |
|---|---:|---|---|
| **OmniaBench** | 12 | Claude Sonnet 5 — 58.54%; GPT-5.6 Sol — 57.14% | [Code](https://github.com/scuuy/OmniaBench) |
| **AgencyBench** | N/A | **GPT-5.2 — 56.5% average rubric score**; open-model leader GLM-4.6 — 38.6% (paper result) | [Paper](https://aclanthology.org/2026.acl-long.337/); [Code](https://github.com/GAIR-NLP/AgencyBench) |
| **GDPval-AA v2** | N/A | Claude Opus 5 Max — 1,831 Elo (official board, checked 2026-08-26) | [Leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa) |
| **Claw-Eval-Live** | 44 | Claude Opus 4.6 — 83.6% (latest released board) | [Code](https://github.com/Claw-Eval-Live/Claw-Eval-Live); [Leaderboard](https://claw-eval-live.github.io/#/leaderboard) |
| **Agent3Sigma** | 30 | Claude Opus 4.6 — 85.1 (latest released board) | [Code / Leaderboard](https://github.com/antgroup/Agent3Sigma) |
| **SkillSafetyBench** | 30 | Safety–utility frontier: Claude Code + Opus 4.6 — 15.5% ASR / 40.0% task success; Codex + GPT-5.5 — 41.8% ASR / 42.6% task success | [Paper](https://arxiv.org/abs/2605.12015); [Code](https://github.com/AI45Lab/skill-safety-bench) |
| **TRUST-Bench** | N/A | **VISTA-Guard + Mistral-7B — 84.2 GuardedJoint in-domain**; VISTA-Guard — 56.9 balanced OOD (paper results) | [Paper / Results](https://arxiv.org/html/2605.17453) |
| **AgentLAB** | N/A | Safety frontier: **Claude 4.5 Sonnet — 28.9% overall long-horizon attack success rate** (lowest of six agents); 0% task-injection ASR | [Paper / Results](https://arxiv.org/html/2602.16901) |
| **TAMAS** | 24 | **Llama-3.1-8B-Instruct + CrewAI decentralized — 80.70 ERS** (safety–utility harmonic mean; paper result) | [Paper](https://aclanthology.org/2026.acl-long.1442/); [Code](https://github.com/microsoft/TAMAS) |
| **ST-WebAgentBench** | N/A | Paper frontier among three open agents: **AWM — 0.238 Completion-under-Policy**; policy-category risk ratios remain separate | [Paper](https://openreview.net/pdf?id=fAmhr96SUw); [Project](https://sites.google.com/view/st-webagentbench/home) |
| **AgentFairBench** | N/A | Official pilot only: Claude Haiku 4.5; no demographic effect above the arity-matched noise floor (0/120 pairwise and 0/9 omnibus contrasts survive correction) | [Paper / Results](https://arxiv.org/html/2606.16723) |
| **HVTB** | N/A | Default-prompt safety frontier: **Kimi K3 — 22.7% reward-hack rate** (lowest of five); at L2, Kimi K3 and GPT-5.6 Sol reach 0%, and Claude Opus 5 joins them at L3 | [Paper / Results](https://arxiv.org/html/2608.22103) |
| **CatchBench** | N/A | No cross-board SOTA; **GPT-5.5 — 0.452 Top-1** on Who&When POST localization; structural leader on SWE-Gym POST detection: auditable size+deps — 0.804 ROC-AUC | [Paper / Results](https://arxiv.org/html/2608.22808) |
| **TheAgentCompany** | 770 | Paper-reported baseline: Gemini-2.5-Pro + OpenHands 0.28.1 — 30% success / 39% partial-credit score; no maintained comparable live board | [Paper](https://arxiv.org/abs/2412.14161); [Code](https://github.com/TheAgentCompany/TheAgentCompany) |
| **AgentDojo** | 768 | Official trade-off results: Claude 3.5 Sonnet — 79.38% utility / 1.11% targeted ASR; Claude 3.7 Sonnet — 88.66% utility / 7.31% targeted ASR (same attack, no defense) | [Code](https://github.com/ethz-spylab/agentdojo); [Results](https://agentdojo.spylab.ai/results/) |
| **AgentHarm** | 643¹ | 2026 safety–utility frontier: **TRIAD + Tri-Guard — 80.92 HS / 13.05 harm score**, averaged over Qwen3-32B, Kimi-2.5, Gemini-2.5-Pro, and GPT-5.1 | [Benchmark](https://ukgovernmentbeis.github.io/inspect_evals/evals/agentharm/); [TRIAD results](https://yuhaosunabc.github.io/TRIAD/) |

¹ Stars belong to a shared suite, toolkit, or method repository rather than a benchmark-only repository.

Detailed task contracts, scores, model coverage, launch dates, and machine-readable registries are maintained in [`docs/`](docs/) and [`data/`](data/).

Contributions are welcome; see [CONTRIBUTING.md](CONTRIBUTING.md).

Licensed under the [MIT License](LICENSE).
