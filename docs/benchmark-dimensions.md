# Benchmark Dimensions

Dimensions classify **what a benchmark evaluates**. Training techniques such as SFT, DPO, GRPO, RLHF, LoRA, and distillation are not top-level dimensions; they are methods an agent may use inside a benchmark, especially a post-training benchmark.

| Dimension ID | Display name | Definition | Example benchmarks |
|---|---|---|---|
| `coding-software-engineering` | Coding & Software Engineering | Repository editing, issue resolution, debugging, tests, and terminal work | SWE-bench, Terminal-Bench, SWE-Lancer, Multi-SWE-bench |
| `machine-learning-engineering` | Machine Learning Engineering | Build and optimize ML systems against a defined dataset and objective | MLE-bench, MLAgentBench, ML-Dev-Bench, DSBench |
| `post-training` | Post-Training | Improve a provided base model under a bounded training and evaluation budget | PostTrainBench, RSI Bench |
| `open-ended-ai-r-and-d` | Open-Ended AI R&D | Propose, implement, and validate AI research improvements | RE-Bench, MLR-Bench, MLRC-Bench, EXP-Bench, MLGym |
| `scientific-discovery` | Scientific Discovery | Solve research problems in biology, chemistry, physics, medicine, materials, or scientific ML | NatureBench, ScienceAgentBench, DiscoveryBench, LAB-Bench, SciCode |
| `paper-reproduction` | Paper Reproduction | Reconstruct code, environments, experiments, and results from research papers | PaperBench, CORE-Bench, SUPER, ResearchCodeBench, SciReplicate-Bench |
| `data-science-analytics` | Data Science & Analytics | Analyze structured data, write SQL, create visualizations, and produce evidence-backed conclusions | DataSciBench, DABench, InfiAgent-DABench, BixBench |
| `web-research-browsing` | Web Research & Browsing | Locate, verify, and synthesize information through web interaction | BrowseComp, WebArena, VisualWebArena, ResearchArena, GAIA |
| `computer-use-daily-life` | Computer Use & Daily Life | Complete everyday workflows in desktop, mobile, and browser environments | OSWorld, AndroidWorld, WindowsAgentArena, AssistantBench, TravelPlanner, WebShop |
| `tool-use` | Tool Use & Customer Interaction | Select and call APIs or tools while following stateful policies | BFCL, ToolBench, tau-bench, tau2-bench, ToolSandbox, MCP-Atlas |
| `professional-enterprise-work` | Professional & Enterprise Work | Complete economically valuable office and knowledge-work workflows | GDPval, TheAgentCompany, WorkArena, SpreadsheetBench 2, APEX-Agents |
| `multi-agent` | Multi-Agent Coordination | Coordinate, delegate, negotiate, or compete across multiple agents | MultiAgentBench, GAMA-Bench, Collab-Overcooked, SOTOPIA |
| `safety-security` | Safety & Security | Measure harmful actions, prompt injection, cyber capability, permissions, and control | AgentDojo, AgentHarm, OS-Harm, CyBench, CVE-Bench, BountyBench |
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
└── AI Research Reproduction
```

Each benchmark receives exactly one `primary_dimension`, zero or more `secondary_dimensions`, and multiple orthogonal `capabilities`. For example, NatureBench is primarily `scientific-discovery`; coding and experimentation are capabilities rather than duplicate top-level classifications.

