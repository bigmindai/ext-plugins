---
name: review-revenue
description: Research accounts and stakeholders, assess deal and renewal risk, review individual or team pipeline, interpret account signals, prioritize opportunities, and synthesize win-loss, competitive, product-feedback, engagement, and revenue patterns using Bigmind. Use for account reviews, pipeline inspection, deal risk, churn or renewal analysis, sales leadership questions, and evidence-grounded revenue intelligence.
---

# Bigmind Revenue Review

Use authorized Bigmind CRM, meetings, email, signals, and company knowledge to explain revenue state, risk, and opportunity. Keep portfolio claims bounded by the data actually returned.

## Run the Review

1. Define the unit of analysis: account, contact, deal, renewal, seller, team, pipeline, or historical cohort.
2. Resolve the requested owner scope, date range, stage, segment, and comparison criteria.
3. Retrieve the smallest complete-enough record set available within Bigmind permissions and tool limits.
4. Join structured CRM facts with conversation, activity, email, signal, and library evidence only as needed.
5. Separate observed facts, derived calculations, and strategic recommendations.
6. State coverage limits before making a conclusion that could be mistaken for an exhaustive report.

Use `whoami` when workspace or connected-user context is unclear. Resolve account names with `searchAccounts`; never invent IDs or silently substitute a similarly named account.

## Route to the Right Recipe

- For one account, stakeholder, deal, renewal, churn question, or save plan, read [references/account-deal-and-renewal.md](references/account-deal-and-renewal.md).
- For portfolio risk, pipeline, rep prioritization, stale deals, slippage, or executive involvement, read [references/pipeline-and-leadership.md](references/pipeline-and-leadership.md).
- For win-loss, competitors, feature requests, persona reactions, customer sentiment, case-study usage, or engagement patterns, read [references/market-and-product-intelligence.md](references/market-and-product-intelligence.md).
- Before answering quantitative, historical, or company-wide questions, read [references/analytics-boundaries.md](references/analytics-boundaries.md).

## Apply Evidence Rules

- Treat opportunity fields, activities, dates, amounts, and stages as structured CRM facts.
- Treat stored deal warnings as existing Bigmind warnings, not a newly calculated risk model.
- Use `listSignalsForAccount` only when signals or monitored changes are relevant. Read returned AI instructions before interpreting a signal.
- Use meeting search for qualitative evidence and preserve its inline citations.
- Use `queryUserEmail` only for the authenticated user's authorized mailbox. Do not imply access to a seller's inbox merely because their opportunities are visible.
- Use `researchCompanyByDomain` only when public-web company research is relevant. Cite returned public sources and distinguish them from private Bigmind evidence.
- Label an inference as an inference when multiple records suggest, but do not directly establish, a conclusion.

## Apply Action Safeguards

Default to analysis. A recommendation to create a task, note, account list, or document is not authorization to do so.

If the user explicitly requests a task or CRM note, resolve the target and verify the write. If the user requests an outreach list, hand the selected and evidence-backed account set to `build-outreach-lists` when that skill is available.

## Present the Result

Lead with the decision-relevant conclusion. Then provide:

1. **Scope and coverage** — records, owners, dates, and any truncation.
2. **Findings** — facts and calculated values.
3. **Evidence** — CRM, meetings, emails, signals, or sources supporting the findings.
4. **Risks or gaps** — missing fields, stale data, or unavailable metrics.
5. **Recommended actions** — prioritized advice, clearly separated from completed actions.

Do not present an incomplete sample as “all,” an association as causation, or a qualitative pattern as a statistically validated model.
