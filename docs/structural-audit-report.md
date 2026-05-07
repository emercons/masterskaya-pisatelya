# Structural audit report

Date: 2026-05-07

## Scope

Cleanup and unification of storytelling infrastructure for `emercons/masteskaya-pisatelya`.

Read before cleanup:

- `README.md`
- `AGENTS.md`
- `docs/story-project-structure.md`
- `prompts/00-workflow.md`

## Legacy files removed

No numbered single-language role prompt duplicates such as `prompts/01-idea-architect.md` were present at cleanup time.

`prompts/ru/` was not present.

Removed drift / non-canonical infrastructure:

- `prompts/brainstorming-prompts.md`
- `prompts/master-prompt.md`
- `prompts/quick-commands.md`
- `prompts/review-prompts.md`
- `prompts/rewrite-prompts.md`
- `agents/`
- `workflows/`
- `templates/`
- `knowledge/`
- `ROADMAP.md`
- `docs/cleanup-plan.md`
- `docs/how-to-use.md`
- `docs/naming.md`

Replaced old `stories/_template` files:

- `stories/_template/story-bible.md`
- `stories/_template/outline.md`
- `stories/_template/characters.md`
- `stories/_template/scenes.md`
- `stories/_template/draft.md`
- `stories/_template/continuity-log.md`
- `stories/_template/revision-log.md`
- `stories/_template/feedback-log.md`

## Canonical bilingual role prompts retained

- `prompts/01-idea-architect--архитектор-идеи.md`
- `prompts/02-brutal-critic--жестокий-критик.md`
- `prompts/03-story-engineer--инженер-сюжета.md`
- `prompts/04-character-psychologist--психолог-персонажей.md`
- `prompts/05-worldlogic-auditor--аудитор-логики-мира.md`
- `prompts/06-thematic-analyst--тематический-аналитик.md`
- `prompts/07-draft-writer--писатель-черновика.md`
- `prompts/08-structural-editor--структурный-редактор.md`
- `prompts/09-style-editor--стилевой-редактор.md`
- `prompts/10-reader-simulator--симулятор-читателя.md`
- `prompts/11-ending-analyst--аналитик-концовки.md`
- `prompts/12-ideology-stress-tester--идеологический-стресс-тестер.md`
- `prompts/13-predictability-analyst--аналитик-предсказуемости.md`
- `prompts/14-continuity-auditor--аудитор-непрерывности.md`

## Canonical workflow files retained

- `prompts/00-workflow.md`
- `prompts/00-handoff-template.md`
- `prompts/00-canonical-story-state-template.md`

## Canonical files added during cleanup

The local repository did not contain advanced reviewer prompt files `11-14` at the start of this cleanup pass, so they were added using the same bilingual naming convention:

- `prompts/11-ending-analyst--аналитик-концовки.md`
- `prompts/12-ideology-stress-tester--идеологический-стресс-тестер.md`
- `prompts/13-predictability-analyst--аналитик-предсказуемости.md`
- `prompts/14-continuity-auditor--аудитор-непрерывности.md`

## Inconsistencies fixed

- `README.md` now lists canonical bilingual prompts `01-14` only.
- `AGENTS.md` now forbids `prompts/ru/`, old single-language role prompts, and unnumbered prompt files as role definitions.
- `prompts/00-workflow.md` now runs through roles `01-14`.
- `docs/story-project-structure.md` now includes handoffs for `01-14` and review outputs for advanced reviewer roles.
- `docs/role-map.md` now maps canonical bilingual prompts `01-14`.
- `stories/_template` now follows the canonical story folder layout.
- Existing private story workspace now has placeholder handoffs/review files for roles `11-14`.
- Concrete story workspaces are now treated as private by default and belong under ignored `private/stories/<story-slug>/`.

## Remaining potential issues

- The existing private story workspace has only actually been processed through role `10`; roles `11-14` are present as pending placeholders.
- The repository has not been committed or pushed.
