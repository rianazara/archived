---
title: Concept map for AI product interviews
topic: ai
review: true
tags: [interviews, product-management, study-map]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/p/DcOoUfok2Uh/
---

The chains to be able to walk, each left-to-right:

- LLMs → foundation models → context windows
- RAG → embeddings → vector stores → reranking
- Agents → tool calling → memory → orchestration
- Evals → groundedness → task completion rate
- Safety → guardrails → prompt injection
- Metrics → latency → **cost per successful task**
- Execution → model routing → observability

A companion post framed the same ground as questions: why LLMs hallucinate,
RAG versus fine-tuning, how RAG actually works, reducing latency, reducing
cost, agents and tool calling, evaluating AI systems, designing for
production, and security.

Both made the same caveat, which is the real point: definitions alone won't
carry an interview. The ask is to explain how these systems work, how you'd
debug them, and how you'd scale them — moving from "I know GenAI" to "I can
build GenAI systems."

"Cost per successful task" is the metric most worth stealing — it prices
failures and retries, which per-token or per-call figures hide.
