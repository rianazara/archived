---
title: Why stateful agents break at scale, and the fix
topic: study
review: true
tags: [system-design, agents, scaling, state]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/reel/DaPKqevsQ2y/
---

At ten users, keeping session state in memory on one process is simple and
fine. At ten million it fails, and not gradually: you can't scale
horizontally when every instance holds different state, load balancing
becomes guesswork, and a crashed pod takes its live sessions with it.
Adding capacity makes it worse.

The architectural shift, in four moves:

1. **Externalize all state.** Session state into a fast shared store,
   long-term memory into a durable one. Any worker can then serve any
   request because state is fetched, not remembered.
2. **Isolate every session.** Scoped namespaces per session, and separate
   execution environments for sensitive workloads, so one user's context
   can never leak into another's.
3. **Make workers stateless and disposable** — spawn, do the job, shut
   down. No reliance on warm instances holding anything.
4. **Make long tasks asynchronous.** Don't block a worker for a 30-second
   tool call: queue it, return a job ID immediately, notify by polling or
   webhook when it finishes.

The note on what interviewers want: not "use Kubernetes" (an answer about
tooling), but stateless workers, externalized state, session isolation,
async execution and context lifecycle management — answers about
properties.

Point 2 matters more than its one line suggests, since cross-session
context leakage is a confidentiality bug, not a performance one.
