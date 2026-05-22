# Agent queue

## Story slug

`<story-slug>`

## Current route

Pending.

## Queue

| id | role | status | session_chunk | fresh_session | execution_mode | parallel_group | allowed_inputs | expected_outputs | prose_editing | stop_after |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Notes

- Created/updated by `003-диспетчер--revision-router--маршрутизатор-правок.md`.
- Use this file to continue the pipeline across sessions without carrying the full previous chat.
- Use `execution_mode: child_agent` for oppositional roles and large/crowded-context roles.
- Use `parallel_group` only for diagnosis-only roles that may run at the same time.
- Keep prose-editing roles sequential.
- Keep concrete story content private.
