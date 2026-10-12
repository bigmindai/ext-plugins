# Bigmind external plugins

Prepare sales calls, send follow-ups, run outreach and keep your CRM up to date with Bigmind.

Bigmind helps sales teams research accounts, prepare calls, summarize meetings, send follow-up emails, enroll prospects in outreach sequences, review deals and pipeline, and prepare forecasts. It brings together your CRM, email, calendar and customer conversations to identify risks and recommend next steps. Works with HubSpot, Salesforce or your connected CRM. Bigmind adds workflows and intelligence to your existing CRM; supported opportunity updates write back to that CRM.

This plugin brings those workflows to Claude Code, Claude Cowork, ChatGPT, Codex and Cursor through the Bigmind MCP server. Requested opportunity changes write back to the connected CRM; Lists, campaigns, tasks, knowledge and coaching use Bigmind platform resources.

Version **1.1.0** adds dedicated workflows for the sales day, accounts, deals, pipeline, customer intelligence and outreach. Native MCP Apps let users review and send emails, add sequences to active campaigns, and apply opportunity stage, amount and close-date changes.

## Installation

The shared plugin is [`plugins/bigmind`](plugins/bigmind). It contains Claude, Codex and Cursor manifests, one canonical `skills/` tree, shared `references/`, assets and `.mcp.json`. For Anthropic directory submission use this repository and subdirectory `plugins/bigmind`.

For Claude:

```bash
claude plugin validate ./plugins/bigmind
claude --plugin-dir ./plugins/bigmind
```

Authenticate through `/mcp`, then use natural language or a workflow such as `/bigmind:call-summary`, `/bigmind:draft-outreach` or `/bigmind:pipeline-review`.

For Codex, add this repository as a marketplace:

```bash
codex plugin marketplace add bigmindai/ext-plugins
```

Install `bigmind` from `bigmind-external` and start a new task. Cursor uses the root `.cursor-plugin/marketplace.json`; its plugin manifest points to the same skills and MCP server. Marketplace availability depends on each platform's review.

## Connection and action access

New users can invoke `/bigmind:setup` for guided CRM connection, Chrome extension installation, and Google Workspace organizational-unit or individual email/calendar setup.

A Bigmind account, workspace access and browser OAuth are required. During OAuth choose the intended workspace and the tool groups needed for the workflow:

| Workflow capability | Access |
| --- | --- |
| Core meeting, CRM context, pipeline, Library and task workflows | Core tools, subject to workspace permissions |
| Email review/send card | Core write or CRM write; an eligible connected sender |
| Opportunity update review card | CRM write; connected CRM access |
| Exact CRM fields and stage picklists | CRM schema read |
| Qualification assessment reads/writes | CRM read/write |
| List creation, imports and enrichment configuration | Lists read/write |
| Campaign and sequence review/enrollment | Campaigns read/write and outreach availability |
| Connected provider enrichment | Enrichment access and an active provider; calls may consume credits |
| Library authoring, trackers and coaching configuration | Corresponding optional tool groups |

After changing OAuth access, reconnect and refresh the client's tool inventory. Skills do not enable missing tools or bypass workspace permissions. The live inventory is authoritative; provider, deployment and client support can differ.

MCP Apps require a host that renders them. Email and opportunity cards prepare changes; the user completes the action inside the card. App-only confirmation tools are not assistant-callable. The assistant can run configured lists, rows, columns and cells, retry errors, and update automatic execution settings through the existing MCP tools. Catalog tools only read metadata; existing list actions are individually exposed when authorized. Where the host cannot render a card, the workflow provides prepared content and a Bigmind handoff. It never reports a draft as sent or applied.

Sequence enrollment is supported for active campaigns configured to accept supplied sequences. Submitted outreach still requires user review and approval in the Bigmind UI before it can be sent; Add to campaign does not approve or send messages. Campaign activation and full-audience generation remain UI-only in the audited contract. Email scheduling and opportunity creation exist elsewhere in Bigmind but are not implemented by these review cards. Broader mailbox sweeping depends on an actually exposed email-reading tool. Booking meetings and assigning CRM leads are not advertised as executable workflows here.

## Workflows

Names align with familiar sales jobs; each skill uses Bigmind evidence and platform resources. Each skill is a focused entry point for a complete workflow.

| Skill | Use it for |
| --- | --- |
| [`account-context`](plugins/bigmind/skills/account-context/SKILL.md) | Assemble a current account brief from connected CRM, conversations, activities, documents, tasks and signals. |
| [`account-plan`](plugins/bigmind/skills/account-plan/SKILL.md) | Create or refresh a strategic Bigmind account plan with customer goals, stakeholder coverage, opportunities and an executable action plan. |
| [`account-research`](plugins/bigmind/skills/account-research/SKILL.md) | Research a company or prospect and assess fit using public sources, connected CRM history and the workspace ICP. |
| [`account-tiering`](plugins/bigmind/skills/account-tiering/SKILL.md) | Score and tier a defined account List or book using transparent ICP fit, engagement and buying-signal evidence. |
| [`build-outreach-list`](plugins/bigmind/skills/build-outreach-list/SKILL.md) | Build, import, enrich and qualify a Bigmind prospect List with targetable people ready for requested outreach. |
| [`call-prep`](plugins/bigmind/skills/call-prep/SKILL.md) | Prepare for a specific upcoming customer call using Bigmind meeting history, CRM context and unresolved commitments. |
| [`call-summary`](plugins/bigmind/skills/call-summary/SKILL.md) | Process a completed customer call into a sourced recap, follow-up email, tasks, record-linked Bigmind notes and reviewed opportunity changes. |
| [`close-plan`](plugins/bigmind/skills/close-plan/SKILL.md) | Build a customer-evidenced business case and mutual action plan, then prepare the communications and opportunity changes needed to close. |
| [`coach-rep`](plugins/bigmind/skills/coach-rep/SKILL.md) | Turn Bigmind deal and call evidence into a focused rep coaching plan, practice simulation and follow-up tasks. |
| [`competitive-intelligence`](plugins/bigmind/skills/competitive-intelligence/SKILL.md) | Analyze a competitor in a deal or across a dated cohort and create evidence-backed Bigmind battlecards and actions. |
| [`configure-revenue-intelligence`](plugins/bigmind/skills/configure-revenue-intelligence/SKILL.md) | Configure Bigmind trackers, frameworks, scorecards and coaching resources for a defined revenue question and scope. |
| [`create-an-asset`](plugins/bigmind/skills/create-an-asset/SKILL.md) | Create a customer-specific business case, one-pager or leave-behind from Bigmind account evidence and approved Library content. |
| [`crm-hygiene-check`](plugins/bigmind/skills/crm-hygiene-check/SKILL.md) | Audit a scoped Bigmind pipeline for missing or inconsistent values and prepare evidence-backed corrections for review. |
| [`customer-health`](plugins/bigmind/skills/customer-health/SKILL.md) | Review a customer’s relationship health and prepare a Bigmind QBR or recovery plan from real account evidence. |
| [`customer-voice`](plugins/bigmind/skills/customer-voice/SKILL.md) | Extract attributed customer quotes and themes from a defined Bigmind conversation cohort for product, sales or enablement questions. |
| [`daily-briefing`](plugins/bigmind/skills/daily-briefing/SKILL.md) | Build a Bigmind morning briefing from today’s customer meetings, closing deals, Inbox items and due tasks. |
| [`deal-advance-gap`](plugins/bigmind/skills/deal-advance-gap/SKILL.md) | Find what is missing to advance or close a specific connected CRM deal and turn the gaps into sequenced actions. |
| [`deal-review`](plugins/bigmind/skills/deal-review/SKILL.md) | Review a connected CRM opportunity’s actual health, qualification evidence, risks and actions using platform frameworks and warnings. |
| [`deal-signals`](plugins/bigmind/skills/deal-signals/SKILL.md) | Review Bigmind warnings, account signals and deal activity for actionable risks or opportunities across a defined book. |
| [`deal-slip-scenario`](plugins/bigmind/skills/deal-slip-scenario/SKILL.md) | Model how a named deal slipping, shrinking or being lost changes a scoped Bigmind forecast and recovery plan. |
| [`draft-outreach`](plugins/bigmind/skills/draft-outreach/SKILL.md) | Prepare a personalized Bigmind email or multi-touch outreach sequence and complete the requested native review or enrollment flow. |
| [`end-of-day`](plugins/bigmind/skills/end-of-day/SKILL.md) | Close the sales day by reconciling recorded calls, open commitments, pending review cards and tomorrow’s priorities in Bigmind. |
| [`expansion-whitespace`](plugins/bigmind/skills/expansion-whitespace/SKILL.md) | Find evidence-backed expansion opportunities within Bigmind customer accounts and prepare the next commercial actions. |
| [`forecast`](plugins/bigmind/skills/forecast/SKILL.md) | Prepare a scoped revenue forecast narrative from connected CRM opportunities and explicit forecast mappings, with evidence and supported review actions. |
| [`handle-objection`](plugins/bigmind/skills/handle-objection/SKILL.md) | Prepare an evidence-grounded response to a customer objection using Bigmind deal history, approved proof points and competitive knowledge. |
| [`inbox-sweep`](plugins/bigmind/skills/inbox-sweep/SKILL.md) | Triage accessible customer email or Bigmind Inbox work and prepare relevant replies and follow-ups. |
| [`lead-triage`](plugins/bigmind/skills/lead-triage/SKILL.md) | Qualify inbound prospects or a supplied lead backlog against the workspace ICP and prioritize next actions in Bigmind. |
| [`log-activity`](plugins/bigmind/skills/log-activity/SKILL.md) | Capture customer interaction outcomes as Bigmind notes and tasks linked to connected CRM records, using typed activity creation only when actually exposed. |
| [`manage-campaign`](plugins/bigmind/skills/manage-campaign/SKILL.md) | Configure, validate, preview and manage Bigmind outreach campaigns, supplied sequences, unsent messages and enrollment receipts. |
| [`pipeline-review`](plugins/bigmind/skills/pipeline-review/SKILL.md) | Review a scoped Bigmind pipeline for coverage, material risks and prioritized interventions using configured pipeline views. |
| [`renewal-radar`](plugins/bigmind/skills/renewal-radar/SKILL.md) | Review upcoming customer renewals in Bigmind and turn evidenced risks into a dated retention plan. |
| [`rep-context`](plugins/bigmind/skills/rep-context/SKILL.md) | Prepare a sales manager’s one-to-one with a named rep from Bigmind pipeline, activity, commitments and coaching evidence. |
| [`setup`](plugins/bigmind/skills/setup/SKILL.md) | Guide post-signup onboarding: connect the CRM, install the Chrome extension, connect team or individual email/calendar, and verify workflow readiness. |
| [`stakeholder-map`](plugins/bigmind/skills/stakeholder-map/SKILL.md) | Map a connected CRM account or deal’s stakeholders, demonstrated influence, engagement gaps and next relationship actions. |
| [`team-pipeline`](plugins/bigmind/skills/team-pipeline/SKILL.md) | Review a team’s Bigmind pipeline by rep and stage, with specific deal interventions and coaching needs. |
| [`update-opportunity`](plugins/bigmind/skills/update-opportunity/SKILL.md) | Review and apply requested connected CRM opportunity stage, amount or close-date changes through the native CRM review card. |
| [`weekly-wrap`](plugins/bigmind/skills/weekly-wrap/SKILL.md) | Summarize a sales week’s outcomes, evidenced deal changes, customer commitments and next-week priorities. |
| [`win-loss-review`](plugins/bigmind/skills/win-loss-review/SKILL.md) | Analyze a bounded set of closed deals and their Bigmind conversation evidence to explain wins, losses and improvements. |

Canonical execution contracts live in [`plugins/bigmind/references`](plugins/bigmind/references). Platform-sensitive action contracts were checked against monorepo commit `dc5f7c754` (October 11, 2026). Historical submission records under `review/` describe version 1.0.0 and are not current capability documentation.

## Validation

Claude can mount each skill independently. Every skill therefore includes regular copies of the shared guides in its own `references/` directory; runtime links must stay inside that skill. After editing canonical guides, run `python3 scripts/sync-skill-references.py` to refresh the bundled copies.

Run `python3 scripts/validate-plugin.py` to check manifests, packaged references, skill metadata and asset paths. The skill-creator quick validator and Claude's plugin validator provide additional package checks. See [`validation/workflow-validation.md`](validation/workflow-validation.md) for behavioral scenarios and live acceptance work still needed.

## Support and policies

- Website: https://bigmind.ai
- Support: https://bigmind.ai/support
- Privacy: https://bigmind.ai/privacy
- Terms: https://bigmind.ai/terms

Licensed under the [MIT License](LICENSE).
