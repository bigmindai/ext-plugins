# Build the Outreach List

## Resolve the Destination

1. Call `listLists` when the user has not provided a list ID.
2. For an existing list, call `getList`, `getListSummary`, and `getListColumns` before editing.
3. Confirm that the destination contains Targetable Account and Targetable People columns.
4. For a new list, call `createList` with template `account-outreach`. Use the returned list and columns rather than assuming IDs.

The template creates campaign-oriented account, thesis, people, and user columns. Inspect the actual returned schema because column IDs and types are authoritative.

## Build the Account Set

Use the source appropriate to the request:

- user-supplied domains or accounts;
- `searchAccounts` or `listAccounts` for CRM accounts;
- opportunity tools for re-engagement or pipeline-derived audiences;
- a previously completed revenue review;
- rows from another Bigmind List when the user identifies the source.

Apply explicit inclusion and exclusion criteria before writing. Deduplicate by normalized domain when the Targetable Account column enforces unique domains.

## Add Rows Safely

1. Map column names to IDs from `getList` or `getListColumns`.
2. Prepare row cells using the live column types.
3. Call `addListRows` in a batch for verified accounts.
4. Read the result and reconcile added versus requested rows.
5. Query targeted rows or summary counts to verify the final list state.

Do not pass column names where IDs are required. Do not create placeholder accounts with invented domains.

## Extend the Schema

Use `addListColumns` for requested research, priority, status, rationale, or outreach-draft fields. Default to input columns unless the user explicitly requests a computed or template-backed column and the live schema supports it.

Use `updateListColumn` only after resolving the exact column. Treat deletion and reordering as high-impact changes requiring explicit scope.

## Add Targetable People

1. Use `queryListTargetablePeople` to inspect current people, personas, contactability, and duplicates.
2. Call `addListTargetablePeople` with account domains, not row IDs.
3. Default to updating matching people unless the user asks for another duplicate strategy.
4. Use `updateListTargetablePeople` for verified people already in the list.
5. Use `removeListTargetablePeople` only when the user explicitly asks to remove resolved people.

Report accounts that could not be matched and people skipped for missing or duplicate identity.
