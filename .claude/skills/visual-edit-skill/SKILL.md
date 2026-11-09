---
name: visual-edit-skill
description: Storyboard-first workflow for motion design and edited videos with seamless, continuous transitions. Use whenever the user asks for an animation, motion graphic, UI motion demo, transition, animated video, video edit, storyboard, or sketch panels, or complains that motion looks jarring, choppy, or not smooth. Flow is brief → sketched storyboard (approved) → style frames (approved) → animatic → final animation verified frame by frame → export for edit.
---

# Visual Edit Skill

Goal: motion that feels like one continuous film, not a set of separate animations.
Never jump straight to final animation code. Every stage below needs the user's
approval before moving to the next one.

## Workflow

| Stage | User gives | Claude delivers | Gate |
|---|---|---|---|
| 1. Brief | Idea/story, length, platform, aspect ratio, design language, textures, colours, fonts, references | A numbered scene list (one main action per scene) | User confirms scene list |
| 2. Storyboard | Notes / mark-ups | Sketch panels (see "Storyboard format") | User approves sketches |
| 3. Style frames | Notes | 2–3 fully styled stills in the user's aesthetic, no motion | User approves look |
| 4. Animatic | Timing notes | Grey-box version: simple shapes, real timing and continuity | User approves timing |
| 5. Final animation | Final notes | Full style + motion, self-verified (see "Verification") | User approves |
| 6. Export | — | Video file (MP4/WebM) at the agreed resolution and fps, ready for the edit | — |

If the user supplies their own sketches or style, skip the matching stage and build from theirs.
Record the approved design language (palette, type, textures, corner radius, shadows, grain,
motion curve) at the top of the project and reuse it in every stage. Ask for it if it's missing.

## Storyboard format

Match the reference style: a clean, minimal, hand-drawn-looking line sketch on white.
- One panel per motion (one main action per panel).
- Arrows show the direction of movement and gestures (drag, tap, swipe).
- A 2–3 word label under each panel: "zoom out", "drag, cards flip", "sheet slides up",
  "tap, coin flies", "rows slide up", "bars spread", "lines draw in", "typed".
- Under the label, a handoff note: which element or end frame carries into the next panel.
- Make panels as SVG (rough line style, e.g. slight stroke jitter, `stroke-linecap: round`)
  laid out in one storyboard page/image. Number every panel so the user can reference it.
- Show the sheet to the user (publish an artifact or send the image) and wait for approval.

## Continuity rules (apply to every transition)

1. **End frame = start frame.** Each scene begins exactly where the previous one ended:
   same element, position, scale, colour. Never reset to zero, never hard-cut between scenes
   unless the storyboard says "cut".
2. **Hero element carries the eye.** One shared element (card, coin, chart, text) travels
   through the transition and becomes part of the next layout (shared-element / FLIP morph).
3. **Overlap moves.** Start the next motion while the previous one settles (about 20–30%
   overlap). No full stops between moves, except a deliberate hold of 300–800ms on a key beat.
4. **One easing family.** Default `cubic-bezier(0.22, 1, 0.36, 1)` (ease-out-quint) or one
   spring (stiffness ~170, damping ~22). Never linear for spatial moves. Exits accelerate
   (ease-in), entries decelerate (ease-out).
5. **Stagger groups.** Lists, bars, icons: 40–80ms between items, all in the same direction.
6. **Keep the direction.** Motion continues its direction across the cut: what leaves upward
   is followed by content entering from below. Never reverse direction at random.
7. **One main action at a time.** The rest of the frame stays still or barely moves.
8. **Animate several properties together.** Combine transform (translate/scale/rotate),
   opacity, and optionally blur (0→8px) or clip-path. Avoid fade-only or slide-only moves.
9. **Durations.** Micro moves 200–350ms, scene transitions 450–800ms, draw-ons/typing are
   paced to read comfortably. Use the same timing scale throughout.
10. **Performance.** Animate only transform, opacity, filter and clip-path. No layout
    properties (top/left/width/height). Target 60fps.

## Build

- Default stack: one self-contained HTML file with a single master timeline (GSAP
  `gsap.timeline()` with position parameters like `"-=0.2"` for overlaps, or the Web
  Animations API). Every scene sits on that one timeline so continuity is exact.
- Build the animatic first using the same timeline, then swap in the styled elements.
- Loop seamlessly when asked: the last frame must match the first.

## Verification (before showing the user anything that moves)

1. Render with headless Chromium (Playwright is pre-installed) and capture frames at
   30–60fps for the full duration (for frame-perfect capture, seek the timeline step by step
   with `tl.progress()` / `tl.seek()` instead of real-time recording).
2. Turn the frames into contact sheets (`ffmpeg -vf "fps=4,scale=360:-1,tile=6x4"`)
   and inspect every transition boundary:
   - any frame where an element pops, jumps, or flashes → fix
   - any dead frame (nothing moving outside a planned hold) → tighten the overlap
   - direction or easing inconsistent with the rules → fix
3. Encode the video: `ffmpeg -framerate 60 -i f%05d.png -c:v libx264 -pix_fmt yuv420p -crf 18 out.mp4`.
4. Tell the user what was checked and anything that's still rough.

## Studying a reference video

When the user shares a reference clip: extract frames (`ffmpeg -vf fps=1,...,tile`), then dense
frames (12–24fps) around each transition. Write down for each transition: the hero element,
direction, overlap, easing feel, and duration. Use those notes as the target for the
storyboard and the animation.
