---
title: Three ways a model can search its own reasoning
topic: ai
tags: [agents, reasoning, patterns]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/reel/DdO9_IWvBgr/
---

Three strategies that sit behind "thinking" behavior in agents, each solving
a different failure:

- **ReAct** — interleave reasoning with acting, so conclusions are grounded
  in real tool results instead of confident guesses. Fixes
  *fabrication*.
- **Tree of Thought** — explore several candidate lines of reasoning before
  committing to one. Fixes *premature commitment* to the first plausible
  path.
- **Monte Carlo Tree Search** — score which branches are actually worth
  pursuing, rather than expanding all of them. Fixes the *cost* of the
  previous one.

Read in that order they're a progression: ground your steps, consider
alternatives, then allocate effort between the alternatives.

Worth noting what this costs — each layer multiplies tokens and latency, so
these are tools for problems where being wrong is expensive, not defaults.
ReAct also appears in [[agent-design-patterns]] as an orchestration pattern;
here it's the reasoning loop underneath.

The post gated its full notes behind a comment, so these are the mechanisms
only. It also attributed them to specific named models' internals, which
isn't something outside observers can verify — the techniques are published
research and stand on their own regardless of who uses what.
