#!/usr/bin/env python3
"""Aggregate each member's progress into the top-level PROGRESS.md table.

Scans `members/<name>/`, counts `- [x]` / `- [ ]` checkboxes per domain in
`progress.md`, reads metadata from `profile.md`, and finds the latest date in
`weekly-log.md`. Regenerates the table between the PROGRESS markers in PROGRESS.md
and prints the rendered table to stdout (used as the GitHub Action job summary).

Standard library only — no dependencies. Run from anywhere:  python scripts/update_progress.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MEMBERS_DIR = ROOT / "members"
PROGRESS_FILE = ROOT / "PROGRESS.md"

START = "<!-- PROGRESS:START -->"
END = "<!-- PROGRESS:END -->"

# (column header, "Domain N" label matched in progress.md headers)
DOMAINS = [
    ("D1 Agentic", "Domain 1"),
    ("D2 Tools/MCP", "Domain 2"),
    ("D3 Claude Code", "Domain 3"),
    ("D4 Prompting", "Domain 4"),
    ("D5 Context", "Domain 5"),
]

CHECKBOX_RE = re.compile(r"^\s*[-*]\s*\[([ xX])\]")
DOMAIN_HEADER_RE = re.compile(r"^#{1,6}\s*(Domain\s*\d)\b", re.IGNORECASE)
DATE_RE = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")

STATUS_LABELS = {
    "in-progress": "🟢 In progress",
    "final-prep": "🎯 Final prep",
    "passed": "✅ Passed",
}


def norm(label: str) -> str:
    return label.lower().replace(" ", "")


def parse_progress(path: Path) -> dict[str, tuple[int, int]]:
    """Return {column_header: (done, total)} from a progress.md file."""
    counts = {key: [0, 0] for key, _ in DOMAINS}
    label_to_key = {norm(label): key for key, label in DOMAINS}
    current = None
    for line in path.read_text(encoding="utf-8").splitlines():
        header = DOMAIN_HEADER_RE.match(line)
        if header:
            current = label_to_key.get(norm(header.group(1)))
            continue
        box = CHECKBOX_RE.match(line)
        if box and current:
            counts[current][1] += 1
            if box.group(1).lower() == "x":
                counts[current][0] += 1
    return {k: (v[0], v[1]) for k, v in counts.items()}


LINK_LABEL_RE = re.compile(r"\[([^\]]+)\]")


def _clean_label(text: str) -> str:
    """Prefer the markdown link label; fall back to raw checkbox text."""
    m = LINK_LABEL_RE.search(text)
    return (m.group(1) if m else text).strip()


def parse_breakdown(path: Path) -> dict[str, list[tuple[str, bool]]]:
    """Return {column_header: [(label, checked), ...]} preserving order."""
    items = {key: [] for key, _ in DOMAINS}
    label_to_key = {norm(label): key for key, label in DOMAINS}
    current = None
    for line in path.read_text(encoding="utf-8").splitlines():
        header = DOMAIN_HEADER_RE.match(line)
        if header:
            current = label_to_key.get(norm(header.group(1)))
            continue
        box = CHECKBOX_RE.match(line)
        if box and current:
            rest = line[box.end():].strip()
            items[current].append((_clean_label(rest), box.group(1).lower() == "x"))
    return items


def render_breakdown(name: str, breakdown: dict[str, list[tuple[str, bool]]]) -> str:
    """Render one member's collapsible per-subdomain breakdown."""
    done = sum(1 for items in breakdown.values() for _, c in items if c)
    total = sum(len(items) for items in breakdown.values())
    summary = f"{name} — {pct(done, total)} overall ({done}/{total} subdomains)"
    lines = ["<details>", f"<summary>{summary}</summary>", ""]
    for key, label in DOMAINS:
        items = breakdown.get(key, [])
        if not items:
            continue
        d = sum(1 for _, c in items if c)
        lines.append(f"**{label} ({pct(d, len(items))})**")
        lines.append("")
        for sub_label, checked in items:
            lines.append(f"- {'✅' if checked else '⬜'} {sub_label}")
        lines.append("")
    lines.append("</details>")
    return "\n".join(lines) + "\n"


def parse_profile(path: Path) -> dict[str, str]:
    meta = {"target": "—", "status": "🟢 In progress"}
    if not path.exists():
        return meta
    text = path.read_text(encoding="utf-8")
    t = re.search(r"target exam date\**\s*[:：]\s*(.+)", text, re.IGNORECASE)
    if t:
        meta["target"] = t.group(1).strip().strip("*").strip() or "—"
    s = re.search(r"\bstatus\**\s*[:：]\s*([A-Za-z-]+)", text, re.IGNORECASE)
    if s:
        val = s.group(1).strip().lower()
        meta["status"] = STATUS_LABELS.get(val, val)
    return meta


def latest_log_date(path: Path) -> str:
    if not path.exists():
        return "—"
    dates = DATE_RE.findall(path.read_text(encoding="utf-8"))
    return max(dates) if dates else "—"


def pct(done: int, total: int) -> str:
    if total == 0:
        return "—"
    return f"{round(done * 100 / total)}%"


def collect_rows() -> list[dict]:
    rows = []
    if not MEMBERS_DIR.is_dir():
        return rows
    for member in sorted(MEMBERS_DIR.iterdir()):
        if not member.is_dir() or member.name.startswith((".", "_")):
            continue
        prog = member / "progress.md"
        if not prog.exists():
            continue
        counts = parse_progress(prog)
        meta = parse_profile(member / "profile.md")
        rows.append(
            {
                "name": member.name,
                "target": meta["target"],
                "cells": [pct(*counts[key]) for key, _ in DOMAINS],
                "last": latest_log_date(member / "weekly-log.md"),
                "status": meta["status"],
            }
        )
    return rows


def render_table(rows: list[dict]) -> str:
    cols = ["Member", "Target exam date", *[k for k, _ in DOMAINS], "Last check-in", "Status"]
    lines = ["| " + " | ".join(cols) + " |", "|" + "|".join(["---"] * len(cols)) + "|"]
    if not rows:
        lines.append("| _No members yet — copy `members/_TEMPLATE` to get started_ |" + " |" * (len(cols) - 1))
    for r in rows:
        link = f"[{r['name']}](members/{r['name']}/)"
        cells = [link, r["target"], *r["cells"], r["last"], r["status"]]
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines) + "\n"


def main() -> int:
    rows = collect_rows()
    table = render_table(rows)

    if not PROGRESS_FILE.exists():
        print(f"error: {PROGRESS_FILE} not found", file=sys.stderr)
        return 1

    content = PROGRESS_FILE.read_text(encoding="utf-8")
    if START not in content or END not in content:
        print(f"error: missing {START} / {END} markers in PROGRESS.md", file=sys.stderr)
        return 1

    block = f"{START}\n{table}{END}"
    new_content = re.sub(
        re.escape(START) + r".*?" + re.escape(END),
        lambda _m: block,
        content,
        flags=re.DOTALL,
    )

    # Always print the table so the Action job summary shows "where everyone is".
    print(table)

    if new_content != content:
        PROGRESS_FILE.write_text(new_content, encoding="utf-8")
        print(f"Updated {PROGRESS_FILE.name} ({len(rows)} member(s)).", file=sys.stderr)
    else:
        print(f"{PROGRESS_FILE.name} already up to date ({len(rows)} member(s)).", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
