# Карта типов систем для AI-assisted storytelling

Цель документа — отделить компоненты, которые полезны даже для небольшого рассказа, от инфраструктуры, которая нужна только для романа, серии книг или большой narrative universe.

Документ не является каталогом всех инструментов. Это архитектурная карта: какие типы систем существуют, какую проблему они закрывают, на каком масштабе начинают окупаться и какие open-source/расширяемые решения стоит рассматривать.

## Масштаб применимости

| Метка | Масштаб | Практический смысл |
|---|---|---|
| S | Небольшой рассказ | 1 рассказ, 1-10 сцен, немного персонажей, короткий канон |
| M | Повесть / роман | Десятки сцен, несколько арок, нужен контроль таймлайна и персонажей |
| L | Серия / большая вселенная | Много произведений, общий лор, канон, timeline, повторное использование мира |
| XL | Франшиза / сериал / multi-season universe | Несколько линий, сезонов, команд, публикаций, производственных пайплайнов |

## Общая таблица типов систем

| # | Тип системы | Что делает | Минимальный масштаб | Нужна для малого рассказа? | Open-source / расширяемые варианты | Комментарий |
|---:|---|---|---|---|---|---|
| 1 | Drafting system | Помогает писать первичный текст сцены или рассказа | S | Да | Codex, Claude Code, локальные LLM через LM Studio/Ollama | Базовый слой. Без него всё остальное вторично. |
| 2 | Rewrite / editing system | Переписывает, сокращает, усиливает сцену | S | Да | Prompt files + Codex; Vale/write-good как lint-подход | Для рассказа полезнее сложного worldbuilding. |
| 3 | Role prompt registry | Хранит роли: критик, стилист, сюжетник, continuity-аудитор | S | Да | Текущий `prompts/` workflow; AGENTS.md-style правила | Нужен даже в малом рассказе, если используется несколько литературных ролей. |
| 4 | Scene workspace | Держит вход, handoff, canonical state, exports | S | Да | Markdown folders + Git | Уже реализуется в этом repo через `private/stories/<slug>/`. |
| 5 | Simple story bible | Фиксирует базовые факты: тема, персонажи, правила мира | S | Да, но минимально | Markdown, Obsidian, Foam | Для рассказа достаточно 1-3 файлов, не нужна большая wiki. |
| 6 | Character notes | Хранит мотивации, голос, ограничения персонажей | S | Да, минимально | Markdown/YAML character sheets | Нужно, если персонажи не одноразовые. |
| 7 | Style guide | Фиксирует тон, регистр, запреты, желаемый язык | S | Да | Markdown style guide; Vale rules | Особенно полезно при нескольких агентских проходах. |
| 8 | Human feedback boundary system | Разделяет авторский фидбек, агентские гипотезы и canonical state | S | Да | Текущие docs + handoff templates | Важнее, чем кажется: предотвращает загрязнение канона случайными идеями агента. |
| 9 | Scene planner | Разбивает историю на сцены/beats | M | Иногда | Markdown tables, YAML scene metadata | Для короткого рассказа можно делать вручную. |
| 10 | Timeline tracker | Следит за порядком событий и причинностью | M | Обычно нет | Obsidian plugins, StoryLine-like workflows, custom Markdown tables | Нужен, когда события начинают путаться. |
| 11 | Continuity reviewer | Проверяет противоречия в фактах, знаниях, мотивации | M | Иногда | Custom agent prompt; spaCy + custom extraction | Для маленького рассказа достаточно ручного continuity prompt. |
| 12 | Semantic retrieval / RAG | Автоматически подтягивает релевантный контекст из repo | M | Обычно нет | LlamaIndex, LangChain, Haystack | Становится важным, когда контекст не помещается в prompt. |
| 13 | Multi-agent orchestration | Запускает роли в правильном порядке, хранит состояние pipeline | M | Не обязательно | LangGraph, CrewAI, AutoGen | Для текущего repo пока можно начинать с ручного диспетчера. |
| 14 | Agent debate / adversarial review | Агенты спорят: критик, защитник, редактор, читатель | M/L | Нет | AutoGen, LangGraph, custom review loops | Полезно для сложных идей, но легко раздувает процесс. |
| 15 | Narrative QA metrics | Меряет pacing, долю диалогов, экспозицию, эмоциональную кривую | M/L | Нет | Custom NLP scripts; spaCy; textstat-like libs | Для рассказа может быть избыточно. |
| 16 | Worldbuilding wiki | Структурирует места, организации, законы мира, артефакты | L | Нет, кроме sci-fi/fantasy с плотным миром | Obsidian, Foam, Dendron, Quartz | Окупается, если мир используется повторно. |
| 17 | Canon database / knowledge graph | Хранит сущности и связи как граф | L | Нет | Neo4j, RDF/OWL, JSON-LD, custom graph | Не начинать рано: высокие накладные расходы. |
| 18 | Automated continuity validator | Машинно ищет расхождения между draft и canon graph | L | Нет | spaCy + graph DB + custom rules | Готовых решений мало; скорее кастомная разработка. |
| 19 | Cross-story universe memory | Использует лор из нескольких рассказов/книг | L | Нет | LlamaIndex over multi-story repo; vector DB | Нужно только при общей вселенной. |
| 20 | Publishing/export pipeline | Собирает Markdown в HTML/PDF/ePub/site | M/L | Не сначала | Pandoc, mdBook, Hugo, Quartz | Для малого рассказа достаточно Markdown/PDF export. |
| 21 | Public lore site | Публикует wiki мира для читателей | L/XL | Нет | Quartz, Hugo, mdBook | Имеет смысл, когда есть аудитория и большой мир. |
| 22 | Marketing asset generator | Делает аннотации, посты, тизеры, quote cards | L/XL | Нет | Static templates + LLM prompts | Поздний слой, после появления текста. |
| 23 | Editorial PR workflow | Использует branches/PR/issues для ревью художественного текста | M/L | Иногда | GitHub PRs, issue templates | Хорошо для команды агентов, но может быть overhead для одного рассказа. |
| 24 | Franchise production system | Управляет сезонами, линиями, релизами, bible, редакторами | XL | Нет | Custom repo + project management + graph/retrieval | Не нужно до реальной серии/франшизы. |

## Минимальный набор для небольшого рассказа

| Компонент | Форма в repo | Зачем нужен |
|---|---|---|
| Идея / raw input | `00-input/` или handoff | Не потерять исходный импульс автора |
| Canonical story state | `01-canonical/canonical-story-state.md` | Хранить только устойчивые решения |
| Handoffs | `02-handoffs/` | Передавать состояние между ролями |
| Drafts | `03-drafts/` или `05-exports/` | Не смешивать черновики и финальные версии |
| Prompt roles | `prompts/NNN-*.md` | Стабильные роли вместо случайного чата |
| Style/editor pass | `090`, `150` roles | Доводка языка |
| Continuity pass | `140` role | Проверка базовых противоречий |

### Для small story НЕ нужно начинать с этого

| Не начинать с | Почему |
|---|---|
| Neo4j / graph DB | Слишком тяжело для одного рассказа |
| Полноценный RAG | Не окупается, пока контекста мало |
| Автоматические метрики pacing | Раньше текста это имитация контроля |
| Debate swarms | Создают шум и много лишнего текста |
| Public lore site | Мир ещё не стабилизирован |
| Marketing pipeline | Продвижение рано, пока нет сильного текста |

## Рекомендуемая эволюция по масштабу

| Этап | Когда переходить | Что добавить |
|---|---|---|
| S1: один рассказ | Всегда | Markdown workspace, prompt roles, handoffs, canonical state |
| S2: несколько редакторских проходов | Когда появился полный draft | continuity pass, style pass, reader simulator |
| M1: длинный рассказ/повесть | Когда сцен больше 10-15 | scene metadata, simple timeline table, character sheets |
| M2: роман | Когда контекст перестал помещаться в prompt | retrieval/RAG over repo, richer scene index |
| L1: общий мир | Когда несколько текстов используют один мир | worldbuilding wiki, shared lore, cross-story canon |
| L2: серия | Когда появляется много арок и повторяющихся персонажей | timeline tracker, continuity validator, relationship graph |
| XL: франшиза | Когда есть публикация/команда/сезоны | production workflow, publishing pipeline, marketing assets, public lore site |

## Практичный вывод для текущего repo

Для `mastesrkaya-pisatelya` ближайшая полезная зона — не большая вселенная, а надежный small-to-medium workflow:

| Приоритет | Что усилить | Почему |
|---|---|---|
| 1 | Canonical state discipline | Это главный антихаос-слой |
| 2 | Scene metadata template | Позволит позже подключить retrieval и analytics |
| 3 | Continuity auditor prompt | Дешево и полезно уже сейчас |
| 4 | Reader simulator + brutal critic | Даёт качество без тяжелой инфраструктуры |
| 5 | Optional Obsidian/Foam compatibility | Можно получить wiki без переписывания repo |

## Возможные open-source базы по слоям

| Слой | База | Роль |
|---|---|---|
| Markdown wiki | Foam | Git-native wiki поверх VS Code |
| Personal knowledge base | Obsidian | Не open-source core, но хорошо работает с Markdown repo |
| Hierarchical notes | Dendron | Структурная база знаний, если Foam/Obsidian мало |
| Retrieval | LlamaIndex | Индексирование lore/drafts/handoffs |
| Agent orchestration | LangGraph | Управление состоянием и порядком агентов |
| Multi-agent roles | CrewAI / AutoGen | Ролевые агенты и review/debate loops |
| NLP extraction | spaCy | Извлечение персонажей, мест, событий |
| Graph storage | Neo4j | Только для L/XL канона |
| Static publishing | Quartz / Hugo / mdBook | Публикация wiki/текстов |
| Export | Pandoc | Markdown to PDF/ePub/HTML |

## Главное ограничение

Не стоит пытаться сразу построить `narrative operating system` для франшизы. Для малых рассказов наибольшую отдачу дают:

1. четкая структура файлов;
2. стабильные роли агентов;
3. canonical state;
4. handoff discipline;
5. 2-3 обязательных reviewer passes.

Остальные системы стоит подключать только по мере роста размера текста и количества взаимосвязанных историй.
