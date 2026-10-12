# Lists to campaign execution

## Audience

Use `listLists`, `getListSummary`, `getListColumns` and targeted rows to resolve an existing audience. Create a requested account List with `createList` template `account-outreach`. Use actual column IDs for writes. Use `addListTargetablePeople` and related people tools rather than manually replacing people arrays. Imports have preview/import tools; inspect mappings and duplicates before import. `importListCSV`, `importListCSVRows` and `importListJSONL` consume the uploaded file, so a subsequent import attempt requires a new upload. Verify whether the first import succeeded before retrying to avoid duplicate lists or rows. Matching CSV imports can overwrite existing cells; keep campaign audience changes off unless requested.

Research with CRM history and `researchCompanyByDomain`; use individually exposed connected enrichment tools only when available and relevant. `listListEnrichmentTools` and `listListColumnActions` read catalog metadata and schemas; they do not execute providers or actions. Provider calls may consume credits; keep them within the requested people, rows and research scope. Use `enrichListTargetablePersonField` or its bounded batch counterpart when exposed for missing people fields.

`runList`, `runListRow`, `runListColumn` and `runListCell` remain assistant-callable for configured list workflows. Choose the requested scope. After inspecting failures, use `retryListExecutionErrors({tableId})` for the whole list, `retryListRowErrors({tableId, rowId})` for one row, or `retryListColumnErrors({tableId, columnId})` for one column. The whole-list retry no longer accepts `scope` or `targetId`. Use only the retry tools available in the connected inventory, and change `autoRunNewRows` with `updateListExecutionSettings` only when requested. Queued work is not completed research: read execution status and resulting cells before reporting completion. Preserve sources and contactability gaps.

Existing underlying actions are also exposed individually when authorized, including `planEmailOutreach`, `slack_notifySlackChannel` and `slack_notifySlackUser`. Their live schemas take an existing matching `listContext` and resolved `inputs`; direct calls do not evaluate column templates, run dependencies, or mark list cells completed. Use the existing list runners for saved column mappings and list results. Do not execute both a direct action and its list run for the same requested effect.

Before `upsertPeopleEnrichmentStrategy` or `configureListPeopleFieldEnrichment`, read the current strategy/column and resolve the requested change. An existing strategy ID updates its saved settings; field configuration can overwrite bindings, and null can remove enrichment or fallback settings. Preserve unrelated configuration.

For an interactive Lists UI, use `openBigmindLists` to browse or `openBigmindList` with `tableId` and optional `viewId` to open a list, when those tools and MCP Apps rendering are available. For assistant-side configuration reads, discover the separate `listListConfigurationUsers`, `listListConfigurationGroups`, `listListConfigurationAgents`, `listListConfigurationAgentModes`, `listListConfigurationCustomTools`, `listListConfigurationSenders`, `listListConfigurationDocuments`, `listListConfigurationIcps`, `listListConfigurationCrmObjects`, or `listListConfigurationCrmFields` tools as needed. Each requires `tableId`; agent modes also require `agentId`, and CRM fields require `objectName`. The former model-callable `getListConfigurationCatalog` is replaced by these tools; the UI keeps its own app-only adapter.

## Campaign setup and preview

Discover `listOutreachCampaigns`; read `getOutreachCampaign` and its access.allowedActions. Call `getOutreachCampaignSetupOptions` for valid audience, people, sender, user/team and skill IDs. Create with `createOutreachCampaignDraft` or edit the resolved campaign with `updateOutreachCampaign`. Preserve expectedUpdatedAt when available. If an edit requires a plan reset, show that consequence and obtain explicit approval before confirmPlanReset=true.

Validate with `validateOutreachCampaign`. For a requested test use `generateOutreachCampaignTestPreview` on 1–5 explicit rows, inspect progress, then read test sequences. Validation and preview neither activate nor send a campaign. Starting a campaign and full-audience generation remain UI-only in the audited MCP contract; link to the returned campaign URL for activation rather than inventing a start tool.

## Supply sequences

For an active campaign configured for supplied sequences, submission schedules outreach in Daily Plan for the user to review and approve in the Bigmind UI before it can be sent. Submission and Add to campaign do not approve or send messages.

To submit:

1. Resolve an existing account row in its audience.
2. Call `getOutreachCampaignSubmissionTargets` for rowId and campaignId. Respect eligibility/reasons and exact recipientKey values; adding a person to a List does not prove campaign eligibility.
3. Build complete sequences using the live schema. First touch is day 0; offsets are nondecreasing days after the first touch. Replies reference an earlier email's 1-based touch number. LinkedIn acceptance branches reference a real earlier connection request. Supported content includes email, call scripts, LinkedIn profile views, connection requests and messages; these are planned tasks, not proof of executed calls or LinkedIn actions.
4. Use basic HTML for email bodies. Campaign sender signatures are appended automatically. Proposed delays are suggestions; campaign rules and sender capacity determine actual slots.
5. Follow [review-actions.md](review-actions.md) for the card or explicitly authorized direct submission. Retain a unique submissionId per submission; retry identical input with the same ID. A pending receipt is accepted for automatic processing, not a reason to submit again with a new ID.
6. Read `listOutreachCampaignSuppliedSequences`, paginating as needed, for actual schedules and task state. Report accounts/people enrolled, rejected or pending separately from messages sent.

One sequence per person per campaign; submission does not overwrite an existing sequence. Use `updateOutreachCampaignEmail` for unsent copy after reading rowId and stepId; use expectedManualEditedAt where available. `removeOutreachCampaignSequence` removes all people sequences for an account row and cancels unfinished work, so resolve that broader scope before removal. It preserves completed history and does not delete the audience account.
