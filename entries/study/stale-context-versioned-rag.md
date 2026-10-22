---
title: Handling stale context with versioned, event-driven retrieval
topic: study
tags: [rag, freshness, system-design, interviews]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/reel/DZbsUyNMV5j/
---

Framed as an interview answer to "how do you handle stale context when the
knowledge base updates every few minutes."

- **Version documents rather than overwriting.** Each update creates a new
  version carrying `doc_id`, `version_id`, `updated_at`, `valid_from`.
  Overwriting embeddings blindly breaks in-flight queries still reading the
  old version.
- **Make retrieval freshness-aware.** Filter to the latest valid versions
  first, *then* rank by semantic similarity, recency and source authority —
  so the retriever asks "is this still valid?" alongside "is this
  relevant?"
- **Add a staleness check before generation.** Validate retrieved chunks
  against metadata; if the document changed after retrieval, re-retrieve,
  warn the model, or refuse to answer depending on how critical it is.
- **Use a change feed, not a schedule.** Create/update/delete events trigger
  re-chunking, re-embedding, index update and cache invalidation — which
  avoids full re-indexing every few minutes.
- **Fall back to a live lookup** when the freshness SLA is violated. For
  high-risk or real-time data, don't rely on retrieval at all.
- **Monitor** retrieval freshness, stale chunk rate, indexing lag, cache
  hit rate, and answer correctness *after* knowledge base updates.

The framing to keep: stale context isn't only a retrieval problem, it's a
data freshness, caching, indexing and observability problem. This is the
interview-ready version of [[rag-drift-and-reindexing]].
