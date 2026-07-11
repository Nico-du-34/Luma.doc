#!/usr/bin/env python3
"""Prepare GitBook sources for mdBook build without modifying the repository."""

from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD_DIR = ROOT / "_mdbook_build"
SKIP_DIRS = {"_mdbook_build", "book", ".git", ".github", "scripts"}


def strip_frontmatter(content: str) -> str:
    """Remove YAML frontmatter (--- ... ---) from the start of a markdown file."""
    if not content.startswith("---"):
        return content
    match = re.match(r"^---\r?\n.*?\r?\n---\r?\n?", content, re.DOTALL)
    if match:
        return content[match.end() :]
    return content


def convert_summary(content: str) -> str:
    """Convert GitBook SUMMARY.md format to mdBook SUMMARY.md format."""
    lines = content.splitlines()
    converted: list[str] = []

    for line in lines:
        if line.startswith("# Table of contents"):
            converted.append("# Summary")
        elif line.startswith("## "):
            converted.append("# " + line[3:])
        elif line.startswith("* "):
            converted.append("-" + line[1:])
        else:
            converted.append(line)

    return "\n".join(converted) + ("\n" if content.endswith("\n") else "")


def should_skip(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts)


def prepare() -> None:
    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)
    BUILD_DIR.mkdir()

    for md_path in ROOT.rglob("*.md"):
        if should_skip(md_path.relative_to(ROOT)):
            continue

        rel_path = md_path.relative_to(ROOT)
        dest = BUILD_DIR / rel_path
        dest.parent.mkdir(parents=True, exist_ok=True)

        content = md_path.read_text(encoding="utf-8")
        if rel_path.name == "SUMMARY.md":
            content = convert_summary(content)
        else:
            content = strip_frontmatter(content)

        dest.write_text(content, encoding="utf-8")

    print(f"Prepared {len(list(BUILD_DIR.rglob('*.md')))} markdown files in {BUILD_DIR}")


if __name__ == "__main__":
    prepare()
