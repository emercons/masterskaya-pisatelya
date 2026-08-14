# 00 - Workflow / Рабочий процесс

This repository is a sequential multi-agent storytelling workshop where the baseline agents are markdown role prompts executed in ordinary ChatGPT chats.

## Source of truth

Canonical role/runtime semantics:

```text
docs/workflow-manifest.md
```

If this file and the manifest disagree, the manifest wins and this file must be repaired.

## Supported baseline runtime

The workflow must work in ordinary ChatGPT, including the mobile app.

- one chat = one session;
- new chat = baseline clean-context isolation;
- GitHub queue/status/canonical/handoffs = durable memory;
- real child agents, VM, terminal, and parallel execution are optional enhancements only.

See `docs/mobile-chatgpt-runtime.md`.

## Non-negotiable operating rule

Before applying every specialist prompt:

```text
You are ONLY the currently assigned specialist.
Forget previous specialist roles.
Do not continue previous analytical styles.
Do not behave as a general assistant.
Your scope is intentionally narrow.
```

## Story isolation

Before substantive work, resolve workflow repo, content repo, exact story slug, and exact role. Keep story-specific reads/writes inside the resolved private workspace unless the task explicitly requires cross-story analysis.

See `docs/story-isolation-contract.md`.

## Inputs allowed for each role

Use only:

- current specialist prompt;
- current story status/queue as needed for routing;
- current canonical story state;
- latest relevant handoff;
- relevant draft/review fragment;
- explicit author decisions;
- external research only when the role explicitly requires it.

Do not drag the full old conversation forward.

## Role order

1. `003-диспетчер--revision-router--маршрутизатор-правок.md` when starting, resuming, or revising a route
2. `005-приёмщик--idea-receiver--приёмщик-идеи.md`
3. `010-архитектор--idea-architect--архитектор-идеи.md`
4. `015-тестер--criterion-stress-tester--тестер-критериев.md` when the premise depends on a rule, criterion, contract, optimization target, or ethical constraint that can be adversarially broken
5. `020-критик--brutal-critic--жестокий-критик.md`
6. `030-сюжетник--story-engineer--инженер-сюжета.md`
7. `040-психолог--character-psychologist--психолог-персонажей.md`
8. `050-мировик--worldlogic-auditor--аудитор-логики-мира.md`
9. `060-тематик--thematic-analyst--тематический-аналитик.md`
10. `070-черновик--draft-writer--писатель-черновика.md`
11. `080-структурщик--structural-editor--структурный-редактор.md`
12. `090-стилист--style-editor--стилевой-редактор.md`
13. `100-читатель--reader-simulator--симулятор-читателя.md`
14. `110-финалист--ending-analyst--аналитик-концовки.md`
15. `120-идеолог--ideology-stress-tester--идеологический-стресс-тестер.md`
16. `130-предсказатель--predictability-analyst--аналитик-предсказуемости.md`
17. `135-оригинальность--similarity-ip-auditor--аудитор-сходства-и-ip.md`
18. `140-сверщик--continuity-auditor--аудитор-непрерывности.md`
19. `150-финред--final-editor--финальный-редактор.md`

`015` is conditional rather than mandatory. It attacks a premise-defining rule itself before later worldlogic work.

`135` is a conditional late diagnosis-only audit. Use it for named/likely close external works or when originality/IP-risk review is needed before finalization. It cannot guarantee legal clearance.

## Revision routing

Use `003` when starting a new pipeline, resuming from an agent queue, or processing mixed/structural author feedback.

The router does not rewrite prose. It sorts feedback, identifies the earliest affected role, builds the minimal safe route, updates the story-specific queue, and maintains the story-status snapshot.

Skip `003` only for narrow obvious local fixes.

## Author feedback checkpoints

Ask for human author feedback after roles `005`, `020`, `060`, `100`, `140`, and `150` unless the author explicitly asked to continue through that checkpoint.

For `015`, stop when materially different surviving criteria require author selection.

For `135`, stop when a high-risk similarity cluster requires premise-, structure-, or ending-level change.

Use `docs/feedback-and-session-boundaries.md`.

## Session isolation

Follow the manifest:

- `fresh_chat_required`: start the role in a new ordinary ChatGPT conversation unless the current chat itself is already a clean launch of that role;
- `fresh_chat_recommended`: prefer a new chat when context is long or biased;
- `same_chat`: may continue when queue and context permit.

A real child agent may substitute only in environments that actually support it. It is never required for baseline use.

## Optional enhanced execution

When real child agents/parallel execution exist, diagnosis-only roles may run in isolated/parallel contexts if they read the same stable draft and write disjoint outputs.

Good optional parallel review candidates after a stable final-candidate draft: `100`, `110`, `120`, `130`, `135`, `140`.

Prose-editing roles `080`, `090`, and `150` must remain sequential.

## Quality gates

Use `docs/quality-gates.md`.

A role with a defined gate ends as `PASS`, `PASS_WITH_KNOWN_RISKS`, `BLOCKED`, or `AUTHOR_DECISION_REQUIRED`. Do not mark a role complete merely because a handoff was generated.

Blocking findings must reroute or stop downstream work.

## After each role

1. Save the output to the story-specific handoff file under `../knigi-content-private/stories/<story-slug>/02-handoffs/`.
2. Update canonical story state if durable decisions changed.
3. Update draft/review files if prose/review output changed and the role is allowed to do so.
4. When role `150` produces an export, save it as `05-exports/full-draft-v<N>-MM-DD.md`; author-review copies use stable paragraph IDs from `docs/stable-paragraph-ids.md`.
5. Update `06-agent-queue/agent-queue.md` when running from a queued route.
6. Update `06-agent-queue/story-status.md` when phase, last/current/next role, checkpoint, latest draft/review, fresh-chat requirement, or manuscript state changed.
7. Compress the role result into a short handoff summary.
8. Reset role identity before the next compatible role or stop at the fresh-chat boundary.

## Framework feedback loop

When recurring friction reveals a workshop defect, use `docs/framework-retrospective.md`. Prefer strengthening an existing role/routing/state contract before adding a new permanent specialist.

## Manuscript completion boundary

After `150` and its author checkpoint/quality gates, the story may become `manuscript_complete`.

Do not equate this with `publication_ready`. Publishing/submission and promotion belong to future sibling frameworks described in `docs/post-manuscript-frameworks.md`.

## Privacy

Concrete story workspaces are private by default and live under:

```text
../knigi-content-private/stories/<story-slug>/
```

Do not save raw ideas, handoffs, drafts, reviews, or final story exports into public tracked folders.

## Do not

- mix roles;
- do general literary analysis when a specific role is active;
- rewrite prose unless the current role requires it;
- convert strange/conflicted elements into generic polished prose;
- require unavailable child agents/VM/background execution;
- read neighboring story workspaces without a task-specific reason;
- treat `150` as publishing/marketing workflow.
