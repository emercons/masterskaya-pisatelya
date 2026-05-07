# Stable paragraph IDs for author review

Use stable paragraph IDs whenever a full story draft is exported or presented for human author review.

## Format

```text
100: First paragraph text.

200: Second paragraph text.

300: Third paragraph text.
```

## Rules

- Number paragraphs, not visual lines.
- Use compact inline IDs: `100: Paragraph text`.
- Do not put the ID on a separate line.
- Do not add leading zeroes.
- Use a base step of 100 for newly numbered drafts: `100`, `200`, `300`, etc.
- Preserve existing paragraph IDs across agent passes whenever possible.
- Do not number empty spacer lines.
- Agent handoffs, reviews, queues, and author feedback may cite these IDs directly.

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

Avoid global renumbering unless the structure has changed so heavily that stable references are no longer useful.

## Export rule

Story-facing exports under `private/stories/<story-slug>/05-exports/` should use these paragraph IDs by default when they are intended for author review.
