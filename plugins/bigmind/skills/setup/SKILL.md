---
name: setup
description: "Guide post-signup Bigmind onboarding: connect a CRM, install the Chrome extension, connect team or individual email and calendar, and verify readiness for sales workflows."
---

# Setup

Read [the workflow contract](references/operating-contract.md) before execution.

Bigmind is a workflow and intelligence layer over the user's existing CRM. Guide new users through the connections below, skipping steps already completed. Establish whether they are setting up just themselves or a team, and which CRM and email/calendar provider they use; ask only for missing information that changes the next step.

## Connect the workspace

1. **CRM:** Direct the user to [Context Graph sources](https://app.bigmind.ai/context-graph/sources) to connect HubSpot, Salesforce, or their supported CRM. Have them choose their actual provider and follow the connection flow. Explain that this supplies CRM context to Bigmind and enables supported writebacks; it does not replace their CRM.
2. **Meeting capture:** Direct each user to install the [Bigmind Chrome extension](https://chromewebstore.google.com/detail/bigmindai/bgjebfdehodangonjglfliigdcejkeba) and complete its sign-in/setup flow. Installation is a browser step; do not claim it is installed based on opening the link.
3. **Email and calendar:** Choose the appropriate route:
   - **Google Workspace team setup:** Use [Google Workspace sources](https://app.bigmind.ai/context-graph/sources/google-workspace) to connect email and calendar for everyone in the intended organizational unit. Guide the administrator through the page's required authorization and organizational-unit selection. Keep the selected unit within the user's intended team scope; a non-admin should hand this step to their Workspace administrator.
   - **Individual setup:** Use [Integrations](https://app.bigmind.ai/integrations) for each user to connect their own email and calendar through the available provider flows. Use this route for user-by-user onboarding, including when organization-wide Google Workspace setup is not appropriate.

Present the relevant links with the next action, not just a list of URLs. Follow the actual page instructions for permissions and provider requirements rather than inventing UI labels. Track CRM, extension, email and calendar separately as connected, pending, or not verified. Successful authorization does not establish that initial sync is complete. Verify status through an exposed read tool or the connection page; otherwise ask the user to confirm the displayed status and continue with available capabilities.

## Verify the plugin and start a workflow

Bigmind source connections and the client's Bigmind MCP OAuth connection are separate setup steps. Authenticate the plugin to the intended workspace if needed.

Use `whoami` and the live inventory to identify the workspace and usable capabilities. Inspect `listSkills` and selected `readSkill` for workspace methodology; consult frameworks or Library resources only for the user's intended workflows.

Explain what is ready: meetings/CRM/pipeline reads, email review cards, opportunity updates, Lists, Campaigns, enrichment and coaching. Email cards accept Core write or CRM write; opportunity cards need CRM write; sequence cards need Campaigns write and outreach availability. Other tools depend on their actual scopes. Missing tools may require reconnecting with the relevant access and refreshing inventory; installing a skill does not grant it.

Return a few relevant starting prompts and the smallest missing setup steps. Do not enable scopes, create configuration or enroll prospects merely to demonstrate the plugin.
