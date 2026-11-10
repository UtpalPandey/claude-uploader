#!/usr/bin/env bash
# Break down a reference video for study.
# Usage: analyze_reference.sh <video> <outdir> [--strips t1,t2,...]
# Writes: meta.txt, sheets/sNN.jpg (2 fps contact sheets), cuts.txt, spectrogram.png,
#         loudness.txt, and strips/strip_<t>.jpg (15 fps, 0.6 s) for any --strips times.
set -euo pipefail
V="$1"; OUT="$2"; STRIPS="${4:-}"
[ "${3:-}" = "--strips" ] || STRIPS=""
mkdir -p "$OUT/sheets" "$OUT/strips"

ffprobe -v error -show_entries format=duration:stream=codec_type,codec_name,width,height,r_frame_rate,sample_rate \
  -of compact "$V" > "$OUT/meta.txt"
cat "$OUT/meta.txt"

# Contact sheets: 2 fps, 7 columns x 3 rows, timestamp burned in.
ffmpeg -v error -y -i "$V" -vf "fps=2,scale=240:-1,drawtext=text='%{pts\:flt}':x=4:y=4:fontsize=18:fontcolor=yellow:box=1:boxcolor=black,tile=7x3" \
  "$OUT/sheets/s%02d.jpg"
echo "contact sheets: $(ls "$OUT/sheets" | wc -l) in $OUT/sheets"

# Scene-change candidates (soft threshold; rhythm.py gives the stricter cut list).
ffmpeg -hide_banner -nostats -i "$V" -vf "select='gt(scene\,0.25)',showinfo" -vsync vfr -f null - 2>&1 \
  | grep -o 'pts_time:[0-9.]*' | cut -d: -f2 > "$OUT/cuts.txt" || true
echo "scene changes: $(wc -l < "$OUT/cuts.txt") (see cuts.txt)"

# Audio: spectrogram + loudness.
if ffprobe -v error -select_streams a -show_entries stream=index -of csv=p=0 "$V" | grep -q .; then
  ffmpeg -v error -y -i "$V" -lavfi "showspectrumpic=s=1600x500:legend=1:scale=log:fscale=log" "$OUT/spectrogram.png"
  ffmpeg -i "$V" -af ebur128 -f null - 2>&1 | grep -A3 "Integrated loudness" > "$OUT/loudness.txt" || true
  cat "$OUT/loudness.txt"
fi

# Transition filmstrips.
if [ -n "$STRIPS" ]; then
  IFS=',' read -ra TS <<< "$STRIPS"
  for t in "${TS[@]}"; do
    ffmpeg -v error -y -ss "$t" -t 0.6 -i "$V" \
      -vf "fps=15,scale=170:-1,drawtext=text='%{pts\:flt}':x=3:y=3:fontsize=14:fontcolor=yellow:box=1:boxcolor=black,tile=9x1" \
      -frames:v 1 "$OUT/strips/strip_$t.jpg"
  done
  echo "strips: $OUT/strips"
else
  echo "tip: rerun with --strips 2.1,5.0,... to get 15 fps filmstrips around transitions"
fi
