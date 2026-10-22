---
title: There is no perfect system, only stated tradeoffs
topic: study
tags: [system-design, principles, interviews]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/p/DZrUzxKD-yf/
---

Every system design concept comes with a cost on the other side:

- speed versus flexibility
- scalability versus complexity
- consistency versus availability

The distinction drawn is between engineers who reproduce tutorial
architectures and engineers who optimize for what actually matters in a
given situation — which requires knowing what you're giving up.

Two questions to ask of any design decision:

- **What am I optimizing for?**
- **What am I sacrificing?**

Being able to answer both is most of what a system design interview is
checking. "I'd use X" is a weak answer; "I'd use X because this workload is
read-heavy and I'm willing to accept staleness in exchange for latency" is
the same choice with the reasoning attached.

It's also why the same question has several right answers — see
[[optimistic-vs-pessimistic-locking]], where both options are correct
depending on expected contention.
