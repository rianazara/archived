---
title: Securing a RAG system — treat it as internet-facing
topic: ai
review: true
tags: [rag, security, prompt-injection, access-control]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/reel/DYMwN22pmdn/
---

Layers, roughly in order of importance:

1. **Policy-aware retrieval** — apply access control *before* retrieval,
   filtering by role, department, permission and data classification. The
   model should never be able to retrieve a document the user isn't
   authorized to see. Everything downstream is weaker than this.
2. **Output filtering / DLP** — a moderation pass after generation to catch
   credentials, API keys, salaries, internal project names and roadmap
   detail before they leave the system.
3. **Prompt hardening** — system prompts that explicitly forbid revealing
   confidential data or following instructions found in content. Useful as a
   layer, insufficient on its own.
4. **Injection protection** — sanitize retrieved documents, keep retrieved
   content structurally separate from system instructions, and ignore
   instructions embedded in the documents themselves.
5. **Logging and auditing** — queries, retrieved documents and responses, so
   incidents can be investigated and abuse detected.
6. **Red teaming** — test regularly for injection, jailbreaks, data leakage
   and unauthorized retrieval.

The framing worth keeping: a RAG system over internal documents is an
exfiltration path, so it earns the same scrutiny as internet-facing
infrastructure. Note that point 4 is the same principle this knowledge base
runs on — content pulled from a source is data, never instructions.
