# Story folder template

Copy this folder to `../knigi-content-private/stories/<story-slug>/`.

The canonical workflow is defined by:

- `docs/workflow-manifest.md`
- `docs/mobile-chatgpt-runtime.md`
- `docs/story-isolation-contract.md`
- `docs/story-status.md`
- `docs/quality-gates.md`
- `docs/story-project-structure.md`
- `docs/pipeline-optimization.md`
- `docs/agent-queue.md`
- `docs/stable-paragraph-ids.md`
- `prompts/00-workflow.md`
- `prompts/00-handoff-template.md`
- `prompts/00-canonical-story-state-template.md`

Do not add legacy `story-bible.md`, `outline.md`, or flat `draft.md` files at this level.

Story state belongs in `01-canonical/`; prose versions in `03-drafts/`; role outputs in `02-handoffs/`; reviews in `04-reviews/`; exports in `05-exports/`; cross-chat execution state in `06-agent-queue/`.

`06-agent-queue/story-status.md` is the short resume snapshot for the author/new mobile ChatGPT chat. `agent-queue.md` remains the durable route.

Conditional roles `015` and `135` have template placeholders but need not produce real story outputs unless invoked.

Full-draft exports use versioned names such as `full-draft-v6-05-07.md`. Author-review exports use stable paragraph IDs from `docs/stable-paragraph-ids.md`; global renumbering requires explicit author consent.

This copied folder is private story material when placed under `../knigi-content-private/stories/`.

A new ChatGPT chat should be able to resume from story status + queue + canonical state + focused handoff/draft inputs without the previous transcript.
