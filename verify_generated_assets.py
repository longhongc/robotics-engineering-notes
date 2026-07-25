#!/usr/bin/env python3
"""Verify that raw non-Markdown assets are copied to generated documentation."""

from __future__ import annotations

import argparse
from pathlib import Path


MARKDOWN_SUFFIXES = {".md", ".markdown", ".mdown", ".mkd"}


def asset_paths(root: Path) -> set[Path]:
    return {
        path.relative_to(root)
        for path in root.rglob("*")
        if path.is_file() and path.suffix.lower() not in MARKDOWN_SUFFIXES
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Check raw/generated asset path preservation."
    )
    parser.add_argument("--raw", type=Path, default=Path("raws"))
    parser.add_argument("--docs", type=Path, default=Path("docs/notes"))
    args = parser.parse_args()

    raw_assets = asset_paths(args.raw)
    generated_assets = asset_paths(args.docs) if args.docs.exists() else set()
    missing = sorted(raw_assets - generated_assets)
    unexpected = sorted(generated_assets - raw_assets)

    if missing:
        print("Missing generated assets:")
        for path in missing:
            print(f"  {args.docs / path}")
    if unexpected:
        print("Unexpected generated assets:")
        for path in unexpected:
            print(f"  {args.docs / path}")
    if missing or unexpected:
        raise SystemExit(1)

    print(f"Verified {len(raw_assets)} generated asset path(s).")


if __name__ == "__main__":
    main()
