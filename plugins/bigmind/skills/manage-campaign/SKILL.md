---
name: manage-campaign
description: "Configure, validate, preview and manage Bigmind outreach campaigns, supplied sequences, unsent messages and enrollment receipts."
---

# Manage Campaign

Read [the workflow contract](references/operating-contract.md) before execution. For this workflow, also read [campaigns](references/campaigns.md), [review actions](references/review-actions.md).

Resolve the campaign or requested new campaign and audience. Read current state, setup options and allowed actions before mutation. Apply requested configuration and validate it; use only explicit bounded test rows for preview.

For active supplied-sequence campaigns resolve eligible targets, prepare native sequence review or carry out explicitly authorized direct submission as described in the action contract. Inspect receipts and actual schedules. Use dedicated unsent-email edits and account-sequence removal tools with exact scope.

Campaign activation/full-audience generation currently require Bigmind UI. Keep draft, previewed, active, enrolled, scheduled and delivered states distinct; do not infer delivery from accepted submission.
