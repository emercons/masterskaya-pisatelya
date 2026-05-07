# Story project structure

This repository is a public infrastructure workflow for AI-assisted storytelling. It is not an application and not a code project.

Concrete stories are private by default.

Every real story lives in its own ignored local folder:

```text
private/stories/<story-slug>/
```

The public `stories/_template/` folder is only a copy source. Do not write actual story content into public `stories/<story-slug>/` folders.

## Required private story structure

```text
private/stories/<story-slug>/00-input/raw-idea-from-chat.md
private/stories/<story-slug>/00-input/author-notes.md

private/stories/<story-slug>/01-canonical/canonical-story-state.md
private/stories/<story-slug>/01-canonical/decisions-log.md

private/stories/<story-slug>/02-handoffs/01-idea-architect--архитектор-идеи.md
private/stories/<story-slug>/02-handoffs/02-brutal-critic--жестокий-критик.md
private/stories/<story-slug>/02-handoffs/03-story-engineer--инженер-сюжета.md
private/stories/<story-slug>/02-handoffs/04-character-psychologist--психолог-персонажей.md
private/stories/<story-slug>/02-handoffs/05-worldlogic-auditor--аудитор-логики-мира.md
private/stories/<story-slug>/02-handoffs/06-thematic-analyst--тематический-аналитик.md
private/stories/<story-slug>/02-handoffs/07-draft-writer--писатель-черновика.md
private/stories/<story-slug>/02-handoffs/08-structural-editor--структурный-редактор.md
private/stories/<story-slug>/02-handoffs/09-style-editor--стилевой-редактор.md
private/stories/<story-slug>/02-handoffs/10-reader-simulator--симулятор-читателя.md
private/stories/<story-slug>/02-handoffs/11-ending-analyst--аналитик-концовки.md
private/stories/<story-slug>/02-handoffs/12-ideology-stress-tester--идеологический-стресс-тестер.md
private/stories/<story-slug>/02-handoffs/13-predictability-analyst--аналитик-предсказуемости.md
private/stories/<story-slug>/02-handoffs/14-continuity-auditor--аудитор-непрерывности.md

private/stories/<story-slug>/03-drafts/draft-v0-raw.md
private/stories/<story-slug>/03-drafts/draft-v1-after-07-draft-writer.md
private/stories/<story-slug>/03-drafts/draft-v2-after-08-structural-editor.md
private/stories/<story-slug>/03-drafts/draft-v3-after-09-style-editor.md
private/stories/<story-slug>/03-drafts/draft-v4-final-candidate.md

private/stories/<story-slug>/04-reviews/reader-notes.md
private/stories/<story-slug>/04-reviews/ending-analysis.md
private/stories/<story-slug>/04-reviews/ideology-stress-test.md
private/stories/<story-slug>/04-reviews/predictability-analysis.md
private/stories/<story-slug>/04-reviews/continuity-audit.md
private/stories/<story-slug>/04-reviews/author-retrospective.md

private/stories/<story-slug>/05-exports/final.md
```

## Why filenames do not include story title

The story title or slug belongs to the parent folder:

```text
private/stories/<story-slug>/
```

Files inside every story folder use stable workflow names. This keeps automation simple and lets agents know exactly where to read and write each stage.

## Core rule

Each specialist role works in sequence. A role receives only:

- the current specialist prompt;
- current canonical story state;
- the latest relevant handoff;
- the relevant draft fragment.

The role must write a compact handoff before the next role begins.

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
prompts/NN-english--русский.md
```

Do not create alternate role prompt locations or non-bilingual role prompt filenames.
