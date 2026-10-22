---
title: "How do you know your agent works?" — build the eval harness
topic: ai
tags: [evaluation, llmops, observability, interviews]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/p/DaZXaVpGO1j/
---

Framed as the question AI engineering interviews now open with, and the one
most candidates have no concrete answer to.

The answer is an artifact, not an opinion — a head-to-head harness that
benchmarks agents the way an LLMOps team would:

- A **experiment runner** to execute the same task set across variants
  (Langfuse's `run_experiment()` was the example).
- **Two scoring modes** — exact match where there's a ground truth, plus an
  LLM-as-judge for open-ended output.
- **Cost and latency tracked per model, per task**, not just quality.
- A **leaderboard** as the output, so comparisons are reproducible.

The distinction being drawn: "I shipped an agent" versus "I proved my agent
works." The second is a portfolio artifact and an interview answer at the
same time.

Pairs with [[seven-layers-of-ai-engineering]], whose principle "evaluation
before optimization" is the same idea stated as a rule.
