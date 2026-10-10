# 00 - Author profile template / Шаблон профиля автора

The author profile stores **cross-story** preferences that otherwise get lost between stories: recurring feedback, voice habits, phrases the author rejects, things never to flatten.

Location (private):

```text
../knigi-content-private/author/author-profile.md
```

Rules:

- It is not story canon. A story's canonical state and voice contract override it for that story.
- Agents may **propose** additions in a handoff; only the author confirms them. Do not record one-off reactions as permanent preferences.
- Keep entries short and dated so stale preferences can be retired.
- Reading it is allowed from any story workspace (see `docs/story-isolation-contract.md`); it must not contain story-specific plot/canon.

```markdown
# Author profile

## Languages and audience

- Writing language(s):
- Default target reader:

## Voice defaults

- Narrative distance / POV preferences:
- Rhythm / sentence habits the author likes:
- Dialogue preferences:

## Never flatten

- <element the author repeatedly protects, e.g. strangeness, unresolved discomfort>

## Rejected phrasing and patterns

Additions to `docs/anti-llm-prose-checklist.md` specific to this author.

| pattern / phrase | why | added |
| --- | --- | --- |

## Recurring feedback

| feedback | stories where it recurred (slugs) | resulting rule | added |
| --- | --- | --- | --- |

## Workflow preferences

- Default route profile / checkpoints the author usually skips or insists on:
- Preferred report language:

## Retired preferences

-
```
