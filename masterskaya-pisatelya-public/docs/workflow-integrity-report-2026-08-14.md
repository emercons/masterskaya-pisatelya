# Workflow integrity report — 2026-08-14

## Verdict

`PASS_WITH_WARNINGS`

No fatal or major contradiction remains among the current canonical role/runtime sources checked in this pass.

## Checks performed

- canonical manifest exists and contains roles `003, 005, 010, 015, 020, 030, 040, 050, 060, 070, 080, 090, 100, 110, 120, 130, 135, 140, 150`;
- canonical prompt directory contains the registered conditional roles `015` and `135`;
- README, role map, `00-workflow`, story-project structure, feedback/session rules, and agent-queue docs were updated to the manifest model;
- baseline runtime is ordinary ChatGPT/mobile, with fresh chats as the required clean-context mechanism and child agents only optional;
- story template contains `015`/`135` handoff placeholders, `similarity-ip-audit.md`, and `06-agent-queue/story-status.md`;
- quality gates exist for `015`, `020`, `050`, `100`, `135`, `140`, with `150` constrained by upstream gates;
- story isolation contract is wired into AGENTS, workflow, router, and critical role prompts;
- `150` now produces at most a `manuscript_complete` candidate and explicitly does not evaluate route-specific publication readiness;
- post-manuscript publishing/promotion responsibilities are separated into future sibling frameworks.

## Findings

| id | severity | file(s) | mismatch | source-of-truth answer | repair/status |
| --- | --- | --- | --- | --- | --- |
| W1 | MINOR | existing private story queues | Some active/legacy queues still use `fresh_session` and may contain older `execution_mode` values. | New canonical field is `chat_mode`; legacy values remain readable. | Compatibility documented; no bulk private rewrite required. |
| W2 | MINOR | `docs/structural-audit-report.md` | Historical 2026-05 report lists the then-current older role inventory. | `docs/workflow-manifest.md` is current source of truth. | Leave historical report intact because it is explicitly dated/audit history. |
| W3 | MINOR | private story workspaces | Not every existing story has been bulk-backfilled with `story-status.md`. | Active stories should converge toward status snapshots when resumed. | Two currently active stories were backfilled; continue opportunistically. |
| W4 | COSMETIC | some older specialist prompts | Some headers still use wording `Fresh session: required/no` rather than new `Chat isolation` vocabulary. | Interpret semantically through manifest; child agents must never be mandatory. | No operational contradiction; normalize opportunistically when those prompts are next edited. |

## Role inventory comparison

Current canonical/explanatory sources checked in this pass agree that:

- `015` is conditional and sits between architecture and brutal criticism when a premise-defining criterion requires adversarial testing;
- `135` is conditional/late and sits before continuity/finalization when external-work similarity/IP-risk review is warranted;
- no generic publishing or promotion role follows `150` inside the literary pipeline.

## Mobile-runtime findings

`PASS`.

The public workflow now explicitly supports ordinary ChatGPT/mobile with no VM, terminal, background worker, or real child-agent requirement.

`fresh_chat_required` is the canonical isolation boundary for adversarial roles. Optional richer runtimes may substitute a child agent but cannot make the workflow non-resumable from mobile ChatGPT.

## Template findings

`PASS`.

The template now includes:

- current conditional handoff namespaces (`015`, `135`);
- similarity/IP review placeholder;
- mobile-first queue schema;
- `story-status.md`.

## Quality-gate findings

`PASS`.

Critical diagnosis roles now have explicit completion gates. `020` additionally has severity classification and a mandatory second hostile pass when the first review is suspiciously mild.

## Isolation/privacy findings

`PASS`.

Story-specific reads/writes are constrained to the resolved private workspace unless cross-story work is explicitly required.

## Post-manuscript-boundary findings

`PASS`.

`manuscript_complete` and `publication_ready` are separate states. Publishing and promotion are documented as future sibling workflows that require current-market research before detailed implementation.

## Recommended patch order for future changes

1. Change `docs/workflow-manifest.md` first when canonical role/runtime semantics change.
2. Update affected specialist prompt(s).
3. Update README/role-map/workflow/story structure/queue/template as applicable.
4. Run `docs/workflow-integrity-check.md`.
5. Backfill private operational state only when an active story needs it; avoid noisy bulk rewrites.

## Files intentionally not rewritten in this pass

- historical audit reports whose dated content describes past state;
- every legacy private queue solely for field renaming;
- unrelated specialist prompts whose existing semantics already permit normal manual/fresh-chat execution;
- private story prose/canon unrelated to the new status snapshot.
