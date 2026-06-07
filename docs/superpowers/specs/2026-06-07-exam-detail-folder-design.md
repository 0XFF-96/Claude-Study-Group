# Exam Detail → Per-Domain Folder + Subdomain Reporting — Design

**Date:** 2026-06-07
**Status:** Approved (design), pending spec review
**Author:** jimmyli (with Claude)

## Problem

`exam_detail.md` is a single 39 KB file holding the full CCA-F skills breakdown
(5 domains, 30 official subdomains, each with *Knowledge of* + *Skills in* bullets).
It is hard to reference and impossible to track against at a useful granularity.

Progress tracking today is **domain-level only**: `scripts/update_progress.py`
counts `- [x]` checkboxes under `## Domain N` headers in each member's
`progress.md` and renders a 5-column group table in `PROGRESS.md`. There is no
way to see *which specific aspects* a member is strong or weak on.

## Goal

Break `exam_detail.md` into a per-domain folder that can be referenced from a
progress report, and extend tracking to **subdomain level** so each member (and
the group) can see strengths and weaknesses per official subdomain (1.1–5.6).

## Decisions (locked)

- **Folder granularity:** one file per domain, subdomains as `## N.M` sections.
- **Report level:** subdomain-level.
- **Old file:** `exam_detail.md` is replaced (deleted; git history preserved).
- **Checklist:** re-aligned to the 30 official subdomains (the current ~6
  hand-grouped bullets per domain do not map 1:1 to the exam blueprint).
- **Tracking unit:** one checkbox per subdomain (binary). Partial mastery shows
  up as the domain rollup %.
- **Report surface:** a single `PROGRESS.md` — group domain table (unchanged)
  plus a per-member collapsible subdomain breakdown.

## The 30 subdomains

| Domain | Subdomains |
|--------|------------|
| 1 — Agentic Architecture & Orchestration (27%) | 1.1 Agentic loops · 1.2 Multi-agent coordinator–subagent · 1.3 Subagent invocation & context passing · 1.4 Multi-step workflow enforcement & handoff · 1.5 Agent SDK hooks · 1.6 Task decomposition · 1.7 Session state, resume & fork |
| 2 — Tool Design & MCP Integration (18%) | 2.1 Tool interface design · 2.2 Structured MCP errors · 2.3 Tool distribution & `tool_choice` · 2.4 MCP server integration · 2.5 Built-in tools |
| 3 — Claude Code Configuration & Workflows (20%) | 3.1 CLAUDE.md hierarchy & modular org · 3.2 Slash commands & skills · 3.3 Path-specific rules · 3.4 Plan mode vs direct execution · 3.5 Iterative refinement · 3.6 CI/CD integration |
| 4 — Prompt Engineering & Structured Output (20%) | 4.1 Explicit criteria · 4.2 Few-shot prompting · 4.3 Structured output via tool use + JSON schema · 4.4 Validation, retry & feedback loops · 4.5 Batch processing · 4.6 Multi-instance & multi-pass review |
| 5 — Context Management & Reliability (15%) | 5.1 Preserve context over long interactions · 5.2 Escalation & ambiguity resolution · 5.3 Error propagation across agents · 5.4 Large-codebase exploration context · 5.5 Human review & confidence calibration · 5.6 Information provenance & multi-source synthesis |

Total: 7 + 5 + 6 + 6 + 6 = **30**.

## Components

### 1. `syllabus/domains/` — reference content

Five files, replacing `exam_detail.md`:

```
syllabus/domains/
  README.md                  # index + "Techniques & products" tag list
  domain-1-agentic.md
  domain-2-tools-mcp.md
  domain-3-claude-code.md
  domain-4-prompt-output.md
  domain-5-context.md
```

Each domain file:

```markdown
# Domain N: <Name> (<weight>%)

## N.M <Subdomain title>

**Knowledge of**
- … (verbatim from exam_detail.md)

**Skills in**
- … (verbatim from exam_detail.md)
```

Content is moved verbatim from `exam_detail.md` (the `ﬁ`/`ﬂ` ligatures in the
source are normalized to plain `fi`/`fl` while moving). `README.md` carries the
`Techniques & products` list and links to each domain file.

### 2. `syllabus/CCA-F.md` — re-aligned checklist

The five `## Domain N` sections each become a checklist of that domain's
subdomains, one box per subdomain, each linking into the detail file:

```markdown
## Domain 1: Agentic Architecture & Orchestration (27%)

- [ ] [1.1 Agentic loops](domains/domain-1-agentic.md#11-design-and-implement-agentic-loops-for-autonomous-task-execution) — loop lifecycle, `stop_reason`, model-driven vs hardcoded, anti-patterns
- [ ] [1.2 Multi-agent coordinator–subagent](domains/domain-1-agentic.md#12-…) — hub-and-spoke, isolated context, dynamic selection, iterative refinement
- …
```

The header/checkbox format the script parses is preserved. The intro text is
updated to explain the new subdomain structure and the link into `domains/`.

### 3. `members/_TEMPLATE/progress.md` — mirror

Same 30-subdomain checklist (without the detail-link clutter is acceptable, but
keeping the links is fine), under the same `## Domain N` headers.

### 4. `scripts/update_progress.py` — subdomain breakdown

Additive change. Existing behavior (parse boxes per `## Domain N`, render the
5-column group table between the `PROGRESS:START/END` markers) is unchanged.

New: while parsing each member's `progress.md`, capture each checkbox's **label
text and state** per domain (not just counts). After the group table, render a
per-member collapsible breakdown:

```markdown
<details>
<summary>jimmyli — 1.1 done · D1 29% · overall 10%</summary>

**Domain 1 — Agentic (29%)**
- ✅ 1.1 Agentic loops
- ✅ 1.2 Multi-agent coordinator–subagent
- ⬜ 1.3 Subagent invocation & context passing
- …
</details>
```

The breakdown is written between new `<!-- BREAKDOWN:START -->` /
`<!-- BREAKDOWN:END -->` markers added to `PROGRESS.md`, so it regenerates
independently of the group table. Labels come from each member's own
`progress.md` checkbox text — no second list to maintain.

### 5. Migration of existing progress

jimmyli's current ticks map onto new subdomains:

| Old (ticked) | New subdomain |
|--------------|---------------|
| Agentic loop lifecycle | 1.1 |
| Loop anti-patterns | 1.1 (same subdomain) |
| Multi-agent orchestration | 1.2 |
| Tool interface design | 2.1 |

Result: **1.1, 1.2, 2.1** ticked; all other subdomain rows start unchecked.

## Data flow

```
syllabus/domains/*.md  (reference, human-read)
        ▲ links
syllabus/CCA-F.md  (authoritative 30-subdomain checklist)
        │ copied by each member
members/<you>/progress.md  (per-member ticks)
        │ parsed by
scripts/update_progress.py
        │ writes
PROGRESS.md  (group domain table + per-member subdomain breakdown)
```

## Error handling / edge cases

- Script must not crash if a member's `progress.md` has a domain with zero boxes
  (already handled by `pct()` returning `—`).
- If `PROGRESS.md` lacks the new `BREAKDOWN` markers, the script appends the
  block once (or errors with a clear message) rather than silently dropping it.
- Ligature normalization (`ﬁ`→`fi`, `ﬂ`→`fl`) applied when moving content so the
  detail files are greppable.

## Testing

- `python scripts/update_progress.py` runs clean; the 5-column group table is
  byte-identical to the pre-change output for the same ticks.
- The per-member breakdown lists exactly 30 subdomains (7/5/6/6/6) per member.
- jimmyli's breakdown shows 1.1, 1.2, 2.1 as ✅ and the rest as ⬜; D1 = 2/7,
  D2 = 1/5, others 0.
- Every subdomain link in `CCA-F.md` resolves to a real anchor in `domains/`.

## Out of scope (YAGNI)

- Bullet-level (Knowledge/Skills) checkboxes — binary per-subdomain is enough.
- Partial/“in-progress” per-subdomain states beyond ✅/⬜.
- Per-member separate `report.md` files — one `PROGRESS.md` holds both levels.
- Changing exam format figures (60q/120min) — tracked separately.
