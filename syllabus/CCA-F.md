# Claude Certified Architect – Foundations (CCA-F) Syllabus

Authoritative topic checklist for the group. Your personal `members/<you>/progress.md`
is a copy of the five domain sections below — tick boxes there as you learn.

> The `## Domain N` headers and `- [ ]` checkboxes are parsed by `scripts/update_progress.py`.
> Keep the header format intact in your `progress.md`.

**Exam format:** 60 multiple-choice questions · 120 minutes · closed-book (no AI assistance) ·
passing score 720 (scaled 100–1000).

| # | Domain | Weight |
|---|--------|--------|
| 1 | Agentic Architecture & Orchestration | 27% |
| 2 | Tool Design & MCP Integration | 18% |
| 3 | Claude Code Configuration & Workflows | 20% |
| 4 | Prompt Engineering & Structured Output | 20% |
| 5 | Context Management & Reliability | 15% |

---

## Domain 1: Agentic Architecture & Orchestration (27%)

- [ ] Agentic loop lifecycle: inspect `stop_reason` (`tool_use` vs `end_turn`), append tool results, model-driven vs hardcoded sequences
- [ ] Loop anti-patterns: don't parse natural-language signals or use arbitrary iteration caps as the primary stop condition
- [ ] Multi-agent orchestration: hub-and-spoke coordinator, isolated subagent context, dynamic subagent selection by query complexity
- [ ] Iterative refinement loops: coordinator evaluates synthesis for gaps and re-delegates until coverage is sufficient
- [ ] Subagent invocation: `Task` tool (`allowedTools` must include `Task`), explicit context passing, `AgentDefinition`, parallel `Task` calls in one turn
- [ ] Workflow enforcement & handoff: programmatic prerequisite gates vs prompt guidance; structured escalation summaries
- [ ] Agent SDK hooks: `PostToolUse` for data normalization; tool-call interception to enforce compliance (e.g. block refunds > $500)
- [ ] Task decomposition: fixed prompt-chaining vs dynamic adaptive decomposition; per-file + cross-file review passes
- [ ] Session state: `--resume <name>` for named sessions, `fork_session` for branches, resume-vs-fresh-summary tradeoffs

## Domain 2: Tool Design & MCP Integration (18%)

- [ ] Tool interface design: clear descriptions, inputs, edge cases, boundaries; avoid overlapping/ambiguous tools
- [ ] Splitting generic tools into purpose-specific tools with defined input/output contracts
- [ ] Structured MCP errors: `isError` flag, `errorCategory` (transient/validation/business/permission), `isRetryable` metadata
- [ ] Tool distribution & `tool_choice`: scope tools per agent (4–5 not 18); `auto` / `any` / forced selection
- [ ] MCP server integration: `.mcp.json` (project) vs `~/.claude.json` (user), env-var expansion, MCP resources as content catalogs
- [ ] Built-in tools: `Grep` (content) vs `Glob` (paths) vs `Read`/`Write`/`Edit`; `Read`+`Write` fallback when `Edit` anchor isn't unique
- [ ] Incremental codebase understanding: start with `Grep` for entry points, then `Read` to follow imports

## Domain 3: Claude Code Configuration & Workflows (20%)

- [ ] CLAUDE.md hierarchy: user (`~/.claude/`) vs project (`.claude/` / root) vs directory scope; user-level isn't shared via VCS
- [ ] Modular memory: `@import` syntax, `.claude/rules/` topic files, `/memory` to verify what's loaded
- [ ] Custom slash commands & skills: `.claude/commands/` vs `~/`, `SKILL.md` frontmatter (`context: fork`, `allowed-tools`, `argument-hint`)
- [ ] Path-specific rules: `.claude/rules/` YAML `paths` globs for conditional convention loading
- [ ] Plan mode vs direct execution: plan for large/multi-approach/architectural changes; execute for well-scoped fixes; `Explore` subagent
- [ ] Iterative refinement: concrete input/output examples, test-driven iteration, interview pattern, batched vs sequential fixes
- [ ] CI/CD integration: `-p`/`--print`, `--output-format json` + `--json-schema`, CLAUDE.md context, independent review instance

## Domain 4: Prompt Engineering & Structured Output (20%)

- [ ] Explicit criteria over vague instructions to cut false positives; concrete severity definitions with examples
- [ ] Few-shot prompting for consistency, ambiguous-case handling, generalization, and reduced extraction hallucination
- [ ] Structured output via tool use + JSON schemas; `tool_choice` `auto`/`any`/forced; optional (nullable) and enum (`other`/`unclear`) fields
- [ ] Validation, retry & feedback loops: retry-with-error-feedback, recognizing when retries won't help, `detected_pattern` fields
- [ ] Batch processing: Message Batches API (50% cost, ≤24h, no SLA, no mid-request tool calls), `custom_id` correlation
- [ ] Multi-instance & multi-pass review: independent reviewer vs self-review; per-file local + cross-file integration passes

## Domain 5: Context Management & Reliability (15%)

- [ ] Preserve critical info over long context: persistent "case facts" block, the "lost in the middle" effect, trim verbose tool outputs
- [ ] Escalation & ambiguity resolution: explicit triggers, honor human requests immediately, ask for IDs on multiple matches
- [ ] Error propagation across agents: structured error context, access-failure vs valid-empty-result, no silent suppression / no whole-workflow abort
- [ ] Large-codebase context: scratchpad files, subagent delegation, `/compact`, crash-recovery state manifests
- [ ] Human review & confidence calibration: stratified sampling, per-type/field accuracy, calibrated field-level confidence routing
- [ ] Information provenance: claim-source mappings, annotate conflicting sources, publication/collection dates, content-appropriate rendering
