# Мастерская писателя

AI-assisted storytelling repository: мультиагентная мастерская, где одна сырая идея рассказа проходит через последовательность специализированных литературных ролей.

Это публичный репозиторий для инфраструктуры: canonical bilingual prompt-файлы, правила handoff, шаблон story workspace и документация. Сами идеи, handoff-файлы, черновики, ревью и финальные тексты считаются приватными.

## Primary runtime: ordinary ChatGPT

The primary supported runtime is an ordinary ChatGPT conversation, including the mobile app.

- One chat is one working session.
- A new chat is the baseline clean-context mechanism for adversarial/high-conflict roles.
- GitHub files carry durable state between chats.
- A VM, terminal, local clone, background worker, real child agent, or parallel-agent runtime is **not required**.
- Richer runtimes may use child agents/parallel execution as optional acceleration only.

See `docs/mobile-chatgpt-runtime.md`.

## Optional Gas City RIG

Optional maintenance runtime for this public repo only; never required for story work. See `docs/gastown-rig-contract.md` and `docs/gas-city-story-rig-preparation.md`.

## Модель двух репозиториев

`masterskaya-pisatelya` — это публичная мастерская: софт/процесс, agents-as-markdown, prompts, templates, routing rules, handoff rules и документация workflow.

`knigi-content-private` — это приватный контентный репозиторий: идеи, голосовые наброски, raw notes, story workspaces, canonical state, handoffs, drafts, reviews, exports и инвентаризации.

Они работают как пара:

```text
../masterskaya-pisatelya/masterskaya-pisatelya-public/  # public workflow / agents / templates
../knigi-content-private/                               # private story content
```

Если агент входит через GitHub connector и видит только этот репозиторий, он должен понимать: здесь нельзя хранить реальные рассказы. Для реального контента нужно открыть соседний private repo `knigi-content-private`.

## Single source of truth

Canonical role/runtime semantics live in:

```text
docs/workflow-manifest.md
```

README, role map, workflow docs, templates, and prompt references must agree with that manifest.

After role/runtime changes, run `python3 scripts/check_integrity.py` (also runs in CI) and the ChatGPT-runnable semantic validator:

```text
docs/workflow-integrity-check.md
```

## Основной цикл работы

1. Автор на ходу диктует идею в ChatGPT.
2. ChatGPT подключает GitHub и находит два репозитория: `masterskaya-pisatelya` и `knigi-content-private`.
3. Черновик, идея или story workspace сохраняется в `../knigi-content-private/stories/<story-slug>/`.
4. Workflow, prompts, role map, шаблоны и правила берутся из `masterskaya-pisatelya`.
5. Рассказ проходит через нужные роли мастерской; `003` маршрутизирует normal/revision route, а `015` и `135` подключаются условно. Перед прозой `060` собирает `pre-draft-brief.md` (сцены, объём, голос), а `070` сначала согласует с автором голос на пробных абзацах.
6. Все handoffs, drafts, reviews и exports остаются в `knigi-content-private`.
7. `06-agent-queue/story-status.md` дает короткий снимок состояния для автора и нового чата.
8. Если в процессе становится понятно, что сам алгоритм мастерской надо улучшить, проблема обобщается через `docs/framework-retrospective.md`, а правка вносится сюда, в public repo.
9. После этого обновлённая публичная инфраструктура применяется к приватным рассказам по мере их следующего запуска.

## Главный принцип

Каждый нумерованный prompt-файл в `prompts/` описывает отдельного специалиста. Прогон начинается с `003-диспетчер--revision-router--маршрутизатор-правок.md`: в простом новом случае он передает работу в `005`, а после авторского фидбека или при возобновлении сессии выбирает минимальный безопасный маршрут по уже существующим ролям.

Новая история создается не в публичной `stories/`, а в соседнем приватном репозитории:

```text
../knigi-content-private/stories/<story-slug>/
```

Название истории не дублируется в каждом файле. Его роль выполняет `story-slug` в имени родительской папки.

После каждой роли результат сохраняется в:

```text
../knigi-content-private/stories/<story-slug>/02-handoffs/
```

Устойчивые решения переносятся в:

```text
../knigi-content-private/stories/<story-slug>/01-canonical/canonical-story-state.md
```

Полные экспортные драфты сохраняются с номером версии и датой:

```text
../knigi-content-private/stories/<story-slug>/05-exports/full-draft-v<N>-MM-DD.md
```

Экспорты для авторского ревью используют стабильные ID абзацев по `docs/stable-paragraph-ids.md`. Полная перенумерация ID запрещена без прямого согласия автора; если локальных числовых зазоров не хватает, используются точечные числовые суффиксы вроде `100.1`.

Межсессионная очередь агентов и оперативный статус хранятся в:

```text
../knigi-content-private/stories/<story-slug>/06-agent-queue/agent-queue.md
../knigi-content-private/stories/<story-slug>/06-agent-queue/story-status.md
```

Новая сессия берет следующий pending-агент и точные разрешённые inputs из queue/status, а не весь прошлый чат.

## Public vs private

Публично коммитится:

- `prompts/`
- `docs/`
- `stories/_template/`
- `ROADMAP.md`
- корневые правила проекта

Не коммитится сюда:

- story content in `../knigi-content-private/`
- реальные story folders
- raw ideas
- canonical state конкретных историй
- handoffs
- drafts
- reviews
- exports

## Обязательные файлы workflow

- `START.md`
- `prompts/00-role-contract.md`
- `prompts/00-pre-draft-brief-template.md`
- `prompts/00-author-profile-template.md`
- `docs/anti-llm-prose-checklist.md`
- `scripts/check_integrity.py`
- `docs/workflow-manifest.md`
- `docs/workflow-integrity-check.md`
- `docs/gastown-rig-contract.md`
- `docs/gas-city-story-rig-preparation.md`
- `docs/mobile-chatgpt-runtime.md`
- `docs/story-isolation-contract.md`
- `docs/story-inventory-index.md`
- `docs/story-status.md`
- `docs/quality-gates.md`
- `docs/framework-retrospective.md`
- `docs/post-manuscript-frameworks.md`
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

## Canonical story roles

The role inventory, order, aliases, isolation, and checkpoints live only in `docs/workflow-manifest.md` (human-friendly alias map: `docs/role-map.md`). They are not repeated here to avoid drift.

## Role reset and shared rules

Rules common to every role (reset, isolation, preflight, gate verdict, after-role updates) live in `prompts/00-role-contract.md`. A new chat boots from `START.md`.

## Story isolation

Before substantive work, resolve workflow repo, content repo, exact story slug, and exact role. Story-specific reads/writes stay under the resolved private workspace unless the task explicitly requires cross-story analysis.

See `docs/story-isolation-contract.md`.

## Completion and publication boundary

Role `150` ends the literary editing pipeline and may produce a `manuscript_complete` candidate after its author checkpoint and quality gates.

`publication_ready` is route-specific and belongs to future sibling Publishing/Promotion workflows, not generic roles `160+` inside this workshop.

See `docs/post-manuscript-frameworks.md`.

## Infrastructure rule

Use only the numbered bilingual files registered by `docs/workflow-manifest.md` as story-role prompt sources of truth.

<!-- emercons-account-docs:start -->
## Account Documentation / Документация аккаунта

Account-level repository inventory, rules, and agent safety boundaries for `emercons` live in the private [emercons account documentation](https://github.com/emercons/emercons-notes-private/blob/main/infrastructure/this-account-%D1%8D%D1%82%D0%BE%D1%82-%D0%B0%D0%BA%D0%BA%D0%B0%D1%83%D0%BD%D1%82-emercons/README.md).
<!-- emercons-account-docs:end -->
