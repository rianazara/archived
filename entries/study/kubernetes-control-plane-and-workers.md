---
title: Kubernetes — control plane versus worker nodes
topic: study
tags: [kubernetes, devops, fundamentals]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/reel/DaahUF1xV6p/
---

The split that every Kubernetes question starts from:

**Control plane — the brain.** Decides what should be running.

- **API server** — the front door; everything talks through it.
- **etcd** — the cluster's state store, the source of truth.
- **Scheduler** — decides which node a new pod lands on.
- **Controller manager** — watches actual state and drives it toward
  desired state.

**Worker node — the muscle.** Actually runs the work.

- **Kubelet** — the agent that starts and reports on containers.
- **Kube-proxy** — handles networking rules so services are reachable.
- **Container runtime** — runs the containers, inside which sit your pods.

The mental model that makes it stick: you declare desired state to the API
server, it's persisted in etcd, and controllers continuously reconcile
reality toward it. "Self-healing" is just that reconciliation loop — nothing
restarts a crashed pod because it noticed a crash, it restarts because
actual state stopped matching declared state.

Being able to say which component does what, in order, is the bar here.
