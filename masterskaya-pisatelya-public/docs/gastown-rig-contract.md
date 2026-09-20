# Gas City public RIG contract

Status: pilot contract for the public workflow repository. The filename is
retained for compatibility; the deployed platform is **Gas City** with the
Gastown pack.

## Purpose

Gas City may operate this repository as one RIG inside the account-level City.
The RIG exists to maintain the Writer's Workshop infrastructure: prompts,
templates, contracts, documentation, and integrity checks.

Gas City is an optional execution layer. It must not become a dependency of
the ordinary ChatGPT/mobile runtime described in `docs/mobile-chatgpt-runtime.md`.

## Repository boundary

This rig owns only the public repository `emercons/masterskaya-pisatelya`.

The sibling `emercons/knigi-content-private` repository is a separate future rig. A worker assigned to this public rig must not read or modify that repository unless the work item explicitly names a narrowly scoped cross-repository contract check.

Concrete story ideas, canon, handoffs, drafts, reviews, exports, and story queue state must never be copied into this public rig, its tracker items, logs, branches, or generated artifacts.

## Eligible autonomous work

A work item is eligible for unattended execution only when all of the following are true:

- it changes public workflow infrastructure rather than a concrete story;
- its scope and expected files are explicit;
- acceptance criteria are testable from this repository;
- it does not require an author to make a literary choice;
- it does not publish, merge to `main`, or perform another external irreversible action;
- it can preserve the ordinary ChatGPT/mobile baseline.

Good pilot work includes:

- detecting and repairing documentation drift;
- maintaining prompt references and templates;
- adding deterministic integrity checks;
- fixing broken internal links;
- applying an already approved framework-retrospective decision;
- preparing a reviewable branch for a narrowly scoped workflow improvement.

## Work that must stop or remain manual

Do not autonomously:

- create or develop a real story;
- read the private story inventory for general orientation;
- choose among literary concepts or resolve an author checkpoint;
- rewrite prose from a private story;
- weaken privacy, isolation, quality-gate, or human-checkpoint rules;
- add, remove, rename, or materially redefine a canonical role without explicit approval;
- merge or push directly to `main`;
- turn Gas City, Beads, a background worker, or child agents into a required runtime.

If a task reaches one of these boundaries, preserve the branch and evidence, mark the work blocked for human review, and state the exact decision required.

## Work-item contract

Every dispatched work item should state:

- objective and non-goals;
- allowed input paths;
- expected output paths;
- acceptance criteria;
- validation procedure;
- whether a change to `docs/workflow-manifest.md` is authorized;
- whether a narrow read of the private sibling repository is authorized;
- required human review boundary.

The worker must read `AGENTS.md` before editing. When canonical role/runtime semantics are in scope, `docs/workflow-manifest.md` remains the source of truth.

## Git ownership and integration

- One work item owns one isolated branch/worktree.
- A worker must begin from a clean checkout of the intended base revision.
- Do not reuse the author's ordinary checkout as an autonomous worker workspace.
- Do not combine unrelated work items in one branch.
- Preserve unrelated tracked content and history.
- Produce a reviewable commit and evidence; do not merge automatically.
- Cross-repository changes require separate commits in the public and private repositories.

## Validation

For every change:

1. run `git diff --check`;
2. verify that no concrete private story content entered the diff;
3. verify changed Markdown links and referenced paths;
4. when role/runtime semantics or their mirrors changed, execute `docs/workflow-integrity-check.md` and record the result;
5. confirm the mobile baseline still works without Gas Town.

Validation evidence belongs in the work item or review, not as invented story state.

## Mapping to workshop concepts

Gas City scheduling must not replace workshop state:

| Workshop concept | Orchestration use |
| --- | --- |
| public repository | one Gas City RIG |
| infrastructure issue | one schedulable work item/bead |
| isolated branch/worktree | worker-owned implementation workspace |
| pull request or branch review | human integration checkpoint |
| `docs/workflow-manifest.md` | canonical role/runtime contract |
| integrity report | validation evidence |

Story-level `agent-queue.md`, `story-status.md`, canonical state, and handoffs remain domain records in the private repository. They are not replaced by Town or Beads state.

## Pilot exit criteria

The public-rig pilot is successful only after several narrowly scoped work items demonstrate that it can:

1. select only eligible infrastructure work;
2. use isolated clean workspaces;
3. obey the public/private boundary;
4. stop at human-review and semantic-change gates;
5. produce repeatable validation evidence;
6. resume after interruption without making mobile ChatGPT dependent on the orchestrator.

Only after those criteria pass should `knigi-content-private` be evaluated as
a second RIG. Its proposed artel model and extra safety gates are in
`docs/gas-city-story-rig-preparation.md`.
