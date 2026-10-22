---
title: What happens between your prompt and the answer
topic: ai
tags: [infrastructure, latency, fundamentals]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/p/DZ6fVA4B_G1/
---

One API call fans out across several systems:

authentication → tokenization → model routing → GPU inference → safety
checks → response streaming → logging and billing

The point most worth internalizing: the overwhelming majority of the wait
isn't network or API overhead, it's generation — the model producing tokens
one at a time. That reframes latency work entirely. Shaving request overhead
is close to pointless; reducing how much the model has to *generate*, or
streaming so the user sees output as it arrives, is where the win is.

Two practical consequences:

- **Cap output length.** Latency scales with tokens produced, so an
  unbounded response is an unbounded wait (and bill — see
  [[llm-cost-scales-with-tokens]]).
- **Stream.** Perceived latency drops sharply even when total time doesn't
  move, because the first token arrives early.

Model routing is the other lever hiding in that list: sending easy requests
to a smaller model is usually a bigger latency and cost win than optimizing
anything else in the chain.
