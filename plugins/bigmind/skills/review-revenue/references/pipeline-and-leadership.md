# Pipeline and Sales Leadership Reviews

## Select the Owner Scope

- Use `listOpportunitiesForUser` for one seller or the connected user.
- Use `listOpportunitiesForDirectReports` for one management layer.
- Use `listOpportunitiesForEventuals` for the permitted reporting tree.
- Use `getPipelineStageSummary` for deal counts and total amount by stage.
- Resolve users and teams with `searchUsers`, `listTeamMembers`, and `listTeams` before applying owner filters.

Apply the requested year, quarter, and stage. Use the actual CRM stage values returned in context; do not translate “commit” or “stage 3” without evidence of the corresponding CRM value.

## Evaluate Risk and Priority

1. Build the opportunity set for the requested scope.
2. Note whether the tool reports more records than it returns. Opportunity listing currently returns a bounded result set; do not call it exhaustive when `hasMore` is true.
3. Retrieve stored warnings with `getWarningsForDeals` in batches of no more than 50 IDs.
4. Add account activities, meetings, notes, todos, contacts, and signals only for deals that require deeper explanation.
5. Rank by user-stated criteria first. Otherwise consider timing, stage, amount, warning severity, recency of engagement, stakeholder gaps, and explicit next steps.

Do not invent a numerical risk score unless the user defines one or the data provides one.

## Answer Common Leadership Questions

- **At-risk deals:** show the warning or evidence, impact, and recommended intervention.
- **Stale deals:** calculate inactivity only from available dated activities; state what activity types were considered.
- **Rep priorities:** explain the prioritization rule and return a manageable ranked set.
- **Executive involvement:** identify the specific stakeholder or obstacle and propose a concrete executive action; do not recommend executive involvement generically.
- **Top opportunities:** define “top” using the user's rule or state the applied rule, such as amount and close timing.

For team email questions, rely on CRM-attributed activities or meeting evidence unless the relevant email belongs to the authenticated user. `queryUserEmail` does not provide arbitrary teammate mailbox access.
