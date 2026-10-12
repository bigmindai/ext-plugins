---
name: forecast
description: "Prepare a scoped revenue forecast narrative from connected CRM opportunities and explicit forecast mappings, with evidence and supported review actions."
---

# Forecast

Read [the workflow contract](references/operating-contract.md) before execution. For this workflow, also read [pipeline and frameworks](references/pipeline-and-frameworks.md), [review actions](references/review-actions.md).

Resolve period, pipeline, owner scope and currency. Retrieve open and closed-won records required for the forecast. Prefer native forecast-category fields when available; otherwise obtain or label a stage-to-bucket mapping. State whether bucket totals are exclusive or cumulative to avoid double counting.

Return booked, commit, best case and pipeline with counts, supporting deals, risks and asks. Compare snapshots/history only when present; otherwise omit change claims. Do not submit or lock an official forecast.

Prepare requested supported stage/amount/date corrections through the opportunity card. The current card does not change forecast category; return that proposal separately unless a tool supports it.
