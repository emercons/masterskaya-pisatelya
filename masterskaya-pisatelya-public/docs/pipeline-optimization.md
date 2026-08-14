# Pipeline optimization notes

The base pipeline is effective for a first full pass because each role has a narrow pressure and writes a compact handoff. Its weak point is author feedback after a complete draft: feedback often mixes worldbuilding, structure, style, ending, and continuity in one message, so starting with the nearest obvious editor can miss the earliest affected layer.

A second identified weak point is premise-defining rules that can be adversarially broken before plotting begins: ethical criteria, contracts, scoring systems, optimization targets, magical rules, or similar constraints. General concept criticism and later worldlogic auditing do not provide a stable same-corpus comparison across multiple candidate formulations.

## Conclusion

Keep the established specialist numbers and do not renumber existing roles.

Use gaps for a genuinely distinct recurring pressure only when author feedback demonstrates that no current role cleanly covers it. The current conditional addition is:

```text
prompts/015-тестер--criterion-stress-tester--тестер-критериев.md
```

`015` is diagnosis-only. It is not mandatory for every story. It runs when the premise depends on a selectable rule/criterion that must survive adversarial comparison before later roles can safely build on it.

The existing lightweight routing role remains:

```text
prompts/003-диспетчер--revision-router--маршрутизатор-правок.md
```

The router is not a prose editor. It sorts author feedback, identifies the earliest affected role, produces the minimal safe route through the existing specialists, and updates the story-specific agent queue.

## When to run 003

Run `003-диспетчер--revision-router--маршрутизатор-правок.md` when:

- starting a new pipeline;
- resuming a partial pipeline in a new session;
- feedback contains several kinds of changes;
- feedback arrives after `100`, `140`, or `150`;
- feedback changes the ending, structure, world rules, or tone contract;
- the next role is not obvious;
- multiple specialist pressures might conflict.

Skip `003` only when the author asks for a narrow, obvious change, such as a pure typo fix or one clearly local style correction.

## When to run 015

Run `015-тестер--criterion-stress-tester--тестер-критериев.md` when:

- several premise-defining criteria or rules are being compared;
- an obvious loophole could collapse the story;
- readers are likely to ask «why didn't they simply do X?»;
- the author wants the same adversarial test corpus applied to different formulations;
- a rule has been patched and needs regression testing against earlier attacks;
- a metric, consent rule, contract, magical law, or optimization target must remain simple in prose while behaving non-trivially.

Do not run `015` merely because a story has worldbuilding. Ordinary plausibility belongs to `050-мировик`.

## Separation between 015 and 050

- `015` attacks the **rule itself** across alternative formulations.
- `050` audits the **selected rule inside the wider world**: institutions, incentives, interfaces, compliance, side effects, and plausibility.

When both are needed, run `015` first, obtain author selection/provisional approval, then let later story development proceed; `050` remains an independent downstream audit.

## How 003 changes the workflow

Instead of sending all feedback to every later role, the router creates:

- a sorted change map;
- the earliest affected role;
- an ordered route;
- session chunks;
- a list of roles allowed to edit prose;
- a list of diagnosis-only roles;
- author choices that must be resolved before rewriting;
- an updated `06-agent-queue/agent-queue.md`.

Example:

```text
Author feedback after final draft
-> 003 Revision Router
-> 080 Structural Editor
-> 090 Style Editor
-> 100 Reader Simulator
-> 110 Ending Analyst
-> 140 Continuity Auditor
-> 150 Final Editor
-> author review
```

Premise-rule example:

```text
Author proposes several alternative governing criteria
-> 003 Revision Router
-> 015 Criterion Stress Tester
-> author selects/provisionally approves survivor
-> earliest affected story role (often 010/030/050)
```

## Guardrails

- The router must not rewrite prose.
- The router must not invent new roles when an existing specialist can handle the issue.
- New public roles must not renumber established roles.
- `015` must not silently choose canon; surviving alternatives go back to the author when materially different.
- The router must not convert uncertain author brainstorming into canon.
- If alternatives are needed, the router assigns stable option IDs for author selection.
- If feedback changes premise, world rules, or ending direction, the route starts at the earliest affected role even if the current draft had already reached `150`.
- If a role is high-conflict or antagonistic, the router should put it in its own queue chunk or mark a fresh session boundary before/after it.
