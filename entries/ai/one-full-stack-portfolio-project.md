---
title: One project that touches every layer beats ten demos
topic: ai
tags: [portfolio, interviews, production, evaluation]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/reel/DZsUJu5PrGF/
---

The argument: you don't need ten projects, you need one that goes through
the whole stack the way production does. The layers named:

- **RAG pipeline** — chunking strategy, embeddings, vector store, hybrid
  search plus reranking, retrieval you can actually tune
- **Eval harness** — benchmark sets, LLM-as-judge, regression tests so
  quality can't silently degrade
- **Guardrails** — prompt-injection defense, input/output validation, PII
  redaction, refusal handling
- **Performance** — semantic caching, token streaming, batching
- **Model strategy** — RAG versus fine-tuning, model tiering, fallback
  routing when the primary fails
- **Agentic layer** — multi-agent orchestration, and why each step exists
- **Observability** — traces, token counts, p95 latency, cost per request
- **Feedback loop** — capture thumbs up/down, log edge cases, route them
  back into evals
- **Reliability** — rate limiting, auth, retries, timeouts, graceful
  degradation
- **Serving** — a clean API, containerized, at a live URL, not a notebook
- **Docs as case study** — problem, decisions, tradeoffs and metrics a
  reader can skim in a minute

The sentence that makes it a study plan rather than a checklist: *each layer
is a decision, and each decision is an interview question waiting to
happen.* Most candidates can discuss models; far fewer can discuss keeping
one running.

Pairs with [[proving-an-agent-works]] — the eval harness is the layer that
converts "I built it" into "I can show it works."
