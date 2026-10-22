---
title: Techniques for making inference faster and cheaper
topic: ai
review: true
tags: [inference, optimization, vocabulary]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/p/DemU7U7meZc/
---

Vocabulary for the serving side, which is a different discipline from
building the application:

- **Quantization** — store and compute weights at lower precision, trading a
  little quality for large memory and speed gains.
- **Knowledge distillation** — train a smaller model to imitate a larger
  one's behavior.
- **KV caching** — reuse attention state across generated tokens instead of
  recomputing it each step.
- **Continuous batching** — keep the GPU fed by admitting new requests as
  others finish, rather than waiting for a whole batch.
- **Speculative decoding** — a cheap model drafts tokens, the expensive one
  verifies them in parallel.
- **Tensor parallelism** — split individual layers across devices.
- **Pipeline parallelism** — split the model by layer stages across devices.

Why it's worth knowing even if you never implement any of it: these are what
providers do on your behalf, and they explain the price and latency
differences you observe between model tiers. They're also the honest answer
to "how would you reduce cost" when prompt-level fixes
([[llm-cost-scales-with-tokens]]) are exhausted.

The post listed names only — no explanations — so the one-liners here are
mine, and each is worth reading properly before relying on it.
