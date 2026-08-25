# Target Model-Family Coverage

**Evidence snapshot:** 2026-08-24 (America/Chicago)

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
| TerminalWorld | Coding / terminal | A | A | A | A | A | [Official live leaderboard](https://terminalworld.ai/) |
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
| RSI Bench (live preview) | Open-ended AI R&D | A | A | ? | ? | T | [Official runs](https://www.rsi-benchmark.com/runs), [official tasks](https://www.rsi-benchmark.com/tasks) |
| RSIBench (coding self-improvement) | Agent/harness improvement | ? | ? | ? | ? | ? | [Official dataset card](https://huggingface.co/datasets/AgPerry/rsi-bench) |
| AI4AI-Bench | Open-ended AI R&D | ? | ? | ? | ? | ? | [Paper](https://arxiv.org/abs/2608.20318); six-system model/configuration audit pending |
| AgentHPOBench | Machine learning engineering | ? | ? | ? | ? | ? | [Paper](https://arxiv.org/abs/2607.29626); 12-agent table audit pending |
| EarthVerse | Scientific discovery | ? | ? | ? | ? | ? | [Paper](https://arxiv.org/abs/2608.23525); 25-system table audit pending |
| SWE Refactor Bench | Coding | ? | A | ? | ? | ? | [Paper](https://arxiv.org/abs/2608.23564); eight-model table audit pending |
| SkillSafetyBench | Safety | ? | ? | ? | ? | ? | [Paper](https://arxiv.org/abs/2605.12015), [code](https://github.com/AI45Lab/skill-safety-bench) |
| TAMAS | Safety | ? | ? | ? | ? | ? | [ACL paper](https://aclanthology.org/2026.acl-long.1442/); 10-backbone table audit pending |
| ST-WebAgentBench | Safety | ? | ? | ? | ? | ? | [Official IBM publication](https://research.ibm.com/publications/st-webagentbench-a-benchmark-for-evaluating-safety-and-trustworthiness-in-web-agents--1) |
| CatchBench | Evaluation auditing | ? | ? | ? | ? | ? | [Paper](https://arxiv.org/abs/2608.22808); judge-family roles require extraction |

## Candidate discovery backlog

The following benchmark families are already in the discovery queue but still need primary-source, role-aware model evidence before becoming detailed registry entries:

- Coding: SWE-Lancer, Multi-SWE-bench, LiveCodeBench, BigCodeBench, KernelBench, TritonBench, DreamBench-SWE, NetConfArena.
- AI R&D: MLRC-Bench, EXP-Bench, MLGym, MLAgentBench, AutoResearchBench, Scientist-Bench, LongWoF-Bench.
- Scientific research: ScienceAgentBench, DiscoveryBench, LAB-Bench, SciCode, AstaBench, SciAgentArena, K-Bench.
- Web and research: GAIA, WebArena, VisualWebArena, WebVoyager, Mind2Web, Online-Mind2Web, ResearchArena.
- Computer and daily life: OSWorld 2.0, AssistantBench, TravelPlanner, WebShop, WorkArena, TheAgentCompany, MobilePA-Bench.
- Tools and professional work: ToolBench, ToolSandbox, SpreadsheetBench 2, APEX-Agents, OfficeQA Pro, SaaS-Bench.
- Multi-agent: SOTOPIA, MultiAgentBench, GAMA-Bench, Collab-Overcooked.
- Safety and cyber: AgentDojo, AgentHarm, AgentPoison, OS-Harm, CyBench, CyberGym, CVE-Bench, BountyBench, TRUST-Bench, AgentLAB, AgentFairBench, HVTB, Trust-Memevo, Manager Coercion Benchmark.

`DeTrustAgent` remains an unresolved name rather than a model-coverage row: no matching primary-source benchmark was located as of 2026-08-24. See the [requested-name audit](2026-frontier-benchmarks.md#detrustagent).

## Inclusion rule

A benchmark enters the detailed registry when at least one of the five target families has a result supported by an official paper, official repository, official leaderboard, official model card, or a reproducible third-party run with artifacts. Search snippets, marketing comparison tables without methodology, and bare model claims are discovery leads rather than verification evidence.
