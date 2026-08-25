<div align="center">

# Awesome Agentic Benchmarks

### A curated, evidence-backed map of benchmarks for autonomous agents, AI R&D, and recursive self-improvement

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Registry](https://img.shields.io/badge/registry-machine--readable-2563eb)
![Model coverage](https://img.shields.io/badge/models-GPT%20%7C%20Claude%20%7C%20GLM%20%7C%20Kimi%20%7C%20Qwen-7c3aed)
![Validation](https://img.shields.io/badge/validation-passing-16a34a)
[![License: MIT](https://img.shields.io/badge/license-MIT-f59e0b.svg)](LICENSE)

[Benchmark Dimensions](docs/benchmark-dimensions.md) · [Model Coverage](docs/model-coverage.md) · [JSON Registry](data/benchmarks.json) · [Taxonomy](docs/taxonomy.md) · [Contributing](CONTRIBUTING.md)

</div>

---

> Agent benchmark scores are properties of a complete evaluation system—not a bare model:
>
> **model + scaffold + tools + environment + compute budget + evaluator**

This repository tracks benchmarks in which agents browse, use tools, operate computers, edit repositories, run experiments, train models, reproduce papers, conduct scientific research, or improve AI systems. It is designed as shared evaluation infrastructure for **AI4AI** and **recursive self-improvement (RSI)** research.

## 🔥 News

- **2026-08-24** — Added role-aware coverage for **GPT, Claude, GLM, Kimi, and Qwen**, distinguishing agent, target, and judge models.
- **2026-08-24** — Added a 31-benchmark evidence matrix and a broader primary-source verification backlog.
- **2026-08-24** — Released the initial machine-readable registry with MLE-bench, NatureBench, and PostTrainBench.
- **2026-08-24** — Added JSON Schema, dependency-free validation, and GitHub Actions checks.

## 📑 Table of Contents

- [Why this repository](#-why-this-repository)
- [Benchmark dimensions](#-benchmark-dimensions)
- [Featured AI4AI benchmarks](#-featured-ai4ai-benchmarks)
- [Benchmark catalog](#-benchmark-catalog)
  - [AI R&D and scientific discovery](#ai-rd-and-scientific-discovery)
  - [Coding and software engineering](#coding-and-software-engineering)
  - [Tool use and interaction](#tool-use-and-interaction)
  - [Computer use and daily life](#computer-use-and-daily-life)
  - [General, professional, and safety agents](#general-professional-and-safety-agents)
- [Model-family coverage](#-model-family-coverage)
- [Machine-readable registry](#-machine-readable-registry)
- [Inclusion criteria](#-inclusion-criteria)
- [Contributing](#-contributing)
- [Related repositories](#-related-repositories)

## ✨ Why this repository

Agentic benchmarks are difficult to compare. Two results using the same underlying model can differ substantially because of the scaffold, available tools, time limit, GPU budget, feedback channel, network policy, inference configuration, or integrity rules.

Awesome Agentic Benchmarks provides:

- a concise, categorized benchmark landscape;
- a machine-readable registry for evaluation infrastructure and research agents;
- evidence-backed coverage of GPT, Claude, GLM, Kimi, and Qwen;
- dated score snapshots tied to the model, scaffold, and resource envelope;
- explicit agent-model, target-model, and judge-model roles;
- an AI4AI/RSI taxonomy based on the object and persistence of improvement;
- benchmark integrity notes covering contamination, artifact substitution, evaluator access, and reward hacking.

## 🧭 Benchmark dimensions

Dimensions describe **what the benchmark evaluates**. SFT, DPO, GRPO, RLHF, LoRA, and distillation are training methods—not top-level benchmark dimensions.

| Dimension | What it evaluates | Example benchmarks |
|---|---|---|
| **Coding & Software Engineering** | Repository editing, issue resolution, debugging, tests, and terminal work | SWE-bench, Terminal-Bench, SWE-Lancer |
| **Machine Learning Engineering** | Building and optimizing ML systems against a defined objective | MLE-bench, MLAgentBench, ML-Dev-Bench |
| **Post-Training** | Improving a provided base model under a bounded compute budget | PostTrainBench, RSI Bench |
| **Open-Ended AI R&D** | Proposing, implementing, and validating AI research improvements | RE-Bench, MLR-Bench, MLRC-Bench |
| **Scientific Discovery** | Solving research problems in scientific domains | NatureBench, ScienceAgentBench, DiscoveryBench |
| **Paper Reproduction** | Reconstructing research code, environments, and results | PaperBench, CORE-Bench, SUPER |
| **Web Research & Browsing** | Locating and synthesizing hard-to-find information | BrowseComp, WebArena, GAIA |
| **Computer Use & Daily Life** | Completing workflows in desktop, mobile, and browser environments | OSWorld, AndroidWorld, TravelPlanner |
| **Tool Use** | Selecting APIs and tools while following stateful policies | BFCL, tau2-bench, MCP-Atlas |
| **Professional Work** | Completing realistic office and knowledge-work deliverables | GDPval-AA, SpreadsheetBench 2, WorkArena |
| **Multi-Agent Coordination** | Delegation, collaboration, negotiation, and competition | MultiAgentBench, GAMA-Bench, SOTOPIA |
| **Safety & Security** | Harmful actions, permissions, prompt injection, and cyber capability | AgentDojo, AgentHarm, CyBench |
| **General Agents** | Broad planning, reasoning, tool use, and long-horizon execution | OmniaBench, AGENCYBENCH, AgentBench |

See the complete definitions and classification rules in [Benchmark Dimensions](docs/benchmark-dimensions.md).

## 🌟 Featured AI4AI benchmarks

These are the first fully documented entries in the registry.

| Benchmark | Primary dimension | Evaluation unit | Output | Environment | Current headline snapshot |
|---|---|---|---|---|---|
| [**MLE-bench**](https://github.com/openai/mle-bench) | Machine Learning Engineering | One offline Kaggle competition | Prediction submission | 24h, A10 GPU | 64.44% Any Medal for the leading comparable entry |
| [**NatureBench**](https://github.com/FrontisAI/NatureBench) | Scientific Discovery | One Nature-family scientific ML problem | Executable pipeline and predictions | 4h, task-dependent GPU | 23.3% Surpass-SOTA for the leading entry |
| [**PostTrainBench**](https://posttrainbench.com/) | Post-Training | One base-model × target-benchmark run | Post-trained model checkpoint | 10h, one H100 | 41.79% weighted average for the leading listed entry, with a fallback caveat |

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

## 📚 Benchmark catalog

Legend: **Detailed** = complete registry entry; **Tracked** = included in the model-coverage and verification pipeline.

### AI R&D and scientific discovery

| Benchmark | Dimension | Status | Paper / Code / Leaderboard |
|---|---|---|---|
| **MLE-bench** | Machine Learning Engineering | Detailed | [Paper](https://arxiv.org/abs/2410.07095) · [Code](https://github.com/openai/mle-bench) · [Leaderboard](https://github.com/openai/mle-bench#leaderboard) |
| **NatureBench** | Scientific Discovery | Detailed | [Paper](https://arxiv.org/abs/2606.24530) · [Code](https://github.com/FrontisAI/NatureBench) · [Leaderboard](https://frontisai.github.io/NatureBench/) |
| **PostTrainBench** | Post-Training | Detailed | [Paper](https://arxiv.org/abs/2603.08640) · [Code](https://github.com/aisa-group/PostTrainBench) · [Leaderboard](https://posttrainbench.com/) |
| **RE-Bench** | Open-Ended AI R&D | Tracked | [Paper](https://arxiv.org/abs/2411.15114) · [Code](https://github.com/METR/RE-Bench) |
| **MLR-Bench** | Open-Ended AI R&D | Tracked | [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/ab8dd000d6f87f40061a73f8bca7fae4-Abstract-Datasets_and_Benchmarks_Track.html) |
| **PaperBench** | Paper Reproduction | Tracked | [Paper](https://arxiv.org/abs/2504.01848) · [Project](https://openai.com/index/paperbench/) |
| **InferenceBench** | AI Systems Optimization | Tracked | [Code](https://github.com/aisa-group/InferenceBench) |
| **ScienceAgentBench** | Scientific Discovery | Discovery queue | [Paper](https://arxiv.org/abs/2410.05080) · [Code](https://github.com/OSU-NLP-Group/ScienceAgentBench) |
| **EXP-Bench** | Open-Ended AI R&D | Discovery queue | [Paper](https://arxiv.org/abs/2505.24785) · [Code](https://github.com/EvolvingLMMs-Lab/EXP-Bench) |

### Coding and software engineering

| Benchmark | Scope | Status | Project |
|---|---|---|---|
| **SWE-bench Verified** | Real GitHub issue resolution | Tracked | [Code](https://github.com/SWE-bench/SWE-bench) |
| **SWE-bench Pro** | Harder professional repository tasks | Tracked | [Project](https://scale.com/leaderboard/swe_bench_pro_public) |
| **SWE-bench Multilingual** | Repository tasks across programming languages | Tracked | [Code](https://github.com/multi-swe-bench/multi-swe-bench) |
| **SWE-bench Multimodal** | UI-facing repository issues with visual context | Tracked | [Code](https://github.com/SWE-bench/SWE-bench) |
| **Terminal-Bench** | Long-horizon terminal tasks | Tracked | [Code](https://github.com/laude-institute/terminal-bench) |
| **TUA-Bench** | General-purpose terminal use | Tracked | [Code](https://github.com/facebookresearch/TUA-Bench) |
| **SWE-Lancer** | Paid freelance software-engineering tasks | Discovery queue | [Code](https://github.com/openai/SWELancer-Benchmark) |

### Tool use and interaction

| Benchmark | Scope | Status | Project |
|---|---|---|---|
| **tau-bench** | Stateful customer-service tool use | Tracked | [Code](https://github.com/sierra-research/tau-bench) |
| **tau2-bench** | Dual-control tool-agent-user interaction | Tracked | [Code](https://github.com/sierra-research/tau2-bench) |
| **BFCL** | Function calling and API selection | Tracked | [Code](https://github.com/ShishirPatil/gorilla) |
| **MCP-Atlas** | Real MCP-server tool use | Tracked | [Code](https://github.com/scaleapi/mcp-atlas) · [Leaderboard](https://labs.scale.com/leaderboard/mcp_atlas) |
| **MCP-Bench** | MCP discovery, selection, and execution | Tracked | [Code](https://github.com/Accenture/mcp-bench) |
| **Toolathlon** | Diverse, realistic, long-horizon tool execution | Tracked | [Project](https://toolathlon.xyz/) |
| **ACEBench** | Normal, special, and agent function calling | Tracked | [Results](https://github.com/Agent-Suite/AgentSuite/blob/main/ACEBench/README.md) |

### Computer use and daily life

| Benchmark | Scope | Status | Project |
|---|---|---|---|
| **OSWorld** | Real desktop applications | Tracked | [Code](https://github.com/xlang-ai/OSWorld) |
| **OSWorld-Verified** | Reliability-focused OSWorld subset | Tracked | [Project](https://os-world.github.io/) |
| **ScreenSpot-Pro** | Professional high-resolution GUI grounding | Tracked | [Code](https://github.com/likaixin2000/ScreenSpot-Pro-GUI-Grounding) |
| **AndroidWorld** | Real Android application workflows | Tracked | [Code](https://github.com/google-research/android_world) |
| **WindowsAgentArena** | Windows application workflows | Tracked | [Code](https://github.com/microsoft/WindowsAgentArena) |
| **TravelPlanner** | Constrained travel planning | Discovery queue | [Code](https://github.com/OSU-NLP-Group/TravelPlanner) |

### General, professional, and safety agents

| Benchmark | Dimension | Status | Project |
|---|---|---|---|
| **OmniaBench** | General Agent | Tracked | [Code](https://github.com/scuuy/OmniaBench) |
| **AGENCYBENCH** | General Agent | Tracked | [Paper](https://aclanthology.org/2026.acl-long.337.pdf) |
| **GDPval-AA v2** | Professional Work | Tracked | [Leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa) |
| **Claw-Eval-Live** | Enterprise Agent Workflows | Tracked | [Code](https://github.com/Claw-Eval-Live/Claw-Eval-Live) |
| **Agent3Sigma** | Agent Safety | Tracked | [Code](https://github.com/antgroup/Agent3Sigma) |
| **TheAgentCompany** | Simulated Knowledge Work | Discovery queue | [Code](https://github.com/TheAgentCompany/TheAgentCompany) |
| **AgentDojo** | Prompt-Injection Safety | Discovery queue | [Code](https://github.com/ethz-spylab/agentdojo) |
| **AgentHarm** | Harmful Agent Behavior | Discovery queue | [Code](https://github.com/UKGovernmentBEIS/inspect_evals) |

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
| SWE-bench Verified | Coding | ✓ | ✓ | ✓ | ✓ | ✓ |
| SWE-bench Pro | Coding | ✓ | ✓ | ✓ | ✓ | ✓ |
| Terminal-Bench | Coding | ✓ | ✓ | ✓ | ✓ | ✓ |
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

## 🧱 Machine-readable registry

The canonical detailed registry is [data/benchmarks.json](data/benchmarks.json), validated against [schema/benchmark.schema.json](schema/benchmark.schema.json).

Each detailed entry records:

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
```

## ✅ Inclusion criteria

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
