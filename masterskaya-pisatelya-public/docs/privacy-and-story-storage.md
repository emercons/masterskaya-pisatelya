# Privacy and story storage

This repository is public. The storytelling infrastructure is public; story content is private.

## Public

Safe to commit:

- `README.md`
- `AGENTS.md`
- `docs/`
- `prompts/`
- `stories/_template/`

## Private

Never commit:

- raw story ideas;
- author notes for a concrete story;
- canonical story state for a concrete story;
- handoffs;
- drafts;
- reviews;
- final exports.

All concrete story workspaces must live under:

```text
../knigi-content-private/stories/<story-slug>/
```

`../knigi-content-private/` is the sibling private repository for real story content. Story content may be tracked there, but should not be committed to this public infrastructure repository.

When a task asks for the latest draft, author feedback, handoff, review, or export, inspect `../knigi-content-private/stories/` explicitly. Do not assume `rg --files` over the public subtree is enough.

## Safety net

The root `.gitignore` also ignores accidental public story instances:

```text
stories/*
!stories/README.md
!stories/_template/
!stories/_template/**
```

This keeps the public template available while preventing `stories/<story-slug>/` from being committed accidentally.

## Next story flow

When the author gives a new story idea:

1. Choose a short slug, for example `nochnoy-kontrakt`.
2. Copy `stories/_template/` to `../knigi-content-private/stories/<story-slug>/`.
3. Save the raw idea to `00-input/raw-idea-from-chat.md`.
4. Run roles in numeric order.
5. Save outputs only inside that private story folder.

## Naming rule

Do not add the story title to every filename. The parent folder slug identifies the story; workflow files keep stable names across all stories.
