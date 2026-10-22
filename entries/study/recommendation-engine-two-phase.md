---
title: Recommendations at scale — generate candidates, then rank
topic: study
review: true
tags: [system-design, recommendations, embeddings, latency]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/reel/DYcreHTTBAq/
---

The question: design a recommendation engine for 300M users, under 100ms.
Nobody runs one model across that population in real time; the answer is
two phases with different cost profiles.

1. **Candidate generation** — narrow tens of millions of items to a few
   hundred. Users and items are represented as vectors learned from
   behaviour (clicks, purchases, watch time, skips), so similar users land
   near each other. Store item vectors in a vector index and take the
   nearest neighbours to the user vector. Approximate search (HNSW) returns
   ~500 candidates in tens of milliseconds even at this scale.
2. **Ranking** — score those few hundred precisely with a lightweight model
   (small neural net or gradient-boosted trees) using richer features:
   recency, context, time of day, device. Return the top handful.

**Pre-compute whatever you can.** Batch jobs every few hours produce and
cache candidate lists per user, leaving the real-time path to do only final
ranking plus genuinely fresh signals like something clicked two minutes ago.

Supporting infrastructure: cached candidates in memory, a dedicated
approximate-nearest-neighbour cluster, a low-latency inference server for
ranking, and anything that doesn't block the response made async.

What's being tested: the generation/ranking split, approximate search, the
pre-computation strategy, and how you trade freshness against latency.
Cheap-then-expensive is the same structure as the filter-then-match pattern
in [[system-design-avoid-the-full-scan]].
