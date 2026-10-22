---
title: Evaluate retrieval and generation separately
topic: study
review: true
tags: [rag, evaluation, metrics, debugging]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/p/DZy9FItkyq8/
---

A RAG system answering a handful of manual test queries correctly means you
got lucky, not that it works. Failures come from one of two places —
retrieval didn't fetch the right context, or generation didn't use the
context it got — and if you don't measure both layers separately you're
debugging blind.

**Retrieval layer**

- **Context precision** — how much of what came back is actually relevant.
- **Context recall** — what relevant material retrieval missed.
- **MRR** — how high the first relevant result ranks.
- **Hit rate** — how often retrieval finds at least one useful chunk.

**Generation layer**

- **Faithfulness** — is the answer grounded in the retrieved context.
- **Answer relevancy** — did it answer the question actually asked.
- **Answer correctness** — is it factually right.
- **Context utilization** — did the model use the context at all.

**The diagnostic matrix**, which is the part worth memorizing:

| Pattern | Diagnosis |
|---|---|
| High recall, low precision | too much noise |
| High precision, low recall | missing important information |
| Good retrieval, low faithfulness | hallucination |
| Good generation, bad retrieval | the model never had a chance |

That last row is the one teams misread most — blaming the model for a
retrieval failure. Production RAG isn't about better prompts; it's about
locating the failure and measuring it consistently.
