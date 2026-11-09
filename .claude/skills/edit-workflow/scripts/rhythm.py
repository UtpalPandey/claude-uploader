#!/usr/bin/env python3
"""Measure the editing rhythm of one or more videos.

Usage: python3 rhythm.py OUTDIR video1.mp4 [video2.mp4 ...] [--start SECONDS]

For each video prints: cut times, shot lengths, near-still holds (>=0.5 s),
pace per 2 s, and mean motion in the 6 frames before vs after cuts.
Saves OUTDIR/rhythm.png: grey bars = motion per frame, red = pace (0.5 s avg),
blue lines = cuts, green = audio loudness (dB).

Motion = mean absolute grey-level change between consecutive frames at 90x160,
resampled to 30 fps. Compare values relatively within and across videos.
Requires ffmpeg, numpy, matplotlib (pip install numpy matplotlib).
"""
import os, subprocess, sys, tempfile
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

W, H, FPS, SR = 90, 160, 30, 16000


def load(video, start, tmp):
    g, a = os.path.join(tmp, "v.gray"), os.path.join(tmp, "v.pcm")
    ss = ["-ss", str(start)] if start else []
    subprocess.run(["ffmpeg", "-v", "error", "-y", *ss, "-i", video, "-vf",
                    f"fps={FPS},scale={W}:{H},format=gray", "-f", "rawvideo", g], check=True)
    frames = np.fromfile(g, np.uint8).reshape(-1, H, W).astype(np.float32)
    r = subprocess.run(["ffmpeg", "-v", "error", "-y", *ss, "-i", video, "-ac", "1", "-ar", str(SR),
                        "-f", "s16le", a])
    audio = np.fromfile(a, np.int16).astype(np.float32) / 32768 if r.returncode == 0 and os.path.exists(a) else None
    return frames, audio


def analyse(frames, audio):
    n = len(frames)
    diff = np.r_[0, np.abs(np.diff(frames, axis=0)).mean(axis=(1, 2))]
    corr = np.r_[1, [np.corrcoef(frames[i].ravel(), frames[i - 1].ravel())[0, 1] for i in range(1, n)]]
    corr = np.nan_to_num(corr, nan=1.0)
    raw = np.where(corr < 0.55)[0]
    cuts = [int(c) for i, c in enumerate(raw) if i == 0 or c - raw[i - 1] > 3]
    mot = diff.copy()
    mot[cuts] = np.nan
    m = np.nan_to_num(mot)
    pace = np.convolve(m, np.ones(15) / 15, "same")
    adb = None
    if audio is not None and len(audio):
        spf = SR // FPS
        rms = np.array([np.sqrt((audio[i * spf:(i + 1) * spf] ** 2).mean() + 1e-12) for i in range(n)])
        adb = 20 * np.log10(rms + 1e-6)
    holds, run = [], 0
    for i, x in enumerate(m):
        if x < 0.6 and i not in cuts:
            run += 1
        else:
            if run >= 15:
                holds.append((round((i - run) / FPS, 2), round(run / FPS, 2)))
            run = 0
    if run >= 15:
        holds.append((round((n - run) / FPS, 2), round(run / FPS, 2)))
    return dict(n=n, m=m, mot=mot, pace=pace, cuts=cuts, holds=holds, adb=adb)


def report(name, r):
    n, cuts, mot = r["n"], r["cuts"], r["mot"]
    dur = n / FPS
    sl = np.diff([0] + [c / FPS for c in cuts] + [dur])
    print(f"== {name}: {dur:.1f}s, {len(cuts)} cuts, shot length mean {sl.mean():.2f}s "
          f"(min {sl.min():.2f}, max {sl.max():.2f}), mean motion {np.nanmean(mot):.1f}")
    print("   cuts (s):", [round(c / FPS, 2) for c in cuts])
    print("   near-still holds (start, dur):", r["holds"])
    print("   pace per 2s:", [round(float(np.nanmean(r["m"][i:i + 60])), 1) for i in range(0, n, 60)])
    pre = [np.nanmean(mot[c - 6:c]) for c in cuts if c > 6]
    post = [np.nanmean(mot[c + 1:c + 7]) for c in cuts if c + 7 < n]
    if pre and post:
        print(f"   motion 6f before cuts {np.nanmean(pre):.1f} | 6f after cuts {np.nanmean(post):.1f}")


def main():
    args = sys.argv[1:]
    start = 0.0
    if "--start" in args:
        i = args.index("--start"); start = float(args[i + 1]); del args[i:i + 2]
    if len(args) < 2:
        print(__doc__); sys.exit(1)
    out, videos = args[0], args[1:]
    os.makedirs(out, exist_ok=True)
    fig, axs = plt.subplots(len(videos), 1, figsize=(20, 3.7 * len(videos)), squeeze=False)
    for ax, v in zip(axs[:, 0], videos):
        with tempfile.TemporaryDirectory() as tmp:
            frames, audio = load(v, start, tmp)
        r = analyse(frames, audio)
        name = os.path.basename(v)
        report(name, r)
        t = np.arange(r["n"]) / FPS
        ax.bar(t, r["m"], width=1 / FPS, color="#888")
        ax.plot(t, r["pace"], color="#d33", lw=2)
        for c in r["cuts"]:
            ax.axvline(c / FPS, color="#36c", lw=1, alpha=.6)
        if r["adb"] is not None:
            ax2 = ax.twinx(); ax2.plot(t, r["adb"], color="#2a2", lw=.8, alpha=.7); ax2.set_ylim(-60, 0)
        ax.set_title(name + (f" (from {start}s)" if start else ""))
        ax.set_xlim(0, t[-1]); ax.set_xticks(np.arange(0, t[-1], 1)); ax.grid(axis="x", alpha=.2)
    plt.tight_layout()
    path = os.path.join(out, "rhythm.png")
    plt.savefig(path, dpi=80)
    print("graph:", path)


if __name__ == "__main__":
    main()
