# Pipeline optimization notes

The base pipeline is effective for a first full pass because each role has a narrow pressure and writes a compact handoff. Its weak point is author feedback after a complete draft: feedback often mixes worldbuilding, structure, style, ending, and continuity in one message, so starting with the nearest obvious editor can miss the earliest affected layer.

## Conclusion

Keep the existing specialist order. Do not renumber established specialist roles; the router uses the early free number `003` so it can decide whether the route continues to `005` or jumps forward.

Add a lightweight routing role:

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

## Guardrails

- The router must not rewrite prose.
- The router must not invent new roles when an existing specialist can handle the issue.
- The router must not convert uncertain author brainstorming into canon.
- If alternatives are needed, the router assigns stable option IDs for author selection.
- If feedback changes premise, world rules, or ending direction, the route starts at the earliest affected role even if the current draft had already reached `150`.
- If a role is high-conflict or antagonistic, the router should put it in its own queue chunk or mark a fresh session boundary before/after it.
