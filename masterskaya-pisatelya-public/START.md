# START — карточка запуска / launch card

Read this first in every new chat. Keep it under 2 KB.

## Repositories

- workflow (public): `emercons/masterskaya-pisatelya`, subtree `masterskaya-pisatelya-public/`
- content (private): `emercons/knigi-content-private`
- story workspace: `knigi-content-private/stories/<story-slug>/`
- author profile: `knigi-content-private/author/author-profile.md`
- story index: `knigi-content-private/inventory/story-index.md` (only when slug is ambiguous)

Never write story content into the public repo.

## Launch line

`работай, <alias>` + `story: <story-slug>` when several stories are active.

Aliases → `docs/workflow-manifest.md` (table: alias, prompt, isolation, checkpoint).

## Read order (stop when you have enough)

1. `docs/workflow-manifest.md` — role row only
2. `prompts/00-role-contract.md`
3. the role prompt `prompts/NNN-…md`
4. `06-agent-queue/story-status.md`
5. queue item in `06-agent-queue/agent-queue.md`
6. `01-canonical/canonical-story-state.md` (+ `pre-draft-brief.md` from `070` on)
7. latest relevant handoff, draft/review fragment

Unclear what to run next → `работай, диспетчер` (`003`).

## Boundaries

- `fresh_chat_required` role and this chat is not its clean launch → stop, give the launch line for a new chat.
- End every role with a gate verdict and update `story-status.md` with `Next launch`.
- Stop at author checkpoints listed in the manifest.

Full rules: `AGENTS.md`. Maintenance of this repo: `docs/workflow-integrity-check.md`.
