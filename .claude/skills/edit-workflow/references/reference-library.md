# Reference library

Studied reels, what each teaches, and measurements. Append new references using the entry format at the bottom (see `ingesting-references.md`). Principles go into the rule files; fingerprints go into `originality.md`.

## Measurements summary

Motion = mean absolute pixel change per frame at 90×160 grey (excluding cut frames). "After/before cut" = mean motion in the 6 frames after vs before each cut.

| Ref | Story type | Length | FPS | Cuts | Avg shot | Motion | Before → after cut | Pattern |
|---|---|---|---|---|---|---|---|---|
| R1 Moon / A119 | History mystery | 40.8 s | 30 | 11 | 3.4 s | 5.8 | 9.7 → 9.5 | Wave |
| R2 James Dyson | Life story | 39.5 s | 30 | 15 | 2.5 s | 2.3 | 2.6 → 5.9 | Breath |
| R3 Stripe buys OpenRouter | Tech business news | 31.5 s | 29.97 | 23 | 1.3 s | 5.9 | 6.2 → 18.5 | Burst then pulse |
| R4 Netflix (+ AE process) | Business story | 25.2 s | 24* | 10 (final part) | 1.6 s | 3.5 | 2.9 → 5.6 | Breath |
| R5 Hedy Lamarr / Wi-Fi | Life story + tech, era mash-up | 32.1 s | 24 source | 30 | 1.0 s | 2.3 | 1.6 → 3.5 | Fast cuts, calm frames |

*R4 file metadata reported 24 fps; its first 8 s are an After Effects screen recording.

All five are ads for the same seller of After Effects project files; the CTA is always the bridge to that product.

---

## R1 — Destroying the Moon (Project A119)
- **Look:** cinematic photoreal AI stills, teal/orange then B&W archive section, grain, vignette, bloom, shallow DOF everywhere.
- **Motif:** the Moon / circle in nearly every shot, and as transition mattes (circle wipe into lunar surface; blue dot iris into a CRT screen).
- **Transitions:** title slam with lens streaks; shrink-to-match (Moon into sky Moon); tilt reveals; whip tilt; red flash + zoom blur; newspaper fly-in with 3D curl; hard cut to black + silence; impact white-out; circle matte; 3D tilt laying text onto a floor; card unfold from a thin strip; whip pan; frame push; iris open.
- **Text:** 3D condensed title with red hero word; debossed text in lunar surface; serif italic twist question scattered in Z-space; grunge billboard with ☢ replacing a letter; typewriter on CRT.
- **Motion measured:** entrances peak in 2–3 frames, ~20-frame settle; sharpness halves during moves (motion blur); constant ~1 px/frame drift before moves.
- **Sound:** continuous VO, sub-bass bed, whoosh/impact per transition, silence at ~12.2 s, riser into explosion, clicks in CTA; −14.7 LUFS.
- **Fingerprints:** fake real-newspaper front pages (avoid), retro CRT + AE icon CTA.

## R2 — James Dyson (5,126 failures)
- **Look:** B&W photoreal AI portraits; **selective yellow** on the object of struggle (folder, vacuum); colour arrives when the story reaches "today"; real colour footage of the person at the end.
- **Proof:** patent drawings on wood, handwritten note with "In total" crossed out, newspaper.
- **Text:** italic serif captions word by word, always at chest height.
- **Rhythm:** breath pattern; "5,126 times" held ~3 s over a drifting scene (living hold); "5,127" held while the hand keeps writing; near-still cream page "most people would've… long before that" right before the payoff.
- **Anticipation seen:** background dims ~4 frames before a newspaper spins in; text dims before cuts; 2–3 empty frames before a word lands; camera accelerates for ~1 s into a cloud wipe.

## R3 — Stripe buys OpenRouter
- **Look:** modern, digital; real news screenshots and founder photos; brand colours (Stripe purple, OpenRouter lime) used in transitions; design-tool selection handles around captions; blueprint grids; RGB glitch frames.
- **Metaphors:** $50M revenue = building rising through clouds; sale = "COMPANIES FOR SALE" shop + "8 BILLION DOLLAR" sign; valuation = hand stacking money cubes; "the bet" = slot machine whose display decodes the URL (CTA bridge).
- **Rhythm:** 3-second burst hook (6 cuts), then pulses; "$8 Billion" huge behind the founder, held ~2 s; calm CTA.
- **Anticipation seen:** logo squares charge into white light before the cut; white square → tile reveal; white silhouette develops into a photo; slow photo tilt then whip.

## R4 — Netflix (with After Effects process)
- **Final part:** gold-framed portrait with the subject breaking out of the frame; camera flies into the frame and the picture becomes the full shot (B&W inside the frame → colour); newspaper collage with a hand-drawn circle around "25 MILLION"; serif "Forty five billion" with an ellipse around "billion" under a switched-on spotlight; yellow money highlight for ~1 s; B&W office for "competing on price"; full-colour real show clips for the turnaround; bold sans "the streaming wars" for the climax.
- **Process learned:** stills (AI + Vecteezy stock) → hand roto into layers → 3D layers + camera on null, groups on nulls → two keyframes per move eased via preset panel → highlight/spotlight as separate layers → placeholder solids first → half/third-res previews. See `build-pipeline.md`.

## R5 — Hedy Lamarr (the woman behind Wi-Fi)
- **Era mash-up:** vintage paper collage cutouts, patent paper, real archival film, colourised WW2 footage with halftone, scanlines and grain — against clean modern design for the payoff (router antennas rising, "BEHIND YOUR WI-FI.", macOS-style Wi-Fi/Bluetooth/GPS labels stacking on radar rings).
- **Bridge moments:** modern text-selection cursor highlighting typewriter text on vintage patent paper; radio tower with pulsing red signal arcs.
- **Metaphor transitions:** rejected idea = tower drawing crumples into a ball and drops into a green bin (only colour in a grey office); years passing = counting years on a blank page.
- **Selective colour:** a tiny red woman in a grey crowd of men ("almost no one realized").
- **Frame rate:** 24 fps — film cadence for a film-era story.
- **Rhythm:** fast cuts (~1 s), calm frames.

---

## Our own library

Components and techniques built for our videos. Add an entry each time (Phase 10).

| Component / technique | First used in | What it does | Notes |
|---|---|---|---|
| — | — | — | — |

---

## Entry format for new references

```
## R<n> — <title>
- **Story type / era:** …
- **Look:** …
- **Motif:** …
- **Assets by role:** world / proof / stakes / surfaces / bridge
- **Transitions:** …
- **Text:** …
- **Rhythm:** pattern, holds, measured numbers
- **Anticipation seen:** …
- **New principles:** (also added to rule files: which)
- **Fingerprints:** (also added to originality.md)
```
