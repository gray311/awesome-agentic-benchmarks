# Target Model-Family Coverage

The registry tracks five target families: **GPT, Claude, GLM, Kimi, and Qwen**.

Coverage is role-aware:

- **A** — verified as the model driving the evaluated agent.
- **T** — verified only as the target model modified by another agent.
- **J** — verified only as an evaluator or judge.
- **M** — reported by an official model provider, but not yet normalized into the detailed registry.
- **?** — no qualifying primary-source evidence has been recorded yet. This does not mean the model has never been tested.

## Verified and high-priority inventory

| Benchmark | Dimension | GPT | Claude | GLM | Kimi | Qwen | Current evidence anchor |
|---|---|---:|---:|---:|---:|---:|---|
| MLE-bench | MLE | A | A | ? | ? | ? | [Official leaderboard](https://github.com/openai/mle-bench#leaderboard) |
| NatureBench | Scientific discovery | A/J | A | A | A | A | [Official repository and results news](https://github.com/FrontisAI/NatureBench) |
| PostTrainBench | Post-training | A/J | A | A | A | T | [Official leaderboard](https://posttrainbench.com/) |
| SWE-bench Verified | Coding | M | M | M | M | M | [Claude results](https://www.anthropic.com/engineering/swe-bench-sonnet), [Kimi results](https://github.com/MoonshotAI/Kimi-K2), [Qwen results](https://qwenlm.github.io/blog/qwen3-coder/) |
| SWE-bench Pro | Coding | M | M | M | M | M | [Claude system card](https://www-cdn.anthropic.com/0b4915911bb0d19eca5b5ee635c80fef830a37ea.pdf), [Qwen model repository](https://github.com/QwenLM/Qwen3-Coder) |
| SWE-bench Multilingual | Coding | ? | M | M | M | ? | [Kimi results](https://github.com/MoonshotAI/Kimi-K2), [GLM results](https://github.com/zai-org/GLM-4.5) |
| SWE-bench Multimodal | Coding | ? | M | ? | ? | ? | [Claude system card](https://www-cdn.anthropic.com/0b4915911bb0d19eca5b5ee635c80fef830a37ea.pdf) |
| Terminal-Bench | Coding | M | M | M | M | M | [Claude 4 results](https://www.anthropic.com/news/claude-4), [GLM results](https://github.com/zai-org/GLM-4.5) |
| BrowseComp | Web research | A | M | M | M | ? | [OpenAI benchmark](https://openai.com/index/browsecomp/), [Kimi repository](https://github.com/MoonshotAI/Kimi-K2), [Claude system card](https://www-cdn.anthropic.com/0b4915911bb0d19eca5b5ee635c80fef830a37ea.pdf) |
| tau-bench | Tool use | M | M | ? | M | ? | [Claude 4 results](https://www.anthropic.com/news/claude-4), [Kimi repository](https://github.com/MoonshotAI/Kimi-K2) |
| tau2-bench | Tool use | M | M | M | M | M | [Claude system card](https://www-cdn.anthropic.com/14e4fb01875d2a69f646fa5e574dea2b1c0ff7b5.pdf), [Qwen benchmark appendix](https://github.com/QwenLM/Qwen-MM-Plugins/blob/main/tests/assets/real/qwen3vl-tex/content/appendix_benchmarks.tex) |
| BFCL | Tool use | M | M | ? | ? | M | [Qwen benchmark appendix](https://github.com/QwenLM/Qwen-MM-Plugins/blob/main/tests/assets/real/qwen3vl-tex/content/appendix_benchmarks.tex) |
| MCP-Atlas | Tool use | A | A | A | A | A | [Official repository](https://github.com/scaleapi/mcp-atlas), [official leaderboard](https://labs.scale.com/leaderboard/mcp_atlas) |
| MCP-Bench | Tool use | A | A | A | A | A | [Official repository and leaderboard](https://github.com/Accenture/mcp-bench) |
| Toolathlon | Tool use | A | A | A | A | A | [Official leaderboard](https://toolathlon.xyz/) |
| ACEBench | Tool use | A | A | ? | ? | A | [Official benchmark results](https://github.com/Agent-Suite/AgentSuite/blob/main/ACEBench/README.md) |
| OSWorld | Computer use | M | A | M | M | A | [Official repository](https://github.com/xlang-ai/OSWorld), [Qwen benchmark appendix](https://github.com/QwenLM/Qwen-MM-Plugins/blob/main/tests/assets/real/qwen3vl-tex/content/appendix_benchmarks.tex) |
| OSWorld-Verified | Computer use | M | M | ? | M | ? | [Claude system card](https://www-cdn.anthropic.com/0b4915911bb0d19eca5b5ee635c80fef830a37ea.pdf) |
| ScreenSpot-Pro | Computer use | ? | M | ? | ? | M | [Claude system card](https://www-cdn.anthropic.com/0b4915911bb0d19eca5b5ee635c80fef830a37ea.pdf), [Qwen benchmark appendix](https://github.com/QwenLM/Qwen-MM-Plugins/blob/main/tests/assets/real/qwen3vl-tex/content/table_flagship_models.tex) |
| AndroidWorld | Computer use | ? | ? | ? | ? | M | [Qwen benchmark appendix](https://github.com/QwenLM/Qwen-MM-Plugins/blob/main/tests/assets/real/qwen3vl-tex/content/table_flagship_models.tex) |
| WindowsAgentArena | Computer use | ? | ? | ? | ? | M | [Qwen benchmark appendix](https://github.com/QwenLM/Qwen-MM-Plugins/blob/main/tests/assets/real/qwen3vl-tex/content/table_flagship_models.tex) |
| OmniaBench | General agent | A | A | A | A | A | [Official repository and leaderboard](https://github.com/scuuy/OmniaBench) |
| AGENCYBENCH | General agent | A | A | A | A | A | [Official ACL paper](https://aclanthology.org/2026.acl-long.337.pdf) |
| TUA-Bench | Terminal use | A | A | A | ? | A | [Official repository](https://github.com/facebookresearch/TUA-Bench) |
| Agent3Sigma | Safety | A | A | A | A | A | [Official repository and leaderboard](https://github.com/antgroup/Agent3Sigma) |
| Claw-Eval-Live | Professional workflows | A | A | A | A | A | [Official repository and leaderboard](https://github.com/Claw-Eval-Live/Claw-Eval-Live) |
| GDPval-AA v2 | Professional work | A | A | A | A | A | [Live leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa) |
| InferenceBench | AI systems optimization | ? | A | A | ? | ? | [Official repository](https://github.com/aisa-group/InferenceBench) |
| PaperBench | Paper reproduction | A | ? | ? | ? | ? | [Official benchmark](https://openai.com/index/paperbench/) |
| RE-Bench | Open-ended AI R&D | A | A | ? | ? | ? | [Official repository](https://github.com/METR/RE-Bench) |
| MLR-Bench | Open-ended AI R&D | A | A | ? | ? | ? | [Official NeurIPS paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/ab8dd000d6f87f40061a73f8bca7fae4-Abstract-Datasets_and_Benchmarks_Track.html) |

## Candidate discovery backlog

The following benchmark families are already in the discovery queue but still need primary-source, role-aware model evidence before becoming detailed registry entries:

- Coding: SWE-Lancer, Multi-SWE-bench, LiveCodeBench, BigCodeBench, KernelBench, TritonBench.
- AI R&D: RSI Bench, MLRC-Bench, EXP-Bench, MLGym, MLAgentBench, AutoResearchBench, Scientist-Bench.
- Scientific research: ScienceAgentBench, DiscoveryBench, LAB-Bench, SciCode, AstaBench.
- Web and research: GAIA, WebArena, VisualWebArena, WebVoyager, Mind2Web, Online-Mind2Web, ResearchArena.
- Computer and daily life: OSWorld 2.0, AssistantBench, TravelPlanner, WebShop, WorkArena, TheAgentCompany.
- Tools and professional work: ToolBench, ToolSandbox, SpreadsheetBench 2, APEX-Agents, OfficeQA Pro, SaaS-Bench.
- Multi-agent: SOTOPIA, MultiAgentBench, GAMA-Bench, Collab-Overcooked.
- Safety and cyber: AgentDojo, AgentHarm, AgentPoison, OS-Harm, CyBench, CyberGym, CVE-Bench, BountyBench.

## Inclusion rule

A benchmark enters the detailed registry when at least one of the five target families has a result supported by an official paper, official repository, official leaderboard, official model card, or a reproducible third-party run with artifacts. Search snippets, marketing comparison tables without methodology, and bare model claims are discovery leads rather than verification evidence.

