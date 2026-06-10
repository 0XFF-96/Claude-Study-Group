# Domain 1: Agentic Architecture & Orchestration (27%)

> Reference detail for the [CCA-F checklist](../CCA-F.md). Source: official study guide skills breakdown.

## 推荐阅读

**考试权重：27%**（最高，建议最先学）

### 本 Domain 总览

| 类型 | 资源 | 说明 |
|------|------|------|
| 课程 | [Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api) | Agents & workflows、multi-agent、chaining — 覆盖 1.1–1.6 |
| 课程 | [Claude Code 101](https://anthropic.skilljar.com/claude-code-101) | Agentic loop、subagents、hooks 基础 — 覆盖 1.1、1.3–1.5 |
| 课程 | [Introduction to subagents](https://anthropic.skilljar.com/introduction-to-subagents) | Subagent 隔离 context、并行委派 — 覆盖 1.2–1.3 |
| 课程 | [Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action) | Session、resume、高级工作流 — 覆盖 1.7 |
| 文档 | [Agent SDK Overview](https://docs.claude.com/en/api/agent-sdk/overview) | SDK 总览 |
| 文档 | [How the agent loop works](https://code.claude.com/docs/en/agent-sdk/agent-loop) | `stop_reason`、hooks 生命周期 |
| 文档 | [Subagents in the SDK](https://code.claude.com/docs/en/agent-sdk/subagents) | `AgentDefinition`、context 传递 |
| 文档 | [Tool use](https://docs.claude.com/en/docs/build-with-claude/tool-use) | Tool results 回传、loop 基础 |
| 文档 | [Hooks](https://docs.claude.com/en/docs/claude-code/hooks) | `PreToolUse` / `PostToolUse` 拦截 |
| 刷题 | [CertSafari — Domain 1](https://www.certsafari.com/anthropic/claude-certified-architect) | 选 Domain Mode → Agentic Architecture |

**建议学习顺序：** 1.1 → 1.2 → 1.3 → 1.4 → 1.5 → 1.6 → 1.7

### 按子主题

#### [1.1 Agentic loops](#11-agentic-loops)

- 课程：[Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api) — *Agents and workflows* 模块
- 课程：[Claude Code 101](https://anthropic.skilljar.com/claude-code-101) — agentic loop 与 tools 协同
- 文档：[How the agent loop works](https://code.claude.com/docs/en/agent-sdk/agent-loop) — `tool_use` vs `end_turn`
- 文档：[Tool use](https://docs.claude.com/en/docs/build-with-claude/tool-use) — tool results 追加到 conversation history
- 考点速记：循环终止看 `stop_reason`，不要用自然语言或任意 iteration cap 作主停止条件

#### [1.2 Multi-agent orchestration](#12-multi-agent-orchestration)

- 课程：[Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api) — coordinator-subagent、hub-and-spoke
- 课程：[Introduction to subagents](https://anthropic.skilljar.com/introduction-to-subagents) — 隔离 context、coordinator 路由
- 文档：[Subagents in the SDK](https://code.claude.com/docs/en/agent-sdk/subagents) — subagent 不继承 parent history
- 考点速记：所有 subagent 通信经 coordinator；iterative refinement 补 coverage gap

#### [1.3 Subagent invocation](#13-subagent-invocation)

- 课程：[Introduction to subagents](https://anthropic.skilljar.com/introduction-to-subagents) — `/agents`、自定义 subagent
- 文档：[Subagents in the SDK](https://code.claude.com/docs/en/agent-sdk/subagents) — `Agent` tool、`allowedTools` 须含 `Agent`
- 文档：[Agent SDK Overview](https://docs.claude.com/en/api/agent-sdk/overview) — `AgentDefinition` 配置
- 考点速记：context 必须显式写入 prompt；同一 turn 可并行多个 Task/Agent 调用

#### [1.4 Workflow enforcement and handoff](#14-workflow-enforcement-and-handoff)

- 课程：[Claude Code 101](https://anthropic.skilljar.com/claude-code-101) — hooks 与权限
- 文档：[Hooks](https://docs.claude.com/en/docs/claude-code/hooks) — programmatic gate vs prompt guidance
- 文档：[How the agent loop works](https://code.claude.com/docs/en/agent-sdk/agent-loop) — `PreToolUse` 阻断不合规 tool call
- 考点速记：金融/身份验证等确定性合规 → hooks 优于纯 prompt；escalation 需结构化 handoff summary

#### [1.5 Agent SDK hooks](#15-agent-sdk-hooks)

- 课程：[Claude Code 101](https://anthropic.skilljar.com/claude-code-101) — hooks 实战
- 文档：[Hooks](https://docs.claude.com/en/docs/claude-code/hooks) — `PostToolUse` 数据归一化
- 文档：[How the agent loop works](https://code.claude.com/docs/en/agent-sdk/agent-loop) — hook 事件表（`PreToolUse`、`PostToolUse`、`SubagentStop` 等）
- 考点速记：`PostToolUse` 统一 timestamp 格式；拦截超阈值退款等须用 hook 非 prompt

#### [1.6 Task decomposition](#16-task-decomposition)

- 课程：[Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api) — chaining、routing、parallelization
- 文档：[Agent SDK Overview](https://docs.claude.com/en/api/agent-sdk/overview) — 工作流模式
- 考点速记：固定 pipeline → prompt chaining；开放调查 → dynamic decomposition；大 review → per-file + cross-file 两 pass

#### [1.7 Session state](#17-session-state)

- 课程：[Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action) — session 管理
- 文档：[Claude Code overview](https://docs.claude.com/en/docs/claude-code/overview) — `--resume`、`fork_session`
- 文档：[Subagents in the SDK](https://code.claude.com/docs/en/agent-sdk/subagents) — fork 探索分支
- 考点速记：stale tool results → 新 session + summary 优于盲目 resume；resume 后告知文件变更

---

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

## 1.2 Multi-agent orchestration

*Official skill: Orchestrate multi-agent systems with coordinator-subagent patterns*

**Knowledge of**

- Hub-and-spoke architecture where a coordinator agent manages all inter-subagent communication, error handling, and information routing
- How subagents operate with isolated context—they do not inherit the coordinator's conversation history automatically
- The role of the coordinator in task decomposition, delegation, result aggregation, and deciding which subagents to invoke based on query complexity
- Risks of overly narrow task decomposition by the coordinator, leading to incomplete coverage of broad research topics

**Skills in**

- Designing coordinator agents that analyze query requirements and dynamically select which subagents to invoke rather than always routing through the full pipeline
- Partitioning research scope across subagents to minimize duplication (e.g., assigning distinct subtopics or source types to each agent)
- Implementing iterative refinement loops where the coordinator evaluates synthesis output for gaps, re-delegates to search and analysis subagents with targeted queries, and re-invokes synthesis until coverage is sufficient
- Routing all subagent communication through the coordinator for observability, consistent error handling, and controlled information flow

## 1.3 Subagent invocation

*Official skill: Configure subagent invocation, context passing, and spawning*

**Knowledge of**

- The Task tool as the mechanism for spawning subagents, and the requirement that allowedTools must include "Task" for a coordinator to invoke subagents
- That subagent context must be explicitly provided in the prompt—subagents do not automatically inherit parent context or share memory between invocations
- The AgentDefinition configuration including descriptions, system prompts, and tool restrictions for each subagent type
- Fork-based session management for exploring divergent approaches from a shared analysis baseline

**Skills in**

- Including complete findings from prior agents directly in the subagent's prompt (e.g., passing web search results and document analysis outputs to the synthesis subagent)
- Using structured data formats to separate content from metadata (source URLs, document names, page numbers) when passing context between agents to preserve attribution
- Spawning parallel subagents by emitting multiple Task tool calls in a single coordinator response rather than across separate turns
- Designing coordinator prompts that specify research goals and quality criteria rather than step-by-step procedural instructions, to enable subagent adaptability

## 1.4 Workflow enforcement and handoff

*Official skill: Implement multi-step workflows with enforcement and handoff patterns*

**Knowledge of**

- The difference between programmatic enforcement (hooks, prerequisite gates) and prompt-based guidance for workflow ordering
- When deterministic compliance is required (e.g., identity verification before financial operations), prompt instructions alone have a non-zero failure rate
- Structured handoff protocols for mid-process escalation that include customer details, root cause analysis, and recommended actions

**Skills in**

- Implementing programmatic prerequisites that block downstream tool calls until prerequisite steps have completed (e.g., blocking process_refund until get_customer has returned a verified customer ID)
- Decomposing multi-concern customer requests into distinct items, then investigating each in parallel using shared context before synthesizing a unified resolution
- Compiling structured handoff summaries (customer ID, root cause, refund amount, recommended action) when escalating to human agents who lack access to the conversation transcript

## 1.5 Agent SDK hooks

*Official skill: Apply Agent SDK hooks for tool call interception and data normalization*

**Knowledge of**

- Hook patterns (e.g., PostToolUse) that intercept tool results for transformation before the model processes them
- Hook patterns that intercept outgoing tool calls to enforce compliance rules (e.g., blocking refunds above a threshold)
- The distinction between using hooks for deterministic guarantees versus relying on prompt instructions for probabilistic compliance

**Skills in**

- Implementing PostToolUse hooks to normalize heterogeneous data formats (Unix timestamps, ISO 8601, numeric status codes) from different MCP tools before the agent processes them
- Implementing tool call interception hooks that block policy-violating actions (e.g., refunds exceeding $500) and redirect to alternative workflows (e.g., human escalation)
- Choosing hooks over prompt-based enforcement when business rules require guaranteed compliance

## 1.6 Task decomposition

*Official skill: Design task decomposition strategies for complex workflows*

**Knowledge of**

- When to use fixed sequential pipelines (prompt chaining) versus dynamic adaptive decomposition based on intermediate findings
- Prompt chaining patterns that break reviews into sequential steps (e.g., analyze each file individually, then run a cross-file integration pass)
- The value of adaptive investigation plans that generate subtasks based on what is discovered at each step

**Skills in**

- Selecting task decomposition patterns appropriate to the workflow: prompt chaining for predictable multi-aspect reviews, dynamic decomposition for open-ended investigation tasks
- Splitting large code reviews into per-file local analysis passes plus a separate cross-file integration pass to avoid attention dilution
- Decomposing open-ended tasks (e.g., "add comprehensive tests to a legacy codebase") by first mapping structure, identifying high-impact areas, then creating a prioritized plan that adapts as dependencies are discovered

## 1.7 Session state

*Official skill: Manage session state, resumption, and forking*

**Knowledge of**

- Named session resumption using --resume <session-name> to continue a specific prior conversation
- fork_session for creating independent branches from a shared analysis baseline to explore divergent approaches
- The importance of informing the agent about changes to previously analyzed files when resuming sessions after code modifications
- Why starting a new session with a structured summary is more reliable than resuming with stale tool results

**Skills in**

- Using --resume with session names to continue named investigation sessions across work sessions
- Using fork_session to create parallel exploration branches (e.g., comparing two testing strategies or refactoring approaches from a shared codebase analysis)
- Choosing between session resumption (when prior context is mostly valid) and starting fresh with injected summaries (when prior tool results are stale)
- Informing a resumed session about specific file changes for targeted re-analysis rather than requiring full re-exploration
