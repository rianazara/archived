---
title: Optimistic versus pessimistic locking
topic: study
review: true
tags: [databases, concurrency, system-design]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/reel/DaPPktuxC1f/
---

Two users click "book this seat" in the same millisecond. Requests still
arrive sequentially — network routing differs by microseconds — and each
runs inside a transaction, with isolation levels keeping parallel
transactions from corrupting each other. The design question is which
locking strategy you choose.

**Pessimistic — lock the row early.** The first request issues a
`SELECT … FOR UPDATE`, taking an exclusive lock. The second waits in line
until the first transaction completes. Right for **high contention**: a
popular release where many people genuinely collide on the same row, and
you'd rather make people queue than fail them after they've started paying.

**Optimistic — check a version at the end.** Both transactions read
`version = 1`. The faster one updates and increments to 2. When the slower
one tries to commit, the mismatch is detected, the update is rejected, and
the user gets "already taken." Right for **low contention**, where conflicts
are rare and holding locks would cost more than occasionally retrying.

The tradeoff in one line: pessimistic pays in waiting, optimistic pays in
failed work. Pick by how often you actually expect collisions.

Related: [[system-design-booking-spike]] uses an atomic in-memory
decrement to sidestep database locking entirely, which is a third answer to
the same problem.
