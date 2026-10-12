---
name: draft-outreach
description: "Prepare a personalized Bigmind email or multi-touch outreach sequence and complete the requested native review or enrollment flow."
---

# Draft Outreach

Read [the workflow contract](references/operating-contract.md) before execution. For this workflow, also read [review actions](references/review-actions.md), [campaigns](references/campaigns.md), [knowledge and coaching](references/knowledge-and-coaching.md).

Resolve audience, goal and destination from the request. Ground copy in real account/deal activity and approved positioning. For one email use `draftEmailToSend`; preserve a real replyContext for replies and use HTML. Unknown addresses may remain empty in the card.

For a sequence resolve an existing campaign and account row, inspect setup/state and eligible recipient keys, then prepare `draftOutreachCampaignSequences`. Use the campaign guide for offsets, reply references and receipts. If a List or campaign must be created, do so only within the requested scope through the corresponding workflow.

Do not stop at paste-ready copy when the requested supported review card can be prepared. After rendering, give a short status rather than repeating all copy. Distinguish card preparation, enrollment and actual delivery.
