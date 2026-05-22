# 00 - Workflow / Рабочий процесс

This repository is a sequential multi-agent storytelling workshop.

Это последовательная мультиагентная мастерская для рассказа.

## Non-negotiable operating rule

Before applying every specialist prompt:

```text
You are ONLY the currently assigned specialist.
Forget previous specialist roles.
Do not continue previous analytical styles.
Do not behave as a general assistant.
Your scope is intentionally narrow.
```

## Inputs allowed for each role

Use only:

- current specialist prompt;
- current canonical story state;
- latest relevant handoff;
- relevant draft fragment.

Do not drag the full old context forward.

## Role order

1. `003-диспетчер--revision-router--маршрутизатор-правок.md` when starting, resuming, or revising a route
2. `005-приёмщик--idea-receiver--приёмщик-идеи.md`
3. `010-архитектор--idea-architect--архитектор-идеи.md`
4. `020-критик--brutal-critic--жестокий-критик.md`
5. `030-сюжетник--story-engineer--инженер-сюжета.md`
6. `040-психолог--character-psychologist--психолог-персонажей.md`
7. `050-мировик--worldlogic-auditor--аудитор-логики-мира.md`
8. `060-тематик--thematic-analyst--тематический-аналитик.md`
9. `070-черновик--draft-writer--писатель-черновика.md`
10. `080-структурщик--structural-editor--структурный-редактор.md`
11. `090-стилист--style-editor--стилевой-редактор.md`
12. `100-читатель--reader-simulator--симулятор-читателя.md`
13. `110-финалист--ending-analyst--аналитик-концовки.md`
14. `120-идеолог--ideology-stress-tester--идеологический-стресс-тестер.md`
15. `130-предсказатель--predictability-analyst--аналитик-предсказуемости.md`
16. `140-сверщик--continuity-auditor--аудитор-непрерывности.md`
17. `150-финред--final-editor--финальный-редактор.md`

## Revision routing

Use `003-диспетчер--revision-router--маршрутизатор-правок.md` when starting a new pipeline, resuming from an agent queue, or processing human author feedback that contains several kinds of changes, changes the ending/structure/world rules, or arrives after roles `100`, `140`, or `150`.

The revision router does not rewrite prose. It sorts feedback, identifies the earliest affected role, builds the minimal safe route through the existing specialists, and writes/updates the story-specific agent queue.

Skip `003` only when the next step is obvious and local, such as a typo fix or one narrow style correction.

## Author feedback checkpoints

Ask for human author feedback after roles `005`, `020`, `060`, `100`, `140`, and `150` unless the author has explicitly asked to continue through that checkpoint.

Use `docs/feedback-and-session-boundaries.md` as the source of truth for feedback checkpoints and high-conflict role transitions.

If author feedback contains actual revision requests, run `003-диспетчер--revision-router--маршрутизатор-правок.md` before starting the next revision pass unless the requested change is narrow and obvious.

## Session boundaries

Some roles deliberately contradict each other. Before crossing a high-conflict transition in a long context window, stop and ask the author to compact the window or start a fresh session.

If the next pending queue item has `fresh_session: required`, stop the current session and name the exact next role and short alias. Do not run that role in the current session.

Carry forward only:

- current canonical story state;
- latest relevant handoff;
- relevant draft fragment;
- explicit author decisions.

## Real child-agent execution

A specialist role can be run either inline in the current session or as a real child agent with its own focused context.

Prefer real child agents for roles that are oppositional, adversarial, or critical. In this workflow those roles are:

- `020-критик--brutal-critic--жестокий-критик.md`;
- `120-идеолог--ideology-stress-tester--идеологический-стресс-тестер.md`;
- `130-предсказатель--predictability-analyst--аналитик-предсказуемости.md`.

Use real child agents for other roles when the work is large, the context window is crowded, or a clean isolated context would protect quality.

Diagnosis-only review roles may run in parallel when they share a stable draft and produce disjoint handoffs/reviews. Good parallel candidates after a final-candidate draft are `100`, `110`, `120`, `130`, and `140`.

Prose-editing roles must run sequentially. Do not run `080`, `090`, or `150` in parallel against the same draft; each one depends on the previous edited text.

## After each role

1. Save the output to the story-specific handoff file under `private/stories/<story-slug>/02-handoffs/`.
2. Update canonical story state if durable decisions changed.
3. Update draft files if prose changed.
4. When role `150` produces an export, save it as `05-exports/full-draft-v<N>-MM-DD.md`, using `MM-DD` such as `05-07` for May 7. For author review, apply stable paragraph IDs according to `docs/stable-paragraph-ids.md`; never do a full or global ID renumbering without explicit author consent, and use local numeric gaps or dot-number suffixes instead.
5. Update `private/stories/<story-slug>/06-agent-queue/agent-queue.md` when running from a queued route.
6. Compress the role result into a short handoff summary.
7. Reset role identity before the next role.

## Privacy

Concrete story workspaces are private by default and must live under:

```text
private/stories/<story-slug>/
```

Do not save raw ideas, handoffs, drafts, reviews, or final story exports into public tracked folders.

## Do not

- Mix roles.
- Do a general literary analysis when a specific role is active.
- Rewrite prose unless the current role requires it.
- Convert strange or conflicted elements into generic polished prose.
- Treat AI-industry jargon as the whole story; it is the second semantic layer.

## Priority

Only numbered bilingual prompt filenames are authoritative.
