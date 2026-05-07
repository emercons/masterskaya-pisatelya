# Agent operating rules

This repository is a sequential AI-assisted storytelling workshop.

## Privacy boundary

This repository is public. Treat every concrete story idea, handoff, canonical state, draft, review, and export as private by default.

Create and read real story workspaces under:

```text
private/stories/<story-slug>/
```

Do not create real story instances under public `stories/`. The public `stories/_template/` folder is only a template.

## Priority order

1. `prompts/00-workflow.md`
2. Current numbered bilingual specialist prompt in `prompts/`
3. Current story's `private/stories/<story-slug>/01-canonical/canonical-story-state.md`
4. Latest relevant handoff in `private/stories/<story-slug>/02-handoffs/`
5. Relevant draft fragment in `private/stories/<story-slug>/03-drafts/`

Do not read the whole repository unless the current task requires it.

## Canonical prompt naming

Use only bilingual role prompt filenames:

```text
prompts/NN-english--русский.md
```

Do not use non-bilingual role prompt filenames or unnumbered prompt files as role definitions.

## Role reset

Before every specialist role:

```text
You are ONLY the currently assigned specialist.
Forget previous specialist roles.
Do not continue previous analytical styles.
Do not behave as a general assistant.
Your scope is intentionally narrow.
```

## Handoff rule

After every role:

- save compact output to the story-specific handoff file under `private/stories/<story-slug>/02-handoffs/`;
- update canonical story state only when durable decisions changed;
- update draft files only when prose changed;
- carry forward a short summary, not the whole prior conversation.

## Do not

- mix roles;
- perform general literary analysis instead of the current role;
- silently invent missing prompt files;
- rewrite artistic prose without role-specific need;
- place story content in public tracked folders;
- flatten strange, conflicting, or ambiguous elements into generic LLM prose;
- make AI jargon the whole story.
