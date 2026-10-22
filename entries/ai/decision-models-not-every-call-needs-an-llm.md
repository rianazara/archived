---
title: Small decisions don't need a paragraph
topic: ai
tags: [architecture, routing, cost, classification]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/reel/DeBA93FMMEm/
---

A pattern worth separating from the product pitching it. AI applications
make constant small decisions:

- Which model should handle this request?
- Is this input trying to bypass the rules?
- Does this retrieved document actually answer the question?

None of those need prose. They need a label, a score, or a probability your
code can branch on. Spending a full generative call — with its latency,
cost and variability — to produce a one-word answer is the wrong tool.

This isn't new; it's classification, which has decided "spam / not spam" for
decades. What's changed is that the inputs, questions and options can now be
expressed in natural language, so you get classifier economics without
building and labelling a bespoke model first.

Where it fits: *alongside* the main model, as the router, the guard, and the
relevance check. Related to the model-routing lever in
[[llm-api-call-stack]] and the guardrails layer in
[[one-full-stack-portfolio-project]].

The caveat the post itself makes, which is the right one: a structured answer
is not automatically a correct answer. You still have to evaluate those
decisions on your own data.

I'd treat the specific product claims in these posts — adoption records,
pricing, pedigree — as launch marketing, and the architectural idea as the
durable part.
