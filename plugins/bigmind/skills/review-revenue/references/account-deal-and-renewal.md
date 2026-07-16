# Account, Deal, and Renewal Reviews

## Resolve the Record

1. Find the account with `searchAccounts` when the user supplies a name or domain.
2. Use `getAccountForContact` or `getAccountForDeal` when the request starts from a known contact or deal ID.
3. Confirm the intended account when multiple matches remain plausible.

## Gather Account Context

Select only relevant sources from:

- `listAccountContacts` for stakeholder coverage and roles;
- `listAccountOpportunities` for commercial context;
- `listAccountActivities` and `lookupActivityById` for engagement history;
- `listNotes` for saved context and warnings;
- `listAccountTodos` for unresolved work;
- `listAccountDocuments` for account-specific documents;
- `listSignalsForAccount` and `describeSignalById` for explicit monitored signals;
- meeting search for objections, decisions, feature requests, sentiment, and commitments;
- the authenticated user's email when relevant recent correspondence is not represented in CRM activities.

Use `getWarningsForDeals` after resolving opportunity IDs when stored warning context is needed.

## Review the Account or Deal

Summarize:

1. current commercial state and timing;
2. stakeholders, decision process, and missing coverage;
3. recent engagement and changes;
4. evidence-backed risks and positive signals;
5. explicit next steps and unresolved commitments;
6. recommended actions ordered by impact and urgency.

For “What is our history with this person?” preserve chronology and distinguish direct interactions from account-level context.

## Review Renewals and Churn

Identify renewal opportunities using returned CRM fields and requested dates. Combine opportunity state with meeting, activity, email, note, and signal evidence.

Do not claim product-usage evidence unless an accessible CRM field or signal actually provides it. When usage is unavailable, say that the assessment covers the available relationship, conversation, email, CRM, and signal evidence.

For an account-save plan, provide:

- stated or inferred churn drivers;
- evidence and confidence for each driver;
- stakeholder map and missing relationships;
- immediate recovery actions;
- medium-term success plan;
- owners and dates only when supported or requested.
