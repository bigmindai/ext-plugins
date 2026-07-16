# Research, Prioritize, and Draft

## Research Accounts

Use relevant private Bigmind context first: account records, opportunities, activities, meetings, notes, todos, signals, and company-library knowledge.

Use `researchCompanyByDomain` when public-web company research is requested or necessary for the account thesis. Preserve returned source URLs and distinguish public research from private relationship evidence.

For each account, produce a compact thesis containing:

- why the account fits the audience;
- relevant business trigger or initiative;
- relationship or opportunity context;
- likely value hypothesis;
- evidence and confidence;
- missing information.

Store research with `updateListCells` only after mapping row and column IDs.

## Prioritize Accounts

Use the user's scoring rule when supplied. Otherwise propose a transparent rubric based on available evidence, such as fit, timing, engagement, explicit signals, relationship strength, and contactability.

Do not call a heuristic score “predictive.” Do not treat missing values as negative evidence. State the analyzed row count and any rows omitted because data was incomplete.

## Select People

Use `queryListTargetablePeople` to filter by requested persona, target flag, contact channel, or text. Prefer stakeholders relevant to the outreach hypothesis rather than selecting every available person.

Do not fabricate an email, phone number, LinkedIn URL, title, persona, or biography. Surface contactability gaps for review.

## Draft Outreach

Ground each draft in the account thesis, relevant relationship history, and approved company knowledge. Avoid implying facts that come only from speculation.

For re-engagement, acknowledge the previous relationship accurately and use the actual loss or timing context when available. Do not claim a previous conversation, objection, or commitment without evidence.

Store drafts only when the user asks. Use a compatible existing column or add a clearly named input column, then write with `updateListCells` using the live schema. Keep each draft reviewable and avoid overwriting existing copy without explicit intent.

Return drafts as drafts. Do not send, schedule, or launch outreach.
