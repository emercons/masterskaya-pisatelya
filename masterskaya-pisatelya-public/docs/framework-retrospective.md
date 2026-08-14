# Framework retrospective / Ретроспектива мастерской

Purpose: use real story work to improve the public framework without turning every one-off story problem into permanent infrastructure.

## When to run

Run a short retrospective when any of these happens:

- the author had to explain the same operational rule more than once;
- a role had to be rerun because its contract was too weak or ambiguous;
- a defect survived several downstream roles before being caught;
- a new specialist role was proposed;
- a story reaches `manuscript_complete`;
- cross-chat continuation was confusing or lost state;
- a story was contaminated by another story's context;
- README/docs/templates drifted from the actual workflow.

## Evidence to collect

For the current story, record only operational evidence:

- repeated author corrections;
- rerun roles and why;
- route backtracks;
- missed checkpoints;
- stale/missing status or queue state;
- failures caused by role contamination;
- quality-gate defects;
- files/docs that disagreed;
- mobile-runtime friction;
- new recurring task not owned by an existing role.

Do not copy private story content into the public repository. Generalize the failure.

## Classification

Classify each finding as:

1. `story_specific` — fix only the private story.
2. `prompt_defect` — an existing specialist needs a stronger contract.
3. `routing_defect` — `003` or queue/checkpoint rules need adjustment.
4. `state_defect` — canonical/handoff/status boundaries are unclear.
5. `documentation_drift` — public sources disagree.
6. `runtime_defect` — workflow assumes capabilities unavailable in ordinary ChatGPT.
7. `missing_recurring_pressure` — no existing role owns a repeated important task.
8. `post_manuscript` — belongs to publishing/promotion rather than writing.

## Rule for adding a new permanent specialist

Prefer strengthening an existing role or adding a conditional sub-protocol before adding a new role.

Add a new recurring role when at least one is true:

- the pressure is structurally distinct and repeatedly appears across stories;
- combining it with an existing role creates role contamination;
- it requires a materially different evidence base/tooling;
- failure to isolate it creates severe integrity, originality, safety, or continuity risk.

A single interesting story-specific problem is not sufficient by itself.

## Retrospective output

```markdown
# Workshop retrospective

## Evidence

## Findings

| id | class | symptom | root cause | recurrence evidence | severity | proposed framework change |
| --- | --- | --- | --- | --- | --- | --- |

## Changes to private story only

## Changes proposed for public workflow

## Existing role to strengthen

## New role justified?

## Mobile-runtime impact

## Documentation/integrity check required

## Decision
```

## Application rule

When a public framework change is made:

1. update `docs/workflow-manifest.md` first if role/runtime semantics changed;
2. update affected prompts/docs/templates;
3. run `docs/workflow-integrity-check.md`;
4. do not retroactively rewrite every private story unless the mismatch blocks current work;
5. apply/backfill changes opportunistically when each story is next resumed.
