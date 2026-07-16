# Market and Product Intelligence

## Define the Cohort and Question

Specify the date range, opportunity state, segment, competitor, persona, product theme, or content type before searching evidence. Avoid blending unlike cohorts.

## Use Existing Trackers When Available

1. Call `listTrackers` to discover competition, product-feedback, keyword, or concept trackers.
2. Use `listMeetingsByTrackerIds` for dated, permission-bounded meeting sets matching those trackers.
3. Read meeting summaries or transcripts when the captured context is insufficient for classification.
4. If no relevant tracker exists, use semantic meeting search and disclose that the result is based on retrieved matches rather than a complete tracker-backed corpus.

## Run the Synthesis

For win-loss, competitor, feature-request, persona, or sentiment analysis:

1. define a mutually exclusive classification scheme before counting;
2. connect conversation evidence to the relevant account or opportunity when possible;
3. separate explicit reasons from analyst inference;
4. count only the analyzed cohort and state its size;
5. preserve representative meeting citations;
6. surface contradictory evidence and unknown outcomes.

For case-study or sales-content usage, use `searchCompanyLibrary`, `listLibraryDocuments`, meeting evidence, and CRM activities. Do not interpret “available in the library” as “shared by a seller.”

## Report Findings

Return the cohort definition, sample or record count, themes with counts, representative evidence, commercial impact, and recommended follow-up. Avoid precise company-wide percentages when the retrieved evidence is sampled or truncated.
