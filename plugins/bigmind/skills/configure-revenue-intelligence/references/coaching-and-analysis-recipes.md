# Coaching and Analysis Recipes

## Meeting Categories

1. Call `listCategories` and inspect a candidate with `getCategory` before updating it.
2. Use `createCategory` for a clearly requested new category and `updateCategory` for an explicitly selected one.
3. Preserve existing classification structure unless replacement is requested.

## Custom Vocabulary

1. Call `listCustomVocabulary` before adding or changing a term.
2. Use `createCustomVocabulary` for a new company, product, acronym, person, or domain term that improves transcription and summarization.
3. Use `updateCustomVocabulary` only for the resolved existing term.
4. Avoid adding ordinary words or unsupported speculative spellings.

## Frameworks

1. Call `listFrameworkTemplates` when the user references a framework template or wants guidance.
2. Inspect an existing framework with `getFramework` before modifying it.
3. Use `createFramework` with UI-compatible components, tracker links, and CRM mappings from the live schema.
4. Do not guess CRM field IDs or tracker IDs.

## Scorecards

1. Discover existing scorecards with `listScorecards`.
2. Inspect draft and staged settings with `getScorecardDraft`.
3. Use `createScorecard` to create a draft.
4. Add questions with `createScorecardQuestion`; update only resolved questions with `updateScorecardQuestion`.
5. Use `updateScorecardDraft` for top-level fields or staged settings.
6. Call `publishScorecard` only when the user explicitly asks to publish or activate the completed draft.
7. Verify whether the result is still a draft or is active.

## Talking Points

1. Discover with `listTalkingPoints` and inspect the selected template with `getTalkingPoints`.
2. Use `createTalkingPoints`, then create ordered sections and questions with `createTalkingPointSection` and `createTalkingPointQuestion`.
3. Preserve section and question structure during updates unless replacement is requested.
4. Report visibility and object type.

## Coaching Simulations

Use `listCoachingSimulations` and `getCoachingSimulation` before update or deletion. Create or update only the exact simulation requested. Treat `deleteCoachingSimulation` as destructive and require an unambiguous user request naming the target.

## Verification

After any configuration write, read the returned object or call the corresponding get tool. Report unresolved dependencies, unpublished drafts, empty sections or questions, missing mappings, and scope choices that may prevent the resource from operating as intended.
