# Tracker Recipes

## Choose a Tracker Type

- **competition:** detect competitor mentions and optionally write cited findings through a battlecard template.
- **product_feedback:** capture product feedback and optionally connect findings to a product document.
- **keyword:** match explicit words or phrases.
- **concept:** detect semantic concepts using positive and excluded examples.
- **manual:** support captures users add manually rather than automatic detection.

Use the exact live schema and returned enum values.

## Common Setup

1. Call `listTrackers` and compare names, type, status, scope, and dependencies.
2. Resolve requested owner users or teams with `searchUsers`, `listTeams`, and `listTeamMembers`.
3. Define `mentioned_by_filter` from the user's intent: anyone, organization representatives, or external participants.
4. Define meeting-owner scope as all permitted owners, selected users, or selected teams.
5. Draft detection inputs and output instructions.
6. Call `createTracker` for a clearly requested new tracker or `updateTracker` for an explicitly selected existing tracker.
7. Verify the result with `getTracker`.

## Competition Tracker

1. Define the competitor name, product names, spoken variants, abbreviations, and meaningful exclusions.
2. If the user requests a battlecard template, call `listDocumentTemplates` with purpose `battlecard`.
3. Read the selected template using `getDocumentById` before using its ID.
4. Do not attach a template selected only by a vague name match; disambiguate using title, purpose, instructions, and preview.
5. Create a tracker of type `competition` with the resolved scope and optional `battlecard_template_id`.

Example intent: “Track external mentions of Gong and Gong.io across my sales team using our competitor battlecard template.”

## Product-Feedback Tracker

1. Define the feedback area and representative positive examples.
2. Add excluded examples to avoid generic praise, support questions, or unrelated feature names.
3. If the user wants cited findings written to a product document, discover the actual product document with `listLibraryDocuments` and inspect it with `getDocumentById`.
4. Create a tracker of type `product_feedback` with the optional `product_document_id`.

## Keyword or Concept Tracker

Use a keyword tracker for exact phrases that should not require interpretation. Use a concept tracker for varied language expressing the same idea, such as pricing objections, legal concerns, timeline risk, or next-step commitment.

For concepts, include diverse positive examples and hard negative examples. Avoid overbroad descriptions such as “track risk” without examples or exclusions.

## After Creation

Return the created ID, status, detection inputs, participant filter, meeting-owner scope, and linked template or document. Explain that future or existing capture behavior depends on Bigmind processing; do not promise historical backfill without explicit tool evidence.
