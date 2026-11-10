# Pacing and rhythm

Pacing differs video to video, and within a video. It is planned as a curve in sections during the rhythm pass (Phase 2), before shots are designed, and measured on the render in QA (Phase 9) with `scripts/rhythm.py`.

## The patterns

Measured on the reference reels (motion = mean absolute pixel change per frame at 90×160; see `reference-library.md`).

| Pattern | Feel | Signature | Seen in |
|---|---|---|---|
| **Wave** | Cinematic glide | Motion rises and falls in smooth hills every ~1.5–2.5 s, never reaches zero; long shots (~3.4 s) but the camera always moves; motion equal before/after cuts | Moon / A119 |
| **Breath** | Calm, documentary, emotional | Low still baseline, short pulses at sentence breaks, real holds before payoffs; motion ~2× higher just after cuts than before | Dyson, Netflix |
| **Burst then pulse** | News-urgent, modern | First ~3 s moves 3–4× more than the rest (6 cuts in 3 s), then sharp hits every ~1.5–2 s, calm CTA; motion ~3× higher after cuts (every cut an impact) | Stripe / OpenRouter |
| **Fast cuts, calm frames** | Brisk storytelling | ~1 s shots but each frame nearly still; energy from cutting rhythm, not camera motion | Hedy Lamarr |
| **Dead stop** (a beat, not a pattern) | Shock, weight | Cut to black + silence for ~0.3–0.5 s before a big moment | Moon / A119 |

## Building a curve from sections

Combine patterns per section. A common shape for the channel:

1. **Hook — high** (burst, 0–3 s): dense cuts, impacts, the strongest image.
2. **Explain — mid** (breath or wave): room for information, holds on numbers.
3. **Reveal / twist — high** (pulse): hits on each new fact.
4. **Payoff — breath before, then land**: the frame slows right before the key line, then it lands.
5. **CTA — calm**: near-still, readable.

Speed is only felt next to slowness: every fast section needs a slower one beside it.

## The rhythm pass (Phase 2)

Mark every beat of the script:
- **HIT** — cut/impact on this word or phrase boundary.
- **GLIDE** — continuous movement carries through.
- **HOLD** — 1.5–3 s; numbers, faces, key lines. Living hold (text still, world drifting).
- **BREATH** — near-still beat before a payoff.

Guidelines:
- Cuts land on phrase boundaries of the voice, not mid-word.
- Numbers get the longest holds (references hold a key number 2–3 s).
- Faces get a beat before the next move.
- The hook is the densest section; the CTA the calmest.

Then draw the target curve: a list of sections with time ranges, pattern, target cut rate and target motion level (low / mid / high).

## Measuring (Phase 9 and reference analysis)

`python3 scripts/rhythm.py OUTDIR video1.mp4 [video2.mp4 ...]` prints cuts, shot lengths, holds, pace per 2 s, and motion before vs after cuts, and saves a graph. Compare against the target curve:
- Is the hook actually the highest-motion section?
- Are the planned holds present (motion near zero, no cuts, ≥0.5 s)?
- Is there a slowdown before the payoff?
- Any accidental dead stretches (motion ~0 where none was planned)?

Rough reference values: high sections ≈ 9–20, mid ≈ 3–7, calm ≈ 0–2 (values depend on content; compare relatively, within one video).
