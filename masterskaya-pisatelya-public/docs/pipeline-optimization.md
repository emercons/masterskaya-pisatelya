# Pipeline optimization notes

`docs/workflow-manifest.md` is authoritative for the current role inventory/runtime semantics. This file explains why conditional/routing roles exist and how to avoid overprocessing.

## Base principle

The base pipeline is effective because each role has a narrow pressure and writes a compact handoff. Its recurring weak points are:

1. mixed author feedback after a developed draft;
2. premise-defining rules that can be adversarially broken before plotting;
3. late originality/similarity concerns that require current external comparison rather than generic literary criticism;
4. context contamination between strongly opposed roles;
5. resuming work from ordinary ChatGPT/mobile without a persistent agent runtime.

## Keep established specialist numbers

Do not renumber existing roles.

Use numeric gaps for a genuinely distinct recurring pressure only when retrospectives show no existing role cleanly owns it.

Current conditional specialist additions:

```text
015-тестер--criterion-stress-tester--тестер-критериев.md
135-оригинальность--similarity-ip-auditor--аудитор-сходства-и-ip.md
```

The lightweight routing role remains:

```text
003-диспетчер--revision-router--маршрутизатор-правок.md
```

## 003 — router

Run `003` when:

- starting a new pipeline;
- resuming a partial pipeline/new chat;
- feedback contains several kinds of changes;
- feedback arrives after `100`, `140`, or `150`;
- feedback changes ending, structure, world rules, tone contract, or premise criterion;
- next role is not obvious;
- specialist pressures conflict.

Skip it only for narrow obvious local fixes.

The router creates/updates:

- sorted change map;
- earliest affected role;
- minimal ordered route;
- safe chat/session chunks;
- quality-gate requirements;
- author choices;
- `06-agent-queue/agent-queue.md`;
- `06-agent-queue/story-status.md`.

It does not rewrite prose.

## 015 — criterion stress tester

Run `015` when:

- several premise-defining criteria/rules are compared;
- an obvious loophole could collapse the story;
- readers are likely to ask `why didn't they simply do X?`;
- a patched rule needs regression testing;
- metric/consent/contract/magical/optimization rules must remain simple in prose but non-trivial under attack;
- long-horizon consequences matter.

Do not run `015` merely because a story has worldbuilding. Ordinary plausibility belongs to `050`.

Separation:

- `015` attacks the **rule itself** across candidate formulations.
- `050` audits the **selected rule inside the wider world**: institutions, incentives, interfaces, adoption, abuse, fallback, side effects.

## 135 — similarity / IP auditor

Run `135` when:

- the author names an inspiration that may be close;
- a draft/premise has a distinctive combination strongly associated with a known external work;
- plagiarism/adaptation/originality perception is a concern;
- a pre-publication risk-reduction pass is warranted.

`135` is diagnosis-only and uses current public research when needed. It distinguishes broad ideas/tropes from distinctive expressive combinations and cannot guarantee legal clearance.

If `135` finds a structural overlap, do not let it silently rewrite the story. Route the required literary changes back through `003` to the earliest affected role, then rerun `135` on the repaired draft when needed.

## Mobile-first session optimization

The canonical baseline is ordinary ChatGPT/mobile:

- one chat is one session;
- `fresh_chat_required` means start a new ordinary chat;
- GitHub status/queue/canon/handoffs carry state;
- real child agents/parallelism are optional acceleration only.

Do not optimize the pipeline in a way that makes mobile execution impossible.

See `docs/mobile-chatgpt-runtime.md`.

## Quality gate optimization

Do not send work downstream merely because a role emitted a handoff. Use `docs/quality-gates.md`.

A blocking `015`, `020`, `050`, `100`, `135`, or `140` finding should stop/reroute the pipeline early enough to avoid expensive prose churn.

## Framework-change guardrails

- Router must not invent new roles.
- New public roles must not renumber established roles.
- `015` must not silently choose canon.
- `135` must not pretend to grant legal clearance.
- Uncertain author brainstorming must not become canon.
- Use stable option IDs for author choices.
- Start revisions at the earliest affected layer.
- Follow `docs/framework-retrospective.md` before treating a one-story problem as permanent architecture.
- After changing role/runtime semantics, run `docs/workflow-integrity-check.md`.

## Example routes

Mixed post-draft feedback:

```text
Author feedback
-> 003
-> earliest affected literary role
-> required downstream edits/reviews
-> author checkpoint
```

Premise-rule repair:

```text
Author proposes/repairs criterion
-> 003
-> 015
-> author choice if needed
-> 010/030/050 as affected
```

Similarity repair:

```text
Named close external work / high-risk resemblance
-> 003
-> 135 on concrete structure/draft
-> if structural repair needed: 003 -> earliest affected role(s)
-> 135 regression pass
-> 140 -> 150
```
