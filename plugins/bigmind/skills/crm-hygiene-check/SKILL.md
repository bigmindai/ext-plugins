---
name: crm-hygiene-check
description: "Audit a scoped Bigmind pipeline for missing or inconsistent values and prepare evidence-backed corrections for review."
---

# Crm Hygiene Check

Read [the workflow contract](references/operating-contract.md) before execution. For this workflow, also read [pipeline and frameworks](references/pipeline-and-frameworks.md), [review actions](references/review-actions.md).

Retrieve the scoped pipeline with complete pagination or disclose the subset. Check available amount, close date, next step, stakeholder coverage and dated activity against the workspace's actual requirements. Distinguish blank from not returned.

Do not compute time-in-stage, unchanged-for-N-days or median-cycle thresholds without history. Missing search results do not prove no proposal exists. Suggest corrections only when evidence supports them.

Return issues with source and proposed resolution. When asked to fix, prepare stage/amount/date cards and requested tasks or notes. Other fields require their own exposed write capability.
