# Feedback and session boundaries

This workflow is sequential, but not every role transition should be automatic. Some transitions need human author feedback; others benefit from a fresh ChatGPT conversation because the next role has intentionally different pressure.

`docs/workflow-manifest.md` is authoritative for current role/checkpoint/isolation semantics.

## Human feedback checkpoints

Ask for author feedback at these points unless the author already explicitly asked to continue:

- After `005-приёмщик`: answer essential intake questions or explicitly allow marked assumptions.
- After `020-критик`: confirm which risks matter and whether the premise should survive.
- After `060-тематик`: confirm premise, structure direction, theme, tone, and forbidden flattening before prose drafting.
- After `100-читатель`: decide whether to revise immediately, run advanced reviews, or accept the candidate.
- After `140-сверщик`: choose which review pressures win before final editing.
- After `150-финред`: stop for author review before marking `manuscript_complete` or starting another major rewrite.

Conditional checkpoints:

- `015-тестер`: stop when materially different surviving criteria/rules require author choice.
- `135-оригинальность`: stop when a high-risk similarity cluster requires premise-, structure-, or ending-level change.
- `003-диспетчер`: stop when conflicting route options need author preference.

If author feedback contains mixed revision requests, run `003` before rewriting.

## High-conflict transitions

These role pressures can contaminate each other in one long chat:

- `005` intake vs `010` premise shaping;
- `010` architecture vs `020` hostile criticism;
- `020` criticism vs `070` drafting voice;
- `080` structural surgery vs `090` style recalibration;
- `100` reader accessibility vs `120` ideology pressure;
- `110` ending payoff vs `130` disruption vs `140` consistency;
- any named-work inspiration discussion vs `135` adversarial originality/IP review.

## Fresh-chat rule

The mobile-safe baseline is a **new ordinary ChatGPT conversation**, not a required child-agent system.

Default `fresh_chat_required` roles from the manifest:

- `020-критик`;
- `120-идеолог`;
- `130-предсказатель`;
- `135-оригинальность`.

Default `fresh_chat_recommended` roles:

- `015-тестер`;
- `050-мировик`;
- `090-стилист`;
- `100-читатель`;
- `110-финалист`;
- `140-сверщик`.

When a required boundary is reached, stop and name the exact next alias/prompt. The author can open a normal new mobile chat and paste the short launch.

## What the next chat reads

Carry forward through GitHub, not transcript memory:

- `06-agent-queue/story-status.md`;
- `06-agent-queue/agent-queue.md`;
- current canonical story state;
- latest relevant handoff;
- relevant draft/review fragment;
- explicit author decisions referenced there.

Do not require the full prior transcript.

## Optional enhanced runtime

A real child agent may substitute for a fresh manual chat only when the environment actually supports it.

Diagnosis-only reviews may optionally run in parallel when they read the same stable draft and write separate outputs. Prose-editing roles remain sequential.

The resulting files/queue/status must remain resumable from ordinary mobile ChatGPT afterward.

## Agent behavior

Before crossing a required high-conflict boundary, stop instead of pretending a role-reset instruction fully cleans a long biased context.

For recommended boundaries, use judgment based on context length and pressure conflict.

Update `story-status.md` so the next chat has an explicit `Next launch` command.
