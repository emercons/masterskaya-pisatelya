# Feedback and session boundaries

This workflow is sequential, but not every role transition should be automatic. Some transitions need human author feedback; others benefit from a fresh or compacted session because the next role has an intentionally different pressure.

## Human feedback checkpoints

Ask for author feedback at these points unless the author has already given an explicit instruction to continue:

- After `005-idea-receiver--приёмщик-идеи.md`: answer essential intake questions, or explicitly allow the next roles to continue with marked assumptions.
- After `020-brutal-critic--жестокий-критик.md`: confirm which risks matter and whether the premise should survive.
- After `060-thematic-analyst--тематический-аналитик.md`: confirm premise, structure direction, theme, tone, and forbidden flattening before prose drafting.
- After `100-reader-simulator--симулятор-читателя.md`: decide whether to revise immediately, run advanced reviews, or accept the candidate.
- After `140-continuity-auditor--аудитор-непрерывности.md`: choose which advanced-review pressures win before final editing.
- After `150-final-editor--финальный-редактор.md`: stop for author review before publication, another major rewrite, or a second final pass.

## High-conflict role transitions

These role pressures can contaminate each other if run in one long, uncompressed session:

- `005` Idea Receiver vs `010` Idea Architect: intake questions and uncertainty tracking vs premise shaping.
- `010` Idea Architect vs `020` Brutal Critic: expansion and protection of strangeness vs attack and risk removal.
- `020` Brutal Critic vs `070` Draft Writer: harsh diagnosis should not become the drafting voice.
- `080` Structural Editor vs `090` Style Editor: scene surgery and clarity vs rhythm, texture, and productive discomfort.
- `100` Reader Simulator vs `120` Ideology Stress Tester: reader accessibility vs preserving ideological complexity and discomfort.
- `110` Ending Analyst vs `130` Predictability Analyst vs `140` Continuity Auditor: emotional payoff, disruption, and consistency can pull the ending in different directions.

## Agent behavior

Before crossing a high-conflict transition, especially in a long context window, the agent may stop and ask the author to compact the window or start a fresh session. Carry forward only:

- current canonical story state;
- latest relevant handoff;
- relevant draft fragment;
- explicit author decisions.

Do not carry a full prior transcript into the next specialist role.
