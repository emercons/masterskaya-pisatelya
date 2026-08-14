# Agent queue

The agent queue is the durable execution plan for running the storytelling pipeline across multiple ChatGPT sessions.

It lives inside each private story workspace:

```text
../knigi-content-private/stories/<story-slug>/06-agent-queue/agent-queue.md
```

A concise derived status snapshot lives beside it:

```text
../knigi-content-private/stories/<story-slug>/06-agent-queue/story-status.md
```

Do not store real story queue/status state in public folders.

## Purpose

Use the queue when the pipeline runs in pieces, when a new chat should continue without reading the whole old conversation, or when high-conflict roles should be isolated.

The queue is created/updated by `003-диспетчер`.

## Baseline runtime

The queue must be executable from ordinary ChatGPT/mobile.

Canonical execution/isolation values:

- `chat_mode`: `same_chat`, `fresh_chat_recommended`, `fresh_chat_required`;
- `execution_mode`: `manual_chat` as baseline, optionally `child_agent` or `either` only in richer runtimes;
- `parallel_group`: optional and never required for baseline mobile use.

For portability, a queue should never require a real child agent to make progress.

## What a new chat reads

A new session should read only:

- public `AGENTS.md`;
- `docs/workflow-manifest.md`;
- `docs/mobile-chatgpt-runtime.md`;
- current specialist prompt;
- private `story-status.md`;
- private `agent-queue.md`;
- current canonical story state;
- latest relevant handoff;
- relevant draft/review fragment;
- explicit author decisions referenced by those files.

Do not carry the full prior conversation.

## Queue item fields

Each queue item should include:

- `id`: stable item id;
- `role`: canonical prompt filename;
- `status`: `pending`, `in_progress`, `blocked`, `completed`, or `skipped`;
- `session_chunk`: chunk id;
- `chat_mode`: `same_chat`, `fresh_chat_recommended`, or `fresh_chat_required`;
- `execution_mode`: normally `manual_chat`; optionally `child_agent`/`either` only when available;
- `parallel_group`: optional group id for diagnosis-only optional parallelism;
- `reason`;
- `allowed_inputs`: exact files/data the role may read;
- `expected_outputs`;
- `prose_editing`: `yes` or `no`;
- `quality_gate`: relevant gate or `none`;
- `stop_after`: `no`, `author_feedback`, `fresh_chat_boundary`, or another explicit stop.

Legacy queues using `fresh_session` remain readable. Interpret:

- `fresh_session: required` as `chat_mode: fresh_chat_required`;
- `fresh_session: recommended` as `chat_mode: fresh_chat_recommended`;
- `fresh_session: no` as `chat_mode: same_chat`.

Do not bulk-rewrite old private queues solely to rename this field.

## Session chunks

Group compatible roles into chunks. A chunk can run in one chat if pressures do not contaminate each other and the manifest permits it.

Use/recommend fresh chats for:

- `015` when rule testing is large/adversarial;
- `020` after protective idea architecture;
- transition out of `020` before prose-heavy work;
- `090` when structural editing has dominated the context;
- `100` when a clean reader simulation matters;
- `120`, `130`, `135` as intentionally adversarial late reviews;
- `140` when a clean formal audit helps.

## Fresh-chat defaults

Follow `docs/workflow-manifest.md` rather than duplicating a separate stale table here.

When stopping, use:

```text
Stop here. Next role should run in a fresh ChatGPT chat:
<short alias> -> <canonical prompt filename>

New chat should read: story status, agent queue, canonical state, latest relevant handoff, relevant draft/review fragment.
```

## Optional parallel execution

Diagnosis-only review roles may optionally run in parallel child agents when the environment supports it and they:

- read the same stable draft;
- do not edit prose;
- write separate outputs;
- do not depend on one another.

This is an optimization only. On mobile, run them as separate chats sequentially and merge pressures later through the queue/router.

Prose-editing roles remain sequential.

## Completion rule

After each role:

1. Write the role handoff under `02-handoffs/`.
2. Apply `docs/quality-gates.md` when the role has a gate.
3. Update canonical state only for durable decisions.
4. Update draft/review/export files only if allowed.
5. Mark the queue item completed only if its gate permits; otherwise block/reroute/ask the author.
6. Update `story-status.md` with current/next role, block/checkpoint, latest files, and next launch.
7. Stop on `author_feedback` or `fresh_chat_required` boundary.

## Queue vs status vs canon

- queue = execution plan;
- status = concise derived resume snapshot;
- canonical state = durable story facts/decisions;
- handoffs = specialist memory;
- drafts = prose.

If status conflicts with queue/canon, recompute status. Do not change canon to match a stale status file.
