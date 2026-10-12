# Knowledge, customer evidence and coaching

Use `searchCompanyLibrary` for focused approved knowledge; `listLibraryDocuments` and `getDocumentById` can locate/read an identified document when semantic search misses it. Existence in the Library does not prove permission for external disclosure or that a rep shared it. Keep internal customer quotes separate from approved customer-facing proof points.

For reusable deliverables discover `listDocumentTemplates`, inspect the chosen template with `getDocumentById`, then use `writeDocument` when saving is requested. Use specific content tools (`createBattlecard`, `updateBattlecard`, `createCaseStudy`, etc.) for those resource types and follow their live requirements. Battlecards require a resolved competitor and template. Preserve inline citation numbers and corresponding source records when saving HTML. Do not assume a generated restricted document is externally shared or sent.

For topic analysis discover `listTrackers`, build a dated cohort with `listMeetingsByTrackerIds`, paginate where completeness matters, and read actual summaries/transcripts. Distinguish customer speech from rep speech; deduplicate sessions and count unique accounts separately from mentions. If no tracker exists, semantic search is a useful sample, not an exhaustive corpus. Include contrary evidence and unknown outcomes.

For coaching use `getSessionScorecards` and verified conversation evidence; separate observed behavior from inferred causes. Use `listCoachingSimulations`/`getCoachingSimulation` before creating/updating a requested simulation. For new scorecards create drafts/questions and publish only when activation is requested. Talking points and playbooks are persistent resources, not just text in a chat.

For future monitoring, use the configuration skill to create or update a tracker with a resolved participant/owner scope. Do not promise historical backfill or recurring execution from configuration creation alone. Discover actual automation tools and existing automations when scheduling is requested; do not invent a create/run automation capability or modify an unrelated automation.
