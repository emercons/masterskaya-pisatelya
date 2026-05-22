# Agent operating rules

This repository is a sequential AI-assisted storytelling workshop.

## Privacy boundary

This repository is public. Treat every concrete story idea, handoff, canonical state, draft, review, and export as private by default.

Real story workspaces live outside the public infrastructure subtree, under root-level `masterskaya-pisatelya-PRIVATE/`. This repository may be private, so story workspaces can remain tracked when the author wants them accessible in git.

Create and read real story workspaces under:

```text
masterskaya-pisatelya-PRIVATE/stories/<story-slug>/
```

Do not create real story instances under public `stories/`. The public `stories/_template/` folder is only a template.

## Repository layout and migration safety

The repository root may contain only local/private working material plus a public infrastructure subtree:

```text
masterskaya-pisatelya-public/
masterskaya-pisatelya-PRIVATE/
```

When working from the repository root, public infrastructure files live under `masterskaya-pisatelya-public/`. Interpret paths in this `AGENTS.md` relative to that subtree unless the task explicitly concerns root-level local storage.

Do not assume the repository is currently public just because the workflow describes a public/private boundary. If tracked story files already exist under `masterskaya-pisatelya-PRIVATE/`, old `private/`, or concrete `stories/<story-slug>/` paths, keep them tracked and accessible unless the author explicitly asks to untrack, remove, or sanitize them. Report the mismatch, but do not silently "fix" it.

Before large moves or cleanup:

- run `git status --short --branch`, `git ls-files`, and `git remote -v`;
- inspect whether apparently private paths are tracked before changing them;
- use `git mv` for tracked files so history and rename detection stay intact;
- if a destination is ignored by a nested `.gitignore`, use `git mv` or `git add -f` only for the exact already-known tracked paths;
- keep root `.gitignore` minimal enough to protect local-only work, but do not let ignore rules hide files that the author wants to keep versioned;
- after staging, run `git diff --cached --name-only` and `git diff --cached --check`;
- before pushing, make sure git author email satisfies GitHub email privacy, for example a verified noreply address.

## Priority order

1. `prompts/00-workflow.md`
2. `prompts/003-диспетчер--revision-router--маршрутизатор-правок.md` when starting, resuming, or revising a route
3. `docs/role-map.md` when resolving a short agent alias
4. Current numbered bilingual specialist prompt in `prompts/`
5. Current story's `masterskaya-pisatelya-PRIVATE/stories/<story-slug>/01-canonical/canonical-story-state.md`
6. Current story's `masterskaya-pisatelya-PRIVATE/stories/<story-slug>/06-agent-queue/agent-queue.md`, if present
7. Latest relevant handoff in `masterskaya-pisatelya-PRIVATE/stories/<story-slug>/02-handoffs/`
8. Relevant draft fragment in `masterskaya-pisatelya-PRIVATE/stories/<story-slug>/03-drafts/`

Do not read the whole repository unless the current task requires it.

For short commands such as `работай, критик`, resolve the alias through `docs/role-map.md` or by searching canonical prompt filenames under `prompts/`, then use only that prompt.

## Canonical prompt naming

Use only bilingual role prompt filenames:

```text
prompts/NNN-короткое--english--русский.md
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

## Stable paragraph IDs for review drafts

When exporting or presenting a full draft for human author review, add stable paragraph IDs inline at the start of each numbered story paragraph:

```text
100: First paragraph text.

200: Second paragraph text.

300: Third paragraph text.
```

Rules:

- Number paragraphs, not visual lines. Number story prose paragraphs, including dialogue paragraphs.
- Do not number empty spacer lines, headings, scene separators, metadata, handoff/review section labels, or other service text.
- Use the compact inline format `100: Paragraph text`; do not put IDs on separate lines.
- Use a base step of 100 for newly numbered drafts: `100`, `200`, `300`, etc.
- Do not add leading zeroes.
- A paragraph ID is an editorial address for a semantic paragraph, not its current position in the file.
- Preserve existing paragraph IDs across agent passes so author feedback remains addressable.
- When a paragraph moves, keep its ID.
- When a paragraph is deleted, retire its ID. Do not reuse deleted IDs for new text.
- When paragraphs are merged, keep the ID of the paragraph that remains the semantic core, usually the first paragraph, and retire the absorbed ID.
- When a paragraph is split, keep the original ID on the most continuous fragment and assign new IDs to the new fragments.
- For inserted paragraphs, choose evenly spaced numbers inside the available interval, for example:
  - one insert between `100` and `200`: `150`;
  - three inserts between `100` and `200`: `125`, `150`, `175`.
- If there is no useful numeric gap left, or if local renumbering would otherwise be tempting, add dot-number suffixes to the nearest stable numeric anchor, for example `100.1`, `100.2`, `100.3`; if suffixes already exist, continue with the next integer suffix.
- Treat dot-number IDs as textual editorial addresses, not decimal numbers: `122.10` follows `122.9`.
- Never do a full or global renumbering, ID refresh, or broad ID reorder without explicit author consent. If it seems necessary, stop and ask the author first; until then, use local numeric gaps or dot-number suffixes.
- If the author explicitly approves a global renumbering, record the affected draft version and the fact of renumbering in the handoff.
- Story-facing exports under `masterskaya-pisatelya-PRIVATE/stories/<story-slug>/05-exports/` should use these IDs by default.
- Clean publication/reader-facing copies without paragraph IDs must be separate files and must not replace the review export.
- Agent handoffs and reviews may cite these paragraph IDs directly.

## Real child-agent policy

Do not merely "perform" every role inside one long session when role pressure or context size can lower quality.

Use real child agents by default for separate roles that are oppositional, adversarial, or critical, especially:

- `020-критик--brutal-critic--жестокий-критик.md`;
- `120-идеолог--ideology-stress-tester--идеологический-стресс-тестер.md`;
- `130-предсказатель--predictability-analyst--аналитик-предсказуемости.md`.

Use real child agents for other roles when the work is large, when the current context is crowded, or when a clean isolated context would protect quality.

Diagnosis-only review roles may run in parallel as child agents when they read the same stable draft and write disjoint handoffs/reviews. Prose-editing roles must run sequentially, because each editor must see the previous edited draft.

## Handoff rule

After every role:

- save compact output to the story-specific handoff file under `masterskaya-pisatelya-PRIVATE/stories/<story-slug>/02-handoffs/`;
- update canonical story state only when durable decisions changed;
- update draft files only when prose changed;
- when role `150` exports a full draft, use `masterskaya-pisatelya-PRIVATE/stories/<story-slug>/05-exports/full-draft-v<N>-MM-DD.md`, for example `full-draft-v6-05-07.md` for version 6 on May 7;
- update the story-specific agent queue when running a queued route;
- carry forward a short summary, not the whole prior conversation.

## Human feedback and session boundaries

Use `docs/feedback-and-session-boundaries.md` for author feedback checkpoints and high-conflict role transitions.

After complex author feedback, or when resuming a partial pipeline in a new session, run `003-диспетчер--revision-router--маршрутизатор-правок.md` before rewriting. The router sorts feedback, chooses the earliest affected role, writes a route handoff, and updates the agent queue. Skip it only for narrow, obvious fixes.

If the next role has a strongly different pressure and the context window is long, stop before switching roles and ask the author to compact the window or start a fresh session. Carry forward only canonical state, latest relevant handoff, relevant draft fragment, and explicit author decisions.

## Do not

- mix roles;
- perform general literary analysis instead of the current role;
- silently invent missing prompt files;
- rewrite artistic prose without role-specific need;
- place story content in public tracked folders;
- flatten strange, conflicting, or ambiguous elements into generic LLM prose;
- make AI jargon the whole story.
