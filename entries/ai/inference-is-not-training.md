---
title: Inference is a different infrastructure problem from training
topic: ai
review: true
tags: [infrastructure, inference, latency]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/reel/Ddmb4F8PhmZ/
---

Most people learned how AI infrastructure works from the *training* story:
huge batch jobs, throughput over latency, data and compute in one place,
delays measured in days.

Serving is close to the opposite — millions of latency-sensitive requests,
GPU capacity scattered across providers and regions, and the data sitting
somewhere else again.

The consequence: putting compute near your users is only half the problem.
The other half is connecting distributed GPU pools, storage and data over
private low-latency links rather than the public internet, since a fast
model behind a slow data path is still a slow product.

Worth holding alongside [[llm-api-call-stack]] — that entry says most
latency is generation, which is true *per request*; this one is about where
the request has to travel and whether capacity exists near the user at all.

Disclosure: this was a sponsored post for a connectivity vendor, so the
"this is where the next race is" framing is self-interested. The underlying
training-versus-serving distinction is real and commonly missed.
