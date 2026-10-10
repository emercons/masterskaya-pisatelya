# Anti-LLM prose checklist / Чек-лист против «нейросетевой» прозы

Used by `070` (self-check before handing off), `090` (primary owner), `100` (reader-side detection), and `150` (final sweep).

The checklist describes **patterns**, not banned words. A pattern is a defect only when it is generic in this story's context; a deliberate stylistic choice recorded in the voice contract wins. Author-specific additions live in `../knigi-content-private/author/author-profile.md` and take precedence over this list.

## How to use

- `070`: run a quick pass on the finished draft; list remaining hits under `Known weaknesses`.
- `090`: run the full pass; report counts per pattern before/after and cite paragraph IDs for remaining deliberate exceptions.
- `100`: report where the reader would sense "machine-written" texture.
- `150`: sweep only for regressions introduced by later edits.

## Structural tics

1. **Triads by reflex** — lists of three adjectives/clauses/images where one precise item would do.
2. **«Не X, а Y» / "not X, but Y"** — corrective antithesis used as a default rhetorical engine.
3. **Paragraph-final summary** — a closing sentence that explains what the paragraph already showed.
4. **Scene-final moral** — a scene or the story ends by naming its meaning, lesson, or emotion.
5. **Uniform rhythm** — consecutive sentences of similar length and shape; every paragraph the same size.
6. **Symmetric dialogue** — characters answer in full, grammatical, equally articulate replies; nobody interrupts, evades, or misunderstands.

## Emotion and interiority

7. **Named emotion** — «она почувствовала тревогу», "a wave of sadness" instead of behavior, body, or action.
8. **Explained subtext** — narration clarifies what dialogue or gesture already implied.
9. **Instant self-insight** — characters articulate their own psychology with therapeutic precision.

## Imagery and diction

10. **Stock imagery** — «время словно остановилось», "silence hung in the air", «сердце пропустило удар», "a testament to".
11. **Simile density** — more than one simile/metaphor per short paragraph without a reason in the voice contract.
12. **Abstract-noun stacking** — «ощущение неизбежности перемен», "a sense of quiet resilience".
13. **Hedged intensifiers** — «словно бы», «какой-то», «почти», "somehow", "seemed to" used as filler.
14. **Register drift** — bookish/official words in the mouth or head of a character who would not use them.
15. **Translationese** (Russian text) — English syntax calques, overuse of possessive pronouns («он поднял свою руку»), passive constructions where Russian prefers active/impersonal forms.

## Story-level genericness

16. **Default setting detail** — weather, coffee, rain on glass, neon, flickering lights used as atmosphere without story function.
17. **Convenient exposition** — characters tell each other what both already know.
18. **Safe ending** — ambiguity resolved into reassurance, or a twist added only to surprise.
19. **Thesis characters** — a character exists to state one side of the theme.

## Reporting format

```markdown
## Anti-LLM pass

| # | pattern | hits before | hits after | kept deliberately (paragraph IDs) |
| --- | --- | --- | --- | --- |
```
