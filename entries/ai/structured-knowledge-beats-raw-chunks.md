---
title: Structured notes retrieve better than scattered documents
topic: ai
review: true
tags: [rag, knowledge-management, retrieval]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/reel/DaJGKX2z5_u/
---

Two different jobs that get conflated:

- **RAG finds** relevant information — embed the documents, retrieve the
  closest chunks per question.
- **An organized knowledge format** decides *what there is to find* —
  knowledge written as structured markdown, one file per concept, with links
  between related concepts, instead of the same material scattered across
  hundreds of documents.

Put together, retrieval stops pulling arbitrary chunks out of PDFs and
starts pulling coherent, self-contained units, which makes answers more
accurate and more consistent.

Directly relevant here: this knowledge base already *is* that pattern — one
concept per file, a topic tree, wiki-style links between related entries,
and a generated index. If these entries ever become a retrieval source for an
assistant, the structure is the feature, not the markdown.

The practical lesson for writing entries: keep one idea per file and make it
make sense alone, because that's also the unit retrieval would hand to a
model.
