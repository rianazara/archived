---
title: Cache before you scale — and measure the threshold
topic: ai
tags: [caching, cost, latency, production]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/p/DeVz6IUmNBq/
---

Posed as an interview question with a chart for an answer: *your LLM bill
doubled — what do you do?*

**Semantic caching** is the first lever. Unlike a key-based cache, it
matches on meaning, so "how do I cancel" and "cancellation process?" can
share one answer. Three things make or break it:

- **The similarity threshold**, derived from your own data rather than
  guessed. Too loose and you serve wrong answers confidently; too tight and
  the cache barely hits.
- **Invalidation** — a plan for clearing stale answers when the underlying
  truth changes, which is the same staleness problem as
  [[rag-drift-and-reindexing]].
- **Honest measurement** of cost and latency, including the embedding call
  the cache itself costs.

The classical version of the same idea, from a separate saved post: a
conventional cache in front of a database — hit returns immediately, miss
fetches, stores with an expiry, then returns. The cache doesn't replace the
database, it stops the backend redoing identical work as traffic grows.

The shared principle is worth stating plainly: before buying more capacity,
find the work you're doing repeatedly and stop doing it twice.
