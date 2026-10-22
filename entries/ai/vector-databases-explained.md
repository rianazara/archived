---
title: What a vector database is actually for
topic: ai
review: true
tags: [vector-database, embeddings, rag, fundamentals]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/p/DbN79dJEVSJ/
---

Conventional databases are excellent at exact questions — find this ID,
filter on this date. What they can't do is "find the things that mean
roughly the same as this."

A vector database fills that gap by storing each item as an **embedding**: a
list of numbers capturing meaning. Search for "heart attack" and it can
surface a note that only ever says "cardiac arrest" — same meaning,
different words, still findable.

Why RAG made them standard equipment: a model only knows its training data,
so asked about your documents it starts guessing. RAG fixes that by pulling
the most relevant passages in before the model answers — and finding those
passages *is* a meaning search, which is what a vector database does.

Worth adding: this is also the honest answer to "do I need one?" If your
retrieval is genuinely keyword- or filter-shaped, a normal index is simpler
and better. Hybrid retrieval exists because both kinds of question show up
in real traffic.

A second saved post adds the surrounding machinery worth understanding
before picking a product: how similarity search actually works, why the
index type matters for speed-versus-accuracy, and **metadata filtering** —
constraining by attributes before or alongside the vector search, which is
what makes access control and freshness filters possible (see
[[stale-context-versioned-rag]]). Commonly named options include Pinecone,
Weaviate, Milvus, Qdrant, Chroma and pgvector; the last is just Postgres
with an extension, which is often the right starting point when you already
run one.
