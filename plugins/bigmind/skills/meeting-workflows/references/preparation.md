# Meeting Preparation

## Build the Meeting Set

1. Convert relative dates such as “next week” into an exact range in the user's timezone.
2. Call `listMeetings` with forward direction for upcoming meetings.
3. Apply requested owner scope and `externalOnly` when the request is specifically about customer meetings.
4. Exclude calendar-only events when the task requires recorded conversation history, but retain them when preparing for a future meeting.
5. If multiple meetings share a similar title or account, disambiguate with date, attendees, and CRM associations.

## Gather Context

For each selected meeting:

1. Resolve the account with returned CRM associations or `searchAccounts`.
2. Read relevant contacts, opportunities, recent activities, notes, todos, documents, and account signals.
3. Search past meeting content for unresolved commitments, objections, decisions, and stakeholder concerns.
4. Query the authenticated user's email only when recent email context is material. Start with a narrow date range and small page; retrieve bodies only when needed.
5. Search the company library for approved positioning, proof points, case studies, or product context relevant to the agenda.

Do not automatically call every account tool. Prefer the smallest evidence set that can change the preparation brief.

## Produce the Brief

Use this structure when useful:

1. **Meeting** — time, attendees, account, and known purpose.
2. **Relationship context** — recent conversations and stakeholder roles.
3. **Commercial context** — active opportunity, stage, amount, timing, and known risks.
4. **Recent developments** — activities, emails, signals, or commitments since the last call.
5. **Recommended focus** — questions, talking points, risks to address, and desired outcome.

Keep facts tied to Bigmind evidence. Label strategic advice as a recommendation.
