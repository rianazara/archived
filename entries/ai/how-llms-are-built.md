---
title: Three stages of building an LLM — and what each failure looks like
topic: ai
tags: [fundamentals, training, alignment, debugging]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/p/DcyKbN1k00D/
---

- **Pre-training — learn.** The model processes enormous amounts of text and
  learns by predicting what comes next. This is where broad knowledge and
  language ability come from.
- **Post-training — improve.** The base model is taught to follow
  instructions and produce useful responses, via supervised fine-tuning and
  methods like LoRA.
- **Alignment — behave.** The model learns preferences, boundaries and
  behaviors that make responses safer and more helpful, through RLHF, DPO
  and other preference- or reward-based methods.

The genuinely useful part is using this as a **diagnostic**. When output is
wrong, ask which stage it belongs to:

- Missing or incorrect facts → a knowledge problem, from pre-training.
- Ignoring instructions or wrong format → a post-training problem.
- Unhelpful refusals, hedging, sycophancy → an alignment problem.

That tells you whether to reach for retrieval, better prompting, or a
different model entirely, instead of blindly rewording the prompt.

Underneath all three, the mechanics: text is split into **tokens**, the
**transformer's attention mechanism** lets the model weigh which words
relate to which, and at **inference** it generates token by token. Not
magic — probability over massive data, plus architecture.
