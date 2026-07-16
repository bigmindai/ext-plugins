---
name: configure-conversation-intelligence
description: Configure Bigmind conversation intelligence and coaching resources, including competition, product-feedback, keyword, and concept trackers; meeting categories; custom vocabulary; frameworks; scorecards and questions; talking points; and coaching simulations. Use when a user asks to create, inspect, update, activate, publish, or organize how Bigmind analyzes and coaches conversations.
---

# Bigmind Conversation Intelligence

Configure persistent Bigmind analysis and coaching resources carefully. Read existing state, choose the correct resource type and template, apply the narrowest requested change, and verify the saved result.

## Run the Configuration Workflow

1. Identify the resource type, business outcome, intended users or meetings, and whether the request is to create or modify.
2. Inventory relevant existing resources and detect likely duplicates.
3. Read the selected resource, built-in template, library document, or document template before deriving configuration.
4. Draft the proposed structure from the user's intent and the live tool schema.
5. Execute additive writes when the request clearly authorizes creation.
6. Require unambiguous target and scope before updates, deletion, activation, or publication.
7. Read the resulting resource and report whether it is draft, active, published, or otherwise live.

Use `whoami` when workspace context is unclear. Never invent resource IDs, template IDs, owner scopes, CRM mappings, or settings.

## Select the Right Recipe

- For competition, product-feedback, keyword, concept, or manual trackers, read [references/tracker-recipes.md](references/tracker-recipes.md).
- For categories, vocabulary, frameworks, scorecards, talking points, or coaching simulations, read [references/coaching-and-analysis-recipes.md](references/coaching-and-analysis-recipes.md).

## Apply Configuration Rules

- Read before update. Use the corresponding list tool to resolve candidates, then the get tool for the selected resource.
- Preserve existing fields and structure unless the user requests replacement.
- Follow the live input schema instead of guessing defaults, enum values, nested methods, or CRM mappings.
- Resolve named users and teams before applying meeting-owner scope.
- Keep organization-wide resources distinct from user-visible or user-scoped resources.
- Create a new resource when requested; do not silently update a similarly named existing one.
- Do not create supporting templates or library documents unless the user asks or the primary request explicitly requires them and the destination is clear.

## Handle High-Impact Changes

Publishing a scorecard makes staged settings live. Deleting a coaching simulation, changing an active tracker, altering organization vocabulary, or broadly changing meeting scope can affect future analysis for many users.

Before such an action, ensure the user explicitly requested the live change and that the exact target is resolved. If the request is “show me” or “suggest,” return a proposal without writing.

## Present the Result

For a proposal, show the resource type, name, purpose, scope, detection or coaching logic, dependencies, and expected output.

For a completed change, report:

1. resource name and identifier;
2. created or updated fields;
3. meeting-owner or visibility scope;
4. template or linked-document dependency;
5. draft, active, or published status;
6. any follow-up needed to make the resource operational.

Do not imply historical meetings were reprocessed unless a tool result explicitly says so.
