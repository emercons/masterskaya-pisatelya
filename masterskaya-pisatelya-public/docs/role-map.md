# Role map

Canonical specialist prompts use numeric ordering and include a short launch alias in the filename.

`docs/workflow-manifest.md` is authoritative for role inventory and runtime semantics. This file is the human-friendly alias map.

| # | Short alias | Prompt file | Purpose | Chat isolation | Mode |
| --- | --- | --- | --- | --- | --- |
| 003 | `диспетчер` | `prompts/003-диспетчер--revision-router--маршрутизатор-правок.md` | Route new starts, resumes, and author feedback into the correct specialist queue. | same chat | routing |
| 005 | `приёмщик` | `prompts/005-приёмщик--idea-receiver--приёмщик-идеи.md` | Receive raw idea, identify missing inputs, and ask numbered clarification questions. | same chat | intake/diagnosis |
| 010 | `архитектор` | `prompts/010-архитектор--idea-architect--архитектор-идеи.md` | Extract core premise, reader-facing story, second semantic layer, emotional conflict. | same chat | design |
| 015 | `тестер` | `prompts/015-тестер--criterion-stress-tester--тестер-критериев.md` | Adversarially compare premise-defining criteria/rules against a stable attack corpus. | fresh chat recommended | diagnosis |
| 020 | `критик` | `prompts/020-критик--brutal-critic--жестокий-критик.md` | Attack concept failure modes before they become expensive. | fresh chat required | opposition/diagnosis |
| 030 | `сюжетник` | `prompts/030-сюжетник--story-engineer--инженер-сюжета.md` | Build causal structure, scene sequence, escalation, ending direction. | same chat | design |
| 040 | `психолог` | `prompts/040-психолог--character-psychologist--психолог-персонажей.md` | Define character desire, fear, shame, shared past, pressure. | same chat | design/diagnosis |
| 050 | `мировик` | `prompts/050-мировик--worldlogic-auditor--аудитор-логики-мира.md` | Check institutions, incentives, interface logic, compliance plausibility. | fresh chat recommended | audit |
| 060 | `тематик` | `prompts/060-тематик--thematic-analyst--тематический-аналитик.md` | Clarify theme, motifs, contradictions, action-based meaning. | same chat | diagnosis |
| 070 | `черновик` | `prompts/070-черновик--draft-writer--писатель-черновика.md` | Write first coherent literary draft from canonical state and handoffs. | same chat | sequential prose |
| 080 | `структурщик` | `prompts/080-структурщик--structural-editor--структурный-редактор.md` | Revise structure, pacing, scene function, escalation, ending pressure. | same chat | sequential prose |
| 090 | `стилист` | `prompts/090-стилист--style-editor--стилевой-редактор.md` | Edit voice, tone, rhythm, image system, anti-generic prose texture. | fresh chat recommended | sequential prose |
| 100 | `читатель` | `prompts/100-читатель--reader-simulator--симулятор-читателя.md` | Simulate ordinary and technical reader response without rewriting. | fresh chat recommended | diagnosis |
| 110 | `финалист` | `prompts/110-финалист--ending-analyst--аналитик-концовки.md` | Stress-test payoff, ambiguity, final image, and emotional residue. | fresh chat recommended | diagnosis |
| 120 | `идеолог` | `prompts/120-идеолог--ideology-stress-tester--идеологический-стресс-тестер.md` | Test implied ideology, blind spots, simplifications, accidental propaganda. | fresh chat required | opposition/diagnosis |
| 130 | `предсказатель` | `prompts/130-предсказатель--predictability-analyst--аналитик-предсказуемости.md` | Check predictability, expected beats, and productive disruption options. | fresh chat required | opposition/diagnosis |
| 135 | `оригинальность` | `prompts/135-оригинальность--similarity-ip-auditor--аудитор-сходства-и-ip.md` | Compare against relevant external works for originality/plagiarism-perception/IP-risk signals. | fresh chat required | diagnosis/web |
| 140 | `сверщик` | `prompts/140-сверщик--continuity-auditor--аудитор-непрерывности.md` | Audit factual, emotional, timeline, terminology, and world-rule continuity. | fresh chat recommended | audit/diagnosis |
| 150 | `финред` | `prompts/150-финред--final-editor--финальный-редактор.md` | Apply restrained final literary edit after reviews. | same chat | sequential prose |

## Mobile execution rule

`fresh chat required` means a new normal ChatGPT conversation is the canonical baseline. The author does not need child-agent tooling.

In environments that support real child agents, one may optionally substitute for a fresh manual chat. Parallel diagnosis is also optional only.

See `docs/mobile-chatgpt-runtime.md`.

## Quality gates

Roles `015`, `020`, `050`, `100`, `135`, and `140` have explicit minimum completion gates in `docs/quality-gates.md`.

## Workflow references

- `docs/workflow-manifest.md`
- `prompts/00-workflow.md`
- `prompts/00-handoff-template.md`
- `prompts/00-canonical-story-state-template.md`
- `docs/feedback-and-session-boundaries.md`
- `docs/pipeline-optimization.md`
- `docs/agent-queue.md`
- `docs/story-status.md`
- `docs/story-isolation-contract.md`
- `docs/quality-gates.md`

## Legacy policy

Use only canonical numbered bilingual prompt files registered in the workflow manifest. Short aliases are part of those filenames.
