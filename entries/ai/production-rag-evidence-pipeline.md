---
title: Production RAG is evidence engineering
topic: ai
tags: [rag, production, retrieval]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/reel/DaNKnWhJtGR/
---

Demo RAG is four steps: question → vector search → top-k chunks → answer.
That's enough to impress and not enough to rely on.

The production shape has ten:

1. **Ingestion**
2. **Metadata** — so retrieval can be filtered and attributed
3. **Query understanding** — what is actually being asked
4. **Query transformation** — rewriting, expansion, decomposition
5. **Query routing** — which source or index should answer this
6. **Hybrid retrieval** — semantic plus keyword
7. **Reranking** — order by relevance, not just similarity
8. **Context compression** — cut what won't be used
9. **Prompt construction**
10. **Validation** — check the answer against the evidence

The reframe that justifies the complexity: the goal isn't retrieving *some
similar text*, it's getting the **smallest useful evidence** in front of the
model before it answers. Steps 7 and 8 are what most pipelines skip, and
they're also where [[llm-cost-scales-with-tokens]] gets paid for — less
context is both cheaper and more accurate.

"Production RAG is not chat with PDF" is the line worth remembering.
