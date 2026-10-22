---
title: Four RAG architectures, and not defaulting to the fancy one
topic: ai
tags: [rag, architecture, retrieval]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/p/DY9DDEimkX3/
---

- **Standard RAG** — simple and fast; fine for chatbots and documentation
  search.
- **Hybrid RAG** — semantic plus keyword search, for better retrieval
  accuracy. Usually the sensible default.
- **Agentic RAG** — the agent reasons, plans, uses tools and decides what to
  retrieve.
- **Graph RAG** — a knowledge graph captures relationships between entities,
  enabling deeper multi-hop reasoning.

The warning attached is the valuable part: the common mistake is reaching
for Agentic or Graph RAG everywhere, when most applications work perfectly
on Standard or Hybrid. Choosing wrongly buys poor retrieval, hallucinations
and complexity you then have to operate.

Selection criteria: what problem you're solving, how complex the data is,
whether relationships between entities actually matter, and whether the task
genuinely requires reasoning rather than lookup.

A related post sketched a heavier multimodal pipeline — parse document
layout, have a vision model describe images and tables, extract entities and
relationships into a graph, then retrieve over that. The case for it is
narrow and specific: questions whose answer only exists inside a chart or a
table. That's a real gap in text-only extraction, and a bad reason to adopt
graphs for everything else.
