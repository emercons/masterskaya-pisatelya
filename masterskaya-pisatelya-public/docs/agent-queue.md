# Agent queue

The agent queue is the durable execution plan for running the storytelling pipeline across multiple sessions.

It lives inside each private story workspace:

```text
private/stories/<story-slug>/06-agent-queue/agent-queue.md
```

Do not store real story queue state in public folders.

## Purpose

Use the queue when the pipeline should be run in pieces, when a new session should continue work without reading the whole old chat, or when high-conflict roles should be isolated.

The queue is created or updated by:

```text
prompts/003-диспетчер--revision-router--маршрутизатор-правок.md
```

## What a new session reads

A new session should read only:

- `AGENTS.md`;
- `prompts/00-workflow.md`;
- `docs/agent-queue.md`;
- the current specialist prompt;
- `private/stories/<story-slug>/06-agent-queue/agent-queue.md`;
- `private/stories/<story-slug>/01-canonical/canonical-story-state.md`;
- the latest relevant handoff from `02-handoffs/`;
- the relevant draft fragment from `03-drafts/`;
- explicit author decisions referenced by the queue.

Do not carry the full prior conversation into the next specialist role.

## Queue item fields

Each queue item should include:

- `id`: stable item id, for example `Q-2026-05-07-001`;
- `role`: prompt filename;
- `status`: `pending`, `in_progress`, `blocked`, `completed`, or `skipped`;
- `session_chunk`: chunk id;
- `fresh_session`: `required`, `recommended`, or `no`;
- `execution_mode`: `inline`, `child_agent`, or `either`;
- `parallel_group`: optional stable group id for diagnosis-only roles that may run at the same time;
- `reason`: why this role is needed;
- `allowed_inputs`: exact canonical/handoff/draft/review files the role may read;
- `expected_outputs`: handoff, draft, review, canonical update, export, or queue update;
- `prose_editing`: `yes` or `no`;
- `stop_after`: whether to stop for author feedback or session boundary.

Interpret `fresh_session` this way:

- `required`: do not run this role in the current session. Stop, tell the author which exact role/alias to start next, and let the next clean session run it.
- `recommended`: stop if the context is long, emotionally biased by the previous role, or the next role has a conflicting pressure.
- `no`: the role can continue in the current session if the allowed inputs are clear.

Interpret `execution_mode` this way:

- `child_agent`: run the role as a real child agent with a focused context.
- `inline`: run the role in the current session.
- `either`: choose based on context size, conflict pressure, and available parallel work.

## Session chunks

The router should group compatible roles into chunks. A chunk can be run in one session if their pressures do not contaminate each other.

Use fresh sessions for:

- `020` Brutal Critic when moving from protective idea expansion into attack mode;
- transitions from `020` into prose-writing roles such as `070`;
- `080` to `090` if structural surgery is likely to dominate style;
- `100` to `120` when reader accessibility and ideological pressure conflict;
- `110`, `130`, and `140` when ending payoff, disruption, and continuity pull against one another.

## Antagonist / clean-session roles

Some roles are intentionally adversarial or strongly diagnostic. If one of these is the next pending queue item and `fresh_session` is `required`, stop the current session and ask the author to start a clean one with the exact alias.

Default clean-session policy:

| Role | Pressure | Default fresh session |
| --- | --- | --- |
| `020-критик--brutal-critic--жестокий-критик.md` | Antagonist / attack | required |
| `050-мировик--worldlogic-auditor--аудитор-логики-мира.md` | World-rule and institution audit | recommended |
| `090-стилист--style-editor--стилевой-редактор.md` | Voice and rhythm recalibration | recommended |
| `100-читатель--reader-simulator--симулятор-читателя.md` | External reader diagnosis | recommended |
| `110-финалист--ending-analyst--аналитик-концовки.md` | Ending stress test | recommended |
| `120-идеолог--ideology-stress-tester--идеологический-стресс-тестер.md` | Antagonist / ideology stress | required |
| `130-предсказатель--predictability-analyst--аналитик-предсказуемости.md` | Antagonist / expectation stress | required |
| `140-сверщик--continuity-auditor--аудитор-непрерывности.md` | Formal audit | recommended |

## Parallel child-agent reviews

Diagnosis-only review roles may run in parallel child agents when:

- they read the same stable draft;
- they do not edit prose;
- they write separate handoffs/review files;
- no role's output is required before another role can start.

Good parallel candidates after a stable final-candidate draft:

- `100-читатель--reader-simulator--симулятор-читателя.md`;
- `110-финалист--ending-analyst--аналитик-концовки.md`;
- `120-идеолог--ideology-stress-tester--идеологический-стресс-тестер.md`;
- `130-предсказатель--predictability-analyst--аналитик-предсказуемости.md`;
- `140-сверщик--continuity-auditor--аудитор-непрерывности.md`.

Prose-editing roles must run sequentially and should not share one parallel group:

- `080-структурщик--structural-editor--структурный-редактор.md`;
- `090-стилист--style-editor--стилевой-редактор.md`;
- `150-финред--final-editor--финальный-редактор.md`.

When stopping, use this shape:

```text
Stop here. Next role should run in a fresh session:
<short alias> -> <canonical prompt filename>

New session should read: agent queue, canonical state, latest relevant handoff, relevant draft fragment.
```

## Completion rule

After each role:

1. Write the role handoff under `02-handoffs/`.
2. Update canonical state only for durable decisions.
3. Update draft/review/export files only if the role is allowed to.
4. Mark the queue item `completed`.
5. Mark the next safe item `pending` or `blocked`.
6. Stop when the queue says `stop_after: author_feedback` or the next pending item says `fresh_session: required`.

## Queue source of truth

The queue does not replace canonical state. It only says what to run next and what files are allowed as inputs.

Canonical facts live in:

```text
private/stories/<story-slug>/01-canonical/canonical-story-state.md
```

Role memory lives in:

```text
private/stories/<story-slug>/02-handoffs/
```

Prose lives in:

```text
private/stories/<story-slug>/03-drafts/
```
