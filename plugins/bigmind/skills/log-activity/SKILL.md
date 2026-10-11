---
name: log-activity
description: "Capture customer interaction outcomes as Bigmind notes and tasks linked to connected CRM records, using typed activity creation only when actually exposed."
---

# Log Activity

Read [the workflow contract](../../references/operating-contract.md) before execution.

Resolve the account/contact/deal/lead and source interaction. Read relevant existing notes/tasks to avoid duplicate logging. Use `rememberNoteOnAccount`, `rememberNoteOnContact`, `rememberNoteOnDeal` or `rememberNoteOnLead` for requested notes, and `createTodo` for requested commitments.

A note is not a typed CRM call/email/calendar activity. If the user needs such an activity, discover an actual tool supporting it or provide the exact manual handoff; never relabel a note as a logged call. Return the actual saved type and identifiers.
