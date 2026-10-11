---
name: call-summary
description: "Process a completed customer call into a sourced recap, follow-up email, tasks, record-linked Bigmind notes and reviewed opportunity changes."
---

# Call Summary

Read [the workflow contract](../../references/operating-contract.md) before execution. For this workflow, also read [review actions](../../references/review-actions.md), [pipeline and frameworks](../../references/pipeline-and-frameworks.md).

Resolve the exact meeting and session using `getMeetingById` and `getSessionsByMeetingId`. Read `getMeetingSummaryBySessionId`, notes and relevant transcript evidence; use `getCrmRecordsBySession` for associations and `listTodosBySession` to avoid duplicate follow-ups.

Separate decisions, our commitments, customer commitments, objections and proposed next steps. For requested email use the native email card; for requested tasks use `createTodo`; save record-linked Bigmind notes with the record-specific remember-note tool. Resolve assignees and due dates rather than inventing customer commitments.

For requested field changes prepare `reviewOpportunityUpdate`; for requested qualification findings use the framework assessment tools. Do not send an internal-only recap to a customer. Report each task/note result and each pending card independently. A request to summarize alone does not authorize those writes.
