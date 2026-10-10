# 00 - Workflow / Рабочий процесс

This repository is a sequential multi-agent storytelling workshop where the baseline agents are markdown role prompts executed in ordinary ChatGPT chats.

## Source of truth

- Role inventory, order, conditionality, isolation, mode, checkpoints: `docs/workflow-manifest.md`.
- Rules shared by every role (reset, isolation, preflight, inputs, gate verdict, after-role updates): `prompts/00-role-contract.md`.
- New-chat boot sequence: `START.md`.

If this file disagrees with the manifest, the manifest wins and this file must be repaired. This file does not repeat the role list.

## Supported baseline runtime

The workflow must work in ordinary ChatGPT, including the mobile app: one chat = one session, a new chat = clean-context isolation, GitHub files = durable memory. Child agents, VM, terminal, and parallel execution are optional enhancements only. See `docs/mobile-chatgpt-runtime.md`.

## Phases

```text
routing   003
intake    005 → author checkpoint
design    010 → 015? → 020 → author checkpoint → 030 → 040 → 050 → 060
          060 compiles 01-canonical/pre-draft-brief.md → author checkpoint
prose     070 (voice calibration → author choice → draft) → 080 → 090
review    100 → author checkpoint → 110 → 120 → 130 → 135? → 140 → author checkpoint
final     150 → author checkpoint → manuscript_complete candidate
```

`015` and `135` are conditional; see the manifest and `docs/pipeline-optimization.md`.

## Key artifacts per phase

- design → `01-canonical/canonical-story-state.md`, `decisions-log.md`, scene table in the `030` handoff;
- pre-draft → `01-canonical/pre-draft-brief.md` (template `prompts/00-pre-draft-brief-template.md`) including the voice contract;
- prose/review → `03-drafts/`, `04-reviews/`, `05-exports/`;
- cross-story → `../knigi-content-private/author/author-profile.md` (template `prompts/00-author-profile-template.md`), `docs/anti-llm-prose-checklist.md`.

## Revision routing

Use `003` when starting a new pipeline, resuming from an agent queue, or processing mixed/structural author feedback. The router sorts feedback, identifies the earliest affected role, builds the minimal safe route, updates the queue, and maintains `story-status.md`. It does not rewrite prose.

Skip `003` only for narrow obvious local fixes.

## Author checkpoints

Use the checkpoint column of the manifest and `docs/feedback-and-session-boundaries.md`. Stop at a checkpoint unless the author explicitly asked to continue through it.

## Optional enhanced execution

When real child agents/parallel execution exist, diagnosis-only roles may run in isolated/parallel contexts if they read the same stable draft and write disjoint outputs. Good candidates after a stable final-candidate draft: `100`, `110`, `120`, `130`, `135`, `140`.

Prose-editing roles `070`, `080`, `090`, and `150` remain sequential.

## Quality gates

Every role ends with a verdict per `docs/quality-gates.md`. Blocking findings reroute or stop downstream work.

## Framework feedback loop

When recurring friction reveals a workshop defect, use `docs/framework-retrospective.md`. Prefer strengthening an existing role/routing/state contract before adding a new permanent specialist. Author-level preferences go to the author profile, not into public prompts.

## Manuscript completion boundary

After `150` and its author checkpoint/quality gates, the story may become `manuscript_complete`. This is not `publication_ready`; see `docs/post-manuscript-frameworks.md`.

## Privacy

Concrete story workspaces are private and live under `../knigi-content-private/stories/<story-slug>/`. Never save raw ideas, handoffs, drafts, reviews, or exports into public tracked folders.
