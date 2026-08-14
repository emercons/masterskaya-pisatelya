# Agent queue

## Story slug

`<story-slug>`

## Current route

Pending.

## Queue

| id | role | status | session_chunk | chat_mode | execution_mode | parallel_group | allowed_inputs | expected_outputs | prose_editing | quality_gate | stop_after |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Notes

- Created/updated by `003-диспетчер--revision-router--маршрутизатор-правок.md`.
- Baseline execution is `manual_chat`; the workflow must remain runnable from ordinary mobile ChatGPT.
- Use `chat_mode` values from `docs/workflow-manifest.md`: `same_chat`, `fresh_chat_recommended`, `fresh_chat_required`.
- `child_agent` and `parallel_group` are optional enhancements only when supported; never make them required for progress.
- Use `quality_gate` for roles covered by `docs/quality-gates.md`.
- Keep prose-editing roles sequential.
- Update `story-status.md` whenever current/next role, checkpoint, latest draft/review, or fresh-chat requirement changes.
- Keep concrete story content private.
