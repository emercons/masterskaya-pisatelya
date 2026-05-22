# Stable paragraph IDs for author review

Use stable paragraph IDs whenever a full story draft is exported or presented for human author review.

## Format

```text
100: First paragraph text.

200: Second paragraph text.

300: Third paragraph text.
```

When numeric gaps are exhausted, dot-number suffixes may be used:

```text
100: Existing paragraph.

100.1: Inserted paragraph.

100.2: Another inserted paragraph.

200: Next existing paragraph.
```

## Rules

- Number paragraphs, not visual lines.
- Number story prose paragraphs, including dialogue paragraphs.
- Do not number empty spacer lines, headings, scene separators, metadata, handoff/review section labels, or other service text.
- Use compact inline IDs: `100: Paragraph text` or `100.1: Paragraph text`.
- Do not put the ID on a separate line.
- Do not add leading zeroes, including in dot-number suffixes: use `122.1`, not `122.01`.
- Use a base step of 100 for newly numbered drafts: `100`, `200`, `300`, etc.
- Preserve existing paragraph IDs across agent passes whenever possible.
- Agent handoffs, reviews, queues, and author feedback may cite these IDs directly.

## Stability principle

A paragraph ID is an editorial address for a semantic paragraph, not its current position in the file.

- When a paragraph is edited, keep its ID.
- When a paragraph moves, keep its ID.
- When a paragraph is deleted, retire its ID. Do not reuse deleted IDs for new text.
- When paragraphs are merged, keep the ID of the paragraph that remains the semantic core, usually the first paragraph, and retire the absorbed ID.
- When a paragraph is split, keep the original ID on the most continuous fragment and assign new IDs to the new fragments.

## Insertions

When inserting new paragraphs between existing IDs, split the available interval evenly.

One new paragraph between `100` and `200`:

```text
100: Existing paragraph.

150: Inserted paragraph.

200: Existing paragraph.
```

Three new paragraphs between `100` and `200`:

```text
100: Existing paragraph.

125: Inserted paragraph A.

150: Inserted paragraph B.

175: Inserted paragraph C.

200: Existing paragraph.
```

If there is no useful numeric gap left, or if local renumbering would otherwise be tempting, add dot-number suffixes to the nearest stable numeric anchor. If suffixes already exist, continue with the next integer suffix.

```text
100: Existing paragraph.

100.1: Inserted paragraph A.

100.2: Inserted paragraph B.

101: Existing paragraph with a tight neighboring ID.
```

Treat dot-number IDs as textual editorial addresses, not decimal numbers. For example, `122.10` follows `122.9`; do not rewrite it as `122.91` or renumber the surrounding draft.

## Global renumbering

Never do a full or global renumbering, ID refresh, or broad ID reorder without explicit author consent.

If global renumbering seems necessary, stop and ask the author first. Until the author explicitly approves it, preserve existing IDs and use local numeric gaps or dot-number suffixes.

If the author explicitly approves a global renumbering, record the affected draft version and the fact of renumbering in the handoff so older author comments remain interpretable.

## Export rule

Story-facing exports under `masterskaya-pisatelya-PRIVATE/stories/<story-slug>/05-exports/` should use these paragraph IDs by default when they are intended for author review.

Clean publication/reader-facing copies without paragraph IDs must be separate files and must not replace the review export.
