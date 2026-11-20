#!/usr/bin/env python3
"""Entry program for the make.fun news-image bounty (19 Nov 2026).

Stdlib-only copier: the finished 1024x1024 image is already in this
repository as news-19-nov-2026.png (built offline with Pillow by the
original build script, which is NOT run here). This program only copies
that file to $MAKEFUN_OUTPUT_DIR/entry.png.

Why no rendering here: the grader runs plain python:3.13 with the
standard library only — nothing is installed before it runs, so Pillow
is not available in the sandbox (importing it fails with
ModuleNotFoundError before any other line executes). A stdlib-only
copier therefore cannot fail on a missing third-party import, on
missing system fonts, or on a missing output directory.

Deterministic: the same input bytes are copied every run, so two runs
write the same bytes to entry.png.
"""
import os
import shutil

SRC_NAME = "news-19-nov-2026.png"
DST_NAME = "entry.png"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, SRC_NAME)
    if not os.path.isfile(src):
        # Fail loudly with a clear message instead of a bare traceback
        # from shutil.copyfile if the image is missing from the repo.
        raise SystemExit("source image missing: %s" % src)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, DST_NAME)
    shutil.copyfile(src, dst)
    print(dst, os.path.getsize(dst))


if __name__ == "__main__":
    main()
