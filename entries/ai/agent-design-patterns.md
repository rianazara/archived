---
title: Agent design patterns worth knowing by name
topic: ai
tags: [agents, patterns, orchestration]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/p/DdooT8dgL-r/
---

A catalog of patterns for how an agent plans, uses tools, divides work and
checks its own answers. The guidance attached was to pick the pattern that
fits the task — better answers, faster work, human checks, or recovery when
something fails — rather than adopting all of them.

- **ReAct loop** — alternate reasoning and tool use.
- **Routing** — classify the request, send it to the right handler.
- **Planner–executor** — one component plans, another carries out steps.
- **Parallel processing** — fan out independent work.
- **Orchestrator–workers** — a coordinator distributes subtasks.
- **Evaluator–optimizer** — generate, score, revise (see
  [[reflexion-generator-critic-loop]]).
- **Supervisor–specialist** — a generalist delegates to narrow experts.
- **Agent handoff** — transfer control with context intact.
- **Human-in-the-loop** — a person approves at a defined gate.
- **Durable execution / checkpointing** — survive restarts and resume.

Honest limitation: the explanations and the "when to use which" guidance
lived in the carousel images, which an export doesn't include. What survived
is the vocabulary — enough to recognize the patterns and look them up, not
the comparison itself.
