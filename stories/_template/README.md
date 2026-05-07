# Story folder template

Copy this folder to `private/stories/<story-slug>/`.

The canonical workflow is defined by:

- `docs/story-project-structure.md`
- `docs/pipeline-optimization.md`
- `docs/agent-queue.md`
- `prompts/00-workflow.md`
- `prompts/00-handoff-template.md`
- `prompts/00-canonical-story-state-template.md`

Do not add legacy `story-bible.md`, `outline.md`, or `draft.md` files at this level. Story state belongs in `01-canonical/`; prose versions belong in `03-drafts/`; role outputs belong in `02-handoffs/`; cross-session execution state belongs in `06-agent-queue/`.

Full-draft exports belong in `05-exports/` and must use versioned names such as `full-draft-v6-05-07.md` (`MM-DD`, so `05-07` means May 7).

This copied folder is expected to be private and ignored by git when placed under `private/stories/`.
