# Agent operating rules

This repository is a sequential AI-assisted storytelling workshop.

## Privacy boundary

This repository is public. Treat every concrete story idea, handoff, canonical state, draft, review, and export as private by default.

The entire `private/` tree is intentionally local-only and ignored by git. It is normal that `rg --files` and tracked-file searches do not show real story workspaces there; inspect `private/` explicitly when the task concerns drafts, author feedback, handoffs, reviews, exports, or an active story.

Create and read real story workspaces under:

```text
private/stories/<story-slug>/
```

Do not create real story instances under public `stories/`. The public `stories/_template/` folder is only a template.

## Priority order

1. `prompts/00-workflow.md`
2. `prompts/003-диспетчер--revision-router--маршрутизатор-правок.md` when starting, resuming, or revising a route
3. `docs/role-map.md` when resolving a short agent alias
4. Current numbered bilingual specialist prompt in `prompts/`
5. Current story's `private/stories/<story-slug>/01-canonical/canonical-story-state.md`
6. Current story's `private/stories/<story-slug>/06-agent-queue/agent-queue.md`, if present
7. Latest relevant handoff in `private/stories/<story-slug>/02-handoffs/`
8. Relevant draft fragment in `private/stories/<story-slug>/03-drafts/`

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

- save compact output to the story-specific handoff file under `private/stories/<story-slug>/02-handoffs/`;
- update canonical story state only when durable decisions changed;
- update draft files only when prose changed;
- when role `150` exports a full draft, use `private/stories/<story-slug>/05-exports/full-draft-v<N>-MM-DD.md`, for example `full-draft-v6-05-07.md` for version 6 on May 7;
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
