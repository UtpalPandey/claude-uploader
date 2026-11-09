# Ingesting a new reference

Learn the way an editor learns: watch closely, break it down, separate what's transferable from what's that creator's signature, then practise the principle in our own way.

## 1. Analyze

Put the video somewhere you control (e.g. the scratchpad) and run:

```bash
bash scripts/analyze_reference.sh <video.mp4> <outdir>
python3 scripts/rhythm.py <outdir> <video.mp4>
```

`analyze_reference.sh` writes metadata, contact sheets (2 fps, timestamped), a cut list, a spectrogram and a loudness summary. `rhythm.py` writes the pace graph and prints cuts, shot lengths, holds, pace per 2 s and motion before/after cuts. (Install `numpy matplotlib` with pip if missing.)

Then look at the images yourself:
1. Read every contact sheet; write a shot-by-shot table (time, shot, camera/animation, transition out).
2. Pull 10–15 fps filmstrips around every transition and big move (`scripts/analyze_reference.sh` prints the strip command; or use `--strips t1,t2,...`). Look for the anticipation devices, easing, blur, and where the cut actually happens.
3. Read the rhythm graph: which pattern(s), where the holds and dead stops are, how the hook compares with the rest.
4. Read the spectrogram: continuous voice, music bed, whoosh/impact streaks at transitions, silences, risers.

If it's a **process / behind-the-scenes** video, focus on the workflow instead: tools visible, layer structure and names, how assets were prepared (masks, cutouts, stock sources), camera rigs, keyframe/easing approach, preview habits. Read full-resolution frames to make out UI text.

## 2. Classify what you found

For each observation, decide:
- **Principle** — transferable craft that would improve any video (an easing behaviour, an anticipation device, a pacing pattern, an asset role, a continuity trick).
- **Fingerprint** — that creator's signature look or recurring asset. Learn why it works; don't reuse it.
- **Already known** — confirms an existing rule (note it as extra evidence, briefly).
- **New** — something not yet in the skill.

Be honest about uncertainty: say what was measured, what was seen, and what is a guess.

## 3. Report to Utpal

Short and concrete:
- What the reference is and how it's built (one table).
- What's **new** compared with what we already know.
- Which principles it adds, and which fingerprints to avoid.
- One or two ideas for how *we* could use the principle differently.

## 4. Integrate

- Append an entry to `references/reference-library.md` (entry format at the bottom of that file) and a row to its measurements table.
- Update the rule file(s) only where the new evidence adds or changes something: `motion-rules.md`, `pacing.md`, `asset-roles.md`, `continuity.md`, `build-pipeline.md`.
- Add fingerprints to `originality.md`.
- Keep rules general (why + default), not tied to one reel's specific objects.
- Commit the changes so they persist beyond the session, and tell Utpal what changed.
