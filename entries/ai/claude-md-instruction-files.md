---
title: Instruction files carry the rules you're tired of repeating
topic: ai
tags: [claude-code, configuration, agents]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/p/DYeVxIbDSW6/
---

The premise: a coding assistant's weak output is often a missing
instructions file rather than a weak model. A `CLAUDE.md` at the project root
is read every session, so it's the right home for anything you'd otherwise
re-explain.

Categories of rule worth having, drawn from the two posts on this:

- **Defaults** — the stack, conventions and preferences you don't want
  restated each time.
- **Behavior locks** — constraints that prevent unrequested refactors or
  changes outside the task.
- **Long-session failures** — the messy ones: an agent reporting "done"
  having skipped half the work, or drifting as context fills.
- **Memory and stack pinning** — what persists across sessions, and what
  must not change versions underneath you.

Treat the numbers with suspicion. The posts claim mistakes fell from 41% to
11% with four rules, then to 3% with twelve, tested across 30 codebases —
with no methodology, no definition of "mistake", and a comment-to-DM gate on
the actual file. The direction is plausible and matches experience; the
precision is marketing. The companion post citing GitHub star counts and a
"root playbook" is the same genre.

The transferable principle, independent of any viral rule list: write down
the correction you find yourself giving twice. That's what the file is for.
