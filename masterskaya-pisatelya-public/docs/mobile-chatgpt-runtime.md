# Mobile ChatGPT runtime / Работа из обычного ChatGPT

## Supported baseline

The workshop must work from an ordinary ChatGPT conversation, including the mobile app.

Assume the author may have only:

- normal chats;
- the ability to start a new chat;
- GitHub connector access;
- no terminal or virtual machine;
- no local filesystem;
- no background workers;
- no guaranteed real child-agent or parallel-agent runtime.

Any workflow feature that requires more than this baseline is optional enhancement, not a requirement.

## Core execution model

### One chat = one session

A chat may run several compatible roles if:

- the queue permits it;
- the context is not polluted by a conflicting prior role;
- no `fresh_chat_required` boundary is crossed.

### New chat = clean-room role isolation

For adversarial/high-conflict roles, starting a new ChatGPT conversation is the canonical baseline isolation mechanism.

Examples:

```text
работай, критик
работай, идеолог
работай, предсказатель
работай, оригинальность
```

A real child agent may substitute for a fresh manual chat only when the environment actually supports it.

### GitHub = durable memory

A new chat must recover from story files, not from the previous chat transcript.

Minimum recovery set:

1. public `AGENTS.md`;
2. `docs/workflow-manifest.md`;
3. current specialist prompt;
4. private `06-agent-queue/story-status.md` if present;
5. private `06-agent-queue/agent-queue.md`;
6. private `01-canonical/canonical-story-state.md`;
7. latest relevant handoff;
8. relevant draft/review fragment;
9. explicit author decisions referenced by those files.

Do not require the author to paste the whole previous conversation.

## Mobile launch protocol

A short launch should be enough when repository and story are already known from project context:

```text
работай, критик
```

When several stories are active or context is ambiguous, use:

```text
работай, критик
story: <story-slug>
```

If repository identity is not already certain, include:

```text
content repo: emercons/knigi-content-private
workflow repo: emercons/masterskaya-pisatelya
story: <story-slug>
role: критик
```

The agent, not the author, should then resolve exact paths and read the required files.

## No fake capabilities

Do not tell the author that a child agent, VM, background process, or parallel execution is required when the current ChatGPT surface does not expose it.

Do not pretend that merely changing role instructions inside one long chat is equivalent to a clean context when the manifest says `fresh_chat_required`.

## Optional enhanced runtimes

If an environment provides real child agents, coding sandboxes, local git, or parallel execution:

- they may accelerate diagnosis-only work;
- they must preserve the same handoff/queue/status contracts;
- they must not change canonical results merely because a richer runtime exists;
- the resulting story must remain resumable from ordinary mobile ChatGPT afterward.

## User experience target

At any author checkpoint, the author should be able to leave the app and later recover by opening a new chat and naming only the story and next role. The GitHub workspace carries the rest.
