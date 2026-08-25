# Contributing

Contributions should make executable discovery tasks and agentic benchmark suites easier to compare and easier for downstream AI4AI systems to consume.

## Adding a discovery task

The preferred contribution is a task-level entry in `data/discovery-tasks.json`. A discovery method or agent name is not sufficient.

Every task must identify:

- the scientific or engineering question;
- agent-visible data, seed artifact or observation state, constraints, legal actions, and feedback;
- required output artifact or terminal action trace;
- metric name, unit, and minimize/maximize direction;
- executable evaluator and validity checks;
- language, dependencies, simulator/data, hardware, and isolation policy;
- reference system and score under the same task contract, or `null` when no matched result exists;
- reported discovery system and score, or `null` with `not-yet-scored` for a verified task awaiting evaluation;
- primary evidence URLs and integrity caveats.

If several tasks come from one project, declare that project once as a `source_suite` and add each problem as a separate task. Methods such as EFT and search frameworks without extracted problems belong in result/configuration provenance, not in the task array.

For interactive discovery, also record what rules or objectives are hidden, observation and action schemas, reset/life/step budgets, terminal states, public/private split, and replay or scorecard policy. Never extract private environments, and never present public development games as a held-out score.

## Adding a benchmark

Before adding an entry, confirm that it satisfies the inclusion criteria in the README. In particular, it should evaluate a multistep agent workflow rather than only a single model response.

Add the benchmark to `data/benchmarks.json` in alphabetical order by `id`.

Every entry must include:

- stable benchmark ID and official name;
- official paper, repository, and leaderboard URLs;
- evaluation unit and task types;
- agent-visible input and hidden information;
- output artifact;
- headline metric and aggregation method;
- time, compute, network, isolation, and scaffold policies;
- dated representative score snapshot;
- integrity risks and controls;
- AI4AI/RSI relevance classification;
- at least two primary sources.

## Score rules

- Record the complete system name, including scaffold and model.
- Include uncertainty and seed count when published.
- Identify results outside the standard resource budget.
- Preserve substitutions, fallbacks, invalidations, reprompting, test feedback, and other comparability caveats.
- Never silently replace a paper result with a current leaderboard result; date both when both are useful.
- Prefer a small representative set of scores over copying an entire unstable leaderboard.

## Source rules

Use primary sources wherever possible:

1. official benchmark repository;
2. official paper;
3. official dataset or leaderboard;
4. official model/system report containing the evaluation configuration.

Blog posts and benchmark aggregators may help discovery but should not be the only evidence for an entry.

## Pull request checklist

- [ ] The entry satisfies the inclusion criteria.
- [ ] Benchmark IDs remain unique and alphabetically ordered.
- [ ] All score snapshots include an `as_of` date.
- [ ] Model and scaffold are both named.
- [ ] Environment and compute budget are recorded.
- [ ] Integrity caveats are preserved.
- [ ] At least two primary sources are linked.
- [ ] `python scripts/validate_registry.py` passes.
- [ ] `python scripts/validate_discovery_tasks.py` passes when task data changes.
- [ ] The README landscape is updated when the new entry represents a new category.

## Taxonomy changes

Taxonomy changes should remain backward-compatible where practical. If a change alters the meaning of an existing field, increment `registry_version` and explain the migration in the pull request.
