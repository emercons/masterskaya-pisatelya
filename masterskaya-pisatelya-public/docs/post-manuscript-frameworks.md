# Post-manuscript frameworks / Что происходит после текста

The Writer's Workshop ends at a literary manuscript checkpoint. Publishing and promotion are separate operational domains and should not be appended as generic roles `160+` to the writing pipeline.

## State boundary

### `manuscript_complete`

Means:

- the literary workflow through `150` has completed;
- blocking literary quality-gate failures are resolved or explicitly accepted;
- a clean manuscript/export exists;
- the author has reached/cleared the final literary checkpoint.

It does **not** mean the work is ready for a specific magazine, publisher, self-publishing platform, language market, contest, or promotional campaign.

### `publication_ready`

Must be defined relative to a concrete publication route, for example:

- ready for submission to a named literary magazine;
- ready for a contest with specific rules;
- ready for agent/publisher query package;
- ready for self-publication in a specific store/format;
- ready for an English/German translation market;
- ready for a public web release.

Publication readiness may require rights checks, formatting, metadata, synopsis/cover letter/bio, translation, policy compliance, and route-specific packaging that do not belong to literary editing.

## Future sibling framework A — Publishing Workshop / Издательская мастерская

Expected responsibilities:

- market/route selection;
- first-publication and exclusivity strategy;
- submission eligibility and policy verification;
- AI-assistance disclosure/policy checks where relevant;
- translation-market strategy;
- synopsis, cover letter, author bio, submission package;
- formatting/export variants;
- submission tracking;
- rights/status tracking;
- rejection/resubmission ladder;
- handoff to self-publication when appropriate.

This framework should use current web research because markets and policies change.

## Future sibling framework B — Promotion Workshop / Мастерская продвижения

Expected responsibilities:

- audience/positioning hypotheses;
- catalog strategy across multiple stories;
- author platform and owned channels;
- launch/release plan;
- community/outreach strategy;
- excerpts/teasers without accidentally destroying submission rights;
- reviewer/book-blog/community outreach where relevant;
- measurement and experiments;
- reuse of stories after rights windows expire;
- coordination across Russian, English, German, or other editions.

This framework should not rewrite the story merely to satisfy marketing heuristics unless the author explicitly routes a literary change back into the Writer's Workshop.

## Research before implementation

Do not implement detailed publishing/promotion role prompts from memory alone.

A dedicated current-market research pass should cover at least:

- short-fiction magazines and anthologies by language/genre;
- contests and open calls;
- simultaneous-submission rules;
- first-publication/reprint rights;
- exclusivity periods;
- AI-generated / AI-assisted submission policies;
- translation rights and prior-publication effects;
- self-publishing platforms and discovery channels;
- mailing-list/author-site/social/community strategies;
- practical submission trackers and metadata needs;
- which channels produce reputation, revenue, audience, or reusable rights.

## Handoff contract

Writer's Workshop output to Publishing Workshop should be a clean package reference, not a new literary role:

```text
story_slug
manuscript_version
clean_export_path
language
word_count
rights_history
prior_publication_status
135/IP-audit status if applicable
author-approved logline/short description if available
```

The publishing workflow then owns route-specific readiness.

## Separation rule

If publishing feedback requires changing plot, character, prose, ending, theme, world logic, or originality distance, route the request back through `003` in the Writer's Workshop. Publishing agents must not silently become literary editors.
