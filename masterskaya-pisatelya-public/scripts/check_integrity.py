#!/usr/bin/env python3
"""Deterministic integrity check for the public workshop.

Covers the mechanical part of docs/workflow-integrity-check.md:
manifest vs prompt files, prompt headers, contract/gate wiring,
role-map and session-boundary agreement, template layout, internal links.

Usage: python3 scripts/check_integrity.py   (from masterskaya-pisatelya-public/ or anywhere)
Exit code 1 when any ERROR is found.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HISTORICAL = re.compile(r"(structural-audit-report|workflow-integrity-report-|retrospective-\d|cleanup-handoff-summary)")

errors, warnings = [], []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def table_rows(text, header_start):
    """Return rows (lists of cells) of the first markdown table whose header starts with header_start."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith(header_start):
            rows = []
            for row in lines[i + 2:]:
                if not row.startswith("|"):
                    break
                rows.append([c.strip().strip("`") for c in row.strip().strip("|").split("|")])
            return rows
    return []


# 1. Manifest
manifest = read("docs/workflow-manifest.md")
roles = {}
for cells in table_rows(manifest, "| id | alias | prompt"):
    rid, alias, prompt, cond, iso, mode, checkpoint = cells[:7]
    roles[rid] = dict(alias=alias, prompt=prompt, iso=iso, mode=mode)
if not roles:
    err("manifest: role table not found")

# 2. Prompt files vs manifest
on_disk = {p.name[:3]: p for p in (ROOT / "prompts").glob("[0-9][0-9][0-9]-*.md")}
for rid, r in roles.items():
    if not (ROOT / r["prompt"]).is_file():
        err(f"{rid}: prompt file missing: {r['prompt']}")
for rid, p in on_disk.items():
    if rid not in roles:
        err(f"{p.name}: prompt not registered in manifest")
    elif f"prompts/{p.name}" != roles[rid]["prompt"]:
        err(f"{rid}: manifest prompt path differs from file name {p.name}")

# 3. Prompt headers and wiring
for rid, r in roles.items():
    path = ROOT / r["prompt"]
    if not path.is_file():
        continue
    t = path.read_text(encoding="utf-8")
    m = re.search(r"Short alias: `([^`]+)`", t)
    if not m or m.group(1) != r["alias"]:
        err(f"{rid}: Short alias does not match manifest alias `{r['alias']}`")
    m = re.search(r"Chat isolation: `([^`]+)`", t)
    if not m:
        err(f"{rid}: missing `Chat isolation:` header")
    elif m.group(1) != r["iso"]:
        err(f"{rid}: Chat isolation `{m.group(1)}` != manifest `{r['iso']}`")
    if "Fresh session:" in t:
        err(f"{rid}: legacy `Fresh session:` header")
    if "prompts/00-role-contract.md" not in t:
        err(f"{rid}: does not reference prompts/00-role-contract.md")
    if "## Gate verdict" not in t:
        err(f"{rid}: output has no `## Gate verdict`")
    if "## Output" not in t:
        err(f"{rid}: no `## Output` section")

# 4. Role map
for cells in table_rows(read("docs/role-map.md"), "| # | Short alias"):
    rid, alias, prompt, _purpose, iso, _mode = cells[:6]
    r = roles.get(rid)
    if not r:
        err(f"role-map: unknown role {rid}")
        continue
    if alias != r["alias"] or prompt != r["prompt"]:
        err(f"role-map: {rid} alias/prompt differ from manifest")
    if iso.replace(" ", "_") != r["iso"]:
        err(f"role-map: {rid} isolation `{iso}` != manifest `{r['iso']}`")
missing = set(roles) - {c[0] for c in table_rows(read("docs/role-map.md"), "| # | Short alias")}
if missing:
    err(f"role-map: roles missing: {sorted(missing)}")

# 5. Session boundaries lists
fb = read("docs/feedback-and-session-boundaries.md")
for kind in ("fresh_chat_required", "fresh_chat_recommended"):
    m = re.search(rf"Default `{kind}` roles[^\n]*\n\n((?:- .*\n)+)", fb)
    listed = set(re.findall(r"`(\d{3})-", m.group(1))) if m else set()
    expected = {rid for rid, r in roles.items() if r["iso"] == kind}
    if listed != expected:
        err(f"feedback-and-session-boundaries: {kind} lists {sorted(listed)}, manifest says {sorted(expected)}")

# 6. Quality gates cover every role
qg = read("docs/quality-gates.md")
for rid in roles:
    if f"`{rid}`" not in qg and f"## {rid} " not in qg:
        err(f"quality-gates: no gate for {rid}")

# 7. Template layout
tpl = ROOT / "stories/_template"
for rel in ["README.md", "00-input/raw-idea-from-chat.md", "01-canonical/canonical-story-state.md",
            "01-canonical/decisions-log.md", "02-handoffs/README.md", "03-drafts/README.md",
            "04-reviews/README.md", "05-exports/README.md",
            "06-agent-queue/agent-queue.md", "06-agent-queue/story-status.md"]:
    if not (tpl / rel).is_file():
        err(f"template: missing {rel}")
for sub in ("02-handoffs", "03-drafts", "04-reviews", "05-exports"):
    extra = [p.name for p in (tpl / sub).glob("*") if p.name != "README.md"]
    if extra:
        warn(f"template: {sub} contains placeholder files {extra}")
public_stories = [p.name for p in (ROOT / "stories").iterdir() if p.name not in ("README.md", "_template")]
if public_stories:
    err(f"public stories/ contains non-template entries: {public_stories}")

# 8. Internal links and stale vocabulary across public markdown
link_re = re.compile(r"`((?:docs|prompts|scripts|stories)/[^`\s<>*]+|START\.md|AGENTS\.md|ROADMAP\.md)`")
for md in ROOT.rglob("*.md"):
    rel = md.relative_to(ROOT).as_posix()
    if HISTORICAL.search(rel):
        continue
    text = md.read_text(encoding="utf-8")
    for target in set(link_re.findall(text)):
        clean = target.rstrip(".,;:")
        if "NNN" in clean or "MM-DD" in clean:
            continue  # naming patterns, not paths
        if not (ROOT / clean).exists():
            err(f"{rel}: broken reference `{clean}`")
    if "Fresh session:" in text and not rel.startswith("prompts/"):
        warn(f"{rel}: legacy `Fresh session:` wording")

for w in warnings:
    print(f"WARN  {w}")
for e in errors:
    print(f"ERROR {e}")
print(f"\n{len(roles)} roles checked: {len(errors)} error(s), {len(warnings)} warning(s)")
sys.exit(1 if errors else 0)
