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

1. `010-idea-architect--архитектор-идеи.md`
2. `020-brutal-critic--жестокий-критик.md`
3. `030-story-engineer--инженер-сюжета.md`
4. `040-character-psychologist--психолог-персонажей.md`
5. `050-worldlogic-auditor--аудитор-логики-мира.md`
6. `060-thematic-analyst--тематический-аналитик.md`
7. `070-draft-writer--писатель-черновика.md`
8. `080-structural-editor--структурный-редактор.md`
9. `090-style-editor--стилевой-редактор.md`
10. `100-reader-simulator--симулятор-читателя.md`
11. `110-ending-analyst--аналитик-концовки.md`
12. `120-ideology-stress-tester--идеологический-стресс-тестер.md`
13. `130-predictability-analyst--аналитик-предсказуемости.md`
14. `140-continuity-auditor--аудитор-непрерывности.md`

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
