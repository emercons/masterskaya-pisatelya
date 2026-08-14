# Story isolation contract / Контракт изоляции рассказа

Purpose: prevent one story, handoff, draft, or queue from contaminating another when several stories are developed in parallel.

## Required identity

Before a specialist does substantive work, it must resolve:

- workflow repository: normally `emercons/masterskaya-pisatelya`;
- content repository: normally `emercons/knigi-content-private`;
- exact `story-slug`;
- exact specialist role/prompt.

If the current project/chat already makes these unambiguous, the author does not need to repeat them.

## Workspace boundary

For a story `<story-slug>`, all story-specific reads/writes must default to:

```text
emercons/knigi-content-private/stories/<story-slug>/
```

Do not read sibling story folders merely because they exist.

## Allowed cross-story access

Cross-story access is allowed only when the current task explicitly requires one of these:

- framework retrospective across several stories;
- deliberate comparison between stories;
- shared-universe continuity;
- duplicate-idea/originality comparison requested by the author;
- migration or repository-wide maintenance.

When cross-story access is used, name that fact in the handoff and do not copy story-specific canon between stories without explicit justification.

## Preflight check

Before substantive specialist work, verify:

1. `story-slug` matches the intended private workspace.
2. `story-status.md`, queue, and canonical state refer to the same story when present.
3. Allowed input paths are inside the resolved workspace, except public workflow docs/prompts and explicitly required external research.
4. Expected story outputs are inside the same private workspace.
5. No concrete story content will be written to the public workflow repository.

If these checks pass, continue silently. Stop only when there is a real contradiction that cannot be resolved from GitHub.

## Queue rule

Every queue item should list exact `allowed_inputs` and `expected_outputs` narrowly enough that a new chat can avoid browsing neighboring story content.

## Handoff rule

A handoff should identify the current story by slug in its metadata/header when there is any realistic risk of parallel-story confusion.

## Public/private boundary

Public repository:

```text
emercons/masterskaya-pisatelya/masterskaya-pisatelya-public/
```

Private story repository:

```text
emercons/knigi-content-private/stories/<story-slug>/
```

No raw idea, canonical state, real handoff, draft, review, or clean manuscript export belongs in the public repository.
