---
title: The AI buildout as a layered supply chain
topic: stocks
tags: [ai, semiconductors, mental-model]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/p/DZ5gyICAKrn/
---

The single idea repeated across most of this collection: AI isn't a software
story or a one-company story, it's a stack, and each layer is a different
business with different economics.

| Layer | What it does |
|---|---|
| Manufacturing equipment | lithography, deposition/etch, metrology — makes advanced chips possible |
| Foundry | actually fabricates them |
| Silicon | accelerators, server CPUs, custom ASICs |
| Memory & storage | HBM and DRAM for bandwidth, NAND/HDD for the datasets |
| Connectivity | networking chips, switches, retimers, optics — moving data between accelerators |
| Specialized cloud | GPU cloud and high-density colocation |
| Power & cooling | generation, grid, nuclear baseload, onsite power, heat removal |

Two framings worth keeping, independent of any ticker:

- **More accelerators don't automatically mean more usable compute.** If
  interconnect bandwidth or memory can't keep up, the extra silicon idles.
  That's why "where is the bottleneck forming" is the more useful question
  than "who makes the best chip."
- **Power is a real constraint, not a footnote.** Several posts argue grid
  capacity and cooling now gate data-centre expansion directly.

This matches the engineering side from the other direction — see
[[inference-is-not-training]] for why serving capacity is distributed and
latency-bound rather than a single big cluster.

_Note on sourcing: this layered framing appeared in at least six saved
posts, two of them with byte-identical captions, and several were sponsored
by a brokerage. The mental model is sound; the accompanying name lists are
marketing. Educational summary only — not investment advice, and I'm not a
licensed advisor._
