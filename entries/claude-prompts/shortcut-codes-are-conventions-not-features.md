---
title: "Claude shortcut codes" are conventions you define, not built-in commands
topic: claude-prompts
review: true
tags: [prompting, claude, misconception]
created: 2026-10-21
updated: 2026-10-21
source: https://www.instagram.com/p/DYhLDnLE3bJ/
---

A widely-shared list of "shortcut codes" for Claude:

| Code | Claimed effect |
|---|---|
| `/ghost` | make the response sound more human |
| `OODA` | analyze via Observe, Orient, Decide, Act |
| `L99` | answer with expert-level depth |
| `/godmode` | give the most complete, direct response |
| `Artifacts` | build an app/site/dashboard in the chat |

**Important correction:** apart from Artifacts, these are not features. There
is no `/godmode` or `L99` parsed by Claude. They work only to the extent
that *you* define them — the model is pattern-matching on suggestive words,
which is why results are erratic. Artifacts is the one genuine capability in
the list.

The post half-admits this ("some shortcut codes may not work consistently"),
and its actual useful advice is the fix: write out what you want explicitly
and save it in Project Instructions, where it applies to every chat. A
defined instruction like "when I write OODA, structure the answer as
Observe/Orient/Decide/Act" is real; the bare code without a definition is
cargo cult.

Takeaway: treat any viral list of secret model commands as a prompt
convention at best, and define it yourself if you want it to work.
