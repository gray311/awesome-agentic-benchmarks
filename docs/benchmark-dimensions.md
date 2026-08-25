# Benchmark Dimensions

Dimensions classify **what a benchmark evaluates**. Training techniques such as SFT, DPO, GRPO, RLHF, LoRA, and distillation are not top-level dimensions; they are methods an agent may use inside a benchmark, especially a post-training benchmark.

For scientific discovery, dimension, task provenance, and evaluated method are separate: `mathematics-discovery` is a dimension, **Erdős minimum overlap** is a task, **SimpleTES** is an evaluated system/task packager, and **EFT** is a training method.

| Dimension ID | Display name | Definition | Example benchmarks |
|---|---|---|---|
| `coding-software-engineering` | Coding & Software Engineering | Repository editing, issue resolution, debugging, tests, and terminal work | SWE-bench, Terminal-Bench, TerminalWorld, SWE Refactor Bench |
| `machine-learning-engineering` | Machine Learning Engineering | Build and optimize ML systems against a defined dataset and objective | MLE-bench, MLAgentBench, ML-Dev-Bench, DSBench |
| `post-training` | Post-Training | Improve a provided base model under a bounded training and evaluation budget | PostTrainBench, RSI Bench post-training tasks |
| `open-ended-ai-r-and-d` | Open-Ended AI R&D | Propose, implement, and validate AI research improvements | AI4AI-Bench, RSI Bench, RE-Bench, MLR-Bench |
| `agent-harness-improvement` | Agent & Harness Improvement | Modify an agent's own scaffold, memory, skills, or reusable procedures and test transfer to held-out tasks | RSIBench, LongWoF-Bench |
| `scientific-discovery` | Scientific Discovery | Solve research problems in biology, chemistry, physics, medicine, Earth science, materials, or scientific ML | NatureBench, EarthVerse, SciAgentArena, ScienceAgentBench |
| `interactive-world-discovery` | Interactive World Discovery | Infer unfamiliar dynamics, rules, objectives, and strategies from action-conditioned feedback rather than a complete natural-language specification | ARC-AGI-3, DiG-bench, EdgeBench, DiscoveryWorld |
| `paper-reproduction` | Paper Reproduction | Reconstruct code, environments, experiments, and results from research papers | PaperBench, CORE-Bench, SUPER, ResearchCodeBench, SciReplicate-Bench |
| `data-science-analytics` | Data Science & Analytics | Analyze structured data, write SQL, create visualizations, and produce evidence-backed conclusions | DataSciBench, DABench, InfiAgent-DABench, BixBench |
| `web-research-browsing` | Web Research & Browsing | Locate, verify, and synthesize information through web interaction | BrowseComp, WebArena, VisualWebArena, ResearchArena, GAIA |
| `computer-use-gui` | Computer Use & GUI Interaction | Ground controls and complete workflows in desktop, browser, mobile, and hybrid GUI+CLI/MCP environments | OSWorld 2.0, WeaveBench, MobileWorld, ScreenSpot-Pro, WindowsWorld |
| `tool-use` | Tool Use & Customer Interaction | Select and call APIs or tools while following stateful policies | BFCL, ToolBench, tau-bench, tau2-bench, ToolSandbox, MCP-Atlas |
| `professional-enterprise-work` | Professional & Enterprise Work | Complete economically valuable office and knowledge-work workflows | GDPval, TheAgentCompany, WorkArena, SpreadsheetBench 2, APEX-Agents |
| `multi-agent` | Multi-Agent Coordination | Coordinate, delegate, negotiate, or compete across multiple agents | MultiAgentBench, GAMA-Bench, Collab-Overcooked, SOTOPIA |
| `safety-security` | Safety & Security | Measure harmful actions, prompt injection, compromised tools, malicious skills, cyber capability, permissions, and control | SkillSafetyBench, TRUST-Bench, AgentLAB, TAMAS, ST-WebAgentBench |
| `evaluation-integrity` | Evaluation Integrity & Reward Hacking | Test whether success is genuine, whether verifiers can be exploited, and whether judges remain reliable under leakage or manipulation | HVTB, CatchBench |
| `embodied-robotics` | Embodied Agents & Robotics | Navigate and manipulate physical or simulated environments | ALFWorld, EmbodiedBench, Habitat, VirtualHome, RoboBench |
| `general-agent` | General Agent Capability | Test broad combinations of planning, reasoning, tools, and long-horizon execution | AgentBench, OmniaBench, Agents' Last Exam, AGENCYBENCH |

## AI4AI hierarchy

AI4AI is an umbrella rather than a mutually exclusive flat dimension:

```text
AI R&D / AI4AI
├── Machine Learning Engineering
├── Data and Pre-Training
├── Post-Training
├── Model Architecture and Algorithm Discovery
├── Evaluation and Reward Design
├── Agent and Harness Improvement
├── Evaluation Integrity and Control
└── AI Research Reproduction
```

Each benchmark receives exactly one `primary_dimension`, zero or more `secondary_dimensions`, and multiple orthogonal `capabilities`. For example, NatureBench is primarily `scientific-discovery`; coding and experimentation are capabilities rather than duplicate top-level classifications.

## Scientific-discovery task domains

These domain labels classify individual problems in [data/discovery-tasks.json](../data/discovery-tasks.json):

| Task domain | Object being discovered | Example tasks |
|---|---|---|
| `quantum-compilation` | Hardware-aware routing or scheduling policy | Superconducting qubit routing; zoned neutral-atom compilation |
| `astrodynamics` | Feasible low-cost mission trajectory | Mariner 10; Voyager 2; Galileo; Cassini; Rosetta |
| `scientific-algorithms` | Faster or more accurate scientific computation | LASSO path solver; ZAPBench forecasting; single-cell denoising |
| `ai-foundations` | Faster AI systems or predictive laws of model behavior | GPU kernels; scaling-law discovery |
| `mathematics-discovery` | Extremal, analytic, geometric, or combinatorial construction | Erdős overlap; autocorrelation inequalities; circle packing; Hadamard determinant |
