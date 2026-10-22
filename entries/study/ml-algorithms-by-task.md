---
title: Classical ML algorithms, organized by what they're for
topic: study
tags: [machine-learning, fundamentals]
created: 2026-10-22
updated: 2026-10-22
source: https://www.instagram.com/reel/DZT2G-HTwCO/
---

The useful reframe: these aren't theory to memorize, they're tools matched
to four kinds of problem — prediction, classification, clustering, and
simplification.

**Predicting a number**
- Linear regression — a straight-line relationship between inputs and a
  continuous output.

**Classifying into categories**
- Logistic regression — despite the name, predicts a probability of class
  membership.
- Decision trees — a sequence of splits; highly interpretable.
- Random forest — many trees voting, trading interpretability for accuracy.
- Support vector machines — finds the boundary with the widest margin
  between classes.
- K-nearest neighbours — classifies by whatever the closest examples are.
- Naive Bayes — probabilistic, assumes features are independent (rarely
  true, often works anyway).

**Finding groups without labels**
- K-means clustering — partitions data into k groups by proximity.

**Reducing dimensions**
- Dimensionality reduction (e.g. PCA) — compresses many correlated features
  into fewer, for visualization or to curb overfitting.

Why this still matters in an LLM-heavy world: for tabular prediction and
classification these remain the right tools, usually beating a language
model on cost, latency and accuracy — which is the same point as
[[decision-models-not-every-call-needs-an-llm]].
