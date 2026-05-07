# Role map

Canonical specialist prompts use numeric ordering and include a short launch alias in the filename.

| # | Short alias | Prompt file | Purpose | Fresh session |
| --- | --- | --- | --- | --- |
| 003 | `диспетчер` | `prompts/003-диспетчер--revision-router--маршрутизатор-правок.md` | Route new starts, resumes, and author feedback into the correct specialist queue. | no |
| 005 | `приёмщик` | `prompts/005-приёмщик--idea-receiver--приёмщик-идеи.md` | Receive raw idea, identify missing inputs, and ask numbered clarification questions. | no |
| 010 | `архитектор` | `prompts/010-архитектор--idea-architect--архитектор-идеи.md` | Extract core premise, reader-facing story, second semantic layer, emotional conflict. | no |
| 020 | `критик` | `prompts/020-критик--brutal-critic--жестокий-критик.md` | Attack concept risks: cliche, overload, reader exclusion, false depth. | required |
| 030 | `сюжетник` | `prompts/030-сюжетник--story-engineer--инженер-сюжета.md` | Build causal structure, scene sequence, escalation, ending direction. | no |
| 040 | `психолог` | `prompts/040-психолог--character-psychologist--психолог-персонажей.md` | Define character desire, fear, shame, shared past, pressure. | no |
| 050 | `мировик` | `prompts/050-мировик--worldlogic-auditor--аудитор-логики-мира.md` | Check institutions, incentives, interface logic, compliance plausibility. | recommended |
| 060 | `тематик` | `prompts/060-тематик--thematic-analyst--тематический-аналитик.md` | Clarify theme, motifs, contradictions, action-based meaning. | no |
| 070 | `черновик` | `prompts/070-черновик--draft-writer--писатель-черновика.md` | Write first coherent literary draft from canonical state and handoffs. | no |
| 080 | `структурщик` | `prompts/080-структурщик--structural-editor--структурный-редактор.md` | Revise structure, pacing, scene function, escalation, ending pressure. | no |
| 090 | `стилист` | `prompts/090-стилист--style-editor--стилевой-редактор.md` | Edit voice, tone, rhythm, image system, anti-generic prose texture. | recommended |
| 100 | `читатель` | `prompts/100-читатель--reader-simulator--симулятор-читателя.md` | Simulate ordinary and technical reader response without rewriting. | recommended |
| 110 | `финалист` | `prompts/110-финалист--ending-analyst--аналитик-концовки.md` | Stress-test payoff, ambiguity, final image, and emotional residue. | recommended |
| 120 | `идеолог` | `prompts/120-идеолог--ideology-stress-tester--идеологический-стресс-тестер.md` | Test implied ideology, blind spots, simplifications, and accidental propaganda. | required |
| 130 | `предсказатель` | `prompts/130-предсказатель--predictability-analyst--аналитик-предсказуемости.md` | Check predictability, expected beats, and productive disruption options. | required |
| 140 | `сверщик` | `prompts/140-сверщик--continuity-auditor--аудитор-непрерывности.md` | Audit factual, emotional, timeline, terminology, and world-rule continuity. | recommended |
| 150 | `финред` | `prompts/150-финред--final-editor--финальный-редактор.md` | Apply a restrained final edit after reader notes and advanced reviews. | no |

## Workflow prompts

- `prompts/00-workflow.md`
- `prompts/00-handoff-template.md`
- `prompts/00-canonical-story-state-template.md`
- `docs/feedback-and-session-boundaries.md`
- `docs/pipeline-optimization.md`
- `docs/agent-queue.md`

## Legacy policy

Use only the canonical numbered prompt files listed above. Short aliases are part of those filenames.
