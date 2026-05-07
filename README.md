# Мастерская писателя

AI-assisted storytelling repository: мультиагентная мастерская, где одна сырая идея рассказа проходит через последовательность специализированных литературных ролей.

Это публичный репозиторий для инфраструктуры: canonical bilingual prompt-файлы, правила handoff, шаблон story workspace и документация. Сами идеи, handoff-файлы, черновики, ревью и финальные тексты считаются приватными.

## Главный принцип

Каждый нумерованный prompt-файл в `prompts/` описывает отдельного специалиста. Прогон начинается с `003-диспетчер--revision-router--маршрутизатор-правок.md`: в простом новом случае он передает работу в `005`, а после авторского фидбека или при возобновлении сессии выбирает минимальный безопасный маршрут по уже существующим ролям.

Новая история создается не в публичной `stories/`, а в локальной ignored-папке:

```text
private/stories/<story-slug>/
```

`private/` является рабочим локальным хранилищем истории и намеренно не попадает в git. Это нормальное состояние проекта: обычный `rg --files` показывает tracked/public-инфраструктуру и может не показать реальные story workspace. Для работы с черновиками, фидбеком, handoff-файлами, ревью и экспортами проверяйте `private/` отдельно.

Название истории не дублируется в каждом файле. Его роль выполняет `story-slug` в имени родительской папки.

После каждой роли результат сохраняется в:

```text
private/stories/<story-slug>/02-handoffs/
```

Устойчивые решения переносятся в:

```text
private/stories/<story-slug>/01-canonical/canonical-story-state.md
```

Полные экспортные драфты сохраняются с номером версии и датой:

```text
private/stories/<story-slug>/05-exports/full-draft-v<N>-MM-DD.md
```

Например, `full-draft-v6-05-07.md` означает полный драфт версии 6 от 7 мая.

Межсессионная очередь агентов хранится в:

```text
private/stories/<story-slug>/06-agent-queue/agent-queue.md
```

Новая сессия берет из очереди следующий pending-агент, а не весь прошлый чат.

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
- `docs/feedback-and-session-boundaries.md`
- `docs/pipeline-optimization.md`
- `docs/agent-queue.md`
- `prompts/00-workflow.md`
- `prompts/00-handoff-template.md`
- `prompts/00-canonical-story-state-template.md`

## Canonical role prompts

Все specialist prompts используют naming convention: `NNN-короткое--english--русский.md`.

1. `prompts/003-диспетчер--revision-router--маршрутизатор-правок.md`
2. `prompts/005-приёмщик--idea-receiver--приёмщик-идеи.md`
3. `prompts/010-архитектор--idea-architect--архитектор-идеи.md`
4. `prompts/020-критик--brutal-critic--жестокий-критик.md`
5. `prompts/030-сюжетник--story-engineer--инженер-сюжета.md`
6. `prompts/040-психолог--character-psychologist--психолог-персонажей.md`
7. `prompts/050-мировик--worldlogic-auditor--аудитор-логики-мира.md`
8. `prompts/060-тематик--thematic-analyst--тематический-аналитик.md`
9. `prompts/070-черновик--draft-writer--писатель-черновика.md`
10. `prompts/080-структурщик--structural-editor--структурный-редактор.md`
11. `prompts/090-стилист--style-editor--стилевой-редактор.md`
12. `prompts/100-читатель--reader-simulator--симулятор-читателя.md`
13. `prompts/110-финалист--ending-analyst--аналитик-концовки.md`
14. `prompts/120-идеолог--ideology-stress-tester--идеологический-стресс-тестер.md`
15. `prompts/130-предсказатель--predictability-analyst--аналитик-предсказуемости.md`
16. `prompts/140-сверщик--continuity-auditor--аудитор-непрерывности.md`
17. `prompts/150-финред--final-editor--финальный-редактор.md`

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
