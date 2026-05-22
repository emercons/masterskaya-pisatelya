# Feedback and session boundaries

This workflow is sequential, but not every role transition should be automatic. Some transitions need human author feedback; others benefit from a fresh or compacted session because the next role has an intentionally different pressure.

## Human feedback checkpoints

Ask for author feedback at these points unless the author has already given an explicit instruction to continue:

- After `005-приёмщик--idea-receiver--приёмщик-идеи.md`: answer essential intake questions, or explicitly allow the next roles to continue with marked assumptions.
- After `020-критик--brutal-critic--жестокий-критик.md`: confirm which risks matter and whether the premise should survive.
- After `060-тематик--thematic-analyst--тематический-аналитик.md`: confirm premise, structure direction, theme, tone, and forbidden flattening before prose drafting.
- After `100-читатель--reader-simulator--симулятор-читателя.md`: decide whether to revise immediately, run advanced reviews, or accept the candidate.
- After `140-сверщик--continuity-auditor--аудитор-непрерывности.md`: choose which advanced-review pressures win before final editing.
- After `150-финред--final-editor--финальный-редактор.md`: stop for author review before publication, another major rewrite, or a second final pass.

If the author's feedback contains mixed revision requests, run `003-диспетчер--revision-router--маршрутизатор-правок.md` before rewriting. It should sort feedback, identify the earliest affected role, update the agent queue, and decide whether author choices are required before the next pass.

## High-conflict role transitions

These role pressures can contaminate each other if run in one long, uncompressed session:

- `005` Idea Receiver vs `010` Idea Architect: intake questions and uncertainty tracking vs premise shaping.
- `010` Idea Architect vs `020` Brutal Critic: expansion and protection of strangeness vs attack and risk removal.
- `020` Brutal Critic vs `070` Draft Writer: harsh diagnosis should not become the drafting voice.
- `080` Structural Editor vs `090` Style Editor: scene surgery and clarity vs rhythm, texture, and productive discomfort.
- `100` Reader Simulator vs `120` Ideology Stress Tester: reader accessibility vs preserving ideological complexity and discomfort.
- `110` Ending Analyst vs `130` Predictability Analyst vs `140` Continuity Auditor: emotional payoff, disruption, and consistency can pull the ending in different directions.

## Mandatory clean-session stops

If the next ordinary pipeline step is an antagonist or hard stress role, stop the current session before running it when the queue marks `fresh_session: required`.

Default required clean-session roles:

- `020-критик--brutal-critic--жестокий-критик.md`
- `120-идеолог--ideology-stress-tester--идеологический-стресс-тестер.md`
- `130-предсказатель--predictability-analyst--аналитик-предсказуемости.md`

Default recommended clean-session roles:

- `050-мировик--worldlogic-auditor--аудитор-логики-мира.md`
- `090-стилист--style-editor--стилевой-редактор.md`
- `100-читатель--reader-simulator--симулятор-читателя.md`
- `110-финалист--ending-analyst--аналитик-концовки.md`
- `140-сверщик--continuity-auditor--аудитор-непрерывности.md`

When stopping, name the exact next prompt and short alias so the author can start a fresh session directly.

## Real child-agent policy

Fresh sessions and child agents solve related but different problems. A fresh session gives the next role a clean conversation boundary; a real child agent gives a role its own focused working context while the main session can continue.

Use real child agents by default for separate roles whose value comes from opposition or criticism:

- `020-критик--brutal-critic--жестокий-критик.md`;
- `120-идеолог--ideology-stress-tester--идеологический-стресс-тестер.md`;
- `130-предсказатель--predictability-analyst--аналитик-предсказуемости.md`.

Use real child agents for non-oppositional roles when the work is large or the current context window is crowded enough to risk lower-quality role separation.

Diagnosis-only reviews can run as parallel child agents when they read the same stable draft and produce separate outputs. Editorial roles that change prose should run sequentially so each editor works from the previous edited draft.

## Agent behavior

Before crossing a high-conflict transition, especially in a long context window, the agent may stop and ask the author to compact the window or start a fresh session. Carry forward only:

- current canonical story state;
- latest relevant handoff;
- relevant draft fragment;
- explicit author decisions.

For cross-session work, carry these through `private/stories/<story-slug>/06-agent-queue/agent-queue.md`. Put antagonist or high-conflict roles in separate queue chunks when their pressure could contaminate the next role.

Do not carry a full prior transcript into the next specialist role.
