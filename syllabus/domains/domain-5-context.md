# Domain 5: Context Management & Reliability (15%)

> Reference detail for the [CCA-F checklist](../CCA-F.md). Source: official study guide skills breakdown.

## 推荐阅读

**考试权重：15%**（概念会渗透到其他 Domain，勿跳过）

### 本 Domain 总览

| 类型 | 资源 | 说明 |
|------|------|------|
| 课程 | [Claude Code 101](https://anthropic.skilljar.com/claude-code-101) | `/compact`、`/clear`、`/context` — 覆盖 5.1、5.4 |
| 课程 | [Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action) | Context management、large codebase — 覆盖 5.4 |
| 课程 | [Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api) | Long context、conversation management — 覆盖 5.1–5.3 |
| 课程 | [Introduction to subagents](https://anthropic.skilljar.com/introduction-to-subagents) | Context 隔离、delegation — 覆盖 5.3–5.6 |
| 文档 | [Memory / CLAUDE.md](https://docs.claude.com/en/docs/claude-code/memory) | 持久记忆、`/memory` |
| 文档 | [How the agent loop works](https://code.claude.com/docs/en/agent-sdk/agent-loop) | `PreCompact` hook、compaction |
| 文档 | [Subagents in the SDK](https://code.claude.com/docs/en/agent-sdk/subagents) | Context budget、structured handoff |
| 文档 | [Prompt engineering](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview) | Escalation few-shot、ambiguity |
| 文档 | [Structured outputs (SDK)](https://code.claude.com/docs/en/agent-sdk/structured-outputs) | Confidence、field-level routing |
| 刷题 | [CertSafari — Domain 5](https://www.certsafari.com/anthropic/claude-certified-architect) | 选 Domain Mode → Context Management |

**建议学习顺序：** 5.1 → 5.4 → 5.3 → 5.2 → 5.6 → 5.5

### 按子主题

#### [5.1 Long-context preservation](#51-long-context-preservation)

- 课程：[Claude Code 101](https://anthropic.skilljar.com/claude-code-101) — context window 管理
- 课程：[Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api) — long context 策略
- 文档：[How the agent loop works](https://code.claude.com/docs/en/agent-sdk/agent-loop) — `PreCompact`、tool result 累积
- 文档：[Memory](https://docs.claude.com/en/docs/claude-code/memory) — 持久 case facts
- 考点速记："lost in the middle"；progressive summarization 丢数字/日期；trim verbose tool output

#### [5.2 Escalation and ambiguity](#52-escalation-and-ambiguity)

- 课程：[Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api) — escalation 设计
- 文档：[Prompt engineering](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview) — few-shot escalation 示例
- 考点速记：客户明确要求人工 → 立即 escalate；policy gap → escalate；多 match → 要 ID 勿 heuristic 选

#### [5.3 Error propagation](#53-error-propagation)

- 课程：[Introduction to subagents](https://anthropic.skilljar.com/introduction-to-subagents) — obstacle reporting
- 文档：[Subagents in the SDK](https://code.claude.com/docs/en/agent-sdk/subagents) — 仅 final message 回传 parent
- 文档：[MCP Tools spec](https://modelcontextprotocol.io/docs/concepts/tools) — 结构化错误 vs 空结果
- 考点速记：返回 failure type + partial results + alternatives；subagent 本地恢复 transient；勿 silent suppress

#### [5.4 Large-codebase context](#54-large-codebase-context)

- 课程：[Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action) — 大型代码库探索
- 课程：[Claude Code 101](https://anthropic.skilljar.com/claude-code-101) — `/compact` 实战
- 文档：[Claude Code overview](https://docs.claude.com/en/docs/claude-code/overview) — subagent 委派探索
- 考点速记：scratchpad 文件持久化发现；crash recovery manifest；phase 间 inject summary 再 spawn subagent

#### [5.5 Human review and confidence](#55-human-review-and-confidence)

- 课程：[Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api) — confidence calibration
- 文档：[Structured outputs (SDK)](https://code.claude.com/docs/en/agent-sdk/structured-outputs) — field-level confidence
- 考点速记：aggregate 97% 可能掩盖某 doc type 差；stratified sampling；按 document type / field 分析准确率

#### [5.6 Information provenance](#56-information-provenance)

- 课程：[Introduction to subagents](https://anthropic.skilljar.com/introduction-to-subagents) — structured output 回传
- 文档：[Subagents in the SDK](https://code.claude.com/docs/en/agent-sdk/subagents) — metadata 与 attribution
- 考点速记：claim-source mapping 贯穿 synthesis；冲突统计 annotate 勿随意选一；日期防 temporal misread

---

## 5.1 Long-context preservation

*Official skill: Manage conversation context to preserve critical information across long interactions*

**Knowledge of**

- Progressive summarization risks: condensing numerical values, percentages, dates, and customer-stated expectations into vague summaries
- The "lost in the middle" effect: models reliably process information at the beginning and end of long inputs but may omit findings from middle sections
- How tool results accumulate in context and consume tokens disproportionately to their relevance (e.g., 40+ fields per order lookup when only 5 are relevant)
- The importance of passing complete conversation history in subsequent API requests to maintain conversational coherence

**Skills in**

- Extracting transactional facts (amounts, dates, order numbers, statuses) into a persistent "case facts" block included in each prompt, outside summarized history
- Extracting and persisting structured issue data (order IDs, amounts, statuses) into a separate context layer for multi-issue sessions
- Trimming verbose tool outputs to only relevant fields before they accumulate in context (e.g., keeping only return-relevant fields from order lookups)
- Placing key findings summaries at the beginning of aggregated inputs and organizing detailed results with explicit section headers to mitigate position effects
- Requiring subagents to include metadata (dates, source locations, methodological context) in structured outputs to support accurate downstream synthesis
- Modifying upstream agents to return structured data (key facts, citations, relevance scores) instead of verbose content and reasoning chains when downstream agents have limited context budgets

## 5.2 Escalation and ambiguity

*Official skill: Design effective escalation and ambiguity resolution patterns*

**Knowledge of**

- Appropriate escalation triggers: customer requests for a human, policy exceptions/gaps (not just complex cases), and inability to make meaningful progress
- The distinction between escalating immediately when a customer explicitly demands it versus offering to resolve when the issue is straightforward
- Why sentiment-based escalation and self-reported confidence scores are unreliable proxies for actual case complexity
- How multiple customer matches require clarification (requesting additional identifiers) rather than heuristic selection

**Skills in**

- Adding explicit escalation criteria with few-shot examples to the system prompt demonstrating when to escalate versus resolve autonomously
- Honoring explicit customer requests for human agents immediately without first attempting investigation
- Acknowledging frustration while offering resolution when the issue is within the agent's capability, escalating only if the customer reiterates their preference
- Escalating when policy is ambiguous or silent on the customer's specific request (e.g., competitor price matching when policy only addresses own-site adjustments)
- Instructing the agent to ask for additional identifiers when tool results return multiple matches, rather than selecting based on heuristics

## 5.3 Error propagation

*Official skill: Implement error propagation strategies across multi-agent systems*

**Knowledge of**

- Structured error context (failure type, attempted query, partial results, alternative approaches) as enabling intelligent coordinator recovery decisions
- The distinction between access failures (timeouts needing retry decisions) and valid empty results (successful queries with no matches)
- Why generic error statuses ("search unavailable") hide valuable context from the coordinator
- Why silently suppressing errors (returning empty results as success) or terminating entire workflows on single failures are both anti-patterns

**Skills in**

- Returning structured error context including failure type, what was attempted, partial results, and potential alternatives to enable coordinator recovery
- Distinguishing access failures from valid empty results in error reporting so the coordinator can make appropriate decisions
- Having subagents implement local recovery for transient failures and only propagate errors they cannot resolve, including what was attempted and partial results
- Structuring synthesis output with coverage annotations indicating which findings are well-supported versus which topic areas have gaps due to unavailable sources

## 5.4 Large-codebase context

*Official skill: Manage context effectively in large codebase exploration*

**Knowledge of**

- Context degradation in extended sessions: models start giving inconsistent answers and referencing "typical patterns" rather than specific classes discovered earlier
- The role of scratchpad files for persisting key findings across context boundaries
- Subagent delegation for isolating verbose exploration output while the main agent coordinates high-level understanding
- Structured state persistence for crash recovery: each agent exports state to a known location, and the coordinator loads a manifest on resume

**Skills in**

- Spawning subagents to investigate specific questions (e.g., "find all test files," "trace refund flow dependencies") while the main agent preserves high-level coordination
- Having agents maintain scratchpad files recording key findings, referencing them for subsequent questions to counteract context degradation
- Summarizing key findings from one exploration phase before spawning sub-agents for the next phase, injecting summaries into initial context
- Designing crash recovery using structured agent state exports (manifests) that the coordinator loads on resume and injects into agent prompts
- Using /compact to reduce context usage during extended exploration sessions when context fills with verbose discovery output

## 5.5 Human review and confidence

*Official skill: Design human review workflows and confidence calibration*

**Knowledge of**

- The risk that aggregate accuracy metrics (e.g., 97% overall) may mask poor performance on specific document types or fields
- Stratified random sampling for measuring error rates in high-confidence extractions and detecting novel error patterns
- Field-level confidence scores calibrated using labeled validation sets for routing review attention
- The importance of validating accuracy by document type and field segment before automating high-confidence extractions

**Skills in**

- Implementing stratified random sampling of high-confidence extractions for ongoing error rate measurement and novel pattern detection
- Analyzing accuracy by document type and field to verify consistent performance across all segments before reducing human review
- Having models output field-level confidence scores, then calibrating review thresholds using labeled validation sets
- Routing extractions with low model confidence or ambiguous/contradictory source documents to human review, prioritizing limited reviewer capacity

## 5.6 Information provenance

*Official skill: Preserve information provenance and handle uncertainty in multi-source synthesis*

**Knowledge of**

- How source attribution is lost during summarization steps when findings are compressed without preserving claim-source mappings
- The importance of structured claim-source mappings that the synthesis agent must preserve and merge when combining findings
- How to handle conflicting statistics from credible sources: annotating conflicts with source attribution rather than arbitrarily selecting one value
- Temporal data: requiring publication/collection dates in structured outputs to prevent temporal differences from being misinterpreted as contradictions

**Skills in**

- Requiring subagents to output structured claim-source mappings (source URLs, document names, relevant excerpts) that downstream agents preserve through synthesis
- Structuring reports with explicit sections distinguishing well-established findings from contested ones, preserving original source characterizations and methodological context
- Completing document analysis with conflicting values included and explicitly annotated, letting the coordinator decide how to reconcile before passing to synthesis
- Requiring subagents to include publication or data collection dates in structured outputs to enable correct temporal interpretation
- Rendering different content types appropriately in synthesis outputs—financial data as tables, news as prose, technical findings as structured lists—rather than converting everything to a uniform format
