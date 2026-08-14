# Roadmap / Дорожная карта

Status: active architecture roadmap.

This roadmap is for the public workflow repository. Concrete story content remains in `emercons/knigi-content-private`.

## Runtime assumption

The primary supported runtime is **ordinary ChatGPT, including the mobile app**:

- one chat can run one or several compatible roles;
- a new chat is the standard isolation mechanism for a fresh role;
- GitHub files are durable memory between chats;
- no virtual machine, local filesystem, background worker, real child agent, or parallel-agent runtime is required;
- environments that do support child agents or parallel execution may use them as optional acceleration only.

See `docs/mobile-chatgpt-runtime.md`.

## Phase 1 — Single source of truth

Goal: stop workflow drift between README, role map, templates, and prompts.

- [x] Create `docs/workflow-manifest.md` as the canonical role/runtime manifest.
- [x] Create a ChatGPT-runnable integrity check in `docs/workflow-integrity-check.md`.
- [x] Register conditional roles `015` and `135` everywhere that describes the canonical pipeline.
- [ ] Periodically run the integrity check after adding/removing/changing a role.

## Phase 2 — Mobile-first execution

Goal: make the workshop fully usable from normal ChatGPT chats.

- [x] Define `fresh_chat` as the baseline isolation mechanism.
- [x] Make child-agent execution optional rather than required.
- [x] Define minimal new-chat launch context.
- [x] Define how a chat recovers from GitHub without reading the old conversation.

## Phase 3 — Story isolation and status

Goal: prevent cross-story contamination and make current progress obvious.

- [x] Add `docs/story-isolation-contract.md`.
- [x] Add `story-status.md` beside the agent queue in each story workspace.
- [x] Require the router to maintain a concise status snapshot.
- [x] Add a template status file for new stories.
- [ ] Backfill status files into active private stories when they are next touched.

## Phase 4 — Quality gates

Goal: prevent a role from being marked complete merely because it produced text.

- [x] Add `docs/quality-gates.md`.
- [x] Strengthen the `020` critic contract toward adversarial failure-finding.
- [x] Define gates for `015`, `050`, `100`, `135`, and `140`.
- [x] Require unresolved gate failures to block or reroute downstream work.
- [ ] Collect empirical failure cases from completed stories and refine thresholds.

## Phase 5 — Framework feedback loop

Goal: let real story work improve the workshop without overfitting to one story.

- [x] Add `docs/framework-retrospective.md`.
- [x] Separate story-specific fixes from recurring workflow defects.
- [x] Require evidence from repeated friction before adding a permanent specialist role, except for clear safety/integrity gaps.
- [ ] Run retrospectives after major story milestones and after publication-ready completion.

## Phase 6 — Manuscript completion boundary

Goal: keep literary production separate from publishing and promotion operations.

- [x] Define `manuscript_complete` vs `publication_ready` in `docs/post-manuscript-frameworks.md`.
- [x] Keep roles after `150` out of the writing pipeline unless they are genuinely literary/editorial.
- [x] Define future sibling frameworks: Publishing Workshop and Promotion Workshop.
- [ ] Research current submission markets, first-publication rights, AI-assistance policies, translation strategy, self-publishing channels, and promotion practices before implementing those frameworks.

## Near-term maintenance

1. Run the integrity check whenever a canonical role changes.
2. Backfill `story-status.md` opportunistically, not by bulk rewriting private stories.
3. Use active story retrospectives to tune quality gates.
4. Do not add automation that makes mobile ChatGPT a second-class runtime.
5. Do not require infrastructure that the author cannot invoke from an ordinary chat.
