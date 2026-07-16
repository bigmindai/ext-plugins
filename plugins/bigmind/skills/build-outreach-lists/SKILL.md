---
name: build-outreach-lists
description: Build and enrich campaign-ready Bigmind account-outreach Lists by selecting target accounts, creating the account-outreach template, adding account rows and targetable people, researching company context, prioritizing prospects, and drafting personalized outreach. Use for target-account lists, prospect research, re-engagement lists, stakeholder selection, account theses, and outreach planning or copy—not campaign launch or message sending.
---

# Bigmind Outreach Lists

Turn a defined audience into a researched, reviewable Bigmind List. Preserve source evidence, use the specialized targetable-person tools, and stop before campaign launch or message sending.

## Run the Workflow

1. Define the audience, qualification criteria, exclusions, desired list, research depth, and requested outreach deliverable.
2. Resolve whether to create a new list or update an existing one.
3. Build or inspect the list schema before writing rows or cells.
4. Add accounts using verified domains, then add targetable people with the dedicated people tools.
5. Research and prioritize only the requested scope.
6. Draft outreach grounded in account, relationship, and company-library evidence.
7. Verify row, account, people, and draft counts and report skipped records.

Use `whoami` when workspace context is unclear. Never invent account domains, people, contact channels, CRM IDs, research findings, or tool results.

## Select the Right Recipe

- To create, inspect, or populate an account-outreach List, read [references/build-list.md](references/build-list.md).
- To research accounts, select people, prioritize rows, or draft outreach, read [references/research-and-draft.md](references/research-and-draft.md).

## Apply List Safeguards

- Call `listLists` when the user has not supplied a list ID. Disambiguate similar names before editing.
- Inspect `getListSummary`, `getListColumns`, and targeted rows before mutation.
- Prefer `createList` with template `account-outreach` for a new campaign-ready account list.
- Map column names to IDs before `addListRows` or `updateListCells`; these tools require column IDs.
- Use `addListTargetablePeople`, `updateListTargetablePeople`, and `removeListTargetablePeople` instead of raw cell updates for people arrays.
- Prefer batch writes for verified sets. Report duplicate, missing-domain, unmatched-account, or skipped-person results.
- Require explicit target and scope before deleting rows, columns, or a list, reordering columns, or broadly overwriting cells.

## Respect the Outreach Boundary

This workflow can create Lists, research accounts, choose targetable people, develop account theses, prioritize prospects, and draft copy. The submitted Bigmind tools do not expose campaign launch or email/message send actions.

Never claim that a campaign was created, scheduled, launched, or sent. Treat outreach content as a draft for review. If another authorized tool is added later, follow its separate approval and safety requirements.

## Present the Result

Report:

1. list name and ID;
2. audience and selection criteria;
3. accounts added, updated, skipped, or unresolved;
4. targetable people added or updated and contactability gaps;
5. research and prioritization method;
6. drafts created and where they were stored;
7. review steps required before campaign use.

Do not repeat the entire list in chat when a concise summary and list identifier are sufficient.
