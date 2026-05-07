# Story project structure

This repository is a public infrastructure workflow for AI-assisted storytelling. It is not an application and not a code project.

Concrete stories are private by default.

Every real story lives in its own ignored local folder:

```text
private/stories/<story-slug>/
```

The `private/` folder is deliberately local-only. It is expected to be absent from tracked-file listings and ordinary `rg --files` output because `.gitignore` excludes it. Agents should still look there explicitly for active story material.

The public `stories/_template/` folder is only a copy source. Do not write actual story content into public `stories/<story-slug>/` folders.

## Required private story structure

```text
private/stories/<story-slug>/00-input/raw-idea-from-chat.md
private/stories/<story-slug>/00-input/author-notes.md

private/stories/<story-slug>/01-canonical/canonical-story-state.md
private/stories/<story-slug>/01-canonical/decisions-log.md

private/stories/<story-slug>/02-handoffs/003-диспетчер--revision-router--маршрутизатор-правок.md
private/stories/<story-slug>/02-handoffs/005-приёмщик--idea-receiver--приёмщик-идеи.md
private/stories/<story-slug>/02-handoffs/010-архитектор--idea-architect--архитектор-идеи.md
private/stories/<story-slug>/02-handoffs/020-критик--brutal-critic--жестокий-критик.md
private/stories/<story-slug>/02-handoffs/030-сюжетник--story-engineer--инженер-сюжета.md
private/stories/<story-slug>/02-handoffs/040-психолог--character-psychologist--психолог-персонажей.md
private/stories/<story-slug>/02-handoffs/050-мировик--worldlogic-auditor--аудитор-логики-мира.md
private/stories/<story-slug>/02-handoffs/060-тематик--thematic-analyst--тематический-аналитик.md
private/stories/<story-slug>/02-handoffs/070-черновик--draft-writer--писатель-черновика.md
private/stories/<story-slug>/02-handoffs/080-структурщик--structural-editor--структурный-редактор.md
private/stories/<story-slug>/02-handoffs/090-стилист--style-editor--стилевой-редактор.md
private/stories/<story-slug>/02-handoffs/100-читатель--reader-simulator--симулятор-читателя.md
private/stories/<story-slug>/02-handoffs/110-финалист--ending-analyst--аналитик-концовки.md
private/stories/<story-slug>/02-handoffs/120-идеолог--ideology-stress-tester--идеологический-стресс-тестер.md
private/stories/<story-slug>/02-handoffs/130-предсказатель--predictability-analyst--аналитик-предсказуемости.md
private/stories/<story-slug>/02-handoffs/140-сверщик--continuity-auditor--аудитор-непрерывности.md
private/stories/<story-slug>/02-handoffs/150-финред--final-editor--финальный-редактор.md

private/stories/<story-slug>/03-drafts/draft-v0-raw.md
private/stories/<story-slug>/03-drafts/draft-v1-after-070-черновик.md
private/stories/<story-slug>/03-drafts/draft-v2-after-080-структурщик.md
private/stories/<story-slug>/03-drafts/draft-v3-after-090-стилист.md
private/stories/<story-slug>/03-drafts/draft-v4-final-candidate.md
private/stories/<story-slug>/03-drafts/draft-v5-after-150-финред.md

private/stories/<story-slug>/04-reviews/reader-notes.md
private/stories/<story-slug>/04-reviews/ending-analysis.md
private/stories/<story-slug>/04-reviews/ideology-stress-test.md
private/stories/<story-slug>/04-reviews/predictability-analysis.md
private/stories/<story-slug>/04-reviews/continuity-audit.md
private/stories/<story-slug>/04-reviews/author-retrospective.md

private/stories/<story-slug>/05-exports/full-draft-v<N>-MM-DD.md

private/stories/<story-slug>/06-agent-queue/agent-queue.md
```

## Why filenames do not include story title

The story title or slug belongs to the parent folder:

```text
private/stories/<story-slug>/
```

Files inside every story folder use stable workflow names. This keeps automation simple and lets agents know exactly where to read and write each stage.

## Export naming

Full-draft exports must be versioned:

```text
private/stories/<story-slug>/05-exports/full-draft-v<N>-MM-DD.md
```

Use the same version number as the source draft or final pass. Use `MM-DD` for the calendar date, for example `05-07` for May 7.

Example:

```text
private/stories/chelovek-kak-biologicheskiy-ai-agent/05-exports/full-draft-v6-05-07.md
```

Do not use an unversioned `final.md` or legacy final-prefixed versioned name as the canonical export. If a temporary convenience copy exists, treat the versioned `full-draft-v...` export as the source of truth.

## Core rule

Each specialist role works in sequence. A role receives only:

- the current specialist prompt;
- current canonical story state;
- the latest relevant handoff;
- the relevant draft fragment.

The role must write a compact handoff before the next role begins.

See `docs/feedback-and-session-boundaries.md` before continuing through author feedback checkpoints or high-conflict role transitions.

Use `prompts/003-диспетчер--revision-router--маршрутизатор-правок.md` when starting or resuming a pipeline, and after complex author feedback, to sort requested changes and choose the earliest affected role before rewriting.

Use `private/stories/<story-slug>/06-agent-queue/agent-queue.md` to continue work across sessions. A new session should read the queue, canonical state, the latest relevant handoff, and the relevant draft fragment, not the full old conversation.

## Canonical story state

The canonical story state is the durable source of truth. It should contain only stable decisions, not every brainstormed option.

Update it when a role changes:

- premise;
- protagonist;
- conflict;
- setting rules;
- ending direction;
- draft-level facts;
- irreversible author decisions.

## Handoffs

Handoffs prevent role contamination. They are compact summaries, not full transcripts.

A good handoff contains:

- what the role did;
- durable decisions;
- unresolved questions;
- next role instructions;
- warnings about what not to flatten or normalize.

## Prompt naming

Use only canonical bilingual prompt filenames:

```text
prompts/NNN-короткое--english--русский.md
```

Do not create alternate role prompt locations or non-bilingual role prompt filenames.
