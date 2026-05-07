# Мастерская писателя

AI-assisted storytelling repository: мультиагентная мастерская, где одна сырая идея рассказа проходит через последовательность специализированных литературных ролей.

Это публичный репозиторий для инфраструктуры: canonical bilingual prompt-файлы, правила handoff, шаблон story workspace и документация. Сами идеи, handoff-файлы, черновики, ревью и финальные тексты считаются приватными.

## Главный принцип

Каждый нумерованный prompt-файл в `prompts/` описывает отдельного специалиста. Роли применяются строго по порядку номеров.

Новая история создается не в публичной `stories/`, а в локальной ignored-папке:

```text
private/stories/<story-slug>/
```

Название истории не дублируется в каждом файле. Его роль выполняет `story-slug` в имени родительской папки.

После каждой роли результат сохраняется в:

```text
private/stories/<story-slug>/02-handoffs/
```

Устойчивые решения переносятся в:

```text
private/stories/<story-slug>/01-canonical/canonical-story-state.md
```

## Public vs private

Публично коммитится:

- `prompts/`
- `docs/`
- `stories/_template/`
- корневые правила проекта

Не коммитится:

- `private/`
- реальные story folders
- raw ideas
- canonical state конкретных историй
- handoffs
- drafts
- reviews
- exports

## Обязательные файлы workflow

- `docs/story-project-structure.md`
- `docs/privacy-and-story-storage.md`
- `prompts/00-workflow.md`
- `prompts/00-handoff-template.md`
- `prompts/00-canonical-story-state-template.md`

## Canonical role prompts

Все specialist prompts используют bilingual naming convention: `NN-english--русский.md`.

1. `prompts/01-idea-architect--архитектор-идеи.md`
2. `prompts/02-brutal-critic--жестокий-критик.md`
3. `prompts/03-story-engineer--инженер-сюжета.md`
4. `prompts/04-character-psychologist--психолог-персонажей.md`
5. `prompts/05-worldlogic-auditor--аудитор-логики-мира.md`
6. `prompts/06-thematic-analyst--тематический-аналитик.md`
7. `prompts/07-draft-writer--писатель-черновика.md`
8. `prompts/08-structural-editor--структурный-редактор.md`
9. `prompts/09-style-editor--стилевой-редактор.md`
10. `prompts/10-reader-simulator--симулятор-читателя.md`
11. `prompts/11-ending-analyst--аналитик-концовки.md`
12. `prompts/12-ideology-stress-tester--идеологический-стресс-тестер.md`
13. `prompts/13-predictability-analyst--аналитик-предсказуемости.md`
14. `prompts/14-continuity-auditor--аудитор-непрерывности.md`

## Role reset

Перед каждым specialist prompt:

```text
You are ONLY the currently assigned specialist.
Forget previous specialist roles.
Do not continue previous analytical styles.
Do not behave as a general assistant.
Your scope is intentionally narrow.
```

## Infrastructure rule

Use only the numbered bilingual file list above as the role prompt source of truth.
