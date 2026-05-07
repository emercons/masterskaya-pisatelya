# 00 - Workflow / Рабочий процесс

This repository is a sequential multi-agent storytelling workshop.

Это последовательная мультиагентная мастерская для рассказа.

## Non-negotiable operating rule

Before applying every specialist prompt:

```text
You are ONLY the currently assigned specialist.
Forget previous specialist roles.
Do not continue previous analytical styles.
Do not behave as a general assistant.
Your scope is intentionally narrow.
```

## Inputs allowed for each role

Use only:

- current specialist prompt;
- current canonical story state;
- latest relevant handoff;
- relevant draft fragment.

Do not drag the full old context forward.

## Role order

1. `005-idea-receiver--приёмщик-идеи.md`
2. `010-idea-architect--архитектор-идеи.md`
3. `020-brutal-critic--жестокий-критик.md`
4. `030-story-engineer--инженер-сюжета.md`
5. `040-character-psychologist--психолог-персонажей.md`
6. `050-worldlogic-auditor--аудитор-логики-мира.md`
7. `060-thematic-analyst--тематический-аналитик.md`
8. `070-draft-writer--писатель-черновика.md`
9. `080-structural-editor--структурный-редактор.md`
10. `090-style-editor--стилевой-редактор.md`
11. `100-reader-simulator--симулятор-читателя.md`
12. `110-ending-analyst--аналитик-концовки.md`
13. `120-ideology-stress-tester--идеологический-стресс-тестер.md`
14. `130-predictability-analyst--аналитик-предсказуемости.md`
15. `140-continuity-auditor--аудитор-непрерывности.md`
16. `150-final-editor--финальный-редактор.md`

## Author feedback checkpoints

Ask for human author feedback after roles `005`, `020`, `060`, `100`, `140`, and `150` unless the author has explicitly asked to continue through that checkpoint.

Use `docs/feedback-and-session-boundaries.md` as the source of truth for feedback checkpoints and high-conflict role transitions.

## Session boundaries

Some roles deliberately contradict each other. Before crossing a high-conflict transition in a long context window, stop and ask the author to compact the window or start a fresh session.

Carry forward only:

- current canonical story state;
- latest relevant handoff;
- relevant draft fragment;
- explicit author decisions.

## After each role

1. Save the output to the story-specific handoff file under `private/stories/<story-slug>/02-handoffs/`.
2. Update canonical story state if durable decisions changed.
3. Update draft files if prose changed.
4. Compress the role result into a short handoff summary.
5. Reset role identity before the next role.

## Privacy

Concrete story workspaces are private by default and must live under:

```text
private/stories/<story-slug>/
```

Do not save raw ideas, handoffs, drafts, reviews, or final story exports into public tracked folders.

## Do not

- Mix roles.
- Do a general literary analysis when a specific role is active.
- Rewrite prose unless the current role requires it.
- Convert strange or conflicted elements into generic polished prose.
- Treat AI-industry jargon as the whole story; it is the second semantic layer.

## Priority

Only numbered bilingual prompt filenames are authoritative.
