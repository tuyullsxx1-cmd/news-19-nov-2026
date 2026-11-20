# Design notes — "The World in One Day", 19 Nov 2026

## System (the top 1–3 grammar, built distinctly)

The live top 3 for this bounty (99.21–99.23%) all share one grammar:
newspaper masthead, 3 big hero stories with drawn illustrations, 10 medium
stories, a world map with numbered pins, a numbered list of the rest, a
date-check box, and a sources footer. This entry follows that grammar —
the 18 Nov entry (97.60%) lost points for using a different one (6 icon
cards, no map) — but with its own layout, copy, and drawings:

1. **Masthead + strips, not a navy banner.** Cream paper, black serif
   title, red italic deck. Below it a region-count strip (7 coloured
   chips) and a numbers strip (3 leaders · 9–6 · $81.3bn · 15.9m ·
   200,000 · 4.9%).
2. **3 heroes, a different trio from every top-3 entry.** Summit + GTA VI
   + ICJ. (#1 used summit + ICJ + COP31; #2 and #3 used summit + GTA VI
   + Anthropic.) Each hero has a flat vector illustration drawn in PIL:
   three leaders at a table with their flags, a neon Vice City skyline
   with a pink car, a court building with scales and a 9–6 badge.
3. **10 medium cards, 5×2, each with its own small drawn scene** (globe +
   thermometer, IPO bars, cyclone spiral, bridge, missile intercept,
   school + clock, strike crowd, falling chart, rain clouds, Arctic
   mountains + Danish flag).
4. **World map with numbered pins** (1–13, red, matching the cards) at
   the bottom left, drawn from rough continent polygons in code.
5. **The remaining 23 stories as a two-column numbered list** (14–36),
   then a red DATE CHECK box naming what was left out and why, and a
   sources footer.

## Legibility choices

- 36 stories: 13 cards + 23 list items. Every card summary is complete
  (no truncation): heroes get 3 lines, medium cards 3 lines at 9.5pt.
- Smallest type is 8–9pt (list sources, footer) — readable at full size,
  the same trade-off the top entries make.
- File is 200,569 bytes at 1024×1024 — smaller than top 1 (318,641 B)
  and top 3 (312,966 B); size is the tie-break, lower is better.

## Revision (20 Nov) — match the top-10 pattern

User asked to close the gaps vs the live top 10 (#1 99.2344%, #10
99.1068%, #50 paid-place cutoff 98.9158%). Changes, all in work/gen.py
(rendered 20 Nov ~16:00 WIB, PNG 226,311 B, still 1024×1024):

- **Distinctive masthead.** Kicker is now "ONE DAY, ONE WORLD" (was "THE
  WORLD IN ONE DAY", the same title #3/#9/#10 use). Main title and deck
  unchanged.
- **Richer illustrations.** Every card's drawing gained detail: summit
  (skyline silhouette, gold APEC banner, microphones), GTA (neon "VI OUT
  NOW" sign, palm silhouettes), court (door, windows, column capitals,
  Myanmar flag), COP (draft document with the fossil line struck out and
  a red CUT stamp), IPO (ANT ticker, buyer crowd), storm (ODISHA label),
  bridge (blast starburst, smoke, KERCH label), missile (city skyline,
  RIYADH label), exam (clock kept), strike (placards), jobs (5-YEAR HIGH
  label), flood (15.3 IN label), Arctic (both flags, ARCTIC PACT label).
  Also fixed the bridge explosion lines, which used to run past the card
  edge.
- **"THE DAY BY HOURS" strip** (new, under the numbers strip): 00:00
  Auckland GTA VI unlocks · before dawn Riyadh sirens · 10:00 Seoul
  offices open · 10:00 The Hague ruling read · Shenzhen three leaders
  meet · New York Anthropic debuts. Clock times come from SOURCES.md
  only; the last two cells carry place names, not invented times.
- **"THE VERDICT" box** (new band): the ICJ 9–6 Myanmar ruling in one
  short paragraph, navy box.
- **"MARKETS & MONEY" box** (new band): $83 ANT IPO price (Wed) ·
  $81.3bn record IPO · Australia jobless 4.9% · RBA cash 4.85% · 48 hrs
  left at COP31.
- **"HOW SURE ARE WE?" legend + tags.** Every card carries a certainty
  tag (REPORTED green / CLAIM red / FORECAST blue) at the top-right of
  its illustration: heroes all REPORTED; medium cards COP31 FORECAST,
  IPO REPORTED, cyclone FORECAST, Kerch REPORTED, Riyadh CLAIM, exam
  REPORTED, strike REPORTED, jobs REPORTED, floods REPORTED, Arctic
  REPORTED.
- **Layout rebalance to fit it all in 1024×1024:** masthead title
  56→52pt, numbers strip tightened, heroes 234→200px (illustration
  118→88px), medium cards 136→134px, list rows 15→12px pitch, map
  198→136px tall. Smallest type stays 8pt (list sources, footer).
  Verified: no truncation anywhere (36 stories fit: 3 heroes + 10
  medium + 23 list), no overlaps, map pins still match the cards.

## Build

- Python PIL only, DejaVu Sans/Serif (bundled in fonts/). No photos, no
  AI image generator, no copyrighted images — every picture is a line
  drawing made in the script (work/gen.py). PNG optimised
  (compress_level 9). Final file 226,311 bytes (221 KB), under the 500 KB
  limit.
- main.py is a stdlib-only copier (see its docstring): the grader runs
  plain python:3.13 with no Pillow, so the program only copies the PNG
  already in the repo to $MAKEFUN_OUTPUT_DIR/entry.png.
- Revisions: the generator went through three renders in one session
  (first render, then fixes for medium-card overflow and the summit
  figures, then fixes for medium-summary truncation, the card-5
  kicker/source collision, and the date-check first line, which was
  drawn with PIL's default white fill). The repo itself has two commits:
  v1 (the full build) and v2 (polish: hair on the summit figures, the
  109–0 badge moved off the flag), plus a DESIGN.md correction commit.
