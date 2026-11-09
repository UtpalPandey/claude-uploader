# Motion rules

Measured from reference reels (frame-by-frame position tracking and sharpness), plus their After Effects workflow. These are defaults that produce the "smooth even at 30 fps, with character" feel. Break one only on purpose.

## Easing

- **Entrances: fast start, long settle.** In a measured frame-push the layer hit peak speed within 2–3 frames (11 → 16 → 17 px/frame at 320 px height) and decayed over ~20 frames. Use a strong exponential ease-out; no ease-in on entrances.
- **Exits: ease-in** (accelerate away), then the cut hides inside the fastest part.
- **Overshoot on pops.** Tags, labels and cards scale past their size and settle back (≈5–10% overshoot, settle in 6–10 frames).
- **One house easing set.** The agency behind the references applies presets from an easing panel to every move — that's why all their animation shares one character. Define our own small set (e.g. `enterExpo`, `exitExpo`, `popOvershoot`, `glide`) once and use it everywhere. Ours can be a little snappier and more digital; decide per channel identity, then keep it consistent.
- Two keyframes per move (start, rest) is enough when the curve is good.

## Smoothness at 30 fps

- **Motion blur on everything that moves.** Measured sharpness dropped by about half during fast moves. Without blur the same animation stutters. In Remotion use sub-frame sampling (camera motion blur, ~180° shutter, 6–10 samples).
- **Living holds.** Nothing is ever fully still: a ~1 px/frame drift or a 3–5% push across a shot. Motion never stops and restarts.
- **Depth of field and parallax.** Separate subject from background; move them at different speeds; blur foreground/background layers. This is cheap 2.5D that reads cinematic.

## Transitions

- **Hide every cut inside motion**: whip pan/tilt with blur, zoom blur, white or colour flash, matte wipe (a shape from the scene grows to fill the frame), iris (a dot opens into the next scene), frame push (whole frame slides like a page), fly-through (camera flies into a picture frame or screen and its contents become the next shot), dim-and-replace, crumple/throw, tile reveal.
- **Short**: ≈6–12 frames (0.2–0.4 s).
- **Motion continues across the cut**: a tilt into a tilt, a flash into a flash. In glide-style edits motion is equal before and after cuts; in breath-style edits it's about twice as high after the cut as before (the new shot arrives moving, then settles).
- **Shape continuity**: the transition shape comes from the scene (the Moon's circle, the dot where the text sat).
- Hard cuts to black are allowed as a deliberate dramatic beat — pair with silence.

## Anticipation devices

The viewer feels "something is about to happen", then it does. The build-up is short (≈2–6 frames) — snappy, but long enough to register.

1. **Box first, content second** — a shape (white square, flat silhouette, empty label, empty search bar) appears, then fills with its content. Strongest device.
2. **Wind-up, then release** — slight opposite motion or a slow start before the fast move (photos tilt slowly for 3–4 frames, then whip).
3. **Dim the room** — the background darkens over ~4 frames before a hero object arrives.
4. **Charge-up** — an object glows or flashes for 1–2 frames before the cut.
5. **Clear the stage** — old text exits or dims, 2–3 empty frames, then the new element lands.
6. **Words lead pictures** — the caption word arrives with the voice; the picture follows.
7. **Constant drift** — because nothing is ever still, any change reads as intentional.

Name the device for every major move in the shot list.

## Text animation

- Word by word at the pace of speech; the hero word is the biggest, coloured and/or textured, and may get its own beat.
- Typical entrances: rise + fade with blur, scale-pop with overshoot, typewriter with cursor, 3D extrusion/deboss into a surface, words scattered in Z-space with the camera flying through.
- Annotations add proof and focus: hand-drawn circle around a number (trim-path stroke), underline marker, text-selection highlight, arrows.
- Captions stay in a stable zone (usually centre or chest height) so the eye never hunts.
- Exits are clean and early — text leaves before the next idea arrives.

## Camera

- Slow push-ins (2–5%) during holds; tilts to reveal (sky → subject); pull-backs to reveal context; fly-through into frames and screens; 3D X-rotation to lay text onto a floor.
- In references the camera sits on a null with layers parented in groups, so a group (e.g. a fan of newspapers) can animate individually and move together.
