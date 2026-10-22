---
title: LLM cost scales with tokens per request, not users
topic: ai
review: true
tags: [cost, tokens, scaling, production]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/reel/DXhDf3JEzCi/
---

The reframe: going from 1K to 100K users doesn't multiply cost because of
compute, it multiplies whatever token waste was already in every request.
Track tokens per user per day, and optimize prompt length before swapping
models.

**Input dominates.** Most of the bill is input tokens — teams routinely send
very long prompts to get short answers. Levers: trim system prompts, drop
redundant few-shot examples, and cap max output tokens so generation can't
run away.

**Context is rented compute.** Every word in the window is paid for on every
call, so at scale a few thousand tokens per request becomes millions per
day. Levers: summarize conversation history rather than replaying it,
retrieve the top few chunks instead of a dozen, and cache embeddings and
repeated responses.

**Tokenization differs between models.** The same text can tokenize
differently across providers, so measure with the model's own tokenizer
rather than assuming parity, and benchmark the same prompt across models
before comparing prices.

**Clearer prompts cost less twice over** — fewer tokens, and fewer retries
from ambiguous instructions.

Two corrections to the original post. It named "Toon" as Anthropic's
tokenizer, which is wrong — TOON is a data serialization format, unrelated,
and Anthropic uses its own tokenizer. The principle (measure natively,
don't assume equivalence) still holds. Its specific percentages and dollar
figures are also illustrative rather than sourced, so treat them as the
shape of the problem, not a quote.
