---
title: Harness engineering — the model is only the engine
topic: ai
review: true
tags: [agents, architecture, tooling]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/reel/DccwvLGMQXV/
---

The analogy: a model is an engine, and an engine alone takes you nowhere.
The harness is the rest of the car.

- **Model** — the raw capability.
- **Prompt engineering** — what you tell it to do.
- **Loop engineering** — how it attempts, checks, and retries.
- **Harness engineering** — the whole environment that lets it actually do
  work: tools, context, rules, memory, feedback, verification.

For a coding agent, the harness is what lets it open files, edit code, run
tests, see what failed, fix the mistake, and try again. Strip that away and
the same model can only talk about code.

The practical consequence: you can often make a system substantially better
without touching the model at all, by giving it better tools, cleaner
context, or a verification step it was missing. Worth checking the harness
before reaching for a bigger model.
