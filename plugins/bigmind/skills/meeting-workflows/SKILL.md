---
name: meeting-workflows
description: Prepare for upcoming customer meetings, review past calls, recover account or contact conversation history, summarize transcripts and notes, identify decisions and commitments, and create requested follow-up tasks or CRM notes using Bigmind. Use for meeting preparation, call recaps, meeting summaries, action items, next steps, and post-meeting follow-up.
---

# Bigmind Meeting Workflows

Use authorized Bigmind meetings, CRM context, email, signals, and company knowledge to prepare for or follow up on customer conversations.

## Run the Workflow

1. Classify the request as upcoming preparation, past-meeting review, relationship history, or follow-up action.
2. Resolve the date range, meeting owner scope, meeting, account, and session before retrieving detailed artifacts.
3. Gather only the evidence needed for the requested outcome.
4. Separate explicit customer statements and commitments from recommendations or inference.
5. Perform a write only when the user explicitly asks to create or save something.
6. Verify the tool result and report exactly what changed.

Use `whoami` when connected user or workspace context is unclear. Never invent meeting content, attendees, CRM associations, IDs, decisions, or action items.

## Select the Right Path

- For an upcoming meeting or schedule-based preparation, read [references/preparation.md](references/preparation.md).
- For a past call, relationship history, recap, transcript review, or follow-up, read [references/review-and-follow-up.md](references/review-and-follow-up.md).

## Resolve Meeting Evidence

- Use `listMeetings` for a defined date range, schedule questions, and exact meeting selection.
- Use `searchMyMeetings` for semantic questions over the connected user's past conversations.
- Use `searchMyTeamsMeetings` only when the user asks about permitted team conversations.
- Use `getMeetingById` and `getSessionsByMeetingId` to resolve the meeting-to-session relationship.
- Use `getMeetingSummaryBySessionId` for a concise recap, `getMeetingNotesBySessionId` for saved notes, and `getMeetingTranscriptBySessionId` when exact wording or deeper evidence is necessary.
- Use `getCrmRecordsBySession` to identify CRM records associated with a session.
- Use `getSessionScorecards` and `listTodosBySession` only when coaching results or existing follow-up tasks are relevant.

Preserve inline citation markers returned by `searchMyMeetings`, `searchMyTeamsMeetings`, and `searchCompanyLibrary`. Do not cite a result that does not support the adjacent claim.

## Apply Follow-Up Safeguards

- Drafting an action item, note, or follow-up message is not authorization to save or send it.
- Use `createTodo` only after the user asks to create a task. Preserve the requested owner, association, and due date; ask when a required value is ambiguous.
- Use the record-specific note tool only after resolving whether the target is an account, contact, deal, or lead.
- Do not claim to send email, create calendar events, or modify a meeting; this app exposes no such action.
- Treat todo and CRM-note writes as potentially synchronized beyond Bigmind and describe the effect accurately.

## Present the Result

For preparation, lead with the meeting objective, account and opportunity context, recent developments, risks, unresolved commitments, and recommended questions.

For review, lead with what happened, decisions, explicit commitments, risks or objections, and next steps. Label inferred recommendations separately from commitments found in the evidence.

For completed writes, list the exact tasks or notes created and include returned identifiers when useful. If no meeting or session is found, state the searched scope and propose the narrowest next query.
