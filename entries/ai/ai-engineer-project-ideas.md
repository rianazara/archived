---
title: Project ideas that each prove one skill
topic: ai
tags: [portfolio, projects, rag, evaluation]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/reel/DZx0ajvjNJb/
---

One project per skill, each small enough to finish and specific enough to
demonstrate something:

| Skill | Project |
|---|---|
| RAG | hybrid search over internal docs, with reranking and citations |
| Agents | orchestration with tools, memory and a human-in-the-loop gate |
| LLMOps | a semantic caching layer that measurably cuts the API bill |
| Evals | a generator that builds test sets from real production logs |
| Fine-tuning | a LoRA pipeline on a domain dataset, base model to benchmark |
| Guardrails | text-to-SQL that blocks destructive queries before they run |

Two of these are unusually good signals. "Evals built from production logs"
shows you understand that test sets drift (see
[[rag-drift-and-reindexing]]), and the text-to-SQL guardrail is a real
safety problem with an observable pass/fail.

A separate post suggested domain-shaped versions of the same idea: a due
diligence copilot over filings and investor material with source-backed
findings; a clinical assistant over guidelines and papers with citations and
confidence scoring; an engineering knowledge hub over docs, repos and
incident reports to speed onboarding and troubleshooting. The common thread
in the good ones is citations and confidence — grounding you can check.

If you'd rather do one thing properly than six small ones, see
[[one-full-stack-portfolio-project]].
