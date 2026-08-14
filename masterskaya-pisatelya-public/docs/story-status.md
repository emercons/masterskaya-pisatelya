# Story status / Оперативный статус рассказа

Each active story should maintain:

```text
../knigi-content-private/stories/<story-slug>/06-agent-queue/story-status.md
```

This is a concise derived snapshot for humans and new ChatGPT sessions. It does not replace canonical state, handoffs, or the agent queue.

## Required fields

```markdown
# Story status

- story_slug: `<story-slug>`
- workflow_version_hint: `<date/commit if useful>`
- current_phase: `<intake|concept|plot|characters|world|theme|draft|editing|review|final|manuscript_complete>`
- last_completed_role: `<id/alias or none>`
- current_role: `<id/alias or none>`
- next_role: `<id/alias or none>`
- status: `<active|blocked_author|blocked_upstream|checkpoint|manuscript_complete>`
- author_action_required: `<none or concise action>`
- fresh_chat_required_next: `<yes|no>`
- latest_canonical: `01-canonical/canonical-story-state.md`
- latest_handoff: `<path or none>`
- latest_draft: `<path or none>`
- latest_review: `<path or none>`
- queue: `06-agent-queue/agent-queue.md`
- publication_state: `<not_applicable|not_ready|manuscript_complete|handed_to_publishing_workflow>`

## Current blocking issue

<1-4 sentences>

## Next launch

`<short command the author can paste into a new ChatGPT chat>`

## Notes

<only operational notes needed to resume>
```

## Update responsibility

`003` owns status creation/update when routing.

Any specialist that completes a queue item should update status if it changes:

- last/current/next role;
- checkpoint/block state;
- latest draft/review/export;
- fresh-chat requirement;
- manuscript completion state.

Do not duplicate long canonical facts here.

## Recovery rule

A new ChatGPT chat should read this file first after the public runtime/manifest docs. It should then open only the queue and exact inputs named here or by the pending queue item.

## Staleness rule

If status contradicts the queue or canonical state, treat status as stale derived data. Recompute/update it; do not overwrite canon to match status.
