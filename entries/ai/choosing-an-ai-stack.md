---
title: Choose the AI stack from the job, not the diagram
topic: ai
tags: [architecture, tooling, open-source]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/p/DekCJNiEw3n/
---

A stack can look impressive on a diagram and still be wrong for what you're
building. The sequence that avoids that: define one job the app must do
well, then add only the layer that serves it — retrieval if it needs answers
from your documents, memory if it needs continuity across conversations.
Each tool should solve a problem you can name and test.

**A distinction worth getting right:** *open source*, *open weights* and
*self-hosted* are not interchangeable.

- **Open source** — the code is available under a license, which may or may
  not permit what you want to do.
- **Open weights** — the model parameters are downloadable, but that says
  nothing about training data, code, or license terms.
- **Self-hosted** — it runs on your infrastructure, which is a deployment
  choice independent of either of the above.

So the three questions are: what may I modify, where does it run, and what
does the license actually allow? Those come apart constantly — plenty of
downloadable models carry use restrictions that make them unusable
commercially.

Closing rule: build one working path first, and add complexity only when you
can state the need. Same instinct as [[rag-architectures]], where reaching
for the sophisticated option by default is the common mistake.
