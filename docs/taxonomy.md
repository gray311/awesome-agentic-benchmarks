# Taxonomy

This taxonomy separates the capability of an agentic system from the capability of its underlying model. It is intended to support benchmark selection, experiment design, capability forecasting, and AI4AI/RSI system architecture.

## 1. Evaluation target

Record what is actually being evaluated:

- **Model**: a single inference call or fixed prompting protocol.
- **Agent**: a model operating through a scaffold and tools.
- **Agent system**: one or more agents plus orchestration, memory, tools, evaluators, and compute allocation.
- **Organization simulator**: multiple specialized roles with persistent workflows and shared artifacts.

The initial registry entries are agent-system evaluations.

## 2. Improvement target

- **External task artifact**: code, prediction file, proof, design, or report.
- **Task-specific ML system**: a trained model built to solve an external task.
- **Scientific method**: an algorithm or model intended to match or exceed a research result.
- **Provided AI model**: another model whose weights or behavior are improved.
- **Agent component**: the evaluated agent changes its own prompt, tools, memory, scaffold, or policy.
- **Whole agent system**: the evaluated system changes and validates a successor version of itself.

This distinction prevents ordinary AutoML from being mislabeled as RSI.

## 3. RSI relevance levels

| Level | Meaning |
|---|---|
| `supporting-capability` | Measures a generic prerequisite such as coding, planning, or tool use. |
| `enabling-capability` | Measures an integrated workflow needed for AI development. |
| `advanced-enabling-capability` | Measures open-ended AI or scientific R&D that may generate novel improvements. |
| `direct-ai-improvement` | The agent directly changes another AI model, algorithm, or training pipeline. |
| `agent-self-improvement` | The evaluated agent modifies a component of itself and is evaluated causally before and after. |
| `recursive-self-improvement` | Successor agents repeatedly improve successor agents under a controlled multigeneration protocol. |

The label should reflect the causal evaluation design, not the benchmark's marketing language.

## 4. Feedback-loop strength

- **None**: no environment result is available before final submission.
- **Weak**: structural checks or public validation only; no objective score.
- **Medium**: limited scores, unit tests, or evaluator feedback support iteration.
- **Strong**: repeated objective evaluation directly guides search, training, or model selection.

Feedback strength affects both capability and reward-hacking risk.

## 5. Artifact and mutation surface

Record whether the agent may modify:

- prediction files;
- source code;
- training data;
- model weights;
- inference configuration or chat templates;
- evaluation code;
- its own scaffold, prompts, memory, or tools.

Evaluation-code mutation should normally be prohibited. Inference-configuration changes must be explicitly classified because they can dominate apparent post-training gains.

## 6. Environment and resource envelope

Minimum fields:

- wall-clock time limit;
- CPU, RAM, accelerator, and storage;
- internet and package-installation policy;
- container or VM isolation;
- scaffold and tool policy;
- human-intervention policy;
- number of seeds;
- whether intermediate evaluation is available.

An agentic score without this envelope is incomplete.

## 7. Evaluation mechanics

Classify evaluators as:

- deterministic exact-match or unit-test grader;
- metric over hidden labels;
- human baseline or leaderboard comparison;
- LLM judge;
- hybrid deterministic and judge system;
- causal before/after improvement test;
- multigeneration improvement curve.

For AI4AI and RSI, downstream generalization must be distinguished from optimization on the visible development evaluator.

## 8. Integrity risks

Common risks include:

- test-item contamination;
- retrieval of published solutions or traces;
- model or artifact substitution;
- external-model distillation;
- evaluator modification;
- reward hacking through formatting or inference configuration;
- hidden-label leakage;
- unauthorized credential or API use;
- human intervention during nominally autonomous runs.

Registry entries should describe both the risk and the implemented control.

## 9. Score reporting

Every score snapshot should include:

- date;
- benchmark version;
- metric and scale;
- model and scaffold;
- resource budget;
- seed count or uncertainty where available;
- integrity caveats;
- primary source.

Never collapse a model-agent-scaffold result into a bare model score.

## 10. What a true RSI benchmark still needs

A rigorous RSI benchmark should additionally provide:

1. a versioned baseline agent;
2. an authorized self-modification surface;
3. a held-out suite that measures general capability rather than evaluator overfitting;
4. a causal comparison between parent and successor;
5. multiple successive improvement generations;
6. fixed total compute accounting across generations;
7. rollback, sandboxing, provenance, and model-identity controls;
8. measurements of capability gain, cost, reliability, alignment, and integrity;
9. controls against importing a stronger external agent;
10. analysis of whether improvement rate accelerates, plateaus, or regresses.

The current registry should help identify which existing benchmarks can supply components for such a protocol.
