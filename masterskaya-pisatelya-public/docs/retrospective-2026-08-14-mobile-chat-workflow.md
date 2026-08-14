# Workshop retrospective — 2026-08-14 mobile/chat workflow

This retrospective contains only generalized workflow findings; no private story content is copied here.

## Evidence

| id | class | symptom | root cause | recurrence evidence | severity | framework change |
| --- | --- | --- | --- | --- | --- | --- |
| R1 | documentation_drift | Newly added conditional roles appeared in workflow/role map before README/template structure caught up. | Several files acted as independent role inventories. | More than one role addition exposed the same drift pattern. | major | Add canonical `workflow-manifest.md` + ChatGPT integrity check. |
| R2 | runtime_defect | Documentation treated real child agents as the preferred/default isolation mechanism even though ordinary mobile ChatGPT mainly exposes separate chats. | Runtime assumptions came from richer agent environments rather than the author's actual primary surface. | Affects every adversarial role transition. | major | Make `fresh_chat_required` the baseline; child agents optional only. |
| R3 | state_defect | Author can be uncertain whether prior work finished and what exact next action is required. | Queue is detailed but not optimized as a human resume snapshot. | Cross-session development repeatedly needs a concise current-state answer. | major | Add `06-agent-queue/story-status.md`. |
| R4 | story_specific -> prompt_defect | A supposedly brutal critical pass can contain too much positive framing and too few independent attacks. | `020` asked for sharpness but lacked an adversarial completion gate and second hostile pass. | Re-running criticism for more negative pressure demonstrates contract weakness. | major | Strengthen `020`; add severity taxonomy + mandatory second hostile pass when first pass is too mild. |
| R5 | state/routing_defect | Parallel story work makes the author over-specify repo/slug/workspace to prevent accidental contamination. | Story isolation was implicit in paths but not an explicit preflight contract. | Repeated need for long launch prompts across different stories. | fatal potential | Add story isolation contract and short mobile launch protocol. |
| R6 | missing_recurring_pressure | Premise-defining criteria and external-work similarity required distinct repeated audits. | Existing general critic/worldlogic roles did not provide stable adversarial comparison or external-work research pressure. | Separate `015` and `135` roles already emerged from real work. | major | Keep them conditional and register them in one manifest. |
| R7 | post_manuscript | Publishing/promotion concerns risk being appended as more literary agents. | No explicit boundary between manuscript completion and route-specific publication readiness. | Expected future workflow expansion. | major | Define sibling Publishing/Promotion frameworks instead of roles `160+`. |

## Changes applied

- Added canonical workflow manifest.
- Added mobile-runnable integrity validator.
- Made ordinary ChatGPT/mobile the primary supported runtime.
- Added story isolation contract.
- Added story-status protocol and template.
- Added explicit quality gates.
- Strengthened `020`, `015`, `050`, `100`, `135`, `140`, and final boundary in `150`.
- Added framework retrospective protocol.
- Defined manuscript-complete vs publication-ready boundary.
- Updated template coverage for `015`, `135`, and story status.

## New-role decision

No additional literary specialist is justified by this retrospective.

The current problem was mainly orchestration/state/runtime quality, not lack of more literary roles.

## Mobile-runtime decision

The workshop must remain fully operable with:

- ordinary ChatGPT chats;
- new chat for clean-role isolation;
- GitHub connector/state files.

Any future automation/child-agent/VM layer must be additive and preserve this fallback.

## Follow-up

Run `docs/workflow-integrity-check.md` after the 2026-08-14 changes and after future role additions.
