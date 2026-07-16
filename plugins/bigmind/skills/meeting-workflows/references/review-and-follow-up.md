# Meeting Review and Follow-Up

## Find the Right Conversation

- Use `listMeetings` when the user supplies a date or narrow range.
- Use `searchMyMeetings` for questions such as “What happened on my last call with ACME?” or “What is our history with Linda?”
- Use `searchMyTeamsMeetings` only for requested team scope and within the user's meeting permissions.
- Resolve an exact meeting to its session with `getMeetingById` and `getSessionsByMeetingId` before calling session-specific tools.
- If several sessions could be “the last call,” identify the latest relevant recorded session by time and participants rather than guessing.

## Choose the Evidence Depth

1. Start with the meeting summary for a normal recap.
2. Add notes for saved context and CRM-oriented outcomes.
3. Read transcript portions when the user requests exact statements, when the summary is incomplete, or when a commitment or objection needs verification.
4. Read session CRM records, scorecards, and existing todos only when relevant to the question.
5. For relationship history, combine multiple dated interactions and preserve chronology.

## Separate Evidence Types

- **Decision:** an outcome explicitly agreed in the conversation.
- **Commitment:** an action explicitly assigned or accepted, including owner and timing when stated.
- **Risk or objection:** a concern expressed by a participant or captured in meeting evidence.
- **Recommendation:** a next step inferred from the evidence; never present it as a customer commitment.

## Complete Requested Follow-Up

1. Draft the recap and proposed action list first.
2. If the user asked to save tasks or notes, resolve each destination record and required fields.
3. Use `createTodo` for requested tasks and the appropriate `rememberNoteOnAccount`, `rememberNoteOnContact`, `rememberNoteOnDeal`, or `rememberNoteOnLead` tool for requested notes.
4. Verify each returned result separately. Report partial success accurately if one of several writes fails.

Do not send a drafted email or message. Return it as a draft unless a separate authorized send tool is available.
