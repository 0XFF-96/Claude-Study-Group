# Exam Detail Folder + Subdomain Reporting Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Split `exam_detail.md` into per-domain reference files under `syllabus/domains/`, re-align the trackable checklist to the 30 official subdomains, and extend `update_progress.py` to render a per-member subdomain breakdown in `PROGRESS.md`.

**Architecture:** Reference content lives in five `syllabus/domains/domain-N-*.md` files (one `## N.M` section per subdomain, with verbatim *Knowledge of* / *Skills in* bullets). The authoritative checklist `syllabus/CCA-F.md` and each member's `progress.md` carry one `- [ ]` per subdomain (30 total), grouped under the existing `## Domain N` headers. `scripts/update_progress.py` keeps the domain-level group table and additionally emits a collapsible per-member subdomain breakdown between new `BREAKDOWN` markers.

**Tech Stack:** Markdown; Python 3 standard library only (no third-party deps); plain-`assert` test runnable with `python3`.

**Branch:** `exam-detail-folder` (already created off `main`; the design spec is already committed here).

---

## Reference: the 30 subdomains, short titles, and anchors

Domain files use **short** `## N.M <title>` headings (keeps GitHub anchors short and matches checklist labels). Anchors below are what GitHub generates and what `CCA-F.md` links must use.

| Subdomain (short title) | Anchor in its domain file |
|---|---|
| 1.1 Agentic loops | `#11-agentic-loops` |
| 1.2 Multi-agent orchestration | `#12-multi-agent-orchestration` |
| 1.3 Subagent invocation | `#13-subagent-invocation` |
| 1.4 Workflow enforcement and handoff | `#14-workflow-enforcement-and-handoff` |
| 1.5 Agent SDK hooks | `#15-agent-sdk-hooks` |
| 1.6 Task decomposition | `#16-task-decomposition` |
| 1.7 Session state | `#17-session-state` |
| 2.1 Tool interface design | `#21-tool-interface-design` |
| 2.2 Structured MCP errors | `#22-structured-mcp-errors` |
| 2.3 Tool distribution and tool_choice | `#23-tool-distribution-and-tool_choice` |
| 2.4 MCP server integration | `#24-mcp-server-integration` |
| 2.5 Built-in tools | `#25-built-in-tools` |
| 3.1 CLAUDE.md hierarchy | `#31-claudemd-hierarchy` |
| 3.2 Slash commands and skills | `#32-slash-commands-and-skills` |
| 3.3 Path-specific rules | `#33-path-specific-rules` |
| 3.4 Plan mode vs direct execution | `#34-plan-mode-vs-direct-execution` |
| 3.5 Iterative refinement | `#35-iterative-refinement` |
| 3.6 CI/CD integration | `#36-cicd-integration` |
| 4.1 Explicit criteria | `#41-explicit-criteria` |
| 4.2 Few-shot prompting | `#42-few-shot-prompting` |
| 4.3 Structured output | `#43-structured-output` |
| 4.4 Validation, retry, and feedback loops | `#44-validation-retry-and-feedback-loops` |
| 4.5 Batch processing | `#45-batch-processing` |
| 4.6 Multi-pass review | `#46-multi-pass-review` |
| 5.1 Long-context preservation | `#51-long-context-preservation` |
| 5.2 Escalation and ambiguity | `#52-escalation-and-ambiguity` |
| 5.3 Error propagation | `#53-error-propagation` |
| 5.4 Large-codebase context | `#54-large-codebase-context` |
| 5.5 Human review and confidence | `#55-human-review-and-confidence` |
| 5.6 Information provenance | `#56-information-provenance` |

**Content-move transformation** (applied in Tasks 1–5). For each subdomain in the source `exam_detail.md`:

1. Source heading line `Subdomain N.M: <full statement>` becomes two lines:
   ```markdown
   ## N.M <short title>

   *Official skill: <full statement>*
   ```
2. Source `Knowledge of:` becomes `**Knowledge of**` (its bullet list follows, unchanged).
3. Source `Skills in:` becomes `**Skills in**` (its bullet list follows, unchanged).
4. Normalize ligatures throughout the moved text: `ﬁ` → `fi`, `ﬂ` → `fl` (the source uses them in words like "ﬂow", "conﬁguration", "speciﬁc").
5. Bullet text is otherwise **verbatim** from the source.

---

## Task 1: Create `syllabus/domains/domain-1-agentic.md`

**Files:**
- Create: `syllabus/domains/domain-1-agentic.md`
- Source: `exam_detail.md` lines 5–107 (subdomains 1.1–1.7)

- [ ] **Step 1: Create the file with the domain header and subdomain 1.1 (worked example)**

Start the file with:

```markdown
# Domain 1: Agentic Architecture & Orchestration (27%)

> Reference detail for the [CCA-F checklist](../CCA-F.md). Source: official study guide skills breakdown.

## 1.1 Agentic loops

*Official skill: Design and implement agentic loops for autonomous task execution*

**Knowledge of**

- The agentic loop lifecycle: sending requests to Claude, inspecting stop_reason ("tool_use" vs "end_turn"), executing requested tools, and returning results for the next iteration
- How tool results are appended to conversation history so the model can reason about the next action
- The distinction between model-driven decision-making (Claude reasons about which tool to call next based on context) and pre-configured decision trees or tool sequences

**Skills in**

- Implementing agentic loop control flow that continues when stop_reason is "tool_use" and terminates when stop_reason is "end_turn"
- Adding tool results to conversation context between iterations so the model can incorporate new information into its reasoning
- Avoiding anti-patterns such as parsing natural language signals to determine loop termination, setting arbitrary iteration caps as the primary stopping mechanism, or checking for assistant text content as a completion indicator
```

(Note: ligatures already normalized above — `flow`, `pre-configured`.)

- [ ] **Step 2: Append subdomains 1.2–1.7**

Apply the transformation rules to source lines 19–107. Use these short titles:
- `## 1.2 Multi-agent orchestration` — official: "Orchestrate multi-agent systems with coordinator-subagent patterns" (source 19–33)
- `## 1.3 Subagent invocation` — official: "Configure subagent invocation, context passing, and spawning" (source 35–49)
- `## 1.4 Workflow enforcement and handoff` — official: "Implement multi-step workflows with enforcement and handoff patterns" (source 51–63)
- `## 1.5 Agent SDK hooks` — official: "Apply Agent SDK hooks for tool call interception and data normalization" (source 65–77)
- `## 1.6 Task decomposition` — official: "Design task decomposition strategies for complex workflows" (source 79–91)
- `## 1.7 Session state` — official: "Manage session state, resumption, and forking" (source 93–107)

- [ ] **Step 3: Verify ligatures are gone**

Run: `grep -nP '[\x{fb00}-\x{fb06}]' syllabus/domains/domain-1-agentic.md`
Expected: no output (exit 1).

- [ ] **Step 4: Verify subdomain count**

Run: `grep -c '^## ' syllabus/domains/domain-1-agentic.md`
Expected: `7`

- [ ] **Step 5: Commit**

```bash
git add syllabus/domains/domain-1-agentic.md
git commit -m "docs: add domain 1 reference file (split from exam_detail)"
```

---

## Task 2: Create `syllabus/domains/domain-2-tools-mcp.md`

**Files:**
- Create: `syllabus/domains/domain-2-tools-mcp.md`
- Source: `exam_detail.md` lines 109–191 (subdomains 2.1–2.5)

- [ ] **Step 1: Create the file**

Header:

```markdown
# Domain 2: Tool Design & MCP Integration (18%)

> Reference detail for the [CCA-F checklist](../CCA-F.md). Source: official study guide skills breakdown.
```

Then apply the transformation rules to source lines 110–191 with these short titles:
- `## 2.1 Tool interface design` — official: "Design effective tool interfaces with clear descriptions and boundaries" (source 110–124)
- `## 2.2 Structured MCP errors` — official: "Implement structured error responses for MCP tools" (source 126–140)
- `## 2.3 Tool distribution and tool_choice` — official: "Distribute tools appropriately across agents and configure tool choice" (source 142–157)
- `## 2.4 MCP server integration` — official: "Integrate MCP servers into Claude Code and agent workflows" (source 159–174)
- `## 2.5 Built-in tools` — official: "Select and apply built-in tools (Read, Write, Edit, Bash, Grep, Glob) effectively" (source 176–191)

- [ ] **Step 2: Verify ligatures gone and count**

Run: `grep -nP '[\x{fb00}-\x{fb06}]' syllabus/domains/domain-2-tools-mcp.md; grep -c '^## ' syllabus/domains/domain-2-tools-mcp.md`
Expected: no ligature matches; count `5`

- [ ] **Step 3: Commit**

```bash
git add syllabus/domains/domain-2-tools-mcp.md
git commit -m "docs: add domain 2 reference file (split from exam_detail)"
```

---

## Task 3: Create `syllabus/domains/domain-3-claude-code.md`

**Files:**
- Create: `syllabus/domains/domain-3-claude-code.md`
- Source: `exam_detail.md` lines 193–289 (subdomains 3.1–3.6)

- [ ] **Step 1: Create the file**

Header:

```markdown
# Domain 3: Claude Code Configuration & Workflows (20%)

> Reference detail for the [CCA-F checklist](../CCA-F.md). Source: official study guide skills breakdown.
```

Apply the transformation to source lines 194–289 with these short titles:
- `## 3.1 CLAUDE.md hierarchy` — official: "Configure CLAUDE.md files with appropriate hierarchy, scoping, and modular organization" (source 194–208)
- `## 3.2 Slash commands and skills` — official: "Create and configure custom slash commands and skills" (source 210–225)
- `## 3.3 Path-specific rules` — official: "Apply path-specific rules for conditional convention loading" (source 227–239)
- `## 3.4 Plan mode vs direct execution` — official: "Determine when to use plan mode vs direct execution" (source 241–255)
- `## 3.5 Iterative refinement` — official: "Apply iterative refinement techniques for progressive improvement" (source 257–272)
- `## 3.6 CI/CD integration` — official: "Integrate Claude Code into CI/CD pipelines" (source 274–289)

- [ ] **Step 2: Verify ligatures gone and count**

Run: `grep -nP '[\x{fb00}-\x{fb06}]' syllabus/domains/domain-3-claude-code.md; grep -c '^## ' syllabus/domains/domain-3-claude-code.md`
Expected: no ligature matches; count `6`

- [ ] **Step 3: Commit**

```bash
git add syllabus/domains/domain-3-claude-code.md
git commit -m "docs: add domain 3 reference file (split from exam_detail)"
```

---

## Task 4: Create `syllabus/domains/domain-4-prompt-output.md`

**Files:**
- Create: `syllabus/domains/domain-4-prompt-output.md`
- Source: `exam_detail.md` lines 291–385 (subdomains 4.1–4.6)

- [ ] **Step 1: Create the file**

Header:

```markdown
# Domain 4: Prompt Engineering & Structured Output (20%)

> Reference detail for the [CCA-F checklist](../CCA-F.md). Source: official study guide skills breakdown.
```

Apply the transformation to source lines 292–385 with these short titles:
- `## 4.1 Explicit criteria` — official: "Design prompts with explicit criteria to improve precision and reduce false positives" (source 292–304)
- `## 4.2 Few-shot prompting` — official: "Apply few-shot prompting to improve output consistency and quality" (source 306–321)
- `## 4.3 Structured output` — official: "Enforce structured output using tool use and JSON schemas" (source 323–339)
- `## 4.4 Validation, retry, and feedback loops` — official: "Implement validation, retry, and feedback loops for extraction quality" (source 341–355)
- `## 4.5 Batch processing` — official: "Design efficient batch processing strategies" (source 357–371)
- `## 4.6 Multi-pass review` — official: "Design multi-instance and multi-pass review architectures" (source 373–385)

- [ ] **Step 2: Verify ligatures gone and count**

Run: `grep -nP '[\x{fb00}-\x{fb06}]' syllabus/domains/domain-4-prompt-output.md; grep -c '^## ' syllabus/domains/domain-4-prompt-output.md`
Expected: no ligature matches; count `6`

- [ ] **Step 3: Commit**

```bash
git add syllabus/domains/domain-4-prompt-output.md
git commit -m "docs: add domain 4 reference file (split from exam_detail)"
```

---

## Task 5: Create `syllabus/domains/domain-5-context.md`

**Files:**
- Create: `syllabus/domains/domain-5-context.md`
- Source: `exam_detail.md` lines 387–487 (subdomains 5.1–5.6)

- [ ] **Step 1: Create the file**

Header:

```markdown
# Domain 5: Context Management & Reliability (15%)

> Reference detail for the [CCA-F checklist](../CCA-F.md). Source: official study guide skills breakdown.
```

Apply the transformation to source lines 388–487 with these short titles:
- `## 5.1 Long-context preservation` — official: "Manage conversation context to preserve critical information across long interactions" (source 388–404)
- `## 5.2 Escalation and ambiguity` — official: "Design effective escalation and ambiguity resolution patterns" (source 406–421)
- `## 5.3 Error propagation` — official: "Implement error propagation strategies across multi-agent systems" (source 423–437)
- `## 5.4 Large-codebase context` — official: "Manage context effectively in large codebase exploration" (source 439–454)
- `## 5.5 Human review and confidence` — official: "Design human review workflows and confidence calibration" (source 456–470)
- `## 5.6 Information provenance` — official: "Preserve information provenance and handle uncertainty in multi-source synthesis" (source 472–487)

- [ ] **Step 2: Verify ligatures gone and count**

Run: `grep -nP '[\x{fb00}-\x{fb06}]' syllabus/domains/domain-5-context.md; grep -c '^## ' syllabus/domains/domain-5-context.md`
Expected: no ligature matches; count `6`

- [ ] **Step 3: Commit**

```bash
git add syllabus/domains/domain-5-context.md
git commit -m "docs: add domain 5 reference file (split from exam_detail)"
```

---

## Task 6: Create `syllabus/domains/README.md` (index + techniques list)

**Files:**
- Create: `syllabus/domains/README.md`
- Source for techniques list: `exam_detail.md` lines 489–545

- [ ] **Step 1: Write the index**

```markdown
# CCA-F Domain Reference

Detailed skills breakdown for each domain, split from the official study guide.
Tick your progress in [`../CCA-F.md`](../CCA-F.md); each checklist item links into
the matching `## N.M` section below.

| Domain | Weight | File |
|--------|--------|------|
| 1 — Agentic Architecture & Orchestration | 27% | [domain-1-agentic.md](domain-1-agentic.md) |
| 2 — Tool Design & MCP Integration | 18% | [domain-2-tools-mcp.md](domain-2-tools-mcp.md) |
| 3 — Claude Code Configuration & Workflows | 20% | [domain-3-claude-code.md](domain-3-claude-code.md) |
| 4 — Prompt Engineering & Structured Output | 20% | [domain-4-prompt-output.md](domain-4-prompt-output.md) |
| 5 — Context Management & Reliability | 15% | [domain-5-context.md](domain-5-context.md) |

## Techniques & products referenced

Claude Code · Claude Agent SDK · Claude API · Model Context Protocol (MCP) ·
Agentic loops · Multi-agent systems · Subagents · Task tool · Agent SDK hooks ·
Tool interfaces · Built-in tools (Read, Write, Edit, Bash, Grep, Glob) ·
CLAUDE.md · Slash commands · Skills · Path-specific rules · Plan mode ·
Direct execution · Iterative refinement · CI/CD pipelines · Prompt engineering ·
Few-shot prompting · Structured output · JSON schemas · Validation · Retry loops ·
Feedback loops · Message Batches API · Multi-instance review architectures ·
Multi-pass review architectures · Conversation context management ·
Progressive summarization · "Lost in the middle" effect · Escalation patterns ·
Ambiguity resolution patterns · Error propagation strategies · Scratchpad files ·
Human review workflows · Confidence calibration · Information provenance ·
Multi-source synthesis · YAML frontmatter · Glob patterns · `stop_reason` ·
`isError` flag · `tool_choice` · `custom_id` · `AgentDefinition` · `PostToolUse` hook ·
`fork_session` · `--resume` flag · `--print` flag · `--output-format json` flag ·
`--json-schema` flag · `/memory` command · `/compact` command
```

- [ ] **Step 2: Commit**

```bash
git add syllabus/domains/README.md
git commit -m "docs: add domains/ index and techniques list"
```

---

## Task 7: Delete `exam_detail.md`

**Files:**
- Delete: `exam_detail.md`

- [ ] **Step 1: Confirm no references remain**

Run: `grep -rn 'exam_detail' --include='*.md' --include='*.py' . | grep -v docs/superpowers`
Expected: no output (the only mentions are in this plan/spec under `docs/superpowers`). If any appear (e.g. README repo-layout table), note them — Task 10 updates README; fix others now.

- [ ] **Step 2: Delete and commit**

```bash
git rm exam_detail.md
git commit -m "docs: remove exam_detail.md (content moved to syllabus/domains/)"
```

---

## Task 8: Re-align `syllabus/CCA-F.md` checklist to 30 subdomains

**Files:**
- Modify: `syllabus/CCA-F.md` (replace the five `## Domain N` sections, lines 22–70)

- [ ] **Step 1: Replace the five domain sections**

Replace everything from `## Domain 1:` to end-of-file with exactly:

```markdown
## Domain 1: Agentic Architecture & Orchestration (27%)

- [ ] [1.1 Agentic loops](domains/domain-1-agentic.md#11-agentic-loops) — loop lifecycle, `stop_reason`, model-driven vs hardcoded, anti-patterns
- [ ] [1.2 Multi-agent orchestration](domains/domain-1-agentic.md#12-multi-agent-orchestration) — hub-and-spoke coordinator, isolated context, dynamic selection, iterative refinement
- [ ] [1.3 Subagent invocation](domains/domain-1-agentic.md#13-subagent-invocation) — `Task` tool, explicit context passing, `AgentDefinition`, parallel calls
- [ ] [1.4 Workflow enforcement and handoff](domains/domain-1-agentic.md#14-workflow-enforcement-and-handoff) — programmatic gates vs prompt guidance, structured escalation summaries
- [ ] [1.5 Agent SDK hooks](domains/domain-1-agentic.md#15-agent-sdk-hooks) — `PostToolUse` normalization, tool-call interception for compliance
- [ ] [1.6 Task decomposition](domains/domain-1-agentic.md#16-task-decomposition) — fixed prompt-chaining vs dynamic adaptive, per-file + cross-file passes
- [ ] [1.7 Session state](domains/domain-1-agentic.md#17-session-state) — `--resume`, `fork_session`, resume-vs-fresh-summary tradeoffs

## Domain 2: Tool Design & MCP Integration (18%)

- [ ] [2.1 Tool interface design](domains/domain-2-tools-mcp.md#21-tool-interface-design) — clear descriptions, inputs, edge cases, boundaries; avoid overlap
- [ ] [2.2 Structured MCP errors](domains/domain-2-tools-mcp.md#22-structured-mcp-errors) — `isError`, `errorCategory`, `isRetryable` metadata
- [ ] [2.3 Tool distribution and tool_choice](domains/domain-2-tools-mcp.md#23-tool-distribution-and-tool_choice) — scope tools per agent (4–5 not 18); `auto`/`any`/forced
- [ ] [2.4 MCP server integration](domains/domain-2-tools-mcp.md#24-mcp-server-integration) — `.mcp.json` vs `~/.claude.json`, env-var expansion, MCP resources
- [ ] [2.5 Built-in tools](domains/domain-2-tools-mcp.md#25-built-in-tools) — `Grep`/`Glob`/`Read`/`Write`/`Edit`; incremental codebase understanding

## Domain 3: Claude Code Configuration & Workflows (20%)

- [ ] [3.1 CLAUDE.md hierarchy](domains/domain-3-claude-code.md#31-claudemd-hierarchy) — user vs project vs directory scope, modular `@import`, `/memory`
- [ ] [3.2 Slash commands and skills](domains/domain-3-claude-code.md#32-slash-commands-and-skills) — `.claude/commands/` vs `~/`, `SKILL.md` frontmatter (`context: fork`, `allowed-tools`)
- [ ] [3.3 Path-specific rules](domains/domain-3-claude-code.md#33-path-specific-rules) — `.claude/rules/` YAML `paths` globs for conditional loading
- [ ] [3.4 Plan mode vs direct execution](domains/domain-3-claude-code.md#34-plan-mode-vs-direct-execution) — plan for large/architectural; execute for scoped fixes; `Explore`
- [ ] [3.5 Iterative refinement](domains/domain-3-claude-code.md#35-iterative-refinement) — concrete I/O examples, test-driven iteration, interview pattern
- [ ] [3.6 CI/CD integration](domains/domain-3-claude-code.md#36-cicd-integration) — `-p`/`--print`, `--output-format json` + `--json-schema`, independent review

## Domain 4: Prompt Engineering & Structured Output (20%)

- [ ] [4.1 Explicit criteria](domains/domain-4-prompt-output.md#41-explicit-criteria) — explicit over vague to cut false positives; concrete severity examples
- [ ] [4.2 Few-shot prompting](domains/domain-4-prompt-output.md#42-few-shot-prompting) — consistency, ambiguous-case handling, generalization, less hallucination
- [ ] [4.3 Structured output](domains/domain-4-prompt-output.md#43-structured-output) — tool use + JSON schema; `tool_choice` `auto`/`any`/forced; nullable/enum
- [ ] [4.4 Validation, retry, and feedback loops](domains/domain-4-prompt-output.md#44-validation-retry-and-feedback-loops) — retry-with-error-feedback, when retries won't help, `detected_pattern`
- [ ] [4.5 Batch processing](domains/domain-4-prompt-output.md#45-batch-processing) — Message Batches API (50% cost, ≤24h, no SLA), `custom_id` correlation
- [ ] [4.6 Multi-pass review](domains/domain-4-prompt-output.md#46-multi-pass-review) — independent reviewer vs self-review; per-file local + cross-file passes

## Domain 5: Context Management & Reliability (15%)

- [ ] [5.1 Long-context preservation](domains/domain-5-context.md#51-long-context-preservation) — persistent "case facts", "lost in the middle", trim verbose outputs
- [ ] [5.2 Escalation and ambiguity](domains/domain-5-context.md#52-escalation-and-ambiguity) — explicit triggers, honor human requests, ask for IDs on multiple matches
- [ ] [5.3 Error propagation](domains/domain-5-context.md#53-error-propagation) — structured error context, access-failure vs valid-empty, no silent suppression
- [ ] [5.4 Large-codebase context](domains/domain-5-context.md#54-large-codebase-context) — scratchpad files, subagent delegation, `/compact`, crash-recovery manifests
- [ ] [5.5 Human review and confidence](domains/domain-5-context.md#55-human-review-and-confidence) — stratified sampling, per-type/field accuracy, calibrated routing
- [ ] [5.6 Information provenance](domains/domain-5-context.md#56-information-provenance) — claim-source mappings, annotate conflicts, dates, content-appropriate rendering
```

- [ ] **Step 2: Verify box count and headers**

Run: `grep -c '^- \[ \]' syllabus/CCA-F.md; grep -c '^## Domain' syllabus/CCA-F.md`
Expected: `30` and `5`

- [ ] **Step 3: Verify every link anchor matches a real heading**

Run:
```bash
python3 - <<'PY'
import re, pathlib
root = pathlib.Path("syllabus")
checklist = (root / "CCA-F.md").read_text()
links = re.findall(r"\]\((domains/[^)]+)\)", checklist)
missing = []
for link in links:
    path, _, anchor = link.partition("#")
    text = (root / path).read_text().lower()
    # GitHub anchor: lowercase, drop non-alphanum except space/hyphen, spaces->hyphen
    heads = []
    for line in text.splitlines():
        if line.startswith("## "):
            h = line[3:].strip()
            h = re.sub(r"[^\w\s-]", "", h).replace(" ", "-")
            heads.append(h)
    if anchor not in heads:
        missing.append(link)
print("MISSING:", missing or "none")
PY
```
Expected: `MISSING: none`

- [ ] **Step 4: Commit**

```bash
git add syllabus/CCA-F.md
git commit -m "docs: re-align CCA-F checklist to 30 official subdomains"
```

---

## Task 9: Update member templates and migrate jimmyli's progress

**Files:**
- Modify: `members/_TEMPLATE/progress.md` (replace the five `## Domain N` sections)
- Modify: `members/jimmyli/progress.md` (replace the five `## Domain N` sections, preserving ticks for 1.1, 1.2, 2.1)

- [ ] **Step 1: Replace `_TEMPLATE/progress.md` domain sections**

Keep its intro lines (1–8). Replace the domain sections with the same 30-item checklist body from Task 8 Step 1 (all boxes unchecked, with the `domains/...` links — but the template's links must use `../../syllabus/` prefix). Use this body verbatim:

```markdown
## Domain 1: Agentic Architecture & Orchestration (27%)

- [ ] [1.1 Agentic loops](../../syllabus/domains/domain-1-agentic.md#11-agentic-loops)
- [ ] [1.2 Multi-agent orchestration](../../syllabus/domains/domain-1-agentic.md#12-multi-agent-orchestration)
- [ ] [1.3 Subagent invocation](../../syllabus/domains/domain-1-agentic.md#13-subagent-invocation)
- [ ] [1.4 Workflow enforcement and handoff](../../syllabus/domains/domain-1-agentic.md#14-workflow-enforcement-and-handoff)
- [ ] [1.5 Agent SDK hooks](../../syllabus/domains/domain-1-agentic.md#15-agent-sdk-hooks)
- [ ] [1.6 Task decomposition](../../syllabus/domains/domain-1-agentic.md#16-task-decomposition)
- [ ] [1.7 Session state](../../syllabus/domains/domain-1-agentic.md#17-session-state)

## Domain 2: Tool Design & MCP Integration (18%)

- [ ] [2.1 Tool interface design](../../syllabus/domains/domain-2-tools-mcp.md#21-tool-interface-design)
- [ ] [2.2 Structured MCP errors](../../syllabus/domains/domain-2-tools-mcp.md#22-structured-mcp-errors)
- [ ] [2.3 Tool distribution and tool_choice](../../syllabus/domains/domain-2-tools-mcp.md#23-tool-distribution-and-tool_choice)
- [ ] [2.4 MCP server integration](../../syllabus/domains/domain-2-tools-mcp.md#24-mcp-server-integration)
- [ ] [2.5 Built-in tools](../../syllabus/domains/domain-2-tools-mcp.md#25-built-in-tools)

## Domain 3: Claude Code Configuration & Workflows (20%)

- [ ] [3.1 CLAUDE.md hierarchy](../../syllabus/domains/domain-3-claude-code.md#31-claudemd-hierarchy)
- [ ] [3.2 Slash commands and skills](../../syllabus/domains/domain-3-claude-code.md#32-slash-commands-and-skills)
- [ ] [3.3 Path-specific rules](../../syllabus/domains/domain-3-claude-code.md#33-path-specific-rules)
- [ ] [3.4 Plan mode vs direct execution](../../syllabus/domains/domain-3-claude-code.md#34-plan-mode-vs-direct-execution)
- [ ] [3.5 Iterative refinement](../../syllabus/domains/domain-3-claude-code.md#35-iterative-refinement)
- [ ] [3.6 CI/CD integration](../../syllabus/domains/domain-3-claude-code.md#36-cicd-integration)

## Domain 4: Prompt Engineering & Structured Output (20%)

- [ ] [4.1 Explicit criteria](../../syllabus/domains/domain-4-prompt-output.md#41-explicit-criteria)
- [ ] [4.2 Few-shot prompting](../../syllabus/domains/domain-4-prompt-output.md#42-few-shot-prompting)
- [ ] [4.3 Structured output](../../syllabus/domains/domain-4-prompt-output.md#43-structured-output)
- [ ] [4.4 Validation, retry, and feedback loops](../../syllabus/domains/domain-4-prompt-output.md#44-validation-retry-and-feedback-loops)
- [ ] [4.5 Batch processing](../../syllabus/domains/domain-4-prompt-output.md#45-batch-processing)
- [ ] [4.6 Multi-pass review](../../syllabus/domains/domain-4-prompt-output.md#46-multi-pass-review)

## Domain 5: Context Management & Reliability (15%)

- [ ] [5.1 Long-context preservation](../../syllabus/domains/domain-5-context.md#51-long-context-preservation)
- [ ] [5.2 Escalation and ambiguity](../../syllabus/domains/domain-5-context.md#52-escalation-and-ambiguity)
- [ ] [5.3 Error propagation](../../syllabus/domains/domain-5-context.md#53-error-propagation)
- [ ] [5.4 Large-codebase context](../../syllabus/domains/domain-5-context.md#54-large-codebase-context)
- [ ] [5.5 Human review and confidence](../../syllabus/domains/domain-5-context.md#55-human-review-and-confidence)
- [ ] [5.6 Information provenance](../../syllabus/domains/domain-5-context.md#56-information-provenance)
```

- [ ] **Step 2: Create `members/jimmyli/progress.md` domain sections from the same body, ticking 1.1, 1.2, 2.1**

Keep jimmyli's intro lines (1–8). Use the identical body from Step 1 but change exactly these three lines from `- [ ]` to `- [x]`:
- `- [x] [1.1 Agentic loops](../../syllabus/domains/domain-1-agentic.md#11-agentic-loops)`
- `- [x] [1.2 Multi-agent orchestration](../../syllabus/domains/domain-1-agentic.md#12-multi-agent-orchestration)`
- `- [x] [2.1 Tool interface design](../../syllabus/domains/domain-2-tools-mcp.md#21-tool-interface-design)`

- [ ] **Step 3: Verify counts**

Run:
```bash
echo "TEMPLATE:"; grep -c '^- \[ \]' members/_TEMPLATE/progress.md
echo "jimmyli unchecked / checked:"; grep -c '^- \[ \]' members/jimmyli/progress.md; grep -c '^- \[x\]' members/jimmyli/progress.md
```
Expected: TEMPLATE `30`; jimmyli unchecked `27`, checked `3`.

- [ ] **Step 4: Commit**

```bash
git add members/_TEMPLATE/progress.md members/jimmyli/progress.md
git commit -m "docs: migrate progress checklists to 30-subdomain structure"
```

---

## Task 10: Update repo docs that reference the old structure

**Files:**
- Modify: `README.md` (repo-layout table row for the syllabus)
- Modify: `syllabus/CCA-F.md` intro (explain subdomain links) — only if not already covered

- [ ] **Step 1: Update the README repo-layout table**

In `README.md`, the layout table row currently reads:

```markdown
| [syllabus/CCA-F.md](syllabus/CCA-F.md) | The exam blueprint & master topic checklist |
```

Replace it with these two rows:

```markdown
| [syllabus/CCA-F.md](syllabus/CCA-F.md) | The 30-subdomain master checklist (tick boxes in your own `progress.md`) |
| [syllabus/domains/](syllabus/domains/) | Detailed per-domain reference (Knowledge of / Skills in for each subdomain) |
```

- [ ] **Step 2: Confirm no other stale references**

Run: `grep -rn 'exam_detail\|master topic checklist' --include='*.md' . | grep -v docs/superpowers`
Expected: no output.

- [ ] **Step 3: Commit**

```bash
git add README.md syllabus/CCA-F.md
git commit -m "docs: point README at syllabus/domains reference folder"
```

---

## Task 11: Add the subdomain breakdown to `update_progress.py` (TDD)

**Files:**
- Modify: `scripts/update_progress.py`
- Create: `tests/test_update_progress.py`
- Modify: `PROGRESS.md` (add BREAKDOWN markers)

### Step 1: Write the failing test

- [ ] **Create `tests/test_update_progress.py`**

```python
"""Tests for update_progress subdomain breakdown. Run: python3 tests/test_update_progress.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import update_progress as up  # noqa: E402

SAMPLE = """# My progress

## Domain 1: Agentic
- [x] [1.1 Agentic loops](../../syllabus/domains/domain-1-agentic.md#11-agentic-loops)
- [ ] [1.2 Multi-agent orchestration](../../syllabus/domains/domain-1-agentic.md#12-multi-agent-orchestration)

## Domain 2: Tools
- [x] [2.1 Tool interface design](../../syllabus/domains/domain-2-tools-mcp.md#21-tool-interface-design)
"""


def test_parse_breakdown_returns_labels_and_state(tmp_path):
    p = tmp_path / "progress.md"
    p.write_text(SAMPLE, encoding="utf-8")
    bd = up.parse_breakdown(p)
    assert bd["D1 Agentic"] == [("1.1 Agentic loops", True), ("1.2 Multi-agent orchestration", False)]
    assert bd["D2 Tools/MCP"] == [("2.1 Tool interface design", True)]


def test_render_breakdown_has_details_and_marks(tmp_path):
    p = tmp_path / "progress.md"
    p.write_text(SAMPLE, encoding="utf-8")
    bd = up.parse_breakdown(p)
    out = up.render_breakdown("jimmyli", bd)
    assert "<details>" in out
    assert "✅ 1.1 Agentic loops" in out
    assert "⬜ 1.2 Multi-agent orchestration" in out
    assert "✅ 2.1 Tool interface design" in out


def _run():
    import tempfile
    failures = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            with tempfile.TemporaryDirectory() as d:
                try:
                    fn(Path(d))
                    print(f"PASS {name}")
                except AssertionError as e:
                    failures += 1
                    print(f"FAIL {name}: {e}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(_run())
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `python3 tests/test_update_progress.py`
Expected: FAIL — `AttributeError: module 'update_progress' has no attribute 'parse_breakdown'` (raised as the test errors out; the runner prints a FAIL line).

### Step 3: Implement `parse_breakdown` and `render_breakdown`

- [ ] **Add to `scripts/update_progress.py`** (after the existing `parse_progress` function, ~line 63):

```python
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
    lines = [f"<details>", f"<summary>{summary}</summary>", ""]
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
```

- [ ] **Step 4: Run the test to verify it passes**

Run: `python3 tests/test_update_progress.py`
Expected: `PASS test_parse_breakdown_returns_labels_and_state` and `PASS test_render_breakdown_has_details_and_marks`, exit 0.

- [ ] **Step 5: Commit**

```bash
git add scripts/update_progress.py tests/test_update_progress.py
git commit -m "feat: add subdomain breakdown parsing/rendering to update_progress"
```

### Step 6: Wire the breakdown into `main()` and `PROGRESS.md`

- [ ] **Add BREAKDOWN markers to `PROGRESS.md`**

After the existing `<!-- PROGRESS:END -->` block and the Legend, append:

```markdown

## Per-member subdomain breakdown

<!-- BREAKDOWN:START -->
<!-- BREAKDOWN:END -->
```

- [ ] **Add breakdown constants near the PROGRESS markers (~line 21)**

```python
BD_START = "<!-- BREAKDOWN:START -->"
BD_END = "<!-- BREAKDOWN:END -->"
```

- [ ] **Extend `collect_rows()` to also capture the breakdown.** Change the `rows.append({...})` block to include the parsed breakdown:

```python
        rows.append(
            {
                "name": member.name,
                "target": meta["target"],
                "cells": [pct(*counts[key]) for key, _ in DOMAINS],
                "last": latest_log_date(member / "weekly-log.md"),
                "status": meta["status"],
                "breakdown": parse_breakdown(prog),
            }
        )
```

- [ ] **In `main()`, after the existing PROGRESS block replacement and before `print(table)`, add the breakdown replacement:**

```python
    breakdown_md = "\n".join(render_breakdown(r["name"], r["breakdown"]) for r in rows) or "_No members yet._\n"
    if BD_START in new_content and BD_END in new_content:
        bd_block = f"{BD_START}\n{breakdown_md}{BD_END}"
        new_content = re.sub(
            re.escape(BD_START) + r".*?" + re.escape(BD_END),
            lambda _m: bd_block,
            new_content,
            flags=re.DOTALL,
        )
    else:
        print(f"warning: missing {BD_START}/{BD_END} markers in PROGRESS.md; skipping breakdown", file=sys.stderr)
```

Note: this block reads/writes `new_content` (the variable already built from the PROGRESS-marker substitution earlier in `main()`), so both replacements land in one write.

- [ ] **Step 7: Run the unit tests again (still green)**

Run: `python3 tests/test_update_progress.py`
Expected: both PASS, exit 0.

- [ ] **Step 8: Run the script end-to-end**

Run: `python3 scripts/update_progress.py`
Expected: stderr `Updated PROGRESS.md (1 member(s)).`; `PROGRESS.md` now has a populated `<details>` block for jimmyli between the BREAKDOWN markers showing ✅ for 1.1, 1.2, 2.1 and ⬜ for the rest, with D1 29%, D2 20%, overall 10%.

- [ ] **Step 9: Verify the group table is unchanged in shape**

Run: `sed -n '/PROGRESS:START/,/PROGRESS:END/p' PROGRESS.md`
Expected: the 5-column table still present; jimmyli row shows D1 29%, D2 20%, D3 0%, D4 0%, D5 0% (counts now out of 7/5/6/6/6).

- [ ] **Step 10: Commit**

```bash
git add scripts/update_progress.py PROGRESS.md
git commit -m "feat: render per-member subdomain breakdown in PROGRESS.md"
```

---

## Task 12: Final verification

- [ ] **Step 1: Full check**

Run:
```bash
python3 tests/test_update_progress.py && \
python3 scripts/update_progress.py && \
echo "subdomain files:" && ls syllabus/domains/ && \
echo "checklist boxes:" && grep -c '^- \[' syllabus/CCA-F.md && \
echo "no exam_detail refs:" && ! grep -rn 'exam_detail' --include='*.md' --include='*.py' . | grep -v docs/superpowers
```
Expected: tests PASS; script updates cleanly; 6 entries in `domains/` (5 domain files + README.md); `30` checklist boxes; no stray `exam_detail` references.

- [ ] **Step 2: Push and open PR**

```bash
git push -u origin exam-detail-folder
gh pr create --title "docs: split exam_detail into per-domain folder + subdomain progress reporting" \
  --body "Splits exam_detail.md into syllabus/domains/, re-aligns the checklist to the 30 official subdomains, and adds a per-member subdomain breakdown to PROGRESS.md. See docs/superpowers/specs/2026-06-07-exam-detail-folder-design.md."
```

---

## Self-Review notes

- **Spec coverage:** domains folder (Tasks 1–6), exam_detail deletion (7), re-aligned checklist (8), template + migration (9), README/doc updates (10), script + report (11), verification (12). All spec components covered.
- **Type consistency:** `parse_breakdown` returns `dict[str, list[tuple[str, bool]]]`; `render_breakdown(name, breakdown)` consumes that exact shape; `collect_rows()` stores it under `"breakdown"`; `main()` reads `r["breakdown"]`. Consistent.
- **Anchors:** Task 8 Step 3 validates every checklist link resolves against a real heading before commit, guarding the short-title/anchor mapping.
