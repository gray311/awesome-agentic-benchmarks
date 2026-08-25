# Computer-Use and GUI Agent Benchmarks

> Evidence snapshot: **2026-08-25** · GitHub stars: **2026-08-25** · **70 artifacts**, including **31 launched in 2026**.

This registry separates the thing being evaluated from the software used to run it. A benchmark contains evaluation tasks; an offline dataset contains recorded states or trajectories; an arena aggregates human preferences; an evaluation suite normalizes other benchmarks. These labels are not interchangeable.

## Evaluation units

| Unit | What one scored example is |
|---|---|
| `static-grounding` | One screenshot plus a target description; predict a point, box, element, or action. |
| `offline-trajectory` | Predict one or more actions from recorded GUI states without controlling a live environment. |
| `interactive-episode` | Act in a resettable live application until success, failure, or a step limit. |
| `long-horizon-workflow` | Produce and verify a multi-step or cross-application outcome, often with partial-progress checks. |
| `arena-preference` | Humans compare trajectories or outcomes; rankings are aggregated from pairwise preferences. |
| `safety-adversarial` | Measure unsafe action, policy violation, prompt-injection susceptibility, privacy leakage, or recovery. |

The central comparison rule is:

> **score = model + scaffold + observation + action space + environment version + step/compute budget + evaluator + attempt policy**

A ScreenSpot click-accuracy result is therefore not comparable to an OSWorld task-success result, and even two OSWorld scores are not comparable unless their versions and protocols match.

## Registry composition

| View | Counts |
|---|---|
| Artifact type | `arena` 1, `benchmark` 61, `evaluation-suite` 3, `offline-dataset` 5 |
| Evaluation unit | `arena-preference` 1, `interactive-episode` 26, `long-horizon-workflow` 19, `offline-trajectory` 13, `safety-adversarial` 7, `static-grounding` 4 |
| Launch year | 2026: **31** · earlier: **39** |

## Reported model-family coverage

A check means a primary benchmark or model source reports an evaluated **agent** result for that family. It does not mean the row is directly comparable to another benchmark or scaffold. Blank means no verified result was attached in this snapshot—not that the family cannot run the task.

| Benchmark | GPT | Claude | GLM | Kimi | Qwen | Evidence |
|---|:---:|:---:|:---:|:---:|:---:|---|
| ClawBench | ✓ | ✓ |  | ✓ | ✓ | [source](https://github.com/TIGER-AI-Lab/ClawBench) |
| MobileWorld | ✓ | ✓ |  | ✓ | ✓ | [source](https://github.com/Tongyi-MAI/MobileWorld) |
| OSWorld-MCP | ✓ | ✓ |  | ✓ | ✓ | [source](https://github.com/X-PLUG/OSWorld-MCP) |
| AndroidWorld | ✓ |  | ✓ |  | ✓ | [source](https://github.com/zai-org/GLM-V/blob/main/examples/gui-agent/glm-45v/agent.md) |
| Computer Agent Arena | ✓ | ✓ |  |  | ✓ | [source](https://github.com/xlang-ai/computer-agent-arena) |
| DeskCraft | ✓ | ✓ |  |  | ✓ | [source](https://github.com/mrwwk/DeskCraft) |
| GUI-Robust | ✓ | ✓ |  |  | ✓ | [source](https://github.com/chessbean1/GUI-Robust) |
| MacAgentBench | ✓ | ✓ |  |  | ✓ | [source](https://github.com/JetAstra/MacAgentBench) |
| MobileBench-OL | ✓ | ✓ |  |  | ✓ | [source](https://github.com/xiaomi-research/mobilebench-ol) |
| OSUniverse | ✓ | ✓ |  |  | ✓ | [source](https://github.com/agentsea/osuniverse) |
| OSWorld | ✓ | ✓ |  |  | ✓ | [source](https://arxiv.org/abs/2404.07972) |
| OSWorld-Verified | ✓ | ✓ |  |  | ✓ | [source](https://os-world.github.io/) |
| SaaS-Bench | ✓ | ✓ |  |  | ✓ | [source](https://arxiv.org/abs/2605.15777) |
| ScreenSpot | ✓ | ✓ |  |  | ✓ | [source](https://github.com/njucckevin/SeeClick) |
| ScreenSpot-Pro | ✓ | ✓ |  |  | ✓ | [source](https://github.com/likaixin2000/ScreenSpot-Pro-GUI-Grounding) |
| ScreenSpot-V2 | ✓ | ✓ |  |  | ✓ | [source](https://github.com/OS-Copilot/OS-Atlas) |
| UI-Vision | ✓ | ✓ |  |  | ✓ | [source](https://github.com/uivision/UI-Vision) |
| VenusBench-Mobile | ✓ | ✓ |  |  | ✓ | [source](https://github.com/inclusionAI/UI-Venus/tree/VenusBench-Mobile) |
| VisualWebArena | ✓ | ✓ |  |  | ✓ | [source](https://github.com/web-arena-x/visualwebarena) |
| VisualWebBench | ✓ | ✓ |  |  | ✓ | [source](https://github.com/VisualWebBench/VisualWebBench) |
| VPI-Bench | ✓ | ✓ |  |  | ✓ | [source](https://arxiv.org/abs/2506.02456) |
| WeaveBench | ✓ | ✓ |  |  | ✓ | [source](https://github.com/weavebench/WeaveBench) |
| WebArena | ✓ | ✓ |  |  | ✓ | [source](https://github.com/web-arena-x/webarena) |
| WebVoyager | ✓ |  | ✓ |  | ✓ | [source](https://github.com/zai-org/GLM-V/blob/main/examples/gui-agent/glm-45v/agent.md) |
| WindowsWorld | ✓ | ✓ |  |  | ✓ | [source](https://github.com/HITsz-TMG/WindowsWorld) |
| WorldGUI | ✓ | ✓ |  |  | ✓ | [source](https://github.com/showlab/WorldGUI) |
| AgentCLUE-CUA |  |  | ✓ |  | ✓ | [source](https://www.cluebenchmarks.com/superclue_2025) |
| AndroidControl |  |  | ✓ |  | ✓ | [source](https://github.com/xiaomi-research/guievalkit) |
| CUAHarm | ✓ | ✓ |  |  |  | [source](https://arxiv.org/abs/2508.00935) |
| GUIEvalKit |  |  | ✓ |  | ✓ | [source](https://github.com/xiaomi-research/guievalkit) |
| macOSWorld | ✓ | ✓ |  |  |  | [source](https://github.com/showlab/macosworld) |
| MAS-Bench |  |  | ✓ |  | ✓ | [source](https://aclanthology.org/2026.acl-long.316/) |
| MedSPOT | ✓ |  |  |  | ✓ | [source](https://github.com/Tajamul21/MedSPOT) |
| MemGUI-Bench |  |  |  | ✓ | ✓ | [source](https://github.com/lgy0404/MemGUI-Bench) |
| Mind2Web | ✓ |  |  |  | ✓ | [source](https://github.com/OSU-NLP-Group/Mind2Web) |
| MobileAgentBench | ✓ |  |  |  | ✓ | [source](https://github.com/MobileAgentBench/mobile-agent-bench) |
| Online-Mind2Web | ✓ | ✓ |  |  |  | [source](https://github.com/OSU-NLP-Group/Online-Mind2Web) |
| OS-Harm | ✓ | ✓ |  |  |  | [source](https://arxiv.org/abs/2506.14866) |
| OSWorld 2.0 | ✓ | ✓ |  |  |  | [source](https://arxiv.org/abs/2606.29537) |
| PPTArena | ✓ | ✓ |  |  |  | [source](https://github.com/michaelofengenden/PPTArena) |
| RTC-Bench / RedTeamCUA | ✓ | ✓ |  |  |  | [source](https://github.com/OSU-NLP-Group/RedTeamCUA) |
| SCUBA |  | ✓ |  |  | ✓ | [source](https://github.com/SalesforceAIResearch/SCUBA) |
| WebCanvas | ✓ | ✓ |  |  |  | [source](https://github.com/iMeanAI/WebCanvas) |
| WindowsAgentArena | ✓ | ✓ |  |  |  | [source](https://arxiv.org/abs/2409.08264) |
| WorkArena | ✓ | ✓ |  |  |  | [source](https://github.com/ServiceNow/WorkArena) |
| WorkArena++ | ✓ | ✓ |  |  |  | [source](https://github.com/ServiceNow/WorkArena) |
| FedGUI |  |  |  |  | ✓ | [source](https://github.com/wwh0411/FedGUI) |
| GUI Odyssey |  |  |  |  | ✓ | [source](https://github.com/OpenGVLab/GUI-Odyssey) |
| GUI-CEval |  |  |  |  | ✓ | [source](https://arxiv.org/abs/2603.15039) |
| MobileGym-Bench |  |  |  |  | ✓ | [source](https://github.com/Purewhiter/mobilegym) |
| OmniGUI |  |  |  |  | ✓ | [source](https://github.com/omni-gui/OmniGUI) |
| OS-Marathon | ✓ |  |  |  |  | [source](https://os-marathon.github.io/) |
| OSWorkerBench |  |  |  |  | ✓ | [source](https://github.com/Tencent/UI-Mate) |
| PPT-Eval |  | ✓ |  |  |  | [source](https://github.com/microsoft/ppteval) |

## Dated score snapshots

These are orientation points, not a normalized leaderboard. Each statement retains the benchmark/version wording in the machine-readable record.

- **OSWorld** — Original paper: best agent 12.24% versus 72.36% human; later OSWorld-Verified runs are a different snapshot. [source](https://arxiv.org/abs/2404.07972)
- **OSWorld 2.0** — At 500 steps, Claude Opus 4.8 reached 20.6% binary / 54.8% partial; GPT-5.5 was about 13% binary in the paper. [source](https://arxiv.org/abs/2606.29537)
- **WindowsWorld** — The paper reports less than 21% multi-app success for evaluated agents. [source](https://github.com/HITsz-TMG/WindowsWorld)
- **MacArena** — The paper reports model-ranking inversions and a greater than 26-point deficit on a native subset for one leading model. [source](https://arxiv.org/abs/2606.06560)
- **MacAgentBench** — Claude Opus 4.6: 73.7% Pass@1 with OpenClaw, 66.9% with Agent-S3, 39.2% with the baseline. [source](https://github.com/JetAstra/MacAgentBench)
- **OSWorld-MCP** — Paper examples: OpenAI o3 improved 8.3→20.4% at 15 steps; Claude 4 Sonnet 40.1→43.3% at 50 steps with tools. [source](https://github.com/X-PLUG/OSWorld-MCP)
- **WeaveBench** — Best reported model-runtime pairing: 41.2% PassRate. [source](https://github.com/weavebench/WeaveBench)
- **DeskCraft** — GPT-5.4: 31.6% on standard tasks and 27.6% on interactive tasks in the release snapshot. [source](https://github.com/mrwwk/DeskCraft)
- **OSWorkerBench** — UI-Mate-27B improves over its Qwen base by 17.67 strict-success points and 24.51 progress points. [source](https://github.com/Tencent/UI-Mate)
- **WebVoyager** — GLM-4.5V reports 84.4% on its WebVoyager2 protocol; do not mix that score with the original 15-site release. [source](https://github.com/zai-org/GLM-V/blob/main/examples/gui-agent/glm-45v/agent.md)
- **ClawBench** — Top release result: 33.3%. [source](https://github.com/TIGER-AI-Lab/ClawBench)
- **SaaS-Bench** — The strongest evaluated agent completed fewer than 4% of tasks end to end. [source](https://arxiv.org/abs/2605.15777)
- **UI-Vision** — Release table includes GPT-4o, Claude 3.5/3.7 Sonnet, and Qwen2/2.5-VL under matched tasks. [source](https://github.com/uivision/UI-Vision)
- **AndroidWorld** — GLM-4.5V reports 57.0% in its matched AndroidWorld evaluation; protocol details must accompany comparison. [source](https://github.com/zai-org/GLM-V/blob/main/examples/gui-agent/glm-45v/agent.md)
- **MobileWorld** — 2026-07 snapshot: Qwen-UI-Agent 82.1%; Kimi-K3 74.4% GUI-only; GPT-5.6-Sol 70.1%; Claude Opus 4.7 56.4% GUI-only / 59.1% user-interaction. [source](https://github.com/Tongyi-MAI/MobileWorld)
- **VenusBench-Mobile** — The paper reports near-zero success for even the strongest agents under environment variations. [source](https://github.com/inclusionAI/UI-Venus/tree/VenusBench-Mobile)
- **MemGUI-Bench** — The 2026-06 leaderboard update reports Kimi-K2.6 as the then-leading model. [source](https://github.com/lgy0404/MemGUI-Bench)
- **SimuWoB** — Average evaluated-agent success: 27.92%; long-horizon subset: 17.82%. [source](https://arxiv.org/abs/2605.25160)
- **AgentCLUE-CUA** — Snapshot: Qwen3-VL-235B-A22B-Thinking 87.37 overall; GLM-4.5V 84.49. [source](https://www.cluebenchmarks.com/superclue_2025)
- **MAS-Bench** — ACL paper reports GLM-4.5V at 68.3% under its hybrid protocol. [source](https://aclanthology.org/2026.acl-long.316/)
- **MobileGym-Bench** — 256-task test snapshot: Gemini 3.1 Pro 58.8% SR; Qwen3.6-Plus 45.7%; Qwen3-VL-4B 9.4% and 22.2% after GRPO. [source](https://github.com/Purewhiter/mobilegym)
- **AndroidDaily** — GRADE reaches 87.37% human agreement; the strongest evaluated model reaches 62.0% success. [source](https://arxiv.org/abs/2605.27761)

## Complete catalog

### Desktop and hybrid computer use

| Benchmark | Launch | Stars | Artifact / unit | Scale | Models reported | Primary artifacts |
|---|---:|---:|---|---|---|---|
| **OSWorkerBench** | 2026-08 | [78](https://github.com/Tencent/UI-Mate) | `benchmark` / `long-horizon-workflow` | Office-centric target tasks plus 33 self-demo and 45 variant-demo pairs | Qwen | [Primary](https://github.com/Tencent/UI-Mate) |
| **WeaveBench** | 2026-06-05 | [159](https://github.com/weavebench/WeaveBench) | `benchmark` / `long-horizon-workflow` | 114 tasks across 8 work domains | GPT, Claude, Qwen | [Primary](https://arxiv.org/abs/2606.09426) · [Code](https://github.com/weavebench/WeaveBench) · [Leaderboard](https://weavebench.github.io/) |
| **DeskCraft** | 2026-06-02 | [91](https://github.com/mrwwk/DeskCraft) | `benchmark` / `long-horizon-workflow` | 538 executable tasks: 386 standard and 152 interactive; 11 applications and 279 assets | GPT, Claude, Qwen | [Primary](https://arxiv.org/abs/2606.03103) · [Code](https://github.com/mrwwk/DeskCraft) · [Leaderboard](https://mrwwk.github.io/DeskCraft/) |
| **OSWorld 2.0** | 2026-06 | [258](https://github.com/xlang-ai/OSWorld-V2) | `benchmark` / `long-horizon-workflow` | 108 workflows | GPT, Claude | [Primary](https://arxiv.org/abs/2606.29537) · [Code](https://github.com/xlang-ai/OSWorld-V2) |
| **MacArena** | 2026-06 | N/A | `benchmark` / `interactive-episode` | 421 tasks across 50 applications, including 49 macOS-native tasks | — | [Primary](https://arxiv.org/abs/2606.06560) |
| **MacAgentBench** | 2026-06 | [49](https://github.com/JetAstra/MacAgentBench) | `benchmark` / `long-horizon-workflow` | 676 tasks across 25 applications; 140 multi-app tasks | GPT, Claude, Qwen | [Primary](https://arxiv.org/abs/2606.22557) · [Code](https://github.com/JetAstra/MacAgentBench) |
| **GUI-vs-CLI** | 2026-06 | [6](https://github.com/rebeccaz4/gui-vs-cli) | `benchmark` / `long-horizon-workflow` | Matched desktop tasks sharing initial state, target state, and verifier | — | [Primary](https://github.com/rebeccaz4/gui-vs-cli) |
| **Cua-Bench** | 2026-06 | [21,885](https://github.com/trycua/cua) | `benchmark` / `interactive-episode` | Versioned collection of desktop and mobile tasks | — | [Primary](https://cua.ai/cuabench) · [Code](https://github.com/trycua/cua) |
| **WindowsWorld** | 2026-04 | [21](https://github.com/HITsz-TMG/WindowsWorld) | `benchmark` / `long-horizon-workflow` | 181 tasks, 17 applications, 77.9% multi-app | GPT, Claude, Qwen | [Primary](https://arxiv.org/abs/2604.27776) · [Code](https://github.com/HITsz-TMG/WindowsWorld) |
| **OS-Marathon** | 2026-01-28 | N/A | `benchmark` / `long-horizon-workflow` | 242 tasks across expense-reporting and transcript-recording domains; the project page also contains one inconsistent 252-task sentence | GPT | [Primary](https://arxiv.org/abs/2601.20650) |
| **PPTArena** | 2025-12 | [28](https://github.com/michaelofengenden/PPTArena) | `benchmark` / `long-horizon-workflow` | 100 decks, 2,125 slides, more than 800 targeted edits | GPT, Claude | [Primary](https://arxiv.org/abs/2512.03042) · [Code](https://github.com/michaelofengenden/PPTArena) |
| **OSWorld-MCP** | 2025-10 | [233](https://github.com/X-PLUG/OSWorld-MCP) | `benchmark` / `interactive-episode` | 250 tool-beneficial tasks, 158 MCP tools, 7 applications, 25 distractor tools | GPT, Claude, Kimi, Qwen | [Primary](https://arxiv.org/abs/2510.24563) · [Code](https://github.com/X-PLUG/OSWorld-MCP) |
| **OSWorld-Verified** | 2025-07-28 | [3,106](https://github.com/xlang-ai/OSWorld) | `benchmark` / `interactive-episode` | 369 tasks; eight Google Drive tasks may be excluded under the official policy | GPT, Claude, Qwen | [Primary](https://xlang.ai/blog/osworld-verified) · [Code](https://github.com/xlang-ai/OSWorld) · [Leaderboard](https://os-world.github.io/) |
| **macOSWorld** | 2025-06 | [35](https://github.com/showlab/macosworld) | `benchmark` / `interactive-episode` | 202 tasks | GPT, Claude | [Primary](https://github.com/showlab/macosworld) |
| **OSUniverse** | 2025-05 | [24](https://github.com/agentsea/osuniverse) | `benchmark` / `interactive-episode` | Task suite spanning real desktop applications | GPT, Claude, Qwen | [Primary](https://arxiv.org/abs/2505.03570) · [Code](https://github.com/agentsea/osuniverse) |
| **WorldGUI** | 2025-02 | [125](https://github.com/showlab/WorldGUI) | `benchmark` / `interactive-episode` | 611 tasks | GPT, Claude, Qwen | [Primary](https://github.com/showlab/WorldGUI) |
| **WindowsAgentArena** | 2024-07 | [890](https://github.com/microsoft/WindowsAgentArena) | `benchmark` / `interactive-episode` | 154 tasks across 11 applications | GPT, Claude | [Primary](https://arxiv.org/abs/2409.08264) · [Code](https://github.com/microsoft/WindowsAgentArena) |
| **OSWorld** | 2024-04 | [3,106](https://github.com/xlang-ai/OSWorld) | `benchmark` / `interactive-episode` | 369 tasks | GPT, Claude, Qwen | [Primary](https://arxiv.org/abs/2404.07972) · [Code](https://github.com/xlang-ai/OSWorld) · [Leaderboard](https://os-world.github.io/) |

<details>
<summary><strong>Evaluation contracts: Desktop and hybrid computer use</strong></summary>

| Benchmark | Input question | Agent-visible input | Required output | Evaluation | Environment |
|---|---|---|---|---|---|
| **OSWorkerBench** | A realistic office workflow, optionally accompanied by one procedural demonstration. | Desktop screenshots, task instruction, and optional same/related-task demonstration. | Computer actions and persistent office artifacts. | Strict success and progress under matched target, environment, budget, and verifier. | Resettable office desktop environment. |
| **WeaveBench** | A real user workflow deliberately requiring GUI plus CLI/code in the same trajectory. | Rendered desktop state, terminal/code tools, dialogue, and task assets. | Interleaved GUI and CLI/code actions plus deliverables and evidence. | Trajectory-aware Agent-as-Judge PassRate; fabricated evidence is zeroed. | Real Ubuntu desktop inside deployed CLI-agent runtimes. |
| **DeskCraft** | A professional creative/engineering workflow, sometimes revised through user interaction. | Desktop screenshots, user dialogue, files, and action history. | GUI actions and saved/exported artifacts. | Task-specific execution checks plus standard and interactive completion reporting. | Live Ubuntu desktop with professional applications. |
| **OSWorld 2.0** | A long-horizon everyday or professional workflow with constraints, hidden state, and possible user interaction. | Screenshots, dialogue, action history, and optional batch tool calls. | GUI/computer actions and a completed persistent end state. | Binary completion and partial-progress score at a declared step budget. | Official resettable OSWorld V2 desktop release with gated task code/assets. |
| **MacArena** | A ported or native macOS task. | Screenshot and trajectory context. | Computer-control actions. | Execution-based task success with subset reporting. | Online macOS environment on Apple Silicon Virtualization.framework. |
| **MacAgentBench** | A real-world macOS desktop task. | Screenshot and agent history; framework-dependent tools. | GUI actions and, in supported agents, hybrid commands. | Deterministic rule-based multi-checkpoint scoring and Pass@1. | Containerized macOS VM, one isolated environment per task. |
| **GUI-vs-CLI** | The same desktop goal expressed for GUI-only or CLI-enabled execution. | Desktop state plus interface-specific task description. | GUI actions or command-line actions under the matched condition. | Shared task verifier, enabling interface comparison. | Unified resettable desktop environment. |
| **Cua-Bench** | A task contract with setup, agent, and evaluator components. | Environment observation defined by each task. | Computer-use actions and task-state changes. | Per-task evaluator result aggregated by benchmark version. | Cua virtual desktop/mobile sandboxes. |
| **WindowsWorld** | A professional cross-application Windows workflow grounded in one of 16 personas. | Screenshot, accessibility tree, screenshot+a11y, or set-of-mark. | PyAutoGUI or OSWorld Computer-13 actions. | Intermediate-checkpoint score and final completion; level-specific 15/25/40/20 step limits. | Windows 10/11 or Server VM under VMware. |
| **OS-Marathon** | Process a scalable collection of receipts or transcript rows through a recurring professional sub-workflow. | Desktop files, office/browser applications, screenshots, and task instruction. | Repeated GUI actions and a fully populated persistent artifact/system state. | Task completion across seven difficulty levels and seven executable environments. | OSWorld-derived desktop plus fully functional task-specific applications. |
| **PPTArena** | An instruction to edit or improve a presentation deck. | Source deck, editing instruction, and GUI or file tools. | Edited presentation artifact. | Instruction-following and visual-quality judges over the result. | Presentation editing via GUI actions and/or result upload. |
| **OSWorld-MCP** | An OSWorld-style task for which GUI actions and MCP tools may both be useful. | Screenshot, history, and an MCP tool catalog. | GUI actions, tool calls, or a mixture. | Task accuracy, tool-invocation rate, and average completion steps. | OSWorld desktop extended with real application MCP servers. |
| **OSWorld-Verified** | Repaired OSWorld natural-language desktop and web goals. | Agent observation mode and action history; leaderboard rows must disclose configuration. | Computer actions in the live VM. | Verified execution-based task success rate. | Updated OSWorld infrastructure with repaired tasks/evaluators and scalable AWS execution. |
| **macOSWorld** | A natural-language task in macOS applications. | macOS screenshots and action history. | Mouse and keyboard actions. | Execution-based task success. | macOS x86 virtual machine. |
| **OSUniverse** | An open-ended operating-system task. | Screenshot and optional structured computer state. | Computer-control actions. | Execution-based success and trajectory diagnostics. | Reproducible full operating-system environments. |
| **WorldGUI** | A desktop task spanning applications and operating-system interactions. | Screenshots and prior actions. | Mouse/keyboard computer actions. | Execution-based task success. | Realistic desktop applications in a resettable environment. |
| **WindowsAgentArena** | A natural-language Windows application workflow. | Screenshot and optional accessibility information plus history. | Mouse and keyboard actions through the Windows agent interface. | Task success from state-based evaluators. | Azure-hosted Windows 11 VM with real applications. |
| **OSWorld** | A natural-language goal requiring work in one or more real desktop or web applications. | Screenshot and optionally accessibility tree plus action history. | Mouse, keyboard, hotkey, scroll, wait, and optional computer-I/O actions. | Execution-based task success rate. | Resettable Ubuntu/Windows/macOS virtual machines with real applications. |

</details>

### Browser, web, and enterprise workflows

| Benchmark | Launch | Stars | Artifact / unit | Scale | Models reported | Primary artifacts |
|---|---:|---:|---|---|---|---|
| **SaaS-Bench** | 2026-05 | [96](https://github.com/UniPat-AI/SaaS-Bench) | `benchmark` / `long-horizon-workflow` | 106 tasks, 23 self-hosted SaaS apps, 6 professional domains | GPT, Claude, Qwen | [Primary](https://arxiv.org/abs/2605.15777) · [Code](https://github.com/UniPat-AI/SaaS-Bench) |
| **DocOS** | 2026-05 | [2](https://github.com/BUAA-IRIP-LLM/DocOS) | `benchmark` / `long-horizon-workflow` | 817 tasks | — | [Primary](https://github.com/BUAA-IRIP-LLM/DocOS) |
| **ClawBench** | 2026-04 | [585](https://github.com/TIGER-AI-Lab/ClawBench) | `benchmark` / `interactive-episode` | 283 tasks: v1 153 tasks/144 live sites and v2 130 tasks | GPT, Claude, Kimi, Qwen | [Primary](https://arxiv.org/abs/2604.08523) · [Code](https://github.com/TIGER-AI-Lab/ClawBench) |
| **PPT-Eval** | 2026-03 | [11](https://github.com/microsoft/ppteval) | `benchmark` / `long-horizon-workflow` | Versioned PowerPoint task registry | Claude | [Primary](https://github.com/microsoft/ppteval) |
| **WebArena-Verified** | 2025-12 | [51](https://github.com/ServiceNow/webarena-verified) | `benchmark` / `interactive-episode` | 812 audited tasks; 258-task hard subset | — | [Primary](https://github.com/ServiceNow/webarena-verified) |
| **SCUBA** | 2025-09-30 | [11](https://github.com/SalesforceAIResearch/SCUBA) | `benchmark` / `long-horizon-workflow` | Salesforce CRM task suites with zero-shot and demonstration-augmented splits | Claude, Qwen | [Primary](https://github.com/SalesforceAIResearch/SCUBA) |
| **Online-Mind2Web** | 2025-03 | [199](https://github.com/OSU-NLP-Group/Online-Mind2Web) | `benchmark` / `interactive-episode` | 300 maintained tasks across 136 live websites | GPT, Claude | [Primary](https://github.com/OSU-NLP-Group/Online-Mind2Web) |
| **WebCanvas** | 2024-06 | [280](https://github.com/iMeanAI/WebCanvas) | `benchmark` / `long-horizon-workflow` | Web tasks emphasizing visual and functional end states | GPT, Claude | [Primary](https://github.com/iMeanAI/WebCanvas) |
| **WorkArena** | 2024-02 | [268](https://github.com/ServiceNow/WorkArena) | `benchmark` / `interactive-episode` | 33 level-1 task templates with seeded variants | GPT, Claude | [Primary](https://arxiv.org/abs/2403.07718) · [Code](https://github.com/ServiceNow/WorkArena) |
| **WebVoyager** | 2024-01 | [1,122](https://github.com/MinorJerry/WebVoyager) | `benchmark` / `interactive-episode` | 643 tasks across 15 live websites in the original release | GPT, GLM, Qwen | [Primary](https://arxiv.org/abs/2401.13919) · [Code](https://github.com/MinorJerry/WebVoyager) |
| **VisualWebArena** | 2024-01 | [485](https://github.com/web-arena-x/visualwebarena) | `benchmark` / `interactive-episode` | 910 visually grounded web tasks | GPT, Claude, Qwen | [Primary](https://arxiv.org/abs/2401.13649) · [Code](https://github.com/web-arena-x/visualwebarena) |
| **WorkArena++** | 2024 | [268](https://github.com/ServiceNow/WorkArena) | `benchmark` / `long-horizon-workflow` | 341 level-2 and 341 level-3 compositional templates | GPT, Claude | [Primary](https://github.com/ServiceNow/WorkArena) |
| **WebArena** | 2023-07 | [1,587](https://github.com/web-arena-x/webarena) | `benchmark` / `interactive-episode` | 812 tasks across self-hosted realistic websites | GPT, Claude, Qwen | [Primary](https://arxiv.org/abs/2307.13854) · [Code](https://github.com/web-arena-x/webarena) |

<details>
<summary><strong>Evaluation contracts: Browser, web, and enterprise workflows</strong></summary>

| Benchmark | Input question | Agent-visible input | Required output | Evaluation | Environment |
|---|---|---|---|---|---|
| **SaaS-Bench** | A multi-step professional SaaS workflow in text-only or multimodal form. | Browser UI plus optional image/audio/PDF assets. | Browser actions that alter live application state. | Weighted verification checkpoints for strict completion and partial progress. | Dockerized self-hosted SaaS stacks on Linux. |
| **DocOS** | A long-tailed GUI task whose solution requires finding and using relevant official documentation. | Open web UI, searchable documentation, and task instruction. | Proactive search plus browser/GUI actions. | Interactive task success with difficulty breakdown. | Dynamic open-web environments. |
| **ClawBench** | A task on a real production website. | Live webpage view and action history. | Browser actions; final external write is intercepted to reduce harm. | Agentic evaluator against human references with five-layer trace recording. | Live websites, with Browserbase support and action interception. |
| **PPT-Eval** | A PowerPoint editing task. | Normalized source PPTX and a natural-language edit instruction. | Modified deck produced through PowerPoint Online GUI or a declared CLI track. | Task verifier and rubric-based visual checks. | Docker-sandboxed PowerPoint Online/OneDrive; separate CLI workspace track. |
| **WebArena-Verified** | An audited WebArena goal. | Browser trajectory or replayable network trace. | Browser actions and final web state. | Deterministic type-aware and structural evaluation without LLM judging. | WebArena websites plus offline network-trace replay. |
| **SCUBA** | A realistic Salesforce business workflow. | Browser or pixel desktop view of a provisioned Salesforce org. | Browser-use or computer-use actions that change CRM state. | Task-specific state verification and completion rate. | Salesforce Developer Org plus browser-use or remote desktop runner. |
| **Online-Mind2Web** | A real-world web task in clothing, food, housing, transportation, or another daily domain. | Live website observation and interaction history. | Browser actions and final task outcome. | Human evaluation or WebJudge outcome evaluation with disclosed judge version. | Changing public websites; invalid tasks are periodically replaced. |
| **WebCanvas** | A browser task requiring creation or manipulation of web content. | Screenshot, instruction, and browser state. | Browser actions and a rendered end artifact/state. | Task-specific functional and visual evaluation. | Interactive browser applications. |
| **WorkArena** | A routine knowledge-worker task in ServiceNow. | Rendered ServiceNow UI and/or accessibility tree. | Browser actions that create the requested enterprise state. | Task-specific validation and success rate. | Provisioned ServiceNow instance through BrowserGym. |
| **WebVoyager** | A real-world website instruction requiring visual browsing. | Screenshot, set-of-mark overlay, and interaction history. | Mouse/keyboard browser actions and final answer. | Automatic multimodal judge with human validation. | Live public websites through Selenium/Chrome. |
| **VisualWebArena** | A web goal whose solution depends on rendered visual content. | Webpage screenshot with optional accessibility/DOM context. | Browser actions and final answer/state. | Task-specific functional success plus visual/answer checks. | Self-hosted visually rich websites. |
| **WorkArena++** | A compositional knowledge-work goal requiring planning across ServiceNow modules. | Rendered ServiceNow UI and task instruction. | Multi-step browser actions and verified enterprise state. | Task-specific success with compositional-level breakdown. | Provisioned ServiceNow instance through BrowserGym. |
| **WebArena** | A natural-language goal involving one or more websites. | Rendered page and/or accessibility/DOM observation plus history. | Browser navigation, click, type, select, and stop actions. | Task-specific functional success and exact/URL checks. | Self-hosted e-commerce, social, map, forum, GitLab, and related sites. |

</details>

### Mobile computer use

| Benchmark | Launch | Stars | Artifact / unit | Scale | Models reported | Primary artifacts |
|---|---:|---:|---|---|---|---|
| **MobilePA-Bench** | 2026-08-24 | N/A | `benchmark` / `interactive-episode` | 212 realistic mobile tools across 13 functional domains | — | [Primary](https://arxiv.org/abs/2608.23035) |
| **LivingScreen** | 2026-06 | [5](https://github.com/BITHLP/LivingScreen) | `benchmark` / `interactive-episode` | Short-video-platform tasks with dynamic living-screen content | — | [Primary](https://arxiv.org/abs/2606.04701) · [Code](https://github.com/BITHLP/LivingScreen) |
| **AndroidDaily** | 2026-05-26 | N/A | `benchmark` / `long-horizon-workflow` | 350 tasks across 94 high-frequency closed-source Android applications | — | [Primary](https://arxiv.org/abs/2605.27761) |
| **SimuWoB** | 2026-05 | N/A | `benchmark` / `interactive-episode` | 120 synthetic mobile GUI tasks | — | [Primary](https://arxiv.org/abs/2605.25160) |
| **MobileGym-Bench** | 2026-05 | [773](https://github.com/Purewhiter/mobilegym) | `benchmark` / `interactive-episode` | 416 parameterized templates: 256 test and 160 train, across 28 simulated apps | Qwen | [Primary](https://arxiv.org/abs/2605.26114) · [Code](https://github.com/Purewhiter/mobilegym) · [Leaderboard](https://mobilegym.dev/) |
| **VenusBench-Mobile** | 2026-04 | [1,010](https://github.com/inclusionAI/UI-Venus) | `benchmark` / `interactive-episode` | User-intent-driven online task collection with capability annotations | GPT, Claude, Qwen | [Primary](https://arxiv.org/abs/2604.06182) · [Code](https://github.com/inclusionAI/UI-Venus/tree/VenusBench-Mobile) |
| **MemGUI-Bench** | 2026-02-03 | [48](https://github.com/lgy0404/MemGUI-Bench) | `benchmark` / `long-horizon-workflow` | Dynamic long-horizon mobile task suite with memory-focused splits | Kimi, Qwen | [Primary](https://arxiv.org/abs/2602.06075) · [Code](https://github.com/lgy0404/MemGUI-Bench) |
| **MobileBench-OL** | 2026-02 | [13](https://github.com/xiaomi-research/mobilebench-ol) | `benchmark` / `interactive-episode` | 1,080 Chinese tasks across 80 applications | GPT, Claude, Qwen | [Primary](https://aclanthology.org/2026.findings-acl.668/) · [Code](https://github.com/xiaomi-research/mobilebench-ol) |
| **AmbiBench** | 2026-02 | [0](https://github.com/YanbeiJiang/ambibench) | `benchmark` / `long-horizon-workflow` | 240 tasks across 25 applications and four instruction-clarity levels | — | [Primary](https://arxiv.org/abs/2602.11750) · [Code](https://github.com/YanbeiJiang/ambibench) |
| **MobileWorld** | 2025-12-23 | [258](https://github.com/Tongyi-MAI/MobileWorld) | `benchmark` / `long-horizon-workflow` | 201 tasks across 20 mobile applications | GPT, Claude, Kimi, Qwen | [Primary](https://github.com/Tongyi-MAI/MobileWorld) · [Leaderboard](https://tongyi-mai.github.io/MobileWorld/) |
| **MAS-Bench** | 2025-09 | [11](https://github.com/Pengxiang-zhao/MAS-Bench) | `benchmark` / `interactive-episode` | Shortcut-augmented hybrid mobile tasks | GLM, Qwen | [Primary](https://arxiv.org/abs/2509.06477) · [Code](https://github.com/Pengxiang-zhao/MAS-Bench) |
| **MobileAgentBench** | 2024-06 | [37](https://github.com/MobileAgentBench/mobile-agent-bench) | `benchmark` / `interactive-episode` | 100 tasks across 10 open-source Android applications | GPT, Qwen | [Primary](https://arxiv.org/abs/2406.08184) · [Code](https://github.com/MobileAgentBench/mobile-agent-bench) |
| **AndroidWorld** | 2024-05 | [857](https://github.com/google-research/android_world) | `benchmark` / `interactive-episode` | 116 parameterized tasks across 20 applications | GPT, GLM, Qwen | [Primary](https://arxiv.org/abs/2405.14573) · [Code](https://github.com/google-research/android_world) |

<details>
<summary><strong>Evaluation contracts: Mobile computer use</strong></summary>

| Benchmark | Input question | Agent-visible input | Required output | Evaluation | Environment |
|---|---|---|---|---|---|
| **MobilePA-Bench** | A complex stateful mobile-planning request requiring tools, ordering, permissions, memory, skills, or sub-agent delegation. | Structured tool catalog, live application database feedback, user profile/memory, and task instruction. | Ordered tool calls, sub-agent delegations, skill invocations, and final verified state. | Evidence-based state verification under strict tool-order, permission, and runtime-error conditions. | Executable interactive function-calling sandbox with live application databases. |
| **LivingScreen** | A task requiring understanding and acting on continually changing short-video feeds. | Live rendered feed, temporal content, instruction, and history. | GUI actions and task result. | Task-specific success with temporal/cross-source capability breakdowns. | Reproducible Flask-hosted short-video platform simulation. |
| **AndroidDaily** | A realistic daily-use request in transportation, shopping, local services, entertainment, creation, social media, or utilities. | Live closed-source Android GUI, instruction, and visual trajectory. | Long-horizon mobile GUI trajectory and completed user-visible result. | GRADE process-aware success using operational obligations, output quality, and negative constraints. | Real-world closed-source Android applications without privileged internal state. |
| **SimuWoB** | A mobile-style task with controlled type and difficulty. | High-fidelity mobile UI rendered as a webpage plus instruction. | GUI actions. | Automatically generated valid rewards and task success. | Backend-free synthetic webpage environments accessible by URL. |
| **MobileGym-Bench** | An everyday mobile task, including structured answer, navigation, payment, and high-risk variants. | Browser-hosted mobile UI, instruction, and action history. | Mobile-style GUI actions plus a typed AnswerSheet when required. | Deterministic state-based Success Rate, Progress Rate, False Complete, and Unexpected Side Effects. | Fully programmable browser-hosted mobile simulator; hundreds of parallel instances per server. |
| **VenusBench-Mobile** | A realistic user-centric mobile request under live environment variation. | Mobile screenshot, instruction, and trajectory context. | Mobile GUI actions. | Task outcome plus perception, reasoning, memory, and robustness diagnostics. | Online real mobile applications with controlled variations. |
| **MemGUI-Bench** | A mobile goal whose relevant state changes or must be remembered over a long trajectory. | Mobile screenshot, history, and previously observed dynamic state. | Mobile actions and memory-dependent completion. | Task success plus memory/capability diagnostics by difficulty. | MobileWorld-style resettable Android runtime. |
| **MobileBench-OL** | A dynamic Chinese mobile task with long-horizon and GUI-noise variants. | Mobile screenshot, instruction, and action history. | Mobile GUI actions. | State-based task success with reasoning, robustness, horizon, and noise breakdowns. | Resettable online Android environment. |
| **AmbiBench** | A detailed, standard, incomplete, or ambiguous mobile request that may require clarification. | Mobile UI, user instruction, dialogue, and history. | Clarifying questions plus mobile GUI actions. | MUSE judge: outcome effectiveness, execution quality, and interaction quality; human correlation audit. | Dynamic real mobile applications. |
| **MobileWorld** | A long-horizon mobile task, possibly cross-app, user-interactive, or MCP-augmented. | Mobile screen, dialogue, history, and optional MCP tools. | GUI actions, user questions, and/or MCP calls. | Deterministic task success with GUI-only and user-interaction tracks. | Containerized reproducible Android environment; real-device support. |
| **MAS-Bench** | A mobile task solvable through GUI actions, Android shortcuts/APIs, or a mixture. | Mobile UI plus discovered shortcut/action catalog. | GUI actions and shortcut/API invocations. | Task success and shortcut-use analysis. | Android apps with a unified GUI-shortcut hybrid interface. |
| **MobileAgentBench** | A mobile app task requiring perception, reasoning, planning, and interaction. | Android screenshots and action history. | Mobile GUI actions. | Task completion and capability-dimension diagnostics. | Resettable Android emulator. |
| **AndroidWorld** | A natural-language mobile task whose parameters are sampled at reset. | Android screenshot and/or accessibility representation plus history. | Tap, type, swipe, navigation, wait, and completion actions. | Task-specific state-based success rate. | Resettable Android emulator with open-source apps. |

</details>

### GUI grounding and offline action prediction

| Benchmark | Launch | Stars | Artifact / unit | Scale | Models reported | Primary artifacts |
|---|---:|---:|---|---|---|---|
| **MementoGUI-Bench** | 2026-05-18 | [0](https://github.com/zzzmyyzeng/MementoGUI) | `benchmark` / `offline-trajectory` | Long-horizon GUI trajectories curated for memory-control evaluation | — | [Primary](https://arxiv.org/abs/2605.18652) · [Code](https://github.com/zzzmyyzeng/MementoGUI) |
| **OmniGUI** | 2026-05 | [19](https://github.com/omni-gui/OmniGUI) | `benchmark` / `offline-trajectory` | 708 expert episodes, 2,572 action steps, 29 real apps, Chinese and English | Qwen | [Primary](https://arxiv.org/abs/2605.18758) · [Code](https://github.com/omni-gui/OmniGUI) |
| **PSPA-Bench** | 2026-03 | [0](https://github.com/Sirius11311/PSPA-Bench-ICLR2026) | `benchmark` / `offline-trajectory` | More than 12,855 personalized instructions, 10 scenarios, 22 apps | — | [Primary](https://arxiv.org/abs/2603.29318) · [Code](https://github.com/Sirius11311/PSPA-Bench-ICLR2026) |
| **MedSPOT** | 2026-03 | [9](https://github.com/Tajamul21/MedSPOT) | `benchmark` / `offline-trajectory` | 216 task videos, 597 annotated keyframes, 10 medical-imaging applications | GPT, Qwen | [Primary](https://arxiv.org/abs/2603.19993) · [Code](https://github.com/Tajamul21/MedSPOT) |
| **GUI-CEval** | 2026-03 | N/A | `benchmark` / `offline-trajectory` | Hierarchical Chinese mobile GUI task suite | Qwen | [Primary](https://arxiv.org/abs/2603.15039) |
| **AgentCLUE-CUA** | 2026 | N/A | `benchmark` / `offline-trajectory` | Chinese offline CUA suite covering grounding, information processing, and agent action | GLM, Qwen | [Primary](https://www.cluebenchmarks.com/superclue_2025) |
| **FedGUI** | 2025-12 | [4](https://github.com/wwh0411/FedGUI) | `benchmark` / `offline-trajectory` | Data from more than 900 mobile apps, 40 desktop apps, and 200 websites | Qwen | [Primary](https://github.com/wwh0411/FedGUI) |
| **UI-Vision** | 2025-03 | [33](https://github.com/uivision/UI-Vision) | `benchmark` / `offline-trajectory` | Desktop screenshots from 83 applications in 6 categories | GPT, Claude, Qwen | [Primary](https://github.com/uivision/UI-Vision) |
| **ScreenSpot-Pro** | 2025-01 | [391](https://github.com/likaixin2000/ScreenSpot-Pro-GUI-Grounding) | `benchmark` / `static-grounding` | 1,581 high-resolution screenshots and 4,304 instructions from 23 professional applications | GPT, Claude, Qwen | [Primary](https://arxiv.org/abs/2501.12326) · [Code](https://github.com/likaixin2000/ScreenSpot-Pro-GUI-Grounding) |
| **ScreenSpot-V2** | 2024-10 | [453](https://github.com/OS-Copilot/OS-Atlas) | `offline-dataset` / `static-grounding` | Re-annotated and harder ScreenSpot grounding set | GPT, Claude, Qwen | [Primary](https://github.com/OS-Copilot/OS-Atlas) |
| **GUI Odyssey** | 2024-06 | [160](https://github.com/OpenGVLab/GUI-Odyssey) | `offline-dataset` / `offline-trajectory` | 8,834 episodes, 6 devices, 212 apps, about 1,400 app combinations | Qwen | [Primary](https://arxiv.org/abs/2406.08451) · [Code](https://github.com/OpenGVLab/GUI-Odyssey) |
| **AndroidControl** | 2024-06 | N/A | `offline-dataset` / `offline-trajectory` | 15,000 demonstrations and more than 800 applications in the source dataset | Qwen, GLM | [Primary](https://arxiv.org/abs/2406.03679) |
| **VisualWebBench** | 2024-04 | [68](https://github.com/VisualWebBench/VisualWebBench) | `benchmark` / `static-grounding` | Seven web-understanding tasks covering perception, grounding, and action | GPT, Claude, Qwen | [Primary](https://github.com/VisualWebBench/VisualWebBench) |
| **ScreenSpot** | 2024-01 | [494](https://github.com/njucckevin/SeeClick) | `offline-dataset` / `static-grounding` | 1,200 screenshot-instruction grounding examples | GPT, Claude, Qwen | [Primary](https://arxiv.org/abs/2401.10935) · [Code](https://github.com/njucckevin/SeeClick) |
| **Mind2Web** | 2023-04 | [1,021](https://github.com/OSU-NLP-Group/Mind2Web) | `offline-dataset` / `offline-trajectory` | 2,350 tasks across 137 websites and 31 domains | GPT, Qwen | [Primary](https://arxiv.org/abs/2306.06070) · [Code](https://github.com/OSU-NLP-Group/Mind2Web) |

<details>
<summary><strong>Evaluation contracts: GUI grounding and offline action prediction</strong></summary>

| Benchmark | Input question | Agent-visible input | Required output | Evaluation | Environment |
|---|---|---|---|---|---|
| **MementoGUI-Bench** | Select, compress, retrieve, and use task-relevant multimodal history to choose the next GUI action. | Long screenshot/action history with text and ROI-level visual evidence. | Next action plus working/episodic memory decisions. | MLLM-based semantic action matching, task progress, and memory consistency. | Offline long-horizon GUI trajectories, evaluated alongside GUI Odyssey and MM-Mind2Web. |
| **OmniGUI** | Predict the next action in an omni-modal smartphone episode. | Interleaved screenshots, audio, short video, text instruction, and action history. | Next TAP/TYPE or other mobile action. | Step-level accuracy across localization, semantics, cross-modal discrimination, temporal reasoning, and instant response. | Offline expert-demonstrated smartphone trajectories. |
| **PSPA-Bench** | A smartphone task conditioned on a user's behavior or preference. | Mobile state, personalized instruction, and user-specific context. | Personalized action process. | Structure-aware process evaluation over personalization capabilities. | Curated smartphone GUI task trajectories. |
| **MedSPOT** | Execute a two- or three-step sequential grounding task in medical imaging software. | Medical GUI screenshot/video context plus instruction and prior actions. | Grounded click/action sequence. | Task Completion Accuracy, Step Hit Rate, Step-1 Accuracy; terminate after the first error. | Offline trajectories from professional medical imaging GUIs. |
| **GUI-CEval** | Perceive, decide, reflect on, or evaluate an action in a Chinese mobile GUI trajectory. | Screenshot, Chinese instruction, and action context. | Grounding, next action, reflection, or post-action judgment. | Hierarchical capability accuracies and aggregate score. | Offline Chinese mobile GUI states and trajectories. |
| **AgentCLUE-CUA** | A Chinese GUI grounding, information-processing, or next-action prompt. | GUI screenshot and Chinese task prompt. | Grounded element, answer, or GUI action. | Overall score plus Grounding, Information Processing, and Agent sub-scores. | Offline cross-platform GUI samples. |
| **FedGUI** | Predict actions across heterogeneous platforms, devices, operating systems, and data sources. | Cross-platform screenshot/state and instruction. | One of 17 unified action types and its arguments. | Three action-level metrics plus heterogeneity/federated-learning breakdowns. | Decentralized offline GUI datasets across mobile, desktop, and web clients. |
| **UI-Vision** | Ground an element/layout or predict the next GUI action. | Desktop screenshot plus task-specific prompt. | Element/layout grounding or action prediction. | Task-specific grounding and action-prediction accuracy. | Offline real-world desktop screenshots. |
| **ScreenSpot-Pro** | A professional GUI grounding instruction. | High-resolution screenshot plus instruction. | Target point or box. | Grounding accuracy, including application/category breakdowns. | Offline screenshots from professional desktop software. |
| **ScreenSpot-V2** | Identify the target GUI element from a natural-language instruction. | Screenshot plus target description. | Click coordinate or bounding box. | Click/grounding accuracy under the V2 annotations. | Offline GUI screenshots. |
| **GUI Odyssey** | A cross-app mobile navigation instruction paired with an expert trajectory. | Screenshot and action history. | Next mobile GUI action or full trajectory. | Action prediction and episode/task-level success on held-out splits. | Offline Android trajectories across devices and applications. |
| **AndroidControl** | A language instruction paired with an Android interaction trajectory. | Screenshot, instruction, and action history. | Next structured mobile action. | Action-level grounding/type accuracy and trajectory metrics. | Offline Android screenshots and demonstrations. |
| **VisualWebBench** | Caption, OCR, QA, element grounding, or action-related prompt over a webpage screenshot. | Rendered webpage screenshot and prompt. | Text answer, grounded location, or action. | Task-specific accuracy and aggregate score. | Offline real-world webpage screenshots. |
| **ScreenSpot** | A short instruction naming the GUI element to interact with. | One screenshot plus instruction. | Click point or bounding box. | Click accuracy: predicted point lies inside the target box. | Offline screenshots from mobile, desktop, and web GUIs. |
| **Mind2Web** | An open-ended language instruction paired with a recorded website trajectory. | HTML candidates, DOM context, screenshot in the multimodal release, and action history. | Target element and CLICK/TYPE/SELECT operation for each step. | Element accuracy, operation F1, step success, and task success; macro averaging is the paper-comparable setting. | Offline snapshots from live real-world websites. |

</details>

### Safety, privacy, prompt injection, and robustness

| Benchmark | Launch | Stars | Artifact / unit | Scale | Models reported | Primary artifacts |
|---|---:|---:|---|---|---|---|
| **OSGuard** | 2026-06 | N/A | `benchmark` / `safety-adversarial` | Action-level safety items plus OSWorld-derived execution variants | — | [Primary](https://arxiv.org/abs/2606.15034) |
| **GUIGuard-Bench** | 2026-01 | N/A | `benchmark` / `safety-adversarial` | Versioned artifacts: paper 630 trajectories/13,830 screenshots; project seed 241/4,080; public eval 121 trajectories | — | [Primary](https://arxiv.org/abs/2601.18842) |
| **CUAHarm** | 2025-08 | [1](https://github.com/db-ol/CUAHarm) | `benchmark` / `safety-adversarial` | 104 security-related tasks, including a 52-task harmful computer-use focus set | GPT, Claude | [Primary](https://arxiv.org/abs/2508.00935) · [Code](https://github.com/db-ol/CUAHarm) |
| **VPI-Bench** | 2025-06 | [26](https://github.com/cua-framework/agents) | `benchmark` / `safety-adversarial` | 306 cases across 5 platforms | GPT, Claude, Qwen | [Primary](https://arxiv.org/abs/2506.02456) · [Code](https://github.com/cua-framework/agents) |
| **OS-Harm** | 2025-06 | [71](https://github.com/tml-epfl/os-harm) | `benchmark` / `safety-adversarial` | 150 tasks | GPT, Claude | [Primary](https://arxiv.org/abs/2506.14866) · [Code](https://github.com/tml-epfl/os-harm) |
| **GUI-Robust** | 2025-06 | [13](https://github.com/chessbean1/GUI-Robust) | `benchmark` / `safety-adversarial` | Step-level and task-level GUI anomaly cases | GPT, Claude, Qwen | [Primary](https://arxiv.org/abs/2506.14477) · [Code](https://github.com/chessbean1/GUI-Robust) |
| **RTC-Bench / RedTeamCUA** | 2025-05 | [60](https://github.com/OSU-NLP-Group/RedTeamCUA) | `benchmark` / `safety-adversarial` | 864 examples across OSWorld, WebArena, and TheAgentCompany settings | GPT, Claude | [Primary](https://arxiv.org/abs/2505.21936) · [Code](https://github.com/OSU-NLP-Group/RedTeamCUA) |

<details>
<summary><strong>Evaluation contracts: Safety, privacy, prompt injection, and robustness</strong></summary>

| Benchmark | Input question | Agent-visible input | Required output | Evaluation | Environment |
|---|---|---|---|---|---|
| **OSGuard** | Decide whether an action is allowed, unrelated, or unsafe, then execute tasks with explicit safety invariants. | Desktop observation, user goal, candidate/history actions, and hazard context. | Safety classification and/or safe computer-action trajectory. | Action-level safety accuracy plus task utility and invariant violations. | OSWorld-derived executable desktop tasks with injected hazards. |
| **GUIGuard-Bench** | A GUI task containing privacy-sensitive information or action boundaries. | GUI screenshots, task context, and privacy labels. | Action prediction or trajectory with privacy-aware behavior. | Privacy-risk and capability measures at action and trajectory levels. | Cross-platform PC and Android trajectories. |
| **CUAHarm** | A potentially harmful computer-use request. | Desktop state and harmful or dual-use instruction. | Action trajectory, refusal, or safe response. | Harmful completion, refusal, and utility/safety trade-off. | Controlled desktop computer-use environment. |
| **VPI-Bench** | A legitimate GUI task whose screenshot contains a visual prompt injection. | Screenshot, user goal, and visually embedded attacker instruction. | GUI action trajectory. | Attempted attack rate and successful attack rate. | Cross-platform CUA evaluation framework. |
| **OS-Harm** | A deliberate-misuse, prompt-injection, or model-misbehavior task in an OSWorld-style environment. | Desktop observation, task request, and possible adversarial content. | Computer actions, refusal, or safe alternative. | Task accuracy and safety judgment; report helpfulness/safety jointly. | OSWorld-based real desktop environment. |
| **GUI-Robust** | Continue or recover when a realistic GUI anomaly disrupts the expected trajectory. | Perturbed GUI state, instruction, and action history. | Recovery action sequence. | Action accuracy, coordinate accuracy, task success, and recovery diagnostics. | Offline and executable GUI perturbation settings. |
| **RTC-Bench / RedTeamCUA** | A benign task exposed to an indirect prompt injection targeting confidentiality, integrity, or availability. | Normal agent goal plus adversarial content embedded in the GUI/environment. | Computer/web actions, ideally ignoring the injection. | Attack success and policy/goal violation across CIA categories. | Hybrid desktop, web, and enterprise benchmark environments. |

</details>

### Arenas and evaluation suites

| Benchmark | Launch | Stars | Artifact / unit | Scale | Models reported | Primary artifacts |
|---|---:|---:|---|---|---|---|
| **GUIEvalKit** | 2025-09 | [25](https://github.com/xiaomi-research/guievalkit) | `evaluation-suite` / `offline-trajectory` | Unified evaluation for AndroidControl, CAGUI, GUI Odyssey, AiTZ, and additional GUI datasets | GLM, Qwen | [Primary](https://github.com/xiaomi-research/guievalkit) |
| **Computer Agent Arena** | 2025-04 | [67](https://github.com/xlang-ai/computer-agent-arena) | `arena` / `arena-preference` | Open crowdsourced pairwise trajectory comparisons | GPT, Claude, Qwen | [Primary](https://github.com/xlang-ai/computer-agent-arena) |
| **ScreenSuite** | 2025-02 | [145](https://github.com/huggingface/screensuite) | `evaluation-suite` / `offline-trajectory` | Unified runners for ScreenSpot family, VisualWebBench, Mind2Web variants, AndroidControl, AndroidWorld, OSWorld, and others | — | [Primary](https://github.com/huggingface/screensuite) |
| **BrowserGym** | 2024-02 | [1,329](https://github.com/ServiceNow/BrowserGym) | `evaluation-suite` / `interactive-episode` | Unified harness covering MiniWoB++, WebArena, VisualWebArena, WorkArena, WebLINX, and others | — | [Primary](https://github.com/ServiceNow/BrowserGym) |

<details>
<summary><strong>Evaluation contracts: Arenas and evaluation suites</strong></summary>

| Benchmark | Input question | Agent-visible input | Required output | Evaluation | Environment |
|---|---|---|---|---|---|
| **GUIEvalKit** | Inherited from each component dataset. | Normalized screenshot, instruction, and history. | Normalized GUI action. | Component action/grounding metrics with common runners. | Offline GUI datasets under a shared inference toolchain. |
| **Computer Agent Arena** | A user-submitted computer task presented to two agents. | Live Ubuntu or Windows desktop observations. | Two agent trajectories/outcomes for human comparison. | Pairwise human preference aggregated into Elo-style ratings. | Open desktop arena with Ubuntu and Windows backends. |
| **ScreenSuite** | Inherited from the component benchmark. | Normalized benchmark-specific GUI observation. | Normalized grounding or agent action. | Inherited component metric under a common model-evaluation harness. | Offline datasets and selected live BrowserGym/Android/desktop environments. |
| **BrowserGym** | Inherited from each hosted benchmark. | Unified browser observations and chat context. | Unified browser action space. | Inherited benchmark metrics under a common experiment API. | Playwright browser with benchmark-specific backends. |

</details>

## Integrity and maintenance notes

- Live-web results age when sites, authentication, CAPTCHAs, or task validity change. Use a dated task manifest.
- Shared-repository stars describe the host method/toolkit, not benchmark popularity. Repository scope is preserved in the JSON.
- A zero-star repository is a verified numeric zero on the snapshot date; `N/A` means no verified official GitHub repository.
- Offline action accuracy tests perception/policy imitation; it does not establish live end-to-end task success.
- LLM/VLM judges require their exact model, prompt, evidence access, and human-agreement audit.
- Safety benchmarks should report both task utility and unsafe-action/attack success; refusal alone is not general computer-use competence.

## Machine-readable source

Every row above is generated from [`data/cua-gui-benchmarks.json`](../data/cua-gui-benchmarks.json). CI validates required task contracts, artifact labels, launch sources, star snapshots, evaluation-unit vocabulary, and five-family coverage.
