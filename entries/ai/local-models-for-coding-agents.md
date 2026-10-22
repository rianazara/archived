---
title: Pointing a coding agent at a local model
topic: ai
review: true
tags: [local-models, ollama, cost, privacy]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/reel/DYpZJxXyGGw/
---

The setup described: install Ollama, pull an open-weight coding model
(Qwen's coder variants were the example), and point the coding agent at your
own machine rather than a hosted API. The interface and workflow stay the
same; inference moves local.

What you gain: no per-token cost, no rate limits, and nothing leaving the
machine — which is the real argument when the codebase is sensitive.

What the post leaves out, and it matters:

- **Capability gap.** A model that fits on a laptop is meaningfully weaker
  at long-horizon, multi-file agentic work than a frontier model. Fine for
  local edits and boilerplate; noticeably worse at the tasks you'd most want
  help with.
- **Local isn't free**, it's prepaid — in RAM, disk, battery and speed.
- **Agent harnesses assume capabilities** like reliable tool calling and
  long-context behavior, which smaller models do less consistently, so
  breakage shows up as the agent flailing rather than a clean error.

Reasonable as a privacy or cost choice made deliberately, with eyes open
about the tradeoff — and a good illustration of
[[harness-engineering]], since swapping the model under the same harness is
exactly the experiment that tells you which one was doing the work.
