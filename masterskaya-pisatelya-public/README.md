# Мастерская писателя

AI-assisted storytelling repository: мультиагентная мастерская, где одна сырая идея рассказа проходит через последовательность специализированных литературных ролей.

Это публичный репозиторий для инфраструктуры: canonical bilingual prompt-файлы, правила handoff, шаблон story workspace и документация. Сами идеи, handoff-файлы, черновики, ревью и финальные тексты считаются приватными.

## Главный принцип

Каждый нумерованный prompt-файл в `prompts/` описывает отдельного специалиста. Прогон начинается с `003-диспетчер--revision-router--маршрутизатор-правок.md`: в простом новом случае он передает работу в `005`, а после авторского фидбека или при возобновлении сессии выбирает минимальный безопасный маршрут по уже существующим ролям.

Новая история создается не в публичной `stories/`, а в отдельной приватной папке рядом с публичной инфраструктурой:

```text
masterskaya-pisatelya-PRIVATE/stories/<story-slug>/
```

`masterskaya-pisatelya-PRIVATE/` является рабочим хранилищем реальных историй. Если репозиторий приватный, эти файлы могут оставаться tracked; если репозиторий станет публичным, сначала нужно явно решить, что делать с этой папкой. Для работы с черновиками, фидбеком, handoff-файлами, ревью и экспортами проверяйте `masterskaya-pisatelya-PRIVATE/stories/` отдельно.

Название истории не дублируется в каждом файле. Его роль выполняет `story-slug` в имени родительской папки.

После каждой роли результат сохраняется в:

```text
masterskaya-pisatelya-PRIVATE/stories/<story-slug>/02-handoffs/
```

Устойчивые решения переносятся в:

```text
masterskaya-pisatelya-PRIVATE/stories/<story-slug>/01-canonical/canonical-story-state.md
```

Полные экспортные драфты сохраняются с номером версии и датой:

```text
masterskaya-pisatelya-PRIVATE/stories/<story-slug>/05-exports/full-draft-v<N>-MM-DD.md
```

Например, `full-draft-v6-05-07.md` означает полный драфт версии 6 от 7 мая.

Экспорты для авторского ревью используют стабильные ID абзацев по `docs/stable-paragraph-ids.md`. Полная перенумерация ID запрещена без прямого согласия автора; если локальных числовых зазоров не хватает, используются точечные числовые суффиксы вроде `100.1`.

Межсессионная очередь агентов хранится в:

```text
masterskaya-pisatelya-PRIVATE/stories/<story-slug>/06-agent-queue/agent-queue.md
```

Новая сессия берет из очереди следующий pending-агент, а не весь прошлый чат.

## Public vs private

Публично коммитится:

- `prompts/`
- `docs/`
- `stories/_template/`
- корневые правила проекта

Не коммитится:

- `masterskaya-pisatelya-PRIVATE/` when the repository is meant to stay public
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
- `docs/stable-paragraph-ids.md`
- `docs/ai-writing-systems-map.md`
- `prompts/00-workflow.md`
- `prompts/00-handoff-template.md`
- `prompts/00-canonical-story-state-template.md`

## Architecture references

- `docs/ai-writing-systems-map.md` — карта типов систем для AI-assisted storytelling с разделением по масштабу: небольшой рассказ, повесть/роман, серия, большая вселенная/franchise-level workflow.

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

<!-- emercons-account-docs:start -->
## Account Documentation / Документация аккаунта

Account-level repository inventory, rules, and agent safety boundaries for `emercons` live in the private [emercons account documentation](https://github.com/emercons/emercons-notes-private/blob/main/infrastructure/this-account-%D1%8D%D1%82%D0%BE%D1%82-%D0%B0%D0%BA%D0%BA%D0%B0%D1%83%D0%BD%D1%82-emercons/README.md).
<!-- emercons-account-docs:end -->
