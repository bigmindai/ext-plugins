# Bigmind external plugins

Public plugin packages for using Bigmind with Claude Code, Claude Cowork, ChatGPT, and Codex.

## Bigmind plugin

The shared plugin lives in [`plugins/bigmind`](plugins/bigmind). It contains one canonical Agent Skills tree and thin platform-specific manifests:

- `.claude-plugin/plugin.json` for Claude Code and Cowork
- `.codex-plugin/plugin.json` for ChatGPT and Codex
- `.mcp.json` for the remote Bigmind MCP server
- `skills/` for shared workflows used by both platforms

Included skills:

| Skill | Purpose |
| --- | --- |
| `meeting-workflows` | Prepare for meetings, review calls, summarize conversations, and handle requested follow-up tasks or notes. |
| `review-revenue` | Research accounts, review deals and renewals, assess pipeline risk, and synthesize revenue intelligence. |
| `configure-conversation-intelligence` | Configure trackers, scorecards, talking points, frameworks, vocabulary, and coaching resources. |
| `build-outreach-lists` | Build campaign-ready account Lists, research accounts, select targetable people, and draft outreach. |

## Requirements

- A Bigmind account and access to at least one Bigmind workspace
- Permissions for the Bigmind data and actions used by a workflow
- Browser-based OAuth authorization when the MCP connection is first used

Bigmind enforces the connected user's workspace permissions. Installing this plugin does not grant additional access.

## Test with Claude

From the repository root:

```bash
claude plugin validate ./plugins/bigmind
claude --plugin-dir ./plugins/bigmind
```

Authenticate the Bigmind MCP server through `/mcp`, then try:

```text
/bigmind:meeting-workflows
/bigmind:review-revenue
/bigmind:configure-conversation-intelligence
/bigmind:build-outreach-lists
```

For Anthropic community-directory submission, use this repository and the plugin subdirectory `plugins/bigmind`.

## Test with Codex

Add this repository as a marketplace:

```bash
codex plugin marketplace add bigmindai/ext-plugins
```

Then install the `bigmind` plugin from the `bigmind-external` marketplace in the ChatGPT desktop app and start a new task.

## Data and action boundaries

The plugin can read and write only through tools exposed by the Bigmind MCP server and authorized for the connected user. Some workflows create or modify tasks, CRM notes, Lists, documents, and analysis or coaching configuration. The included skills distinguish recommendations from authorized actions and require explicit intent for destructive or high-impact changes.

The current outreach workflow can prepare Lists and draft copy. It does not launch campaigns or send messages.

## Support and policies

- Website: https://bigmind.ai
- Support: https://bigmind.ai/support
- Privacy: https://bigmind.ai/privacy
- Terms: https://bigmind.ai/terms

## License

This repository is licensed under the [MIT License](LICENSE).
