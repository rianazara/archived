---
title: Ask for the architecture before asking for the code
topic: study
tags: [claude-code, prompting, workflow]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/p/DZzzH4Cje60/
---

The common failure: "write the code," which returns messy output, incidental
bugs, and files you don't understand well enough to maintain.

The suggested reordering is to ask for the senior-engineer work first:

- design the architecture and explain the intended file structure
- audit the existing codebase before changing it
- identify bottlenecks rather than optimizing by guess
- review for security risks
- prepare deployment

Why it works beyond the framing: each of those produces an artifact *you*
can evaluate before any code is written, which is when changing direction is
cheap. It also surfaces disagreements about approach while they're still
sentences rather than files.

The same idea as [[prd-before-you-build]] — clarity first — and it pairs
with [[claude-md-instruction-files]], since the architectural decisions you
settle this way are exactly what belongs in a persistent instructions file
instead of being re-litigated each session.
