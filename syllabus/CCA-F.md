# Claude Certified Architect – Foundations (CCA-F) Syllabus

Authoritative topic checklist for the group. Your personal `members/<you>/progress.md`
is a copy of the five domain sections below — tick boxes there as you learn.

> The `## Domain N` headers and `- [ ]` checkboxes are parsed by `scripts/update_progress.py`.
> Keep the header format intact in your `progress.md`.

**Source:** [CertSafari — Claude Certified Architect (CCA-F)](https://www.certsafari.com/anthropic/claude-certified-architect) (exam guide + practice bank).

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
