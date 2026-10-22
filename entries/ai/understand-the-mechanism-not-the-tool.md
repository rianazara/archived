---
title: Knowing a tool and understanding it are different claims
topic: ai
review: true
tags: [fundamentals, system-design, interviews]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/p/DdiciQCmmOv/
---

The gap: you've used Kafka, Redis, Kubernetes, database indexes, load
balancers, CDNs and containers, and you know what each *does*. The
engineering question is what happens underneath.

The worked examples of that distinction:

- How does Kafka store and track messages?
- Why is Redis actually fast?
- How does Kubernetes know a pod has crashed?
- What does a database index really do?
- How does a CDN serve content without hitting the origin each time?

Stated as the contrast that lands in an interview: "I have worked with
Kafka" versus "I understand partitions, offsets, consumer groups, and why
Kafka is designed this way."

Why it generalizes beyond interviews — mechanism knowledge is what lets you
*debug*. You can use a tool from its documentation, but diagnosing why it's
slow, wrong or inconsistent requires a model of what it's doing internally.
The same applies to the AI stack: knowing RAG retrieves documents won't help
when retrieval quietly degrades (see [[rag-drift-and-reindexing]]).
