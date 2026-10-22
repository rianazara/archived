---
title: Surviving a booking spike — queue the crowd, count in Redis
topic: smart-techniques-for-interviews
review: true
tags: [system-design, redis, concurrency]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/reel/DbQi90JtFZN/
---

Scenario: two million users arrive at the same second for a ticket release.
Letting them reach the database kills it.

1. **Virtual waiting room** — everyone lands on the load balancer and enters
   a Redis queue with a position, rather than hitting the booking service.
2. **Token system** — only the first few thousand get active tokens; the
   rest see a queue position. This converts a 2M spike into a controlled few
   thousand requests per second.
3. **Inventory in Redis, not Postgres** — decrement an atomic counter per
   train/date/coach. Atomicity means two simultaneous requests can't both
   succeed; a Lua script makes check-and-decrement one operation.
4. **Lock with a TTL** — once the decrement succeeds the seat is held for a
   few minutes while the user pays. On failure or timeout, an increment
   returns it automatically, so abandoned carts self-heal.
5. **No double booking** — an idempotency key of user + train + date,
   sharding by train and journey date, and payment handled asynchronously
   via a queue.

Summary: queue the crowd, keep inventory in an atomic in-memory counter, and
keep the database off the hot path.

Caveat: Redis-as-source-of-truth for inventory trades durability for speed —
the design needs persistence or reconciliation against the database, which
the post didn't address.
