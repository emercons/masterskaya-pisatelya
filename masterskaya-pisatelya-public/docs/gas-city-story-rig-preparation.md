# Gas City story RIG — preparation / Подготовка текстового RIG

Status: design for review. This document prepares a private-story RIG; it does
not authorize registering it, creating Beads, starting workers, or opening a
real story to an external provider.

## Decision in brief

The account platform is **Gas City** with the Gastown pack.  A RIG is a
repository-level execution boundary, not a new RIG for every story.  The
proposed second RIG is the private repository `emercons/knigi-content-private`.
Inside it, every story gets a separate, short-lived **artel**: a directed group
of canonical workshop roles working only on that story's declared files.

```text
Gas City control plane
├── public-workflow RIG: emercons/masterskaya-pisatelya
│   └── prompts, templates, contracts, integrity checks
└── proposed private-story RIG: emercons/knigi-content-private
    ├── story <slug A> artel: role beads + isolated worktrees
    └── story <slug B> artel: role beads + isolated worktrees

Each artel: canonical state -> role handoffs/reviews -> author gate -> next bead
```

One RIG per repository preserves one deliberate Git boundary, a durable
project ledger and a controllable wake/sleep lifecycle.  One RIG per story
would multiply agents, ledgers and recovery surfaces without improving the
workshop's existing story isolation.  Story identity belongs in a bead's
explicit, minimally disclosed work contract and its private paths, not in the
RIG identity.

`docs/workflow-manifest.md`, the private story's canonical state, queue,
status and handoffs remain the literary source of truth.  Gas City's
Beads/Dolt state is only durable task ownership and execution evidence.

## Two different kinds of agents

Gas City/Gastown agents and workshop specialists must not be conflated.

| Plane | Agents | Authority |
| --- | --- | --- |
| City mechanics | controller, Mayor, deacon, witness, polecats, refinery, dogs | scheduling, worktree lifecycle, task recovery and health; no literary choice or canon authority |
| Literary artel | canonical numbered roles `003`–`150` | analyse, design, audit or edit one text only under the manifest, quality gates and author checkpoints |

`003-диспетчер` is the literary route owner, not a replacement Mayor.
The Mayor must not choose a premise, resolve critique, accept a revision, or
decide that a manuscript is ready.  Conversely, the dispatcher does not own
the City scheduler, provider configuration or worker recovery.

The existing role inventory does **not** need to be renamed or rewritten for
the first pilot.  Add orchestration metadata beside it only after this design
is accepted; changing a canonical role still requires an explicit update of
`docs/workflow-manifest.md` and the integrity check.

## Artel profile for one story

An artel is instantiated from a stable private snapshot.  Its parent bead (or
formula/molecule root) is an opaque identifier such as
`story:<slug>:cycle:<n>`; titles, notes, logs and receipts must not contain raw
ideas, prose, detailed canon or long excerpts.

| Artel leg | Canonical roles | Execution shape | Output / gate |
| --- | --- | --- | --- |
| route and conception | `003`, `005`, `010`, `015?`, `020`, `030`, `040`, `050`, `060` | mostly sequential; `015`/`050` may be separate read-only reviews of the same approved snapshot | handoffs and canon changes; stop at the manifest's author checkpoints |
| prose chain | `070`, `080`, `090` | strictly sequential, one declared input draft per step | a new private draft version, never a merge decision |
| review circle | `100`, `110`, `120`, `130`, `135?`, `140` | read-only diagnostics may run in parallel only against the same immutable draft snapshot | separate reviews; author/router reconciles conflicts |
| final edit | `150` | strictly sequential after required reviews and decisions | `manuscript_complete` candidate, then the required author checkpoint |

The conditional roles remain conditional: `015` is not forced where no
premise-defining rule exists, and `135` is not a routine content-export job.
No two prose editors may change the same draft concurrently.  A review circle
can be parallel only when each member has its own output path and no member
rewrites prose.

## Work-bead contract

Every artel task must carry, or point to a private contract containing, all of
the following.  A missing field means the task is blocked, not inferred.

```text
story_slug: exact private workspace identity
cycle: stable author-approved revision cycle
role: canonical prompt filename and numeric id
mode: diagnosis | design | audit | sequential_prose
snapshot: input draft/canon/handoff version or Git commit
allowed_inputs: exact private paths plus named public prompt/docs
expected_outputs: exact private paths
prose_editing: yes | no
parallel_group: blank, or immutable-snapshot group id
quality_gate: named gate or none
author_gate: none | required-before-start | required-after-result
provider_route: approved lane and data-handling profile
remote_effects: false
push_merge: false
stop_condition: precise blocker or checkpoint
```

The content of the task belongs in the private worktree.  The ledger receives
only the minimum metadata necessary to recover ownership: identifiers, paths
where approved, branch/worktree, base and result commits, validation outcome,
drain state and the next human decision.  It must never become a duplicate
story database.

## Provider and mutation policy for the first private pilot

The City currently distinguishes provider lanes by qualification and does not
let a helper consume arbitrary ready work.  The proposed private RIG is even
stricter:

| Lane | Proposed first-pilot use in the private RIG |
| --- | --- |
| `codex-lso` | default candidate for explicitly approved read/write artel work; review and author gates remain mandatory |
| `claude-subscription` | no story work until an operator approves a literary-content route profile and a synthetic-fixture privacy/receipt test passes |
| `nvidia-helper` | no real story content in the first pilot; it remains explicitly routed and review-required |
| `zai-helper` | unavailable: external entitlement is blocked and it has no private-story role |

Repository visibility is not a sensitivity classification.  The author or
operator must explicitly classify the material and approve a lane for each
task class.  A provider's ability to edit locally does not authorize it to
read a real manuscript.  No route may push, open a pull request, merge,
publish, submit, message anyone, or make an external-world change.

## Required safety adaptation before any launch

The stock Gastown coding flow includes a refinery and may push or merge code.
It must **not** be pointed at private stories unchanged.  Before the private
RIG is registered, implement and review a dedicated story-artel formula or
policy overlay that:

1. starts the RIG suspended and wakes it only for an approved bounded cycle;
2. creates one isolated worktree and branch per bead, scoped to one story;
3. forbids `git push`, PR creation, refinery handoff and every automatic merge;
4. has workers stop at `author_gate` instead of treating a literary choice as a
   recoverable mechanical blocker;
5. writes handoffs, queue/status and review files only to declared private
   paths, while changing canon only where the role is allowed;
6. requires `git diff --check`, allowed-path review, output existence and the
   role's quality gate before a receipt can be closed;
7. suspends/drains after the approved cycle without deleting unreviewed work.

The witness may report a stalled task and preserve evidence, but it must not
salvage, commit, push or reroute story changes around an author gate.  A dog
may only stop a clearly unhealthy worker through the standard City warrant
process; it has no authority over manuscript state.

## Pilot sequence and exit gate

Do not register the RIG while the public workflow RIG is still only a paper
contract.  The sequence is:

1. finish several safe public-workflow RIG tasks and retain their receipts;
2. approve this design, the private RIG name/prefix and data-handling routes;
3. build the no-push/no-merge story-artel overlay and test it against a
   disposable synthetic private fixture, never a real story;
4. prove path confinement, role isolation, receipt completeness, author-gate
   stopping, worktree recovery and clean drain;
5. register the real private RIG suspended, with no queued story work;
6. run one author-approved low-risk diagnostic cycle for exactly one story;
7. review every local diff, handoff, receipt and City record before allowing
   any prose-editing cycle or a second provider lane.

The pilot passes only if it preserves the mobile/manual workflow, never copies
content into public/City-visible artifacts, keeps text changes reviewable and
recoverable, and stops reliably at every author checkpoint.  Failure means
suspend the RIG and retain the evidence; it does not mean silently continue in
another lane.

## What remains manual

- selecting a story, premise, canon, literary direction or final revision;
- releasing an author checkpoint or resolving conflicting reviews;
- content classification and provider/lane approval;
- registering/suspending a real RIG, changing City configuration or routes;
- pushing, merging, publishing, submitting or communicating externally.

## Implementation follow-up

After approval, create a small private-RIG implementation packet in the
orchestration repository: rig name/prefix, path policy, non-secret pack
overlay, receipt schema, synthetic fixture, exact validation commands and a
rollback/suspension runbook.  Then update the public role map with a separate
*orchestration profile* column; do not replace the canonical role names or
mobile-first semantics.

Related documents:

- [public workflow RIG boundary](gastown-rig-contract.md);
- [canonical literary roles and checkpoints](workflow-manifest.md);
- [story queue/status semantics](agent-queue.md);
- [per-story path boundary](story-isolation-contract.md);
- [completion gates](quality-gates.md).
