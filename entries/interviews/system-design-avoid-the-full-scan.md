---
title: Billion-scale matching — don't search everything
topic: interviews
tags: [system-design, sharding, scale]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/reel/DdMoZsZtQaY/
---

Posed as a system design question: how do you match one new fingerprint
against 1.3+ billion records in seconds? Comparing against every record is
hopeless, so the answer isn't a faster scan.

**Partition → filter → match in parallel → aggregate**

1. **Shard** the dataset across many servers, so many machines each handle a
   slice instead of one machine walking a giant table.
2. **Filter candidates cheaply** first — fast indexing, feature-based
   filtering, or approximate matching to discard unlikely records before any
   expensive comparison.
3. **Match the survivors in parallel**, each worker returning its best match
   or "no match" with a confidence score.
4. **Aggregate** in a coordinator layer that collects worker results,
   weighs the scores, and makes the final match/no-match call.

The transferable insight is the reframe: the win isn't searching a billion
records faster, it's arranging things so you never perform a full sequential
search.

The post was explicit that this is a general approach to large-scale
biometric search and that Aadhaar's actual internal architecture isn't
public — worth preserving that caveat rather than citing it as how Aadhaar
works.
