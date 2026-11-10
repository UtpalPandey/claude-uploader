---
name: visual-identity
description: "Visual Identity — Utpal's library of visual styles for videos (built on the open Lemo-Opuscar library of 66+ film styles: painting, printmaking, anime, games, cinema eras, 3D materials, evidence and documentary styles, each with a style prompt, palette, shot directions and a demo frame). Use this skill whenever Utpal wants to see, browse, compare or pick visual styles or looks for a video, asks for a style board or style options, says \"visual identity\", \"styles dikhao\", \"kaunsa look\", or when the edit-workflow skill reaches its style step (Phase 3a). Also use it to turn his own style references into a saved style."
---

# Visual Identity

Utpal's style library. It lets him choose a video's look by **seeing** styles, not reading their names. Under the hood it uses the open-source Lemo-Opuscar library (github.com/lemomo-ai/lemo-opuscar, by Lemomo; MIT code, CC BY 4.0 content — credit it if a style is used publicly as-is). Every style there has a `styles/<slug>/style.json` (name, category, one-line film, uses), a `STYLE.md` (the style prompt, palette, rules), a `DEMO.md` (shots and direction) and a demo frame.

This skill is the style *catalogue*. Production of Utpal's videos follows the `edit-workflow` skill; Lemo-Opuscar's own film-making pipeline is only used if he explicitly wants a film made purely in that library's way (then load the `lemo-opuscar` skill).

## Get the library and the visuals

```bash
bash scripts/make_gallery.sh <outdir>          # clones/updates ~/lemo-opuscar, builds <outdir>/style_gallery.html
```

Publish `style_gallery.html` as an Artifact (or open it) so Utpal can scroll every style with its frame. Look at frames yourself with the Read tool before recommending.

## Making a style board for a video

1. Read the story's beat sheet/era/tone (from edit-workflow, or ask).
2. Shortlist 3–5 styles: one safe, one bold, one unexpected. Check `favourites.md` first and prefer those when they fit. Judge fit by era, tone, pacing and production effort.
3. For each: read its `STYLE.md` and `DEMO.md`; note palette, texture, type, motion feel, and what it costs to make (pure code, AI stills, real footage).
4. Show a board: frame + name + number + one line on why it fits + what it implies. Then sample *this* video's key shot in each shortlisted style if Utpal wants (free code render first; paid images per edit-workflow's credit rules).
5. He picks one, mixes two, or brings his own. Lock the choice into the visual bible: style name/number, palette, style suffix for image prompts, grade, texture, type, motion character.

## Translating a style to an AI-image look

Lemo-Opuscar styles are drawn in code. When the video uses AI stills instead, convert the style: take palette hex values, texture, line/brush rules, lighting and composition rules from `STYLE.md` and write them into a reusable prompt suffix. Show one test image before generating a set.

## His own styles

If Utpal brings references (images, reels, links, a description), break them down (palette, texture, light, type, motion, era signals), write a style spec in the same shape as a `STYLE.md`, and save it to `my-styles/<name>.md` in this skill when he wants to keep it. Add it to `favourites.md`.

## Files

- `favourites.md` — styles Utpal likes (numbers and names); grows over time.
- `my-styles/` — his own saved styles.
- `scripts/make_gallery.sh`, `scripts/build_gallery.py` — fetch library + build the visual gallery.

Anything learned or saved only persists if these files are committed; commit and tell him.
