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

No numbered single-language role prompt duplicates were present at cleanup time.

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

- `prompts/003-диспетчер--revision-router--маршрутизатор-правок.md`
- `prompts/005-приёмщик--idea-receiver--приёмщик-идеи.md`
- `prompts/010-архитектор--idea-architect--архитектор-идеи.md`
- `prompts/020-критик--brutal-critic--жестокий-критик.md`
- `prompts/030-сюжетник--story-engineer--инженер-сюжета.md`
- `prompts/040-психолог--character-psychologist--психолог-персонажей.md`
- `prompts/050-мировик--worldlogic-auditor--аудитор-логики-мира.md`
- `prompts/060-тематик--thematic-analyst--тематический-аналитик.md`
- `prompts/070-черновик--draft-writer--писатель-черновика.md`
- `prompts/080-структурщик--structural-editor--структурный-редактор.md`
- `prompts/090-стилист--style-editor--стилевой-редактор.md`
- `prompts/100-читатель--reader-simulator--симулятор-читателя.md`
- `prompts/110-финалист--ending-analyst--аналитик-концовки.md`
- `prompts/120-идеолог--ideology-stress-tester--идеологический-стресс-тестер.md`
- `prompts/130-предсказатель--predictability-analyst--аналитик-предсказуемости.md`
- `prompts/140-сверщик--continuity-auditor--аудитор-непрерывности.md`
- `prompts/150-финред--final-editor--финальный-редактор.md`

## Canonical workflow files retained

- `prompts/00-workflow.md`
- `prompts/00-handoff-template.md`
- `prompts/00-canonical-story-state-template.md`

## Canonical files added during cleanup

The local repository did not contain advanced reviewer prompt files `110-140` at the start of this cleanup pass, so they were added using the same bilingual naming convention:

- `prompts/110-финалист--ending-analyst--аналитик-концовки.md`
- `prompts/120-идеолог--ideology-stress-tester--идеологический-стресс-тестер.md`
- `prompts/130-предсказатель--predictability-analyst--аналитик-предсказуемости.md`
- `prompts/140-сверщик--continuity-auditor--аудитор-непрерывности.md`

Later workflow additions:

- `prompts/003-диспетчер--revision-router--маршрутизатор-правок.md`
- `prompts/005-приёмщик--idea-receiver--приёмщик-идеи.md`
- `prompts/150-финред--final-editor--финальный-редактор.md`
- `docs/feedback-and-session-boundaries.md`
- `docs/agent-queue.md`

## Inconsistencies fixed

- `README.md` now lists canonical bilingual prompts `003-150`, with `003` as the revision router.
- `AGENTS.md` now forbids `prompts/ru/`, old single-language role prompts, and unnumbered prompt files as role definitions.
- `prompts/00-workflow.md` now runs through roles `003-150`, with `003` as the revision router.
- `docs/story-project-structure.md` now includes handoffs for `003-150`, the agent queue, review outputs for advanced reviewer roles, and the final-editor draft.
- `docs/role-map.md` now maps canonical bilingual prompts `003-150`.
- `docs/feedback-and-session-boundaries.md` now defines author feedback checkpoints and high-conflict role transitions.
- `stories/_template` now follows the canonical story folder layout.
- Existing private story workspace has completed content through role `150`.
- Concrete story workspaces are now treated as private by default and belong under ignored `private/stories/<story-slug>/`.

## Remaining potential issues

- The inserted intake role `005` was added after the first private story had already passed through the pipeline, so existing stories may need a retrospective or pending `005` handoff if strict completeness is required.
