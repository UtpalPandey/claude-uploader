# Build pipeline

## How the reference agency builds (from their After Effects process footage)

1. **Stills as raw material** — AI-generated and stock (Vecteezy) images; almost no live footage except real clips used as proof.
2. **Cut every image into layers** — hand-drawn pen masks (e.g. around a collar at 200%) to separate subject from background. This enables parallax and **frame-breaking** (a person's head poking out of a picture frame).
3. **3D space with a camera** — camera parented to a null ("NULL Cam"); groups of layers parented to nulls so they animate individually but move together.
4. **Two keyframes per move, eased with a preset panel** — consistent motion character.
5. **Highlights as separate layers** — a duplicate of the money layer, masked, filled yellow, switched on for ~1 s. A spotlight = soft feathered shape at low opacity, switched on as a reveal.
6. **Box-first blocking** — flat coloured placeholders in 3D space before the real images go in.
7. **Low-resolution previews** (Half/Third) and constant scrubbing — fast iteration over pretty previews.

## Our equivalent

| Their step | Ours |
|---|---|
| After Effects comps | **Remotion** (React video) compositions; three.js inside Remotion for true 3D camera moves; Blender via Python for heavy 3D if needed |
| Preset easing panel | A small easing module (`enterExpo`, `exitExpo`, `popOvershoot`, `glide`) used by every component |
| Hand roto | Automatic subject cutout + depth estimation models (needs network access to model hosts — see limits) ; manual masks as fallback |
| Camera on null | A camera rig component with parented layer groups |
| Highlight layers | `Highlight`, `Spotlight`, `AccentPop` components |
| Placeholder solids | The greybox animatic (Phase 5) |
| Half-res preview | Low-res draft renders + filmstrip checks |
| Motion blur | Sub-frame sampling (Remotion camera motion blur) |

Reusable components grow over time (list them in `reference-library.md` → "Our own library"). Typical: `CircleMatteWipe`, `IrisOpen`, `BlurWhip`, `FlashCut`, `FramePush`, `FlyThroughFrame`, `TileReveal`, `DevelopIn` (silhouette → photo), `DimAndReplace`, `CrumpleThrow`, `NewspaperFlyIn`-style proof fly-ins (with invented mastheads), `ExtrudedTitle`, `StaggerWords`, `TagPop`, `TypeOnSearchBar`, `ZScatterWords`, `CircleAnnotate`.

## Asset generation (Phase 7)

- Load the `kling-ai` skills before any Kling call and follow their rules: confirm each paid job with Utpal, never auto-retry or silently change parameters, report failures.
- Lock one style suffix (lens, light, grade, texture) shared by every prompt in a video.
- Generate at the final aspect ratio; ask for clean separable compositions (subject not touching frame edges if it must be cut out; plain or easily separable backgrounds when layering).
- Image-to-video only for shots that need organic motion (people, smoke, water); everything else is stills + 2.5D.

## Sound

- Voiceover leads; music bed under (often a sub-bass drone or pulse).
- A whoosh or impact on nearly every transition; risers into big moments; silence before shock beats; UI clicks/typing for interface scenes.
- Mix to about −14 LUFS integrated for social platforms.
- Needs an SFX library and licensed music from Utpal (or a provider he approves).

## Environment limits (cloud sessions)

- Tools available: ffmpeg, Chromium + Playwright, Python (numpy/matplotlib installable via pip), Node for Remotion.
- Model downloads from HuggingFace (Whisper for transcription, depth/cutout models) have been blocked by the network proxy. If needed, follow the environment tools' process to request host access; until then, take word timings from on-screen captions or a provided transcript.
- Voice APIs (e.g. ElevenLabs) need a key through the secure credential request, never pasted in chat.
- Anything worth keeping must be committed; the container is ephemeral.
