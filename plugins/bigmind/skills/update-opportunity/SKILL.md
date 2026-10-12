---
name: update-opportunity
description: "Review and apply requested connected CRM opportunity stage, amount or close-date changes through the native CRM review card."
---

# Update Opportunity

Read [the workflow contract](references/operating-contract.md) before execution. For this workflow, also read [review actions](references/review-actions.md).

Resolve the exact opportunity and current values. For stage changes use the live CRM schema's stored value. Explain evidence for suggestions; for an explicit user-specified change prepare that exact change without inventing extra edits.

Call `reviewOpportunityUpdate` with only id and requested supported fields. The user edits/selects/confirms in the app; the model must not call app-only apply tools. If the record changed, reread and create a fresh review card.

Report the actual applied fields from the result, or that the card awaits review. Next-step, owner, forecast category and opportunity creation are separate capabilities: discover a supported tool or provide a precise handoff.
