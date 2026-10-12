# Pipeline and qualification

Use `listPipelineViews` with the intended user/team scope, then `queryPipelineView` using the returned externalPipelineId (not the internal view ID) and identical scope. Preserve view attribute filters. Omit stageId for all stages in that pipeline, not every CRM pipeline. Follow nextCursor when all rows are required. Use `groupPipelineView` for stage/owner or activated custom-field totals; do not aggregate a first page as the whole book. Keep currencies separate unless a supported conversion basis is supplied.

The older opportunity-list tools remain useful for small bounded reviews; state truncation. Read stored warnings with `getWarningsForDeals` (up to 50 IDs per call) and investigate selected material deals with `searchDealActivities`. Current state alone does not prove stage movement, close-date slippage or next-step changes. For deltas obtain dated field history or comparable snapshots; label a missing record unresolved rather than won/lost.

For qualification use returned frameworkAssessments and `listApplicableFrameworks` / `getFrameworkAssessment`. Preserve the configured framework's name, components, applicability, evidence, score and coverage. Missing components mean missing evidence, not customer rejection. Do not replace the platform's framework with assumed MEDDIC or arbitrary win-probability adjustments.

If asked to refresh, `evaluateFramework` recalculates; if asked to save findings, discover answer_requirements then `updateFrameworkAssessment` with evidence-backed values and the exact answer types. Read back the result. Configuration (`createFramework`/`updateFramework`) is separate from updating an account/deal assessment.

For forecast, quota, stage aging, conversion, renewal and expansion analysis, first establish that the required fields, purchase/usage data, history and complete cohort are available. Prefer actual forecast categories to inferred stage mappings. Disclose assumptions and unavailable dimensions; never call a partial qualitative sample a company-wide rate or a heuristic a calibrated prediction.
