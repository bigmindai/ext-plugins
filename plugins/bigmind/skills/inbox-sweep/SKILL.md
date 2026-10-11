---
name: inbox-sweep
description: "Triage accessible customer email or Bigmind Inbox work and prepare relevant replies and follow-ups."
---

# Inbox Sweep

Read [the workflow contract](../../references/operating-contract.md) before execution. For this workflow, also read [review actions](../../references/review-actions.md).

Check the actual inventory. Use `queryUserEmail` only if exposed, for the authenticated user's mailbox, starting with a bounded overview and retrieving bodies for relevant messages. Its implementation alone does not guarantee MCP availability. Deal/account-linked email can be researched separately but is not a full mailbox sweep.

If only `listInboxItems` is available, explicitly offer/use the Bigmind work Inbox when it matches the request; do not label it unread email. Prioritize customer commitments and time-sensitive replies from available evidence.

Prepare requested replies with real threading context via the email card and manage requested tasks through Inbox/todo actions. State mailbox and coverage gaps; no inferred access to teammates' private mail.
