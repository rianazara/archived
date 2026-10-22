---
title: RAG systems rot — drift, re-embedding, and index swaps
topic: ai
review: true
tags: [rag, production, drift, observability]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/reel/Dc_rzFvzRKw/
---

The framing that makes this click: when retrieval quality falls with *zero
code changes*, the pipeline didn't break — the world moved while the index
stood still. The junior reflex is to tune the prompt; the better question is
what changed underneath.

**Five causes, none of them code:**

- **Content drift** — source documents changed but were never re-embedded.
- **Embedding model change** — a new provider or model version puts vectors
  in a different space, so old and new aren't comparable.
- **Vocabulary drift** — users start asking about terms, products or
  concepts absent from the original corpus.
- **Index staleness** — documents added, updated or deleted without the
  vector store reflecting it.
- **Query distribution shift** — real traffic wanders away from whatever
  your evaluation set covered.

**Keeping the store in sync:** incrementally re-embed changed documents,
delete vectors when sources are deleted, trigger re-indexing on source
change, periodically reconcile the source of truth against the store, and
carry metadata — document version, timestamp, embedding model.

**Detecting drift:** track retrieval relevance over time, measure Recall@K /
Precision@K where labels exist, keep a stable benchmark set, watch query
distribution, and periodically re-check against known-good results.

**Re-embedding safely:** version your embeddings and never mix incompatible
ones in a single index. Pattern: build a new index → re-embed → validate →
swap → monitor → roll back if needed.

The distinction worth keeping: a RAG system isn't done when it ships. Data,
embeddings, index and query distribution all drift, which is why "it worked
in testing" and "it's production-ready" are different claims.
