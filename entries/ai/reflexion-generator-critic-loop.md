---
title: Reflexion — make the agent grade its own work
topic: ai
review: true
tags: [agents, evaluation, patterns]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/p/DaFwEGRGGIg/
---

The observation: a single answer is just a first attempt — no second look,
no quality check. Reflexion closes that loop.

The worked structure, on a cold-email task:

1. A **generator** produces the draft.
2. A **critic** scores it against an explicit rubric, 0–10.
3. On a fail, it loops back with the critique as feedback.
4. On a pass, a **stronger model** gives the final verdict.
5. Plot where additional revisions stop improving the score.

That last step is the part most people skip and the most useful: revision
loops have diminishing returns, and without measuring them you're paying for
iterations that no longer help.

The rubric is doing the real work here — a critic without explicit criteria
tends to agree with whatever the generator produced.
