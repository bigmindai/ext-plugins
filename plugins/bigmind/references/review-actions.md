# Native review actions

These contracts were checked against monorepo commit dc5f7c754 (2026-10-11). The connected inventory and returned schema remain authoritative. Bigmind's broader platform capabilities do not imply that every action is available in every MCP client.

## Email

Use `draftEmailToSend` to prepare the native editable email card. Supply subject and basic HTML body; use verified recipient addresses, or leave `to` empty when unknown so the user can fill it in. For a reply, copy the exact source `replyContext` (emailAccountId and threadId); do not invent threading identifiers. The user chooses an eligible sender and clicks Send email.

This tool does not send. `sendReviewedEmail` is app-only: do not call it from the assistant, simulate the confirmation, or use another send path to bypass the card. Once the card is displayed, acknowledge briefly without repeating the complete email. Report sent only from a successful send result; a canceled card remains unsent. If the result is uncertain, verify Sent mail through an available authorized read or ask the user to check before attempting another send. operationId alone is not a guaranteed server-side send deduplication mechanism.

The current MCP email card supports sending, not scheduling or arbitrary attachments. Bigmind has additional internal email capabilities; only use them if a separately exposed tool actually supports the requested operation. Otherwise retain the draft and explain the handoff.

## Opportunity changes

Resolve the opportunity through account opportunities or a pipeline view. Inspect the current record and `listCrmSchema` when exact stage values are needed. Use `reviewOpportunityUpdate` with `id` and only the requested supported changes: numeric `amount`, date-only `closeDate` (YYYY-MM-DD), and exact CRM `stage` value. Labels are not necessarily stored values. Do not pass next-step, owner, forecast category, arbitrary fields or null-clearing operations to this card.

The card shows current/proposed values and lets the user edit, select and confirm. `applyReviewedOpportunityUpdate` is app-only. A prepared card is not a saved CRM change. The service detects concurrent changes to selected fields: if stale, reread and prepare a new card for review, never force the old values. Confirm the actual saved values, including user edits, from the completion result or an authorized readback.

Opportunity creation exists in Bigmind's internal UI, but this commit adds no external creation card. Discover an actual create tool before promising creation; otherwise produce a creation-ready proposal and hand off to Bigmind.

## Sequence enrollment

For interactive review use `draftOutreachCampaignSequences`, with the exact eligible recipient keys from `getOutreachCampaignSubmissionTargets`. The user edits recipients/messages/delays and clicks Add to campaign. This card does not enroll by itself. Read [campaigns.md](campaigns.md) before assembling a sequence.

`submitOutreachCampaignSequences` is also a model-callable mutation. Use it directly only when the user explicitly requests submission of a resolved sequence to a resolved active campaign and a review-card interaction is not required by their request or client permissions. Do not call it after opening a card to bypass confirmation or as an automatic fallback when the card is canceled/unavailable. Never submit both paths for the same action.

Distinguish accepted/pending enrollment from scheduling and delivery. Verify receipt and `listOutreachCampaignSuppliedSequences`; preserve submissionId on an identical retry. A user-edited sequence is the authoritative submitted content.

## Client without MCP Apps

If a review tool or app renderer is unavailable, provide the prepared content and a clear Bigmind handoff. Do not claim an invisible card was confirmed. Do not invoke app-only tools through raw RPC, browser automation or another connector to complete its confirmation. Complete independent authorized tasks/notes and report the remaining review step.
