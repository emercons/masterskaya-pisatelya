# 00 - Pre-draft brief template / Шаблон брифа перед черновиком

The pre-draft brief is the **single input package** for `070`. It is compiled by `060` at the end of the design phase and approved at the `060` author checkpoint, so the draft writer does not depend on whichever handoff happened to be last.

Location (private):

```text
../knigi-content-private/stories/<story-slug>/01-canonical/pre-draft-brief.md
```

Rules:

- It compiles approved decisions from `010`, `015`, `020`, `030`, `040`, `050`, `060`; it does not invent new ones.
- Where it conflicts with `canonical-story-state.md`, canonical state wins and the brief must be regenerated.
- The `Voice contract` section may stay `pending` until `070` voice calibration is approved by the author.
- Keep it compact: roughly 1–2 screens; link to handoffs for detail rather than copying them.

```markdown
# Pre-draft brief

- story_slug:
- compiled_by: 060
- compiled_from: <handoff files and dates>
- approved_by_author: yes/no (date)

## Format

- Target length: <words or characters, range>
- Form: <short story / flash / novelette / ...>
- Target venue or reader, if known:

## Premise in one paragraph

## Reader-facing story vs second layer

## Scene plan

Copied from the `030` scene table after `040`/`050` adjustments.

| scene id | function | what changes | POV / location | approx. length |
| --- | --- | --- | --- | --- |

## Characters (from 040)

- Protagonist: want / fear / self-deception / behavior under pressure
- Key secondary:
- Relationship that carries conflicting loyalty:

## World rules that must be visible on the page (from 015/050)

## Theme, motifs, contradictions (from 060)

- Thematic question:
- Motifs and where they recur:
- What must stay ambiguous:

## Risks the draft must not reintroduce (from 020)

## Forbidden flattening

## Voice contract

- status: pending | approved (date)
- POV and tense:
- Narrative distance:
- Sentence rhythm and paragraph size:
- Dialogue rules:
- Register / vocabulary field:
- Imagery density and source domains:
- Story-specific banned patterns (beyond `docs/anti-llm-prose-checklist.md` and author profile):
- Approved voice sample: <paragraph or link to 070 handoff option ID>
```
