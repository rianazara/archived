---
title: Seven layers of AI engineering, learned through one project
topic: ai
review: true
tags: [learning-path, agents, evaluation]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/reel/Dd0drrasKvg/
---

Layers: software fundamentals → data and ML → LLM mechanics → context and
retrieval → tools and agents → evaluation and observability → production.

The method is to pick one small project and build through them rather than
studying each to completion first; the project reveals what you need next.
Suggested sequence of projects: a grounded assistant, then a structured
extraction pipeline, then a tool-using agent.

Useful debugging map, tying symptoms to layers:

- Assistant retrieves the wrong document → look at search and chunking.
- Agent takes the wrong action → look at tool definitions, state and
  permissions.
- A change *looks* like an improvement → run evals to find out whether it
  actually was.

Three principles that carry beyond this roadmap:

- **Fundamentals before frameworks.**
- **Evaluation before optimization** — otherwise you're tuning blind.
- **Permissions before autonomy** — decide what it may not touch before
  widening what it can do.

The payoff described is being able to explain why your system works, where
it fails, and what to improve, which is also what interviews probe for.
