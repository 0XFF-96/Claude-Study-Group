# KenLoong — CCA-F 完整学习路径（单文档版）

> **本文档是唯一学习入口** — 含 30 个子主题的官方考点（Knowledge of / Skills in）、推荐阅读、考点速记与练习建议。  
> 无需再打开 `syllabus/domains/domain-*.md`。  
> 配套：`progress.md`（勾选）· `weekly-log.md`（打卡）· `notes/domain-*.md`（个人笔记）  
> 最后更新：2026-06-10

**考试格式：** 60 题 · 120 分钟 · 闭卷 · 及格 720/1000  
**Domain 权重：** D1 27% · D2 18% · D3 20% · D4 20% · D5 15%

---

## 一、全局资源

### 考试官方材料

| 资源 | 链接 | 用途 |
|------|------|------|
| CCA-F 报名 & Exam Guide PDF | [Skilljar 考试入口](https://anthropic.skilljar.com/claude-certified-architect-foundations-access-request) | 官方 PDF、Practice Exam（60 题） |
| CertSafari 练习库 | [636 道练习题](https://www.certsafari.com/anthropic/claude-certified-architect) | 按 Domain 刷题 |

### Anthropic Academy 课程（免费）

| 课程 | 链接 | 覆盖 |
|------|------|------|
| Building with the Claude API | [链接](https://anthropic.skilljar.com/claude-with-the-anthropic-api) | D1、D2、D4、D5 |
| Claude Code 101 | [链接](https://anthropic.skilljar.com/claude-code-101) | D1、D3、D5 |
| Claude Code in Action | [链接](https://anthropic.skilljar.com/claude-code-in-action) | D1、D3、D5 |
| Introduction to subagents | [链接](https://anthropic.skilljar.com/introduction-to-subagents) | D1、D3、D5 |
| Introduction to agent skills | [链接](https://anthropic.skilljar.com/introduction-to-agent-skills) | D3 |
| Introduction to MCP | [链接](https://anthropic.skilljar.com/introduction-to-model-context-protocol) | D2 |
| MCP Advanced Topics | [链接](https://anthropic.skilljar.com/model-context-protocol-advanced-topics) | D2 |
| 课程总目录 | [anthropic.skilljar.com](https://anthropic.skilljar.com/) | 全部 |

### 官方文档速查

| 文档 | 链接 |
|------|------|
| Agent SDK Overview | [docs](https://docs.claude.com/en/api/agent-sdk/overview) |
| Agent loop | [code.claude.com](https://code.claude.com/docs/en/agent-sdk/agent-loop) |
| Subagents (SDK) | [code.claude.com](https://code.claude.com/docs/en/agent-sdk/subagents) |
| Structured outputs | [code.claude.com](https://code.claude.com/docs/en/agent-sdk/structured-outputs) |
| Tool use | [docs](https://docs.claude.com/en/docs/build-with-claude/tool-use) |
| Prompt engineering | [docs](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview) |
| Batch processing | [docs](https://docs.claude.com/en/docs/build-with-claude/batch-processing) |
| CLAUDE.md / Memory | [docs](https://docs.claude.com/en/docs/claude-code/memory) |
| Hooks | [docs](https://docs.claude.com/en/docs/claude-code/hooks) |
| Skills | [docs](https://docs.claude.com/en/docs/claude-code/skills) |
| Slash commands | [docs](https://docs.claude.com/en/docs/claude-code/slash-commands) |
| Common workflows | [docs](https://docs.claude.com/en/docs/claude-code/common-workflows) |
| Headless / CI | [docs](https://docs.claude.com/en/docs/claude-code/headless) |
| MCP (Claude Code) | [docs](https://docs.claude.com/en/docs/claude-code/mcp) |
| MCP 规范 | [modelcontextprotocol.io](https://modelcontextprotocol.io/) |

---

## 二、学习顺序

```text
Phase 0  入门（1 天）→ 读本文档 §三 Domain 1 开头 + 下载 Exam Guide PDF
Phase 1  Domain 1（27%，约 2 周）← 最重要
Phase 2  Domain 2（18%，约 1.5 周）
Phase 3  Domain 3（20%，约 1.5 周）
Phase 4  Domain 4（20%，约 1.5 周）
Phase 5  Domain 5（15%，约 1 周）
Phase 6  CertSafari 全 Domain 刷题 + Practice Exam（1–2 周）
```

**每个子主题流程：** 读本节考点 → 看推荐阅读 → CertSafari 刷 10–20 题 → 写 `notes/` → 勾选 `progress.md`

---

## 三、完整考试大纲（30 子主题）

---

# Domain 1 — Agentic Architecture & Orchestration（27%）

**本周课程：** Building with the Claude API → Introduction to subagents → Claude Code 101  
**建议顺序：** 1.1 → 1.2 → 1.3 → 1.4 → 1.5 → 1.6 → 1.7  
**Domain 刷题：** [CertSafari Domain 1](https://www.certsafari.com/anthropic/claude-certified-architect)  
**动手练习：** 写最小 agentic loop（`stop_reason` 控制）；用 `/agents` 建 reviewer subagent

---

### 1.1 Agentic loops

*Official skill: Design and implement agentic loops for autonomous task execution*

**Knowledge of（需理解）**
- Agentic loop 生命周期：发请求 → 检查 `stop_reason`（`tool_use` vs `end_turn`）→ 执行 tool → 返回结果进入下一轮
- Tool results 追加到 conversation history，供模型推理下一步
- Model-driven（模型根据 context 选 tool）vs 预配置决策树/固定 tool 序列的区别

**Skills in（需会做）**
- `stop_reason == tool_use` 继续循环，`end_turn` 终止
- 迭代间把 tool results 加入 context
- **反模式（考试高频）：** 用自然语言判断终止 · 任意 iteration cap 作主停止条件 · 用 assistant 文本内容作完成标志

**推荐阅读**
- 课程：[Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api) — Agents & workflows
- 课程：[Claude Code 101](https://anthropic.skilljar.com/claude-code-101)
- 文档：[Agent loop](https://code.claude.com/docs/en/agent-sdk/agent-loop) · [Tool use](https://docs.claude.com/en/docs/build-with-claude/tool-use)

**考点速记：** 循环终止只看 `stop_reason`，不看自然语言。

**勾选：** `progress.md` → 1.1

---

### 1.2 Multi-agent orchestration

*Official skill: Orchestrate multi-agent systems with coordinator-subagent patterns*

**Knowledge of**
- Hub-and-spoke：coordinator 管理所有 subagent 间通信、错误处理、信息路由
- Subagent 隔离 context，**不自动继承** coordinator 的 conversation history
- Coordinator 负责：任务分解、委派、结果聚合、按 query 复杂度动态选 subagent
- Coordinator 分解过窄 → 广泛研究 topic coverage 不完整

**Skills in**
- Coordinator 动态选 subagent，而非总是走完整 pipeline
- 按 subtopic/source type 分区，减少 subagent 间重复
- Iterative refinement：coordinator 评估 synthesis 缺口 → 针对性 re-delegate → 再 invoke synthesis
- 所有 subagent 通信经 coordinator（可观测性、一致错误处理）

**推荐阅读**
- 课程：[Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api) — multi-agent
- 课程：[Introduction to subagents](https://anthropic.skilljar.com/introduction-to-subagents)
- 文档：[Subagents SDK](https://code.claude.com/docs/en/agent-sdk/subagents)

**考点速记：** 所有通信经 coordinator；用 iterative refinement 补 coverage gap。

**勾选：** `progress.md` → 1.2

---

### 1.3 Subagent invocation

*Official skill: Configure subagent invocation, context passing, and spawning*

**Knowledge of**
- `Task` tool 用于 spawn subagent；coordinator 的 `allowedTools` 须含 `"Task"`
- Subagent context **必须显式**写在 prompt 里；不继承 parent、不共享 memory
- `AgentDefinition`：description、system prompt、tool restrictions
- `fork_session`：从共享分析基线探索分歧方案

**Skills in**
- 把前序 agent 完整 findings 写入 subagent prompt（搜索结果、文档分析等）
- 结构化格式分离 content 与 metadata（URL、文档名、页码）保留 attribution
- **同一 coordinator response** 里 emit 多个 Task 调用 → 并行 subagent
- Coordinator prompt 写研究目标与质量标准，而非逐步操作指令

**推荐阅读**
- 课程：[Introduction to subagents](https://anthropic.skilljar.com/introduction-to-subagents)
- 文档：[Subagents SDK](https://code.claude.com/docs/en/agent-sdk/subagents) · [Agent SDK Overview](https://docs.claude.com/en/api/agent-sdk/overview)

**考点速记：** Context 只能经 prompt 传递；同 turn 可并行多个 Task。

**勾选：** `progress.md` → 1.3

---

### 1.4 Workflow enforcement and handoff

*Official skill: Implement multi-step workflows with enforcement and handoff patterns*

**Knowledge of**
- Programmatic enforcement（hooks、prerequisite gates）vs prompt-based guidance
- 确定性合规（身份验证后才金融操作）→ 纯 prompt 有非零失败率
- 中途 escalation 需结构化 handoff：客户信息、根因、建议操作

**Skills in**
- Programmatic prerequisite：阻断下游 tool 直到前置完成（如 `get_customer` 验证后才 `process_refund`）
- 多诉求请求分解为独立 item → 并行调查 → 统一 synthesis
- Escalation 给人工时编译结构化 summary（customer ID、root cause、refund amount、recommended action）

**推荐阅读**
- 课程：[Claude Code 101](https://anthropic.skilljar.com/claude-code-101) — hooks
- 文档：[Hooks](https://docs.claude.com/en/docs/claude-code/hooks) · [Agent loop](https://code.claude.com/docs/en/agent-sdk/agent-loop)

**考点速记：** 金融/身份验证 → hooks 优于纯 prompt；handoff 要结构化。

**勾选：** `progress.md` → 1.4

---

### 1.5 Agent SDK hooks

*Official skill: Apply Agent SDK hooks for tool call interception and data normalization*

**Knowledge of**
- `PostToolUse`：拦截 tool results 做 transformation 再给模型
- 拦截 outgoing tool calls 强制合规（如超阈值退款）
- Hooks = 确定性保证；prompt = 概率性合规

**Skills in**
- `PostToolUse` 归一化异构数据（Unix timestamp、ISO 8601、status code）
- 拦截违规 tool call 并 redirect（如 >$500 退款 → 人工 escalation）
- 业务规则需 guaranteed compliance 时选 hooks 而非 prompt

**推荐阅读**
- 课程：[Claude Code 101](https://anthropic.skilljar.com/claude-code-101)
- 文档：[Hooks](https://docs.claude.com/en/docs/claude-code/hooks) · [Agent loop § Hooks](https://code.claude.com/docs/en/agent-sdk/agent-loop)

**考点速记：** `PostToolUse` 归一化 MCP 异构输出；合规拦截用 hook。

**勾选：** `progress.md` → 1.5

---

### 1.6 Task decomposition

*Official skill: Design task decomposition strategies for complex workflows*

**Knowledge of**
- 固定 sequential pipeline（prompt chaining）vs 基于中间发现的 dynamic adaptive decomposition
- Prompt chaining：逐文件分析 → cross-file integration pass
- Adaptive plan：每步根据发现生成 subtask

**Skills in**
- 可预测多维度 review → prompt chaining；开放调查 → dynamic decomposition
- 大 code review：per-file local pass + 独立 cross-file integration pass（防 attention dilution）
- 开放任务（如 legacy 补测试）：先 map 结构 → 识别 high-impact → 自适应优先级计划

**推荐阅读**
- 课程：[Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api) — chaining & routing
- 文档：[Agent SDK Overview](https://docs.claude.com/en/api/agent-sdk/overview)

**考点速记：** 固定流程 → chaining；开放探索 → dynamic；大 review 两 pass。

**勾选：** `progress.md` → 1.6

---

### 1.7 Session state

*Official skill: Manage session state, resumption, and forking*

**Knowledge of**
- `--resume <session-name>` 恢复指定会话
- `fork_session` 从共享基线创建独立分支探索不同方案
- Resume 后须告知 agent 已分析文件的变更
- Stale tool results 时：新 session + structured summary **优于**盲目 resume

**Skills in**
- 用 session name `--resume` 跨工作日继续调查
- `fork_session` 并行比较两种策略（如两种测试/重构方案）
- Prior context 大多有效 → resume；tool results 过期 → fresh + injected summary
- Resume 后告知具体文件变更，做 targeted re-analysis

**推荐阅读**
- 课程：[Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action)
- 文档：[Claude Code overview](https://docs.claude.com/en/docs/claude-code/overview) · [Subagents SDK](https://code.claude.com/docs/en/agent-sdk/subagents)

**考点速记：** Stale results → 新 session + summary；resume 后说明文件变更。

**勾选：** `progress.md` → 1.7

---

# Domain 2 — Tool Design & MCP Integration（18%）

**本周课程：** Introduction to MCP → MCP Advanced → Building with the Claude API（MCP 章）  
**建议顺序：** 2.1 → 2.3 → 2.2 → 2.4 → 2.5  
**Domain 刷题：** [CertSafari Domain 2](https://www.certsafari.com/anthropic/claude-certified-architect)  
**动手练习：** 写带 `isError` + `errorCategory` 的 MCP server；配置 `.mcp.json` + `${ENV_VAR}`

---

### 2.1 Tool interface design

*Official skill: Design effective tool interfaces with clear descriptions and boundaries*

**Knowledge of**
- Tool description 是 LLM 选 tool 的主要机制；描述过简 → 相似 tool 间选择不可靠
- 描述须含：input 格式、示例 query、edge case、边界说明
- 模糊/重叠描述导致 misrouting（如 `analyze_content` vs `analyze_document`）
- System prompt 关键词敏感指令可覆盖良好 tool description

**Skills in**
- 写清 purpose、inputs、outputs、与相似 tool 的选用时机
- Rename + 更新 description 消除重叠（如 `analyze_content` → `extract_web_results`）
- 拆分泛用 tool 为专用 tool（`extract_data_points`、`summarize_content`、`verify_claim_against_source`）
- 审查 system prompt 中可能 override tool description 的关键词指令

**推荐阅读**
- 课程：[Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api)
- 文档：[Tool use](https://docs.claude.com/en/docs/build-with-claude/tool-use) · [MCP Tools spec](https://modelcontextprotocol.io/docs/concepts/tools)

**考点速记：** 重叠 tool 要 rename/split；system prompt 勿覆盖 tool description。

**勾选：** `progress.md` → 2.1

---

### 2.2 Structured MCP errors

*Official skill: Implement structured error responses for MCP tools*

**Knowledge of**
- MCP `isError` flag 向 agent 传达 tool 失败
- 错误类型：transient / validation / business / permission
- 统一 "Operation failed" → agent 无法做恢复决策
- Retryable vs non-retryable；结构化 metadata 避免无效重试

**Skills in**
- 返回 `errorCategory`、`isRetryable`、human-readable description
- Business violation 含 `retriable: false` + 客户友好说明
- Subagent 本地恢复 transient；无法解决才上报 coordinator（含 partial results + 已尝试操作）
- 区分 access failure（需 retry 决策）vs valid empty result（查询成功无匹配）

**推荐阅读**
- 课程：[Introduction to MCP](https://anthropic.skilljar.com/introduction-to-model-context-protocol)
- 文档：[MCP Tools spec](https://modelcontextprotocol.io/docs/concepts/tools) · [Subagents SDK](https://code.claude.com/docs/en/agent-sdk/subagents)

**考点速记：** `errorCategory` + `isRetryable`；空结果 ≠ 访问失败。

**勾选：** `progress.md` → 2.2

---

### 2.3 Tool distribution and tool_choice

*Official skill: Distribute tools appropriately across agents and configure tool choice*

**Knowledge of**
- 过多 tools（18 个 vs 4–5 个）降低选择可靠性
- 非专长 agent 误用 tools（如 synthesis agent 做 web search）
- Scoped tool access：每 agent 仅角色所需 tools + 少量跨角色高频 tool
- `tool_choice`：`auto` / `any` / forced `{"type":"tool","name":"..."}`

**Skills in**
- 每 subagent 仅角色相关 tools
- 泛用 tool 换约束版（`fetch_url` → `load_document` 校验 URL）
- 高频跨角色需求给 scoped tool（如 synthesis 的 `verify_fact`），复杂 case 经 coordinator
- Forced tool_choice 确保特定 tool 先执行（如先 `extract_metadata`）
- `tool_choice: "any"` 保证模型必须调 tool 而非返回对话文本

**推荐阅读**
- 课程：[Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api)
- 文档：[Tool use](https://docs.claude.com/en/docs/build-with-claude/tool-use) · [Subagents SDK](https://code.claude.com/docs/en/agent-sdk/subagents)

**考点速记：** 每 agent 4–5 tools；synthesis agent 不应有 web search。

**勾选：** `progress.md` → 2.3

---

### 2.4 MCP server integration

*Official skill: Integrate MCP servers into Claude Code and agent workflows*

**Knowledge of**
- Project-level `.mcp.json`（团队共享）vs user-level `~/.claude.json`（个人/实验）
- `.mcp.json` 中 `${GITHUB_TOKEN}` 等 env 变量展开，免提交 secret
- 连接时发现所有 MCP server tools，同时可用
- MCP resources 暴露内容目录（issue 摘要、文档层级、DB schema）减少 exploratory calls

**Skills in**
- 团队 server 配在 project `.mcp.json` + env 变量认证
- 个人/实验 server 配在 `~/.claude.json`
- 增强 MCP tool description，防 agent 偏好内置 Grep 而忽略更强 MCP tool
- 标准集成（Jira）用社区 server；自定义 server 留给团队特有 workflow
- 用 MCP resources 暴露 catalog，免 exploratory tool calls

**推荐阅读**
- 课程：[Introduction to MCP](https://anthropic.skilljar.com/introduction-to-model-context-protocol) · [MCP Advanced](https://anthropic.skilljar.com/model-context-protocol-advanced-topics) · [Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action)
- 文档：[Claude Code MCP](https://docs.claude.com/en/docs/claude-code/mcp) · [MCP Resources](https://modelcontextprotocol.io/docs/concepts/resources)

**考点速记：** 团队 `.mcp.json`；个人 `~/.claude.json`；优先社区 server。

**勾选：** `progress.md` → 2.4

---

### 2.5 Built-in tools

*Official skill: Select and apply built-in tools (Read, Write, Edit, Bash, Grep, Glob) effectively*

**Knowledge of**
- **Grep**：搜文件**内容**（函数名、错误信息、import）
- **Glob**：按路径/扩展名模式找文件
- **Read/Write**：完整文件读写；**Edit**：唯一文本锚点做局部修改
- Edit 因非唯一匹配失败时 → Read + Write 兜底

**Skills in**
- Grep 找 caller、错误信息；Glob 找 `**/*.test.tsx`
- Edit 锚点不唯一 → Read 全文 + Write
- 增量理解代码库：Grep 找入口 → Read 跟 import，**勿**一次 Read 全库
- Wrapper 模块：先列 exported names → 逐个 Grep 全库

**推荐阅读**
- 课程：[Claude Code 101](https://anthropic.skilljar.com/claude-code-101)
- 文档：[Claude Code overview](https://docs.claude.com/en/docs/claude-code/overview)

**考点速记：** 内容 Grep，文件名 Glob；Edit 失败用 Read+Write。

**勾选：** `progress.md` → 2.5

---

# Domain 3 — Claude Code Configuration & Workflows（20%）

**本周课程：** Claude Code 101 → Introduction to agent skills → Claude Code in Action  
**建议顺序：** 3.1 → 3.2 → 3.3 → 3.4 → 3.5 → 3.6  
**Domain 刷题：** [CertSafari Domain 3](https://www.certsafari.com/anthropic/claude-certified-architect)  
**动手练习：** 写项目 `.claude/CLAUDE.md` + `SKILL.md`（`context: fork`）；`claude -p` + `--output-format json` CI 命令

---

### 3.1 CLAUDE.md hierarchy

*Official skill: Configure CLAUDE.md files with appropriate hierarchy, scoping, and modular organization*

**Knowledge of**
- 层级：user `~/.claude/CLAUDE.md` · project `.claude/CLAUDE.md` 或根 `CLAUDE.md` · directory 级子目录 `CLAUDE.md`
- User-level 仅本用户，**不进 version control**，队友收不到
- `@import` 引用外部文件保持模块化
- `.claude/rules/` 替代单体大 CLAUDE.md

**Skills in**
- 诊断层级问题（新成员收不到指令 → 可能在 user-level 而非 project-level）
- `@import` 按 package 选择性引入标准文件
- 大 CLAUDE.md 拆到 `.claude/rules/`（testing.md、api-conventions.md 等）
- `/memory` 验证加载了哪些 memory 文件

**推荐阅读**
- 课程：[Claude Code 101](https://anthropic.skilljar.com/claude-code-101) · [Introduction to agent skills](https://anthropic.skilljar.com/introduction-to-agent-skills)
- 文档：[Memory / CLAUDE.md](https://docs.claude.com/en/docs/claude-code/memory)

**考点速记：** 团队共享 → project-level；`/memory` 诊断；`@import` 模块化。

**勾选：** `progress.md` → 3.1

---

### 3.2 Slash commands and skills

*Official skill: Create and configure custom slash commands and skills*

**Knowledge of**
- Project `.claude/commands/`（版本控制共享）vs user `~/.claude/commands/`（个人）
- Skills：`.claude/skills/SKILL.md`，frontmatter 支持 `context: fork`、`allowed-tools`、`argument-hint`
- `context: fork`：skill 在隔离 sub-agent context 运行，不污染主会话
- 个人 skill 放 `~/.claude/skills/` 换名，避免影响队友

**Skills in**
- Project slash commands 团队共享
- Verbose 输出 skill 用 `context: fork`（代码库分析、brainstorm）
- `allowed-tools` 限制 skill 执行期 tool（如仅写文件防破坏）
- `argument-hint` 提示必填参数
- Skills（按需任务 workflow）vs CLAUDE.md（始终加载的通用标准）

**推荐阅读**
- 课程：[Introduction to agent skills](https://anthropic.skilljar.com/introduction-to-agent-skills)
- 文档：[Skills](https://docs.claude.com/en/docs/claude-code/skills) · [Slash commands](https://docs.claude.com/en/docs/claude-code/slash-commands)
- 博客：[Agent Skills 工程文](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

**考点速记：** Verbose skill → `context: fork`；个人 skill 换名放 `~/`。

**勾选：** `progress.md` → 3.2

---

### 3.3 Path-specific rules

*Official skill: Apply path-specific rules for conditional convention loading*

**Knowledge of**
- `.claude/rules/` 文件 YAML frontmatter `paths` 字段含 glob
- 仅编辑匹配文件时加载 → 减 irrelevant context 和 token
- 跨目录约定（如散落各处的 test 文件）→ glob rules 优于 subdirectory CLAUDE.md

**Skills in**
- `paths: ["terraform/**/*"]` 等条件加载
- `**/*.test.tsx` 按文件类型跨目录应用
- 约定跨多目录时选 path-specific rules 而非子目录 CLAUDE.md

**推荐阅读**
- 课程：[Introduction to agent skills](https://anthropic.skilljar.com/introduction-to-agent-skills)
- 文档：[Memory § rules](https://docs.claude.com/en/docs/claude-code/memory)

**考点速记：** `**/*.test.tsx` glob 优于多目录 CLAUDE.md。

**勾选：** `progress.md` → 3.3

---

### 3.4 Plan mode vs direct execution

*Official skill: Determine when to use plan mode vs direct execution*

**Knowledge of**
- **Plan mode**：大规模变更、多种可行方案、架构决策、多文件修改
- **Direct execution**：简单、范围明确的变更（单函数加校验）
- Plan mode 先探索设计再改，防昂贵返工
- **Explore subagent** 隔离 verbose 发现阶段，摘要回主会话

**Skills in**
- 架构级任务（微服务重构、45+ 文件迁移）→ Plan
- 单文件明确 bug（清晰 stack trace）→ direct
- 多阶段 verbose discovery → Explore subagent 防 context 耗尽
- Plan 调查 + direct 实施（如先 plan 迁移方案再执行）

**推荐阅读**
- 课程：[Claude Code 101](https://anthropic.skilljar.com/claude-code-101) · [Introduction to subagents](https://anthropic.skilljar.com/introduction-to-subagents)
- 文档：[Common workflows](https://docs.claude.com/en/docs/claude-code/common-workflows)

**考点速记：** 架构/多文件 → Plan；单文件 bug → direct；发现阶段 → Explore subagent。

**勾选：** `progress.md` → 3.4

---

### 3.5 Iterative refinement

*Official skill: Apply iterative refinement techniques for progressive improvement*

**Knowledge of**
- 具体 input/output 示例比 prose 更有效（prose 易被不一致解读）
- TDD：先写 test suite，用 test failure 引导迭代
- Interview pattern：让 Claude 先提问暴露未考虑的设计点
- 交互问题一次 message 修；独立问题可顺序修

**Skills in**
- 2–3 个 concrete I/O 示例澄清 transformation
- 先写覆盖 expected/edge/performance 的 tests，再 share failures 迭代
- Interview pattern 暴露 cache invalidation、failure modes 等
- 具体 test case（input + expected output）修 edge case（如 migration null）
- 多个 interacting issues → 单条详细 message；独立 issues → 顺序迭代

**推荐阅读**
- 课程：[Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action)
- 文档：[Prompt engineering](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)

**考点速记：** I/O 示例 > prose；TDD 迭代；交互问题一次修完。

**勾选：** `progress.md` → 3.5

---

### 3.6 CI/CD integration

*Official skill: Integrate Claude Code into CI/CD pipelines*

**Knowledge of**
- `-p` / `--print`：非交互模式，CI 不 hang
- `--output-format json` + `--json-schema`：CI 结构化输出
- CLAUDE.md 向 CI 实例注入测试标准、fixture 约定、review 标准
- **同 session 生成+自审 < 独立 review instance**（保留生成 reasoning 难质疑自己）

**Skills in**
- CI 用 `-p` 防交互阻塞
- `--output-format json` + `--json-schema` → 机器可解析 findings → 自动 PR comment
- 重跑 review 时带入 prior findings，只报新/未解决问题
- 提供已有 test 文件避免重复场景建议
- CLAUDE.md 记录 testing standards、valuable test criteria、fixtures

**推荐阅读**
- 课程：[Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action)
- 文档：[Headless / CI](https://docs.claude.com/en/docs/claude-code/headless) · [Memory](https://docs.claude.com/en/docs/claude-code/memory)

**考点速记：** CI 用 `-p`；review 用独立 instance；重跑只报新问题。

**勾选：** `progress.md` → 3.6

---

# Domain 4 — Prompt Engineering & Structured Output（20%）

**本周课程：** Building with the Claude API（prompting + structured output）  
**建议顺序：** 4.1 → 4.2 → 4.3 → 4.4 → 4.5 → 4.6  
**Domain 刷题：** [CertSafari Domain 4](https://www.certsafari.com/anthropic/claude-certified-architect)  
**动手练习：** extraction tool + JSON schema，对比 `tool_choice` 三种模式；Message Batches + `custom_id`

---

### 4.1 Explicit criteria

*Official skill: Design prompts with explicit criteria to improve precision and reduce false positives*

**Knowledge of**
- Explicit criteria 优于模糊指令（"claimed behavior contradicts actual code" vs "check comments are accurate"）
- "be conservative" / "only high-confidence" **不能**替代具体分类标准
- 高 FP 率损害开发者对准确类别的信任

**Skills in**
- 明确 report（bugs、security）vs skip（minor style、local patterns），不靠 confidence 过滤
- 高 FP 类别暂时 disable 恢复信任，同时改进 prompt
- 每 severity level 用具体代码示例定义标准

**推荐阅读**
- 课程：[Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api)
- 文档：[Prompt engineering](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)

**考点速记：** "be conservative" 无效；高 FP 先 disable；severity 用代码示例。

**勾选：** `progress.md` → 4.1

---

### 4.2 Few-shot prompting

*Official skill: Apply few-shot prompting to improve output consistency and quality*

**Knowledge of**
- 详细指令仍不一致时，few-shot 最有效
- Few-shot 演示 ambiguous-case handling（tool 选择、test coverage gap）
- 帮助泛化到 novel patterns，非仅匹配预设 case
- Extraction 任务减少 hallucination（非正式度量、多变文档结构）

**Skills in**
- 2–4 个 targeted examples，展示为何选 A 而非 plausible B
- 示范输出格式（location、issue、severity、suggested fix）
- 区分 acceptable pattern vs genuine issue，减 FP 且可泛化
- 演示 varied document structures（inline citation vs bibliography 等）
- 展示 varied format 的正确 extraction，修 empty/null 必填字段

**推荐阅读**
- 课程：[Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api)
- 文档：[Prompt engineering](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)

**考点速记：** 2–4 examples；ambiguous case 展示 reasoning。

**勾选：** `progress.md` → 4.2

---

### 4.3 Structured output

*Official skill: Enforce structured output using tool use and JSON schemas*

**Knowledge of**
- `tool_use` + JSON schema 最可靠，消除 JSON syntax errors
- `tool_choice`：`auto`（可返回文本）/ `any`（必须调某 tool）/ forced 指定 tool
- Schema 消除 syntax error **不防** semantic error（行项不加总、字段放错）
- Schema 设计：required vs optional；enum + `"other"` + detail 字段

**Skills in**
- Extraction tool 的 JSON schema 作 input parameters，从 `tool_use` response 取数据
- 多 schema 且文档类型未知 → `tool_choice: "any"`
- 强制 `extract_metadata` 先于 enrichment → forced tool_choice
- 源文档可能缺失的信息 → optional/nullable 字段，防 fabrication
- enum 加 `"unclear"`；`"other"` + detail 可扩展分类
- Prompt 中加 format normalization rules 配合 strict schema

**推荐阅读**
- 课程：[Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api)
- 文档：[Tool use](https://docs.claude.com/en/docs/build-with-claude/tool-use) · [Structured outputs SDK](https://code.claude.com/docs/en/agent-sdk/structured-outputs)

**考点速记：** Schema 不防 semantic error；nullable 防 fabrication；`any` 保证 structured。

**勾选：** `progress.md` → 4.3

---

### 4.4 Validation, retry, and feedback loops

*Official skill: Implement validation, retry, and feedback loops for extraction quality*

**Knowledge of**
- Retry-with-error-feedback：把具体 validation errors 追加到 prompt
- 信息根本不在源文档 → retry 无效（vs 格式/结构错误可修）
- `detected_pattern` 字段追踪触发 finding 的 code construct，分析 dismissal
- Semantic validation error vs schema syntax error（后者 tool use 已消除）

**Skills in**
- Follow-up 含原文档 + 失败 extraction + 具体 validation errors
- 判断 retry 何时无效（信息在外部未提供文档）vs 有效（格式不匹配）
- `detected_pattern` 分析开发者 dismiss 的 FP 模式
- `calculated_total` vs `stated_total` 自检；`conflict_detected` boolean

**推荐阅读**
- 课程：[Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api)
- 文档：[Structured outputs SDK](https://code.claude.com/docs/en/agent-sdk/structured-outputs)

**考点速记：** 信息不在文档 → retry 无用；`detected_pattern` 分析 FP。

**勾选：** `progress.md` → 4.4

---

### 4.5 Batch processing

*Official skill: Design efficient batch processing strategies*

**Knowledge of**
- Message Batches API：50% 成本、最长 24h、**无 latency SLA**
- 适合：overnight report、weekly audit、nightly test generation
- 不适合：blocking pre-merge checks
- 单 request **不支持** multi-turn tool calling
- `custom_id` 关联 request/response

**Skills in**
- Blocking pre-merge → sync API；overnight/weekly → batch
- 按 SLA 算提交频率（如 4h 窗口 + 24h batch 保证 30h SLA）
- 失败只重提交 failed docs（`custom_id` 定位），超大文档 chunk
- 大批量前先 sample set  refine prompt 提高首轮成功率

**推荐阅读**
- 课程：[Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api)
- 文档：[Batch processing](https://docs.claude.com/en/docs/build-with-claude/batch-processing) · [Messages Batch API](https://docs.claude.com/en/api/messages-batch)

**考点速记：** Pre-merge → sync；overnight → batch；batch 无 multi-turn tool。

**勾选：** `progress.md` → 4.5

---

### 4.6 Multi-pass review

*Official skill: Design multi-instance and multi-pass review architectures*

**Knowledge of**
- 自审局限：同 session 保留 generation reasoning，难质疑自己
- 独立 review instance（无 prior reasoning）> 自审指令或 extended thinking
- Multi-pass：per-file local + cross-file integration，防 attention dilution 和矛盾 findings

**Skills in**
- 第二个独立 Claude instance review，无 generator reasoning
- 大 review：per-file pass（local issues）+ integration pass（cross-file data flow）
- Verification pass 自报 confidence，用于 calibrated routing

**推荐阅读**
- 课程：[Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action)
- 文档：[Structured outputs SDK](https://code.claude.com/docs/en/agent-sdk/structured-outputs) · [Agent SDK Overview](https://docs.claude.com/en/api/agent-sdk/overview)

**考点速记：** 自审 < 独立 reviewer；大 review 两 pass。

**勾选：** `progress.md` → 4.6

---

# Domain 5 — Context Management & Reliability（15%）

**本周课程：** Claude Code 101（context）→ Building with the Claude API（long context）  
**建议顺序：** 5.1 → 5.4 → 5.3 → 5.2 → 5.6 → 5.5  
**Domain 刷题：** [CertSafari Domain 5](https://www.certsafari.com/anthropic/claude-certified-architect)  
**动手练习：** 长对话 `/compact` 对比 case facts 保留；设计 error schema：`status` + `partial_results`

> D5 概念会渗透到 D1–D4，勿跳过。

---

### 5.1 Long-context preservation

*Official skill: Manage conversation context to preserve critical information across long interactions*

**Knowledge of**
- Progressive summarization 风险：数字、百分比、日期、客户期望被压缩成模糊表述
- **"Lost in the middle"**：长输入首尾可靠，中间 section 易遗漏
- Tool results 累积占 token（如 order lookup 40+ 字段仅 5 个相关）
- 后续 API 请求须传完整 conversation history 保持连贯

**Skills in**
- 交易事实（金额、日期、订单号、状态）→ 持久 **"case facts"** block，每 prompt 附带
- 多 issue session：结构化 issue data 独立 context layer
- Trim verbose tool output 为相关字段再入 context
- 关键 findings 放 aggregated input **开头**；详细结果用 section headers
- Subagent 输出含 metadata（日期、来源、方法学 context）
- 上游 agent 返回 structured data（key facts、citations、scores）而非 verbose reasoning chain

**推荐阅读**
- 课程：[Claude Code 101](https://anthropic.skilljar.com/claude-code-101) · [Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api)
- 文档：[Memory](https://docs.claude.com/en/docs/claude-code/memory) · [Agent loop](https://code.claude.com/docs/en/agent-sdk/agent-loop)

**考点速记：** Case facts 块；lost in the middle；trim tool output。

**勾选：** `progress.md` → 5.1

---

### 5.2 Escalation and ambiguity

*Official skill: Design effective escalation and ambiguity resolution patterns*

**Knowledge of**
- Escalation 触发：客户要人工、policy 例外/空白、无法取得进展（非仅"复杂"）
- 客户明确要求人工 → 立即 escalate；简单问题可先 offer 解决
- Sentiment、自报 confidence **不可靠**作复杂度代理
- 多 customer match → 要额外 identifier，勿 heuristic 选择

**Skills in**
- System prompt 加 explicit escalation criteria + few-shot 示例
- 客户明确要求人工 → 立即执行，不先调查
- 有能力解决时先 acknowledge + offer resolution；客户坚持再 escalate
- Policy 模糊/沉默（如竞品价格匹配）→ escalate
- 多 match → 要求额外 ID

**推荐阅读**
- 课程：[Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api)
- 文档：[Prompt engineering](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)

**考点速记：** 客户要人工 → 立即；policy gap → escalate；多 match 要 ID。

**勾选：** `progress.md` → 5.2

---

### 5.3 Error propagation

*Official skill: Implement error propagation strategies across multi-agent systems*

**Knowledge of**
- 结构化 error context（failure type、attempted query、partial results、alternatives）助 coordinator 恢复
- Access failure（timeout）vs valid empty result（成功无匹配）
- 泛化 "search unavailable" 隐藏 valuable context
- 静默吞错（空结果当成功）和单点失败终止全流程都是反模式

**Skills in**
- 返回 failure type、已尝试、partial results、alternatives
- 区分 access failure vs valid empty
- Subagent 本地恢复 transient；无法解决才上报（含已尝试 + partial）
- Synthesis 输出含 coverage annotations（well-supported vs gap areas）

**推荐阅读**
- 课程：[Introduction to subagents](https://anthropic.skilljar.com/introduction-to-subagents)
- 文档：[Subagents SDK](https://code.claude.com/docs/en/agent-sdk/subagents) · [MCP Tools spec](https://modelcontextprotocol.io/docs/concepts/tools)

**考点速记：** 结构化 error context；勿 silent suppress；局部恢复 transient。

**勾选：** `progress.md` → 5.3

---

### 5.4 Large-codebase context

*Official skill: Manage context effectively in large codebase exploration*

**Knowledge of**
- 长 session context degradation：答案不一致、引用"典型模式"而非早前发现的具体 class
- **Scratchpad files** 跨 context 边界持久化发现
- Subagent 委派隔离 verbose 探索；主 agent 保持高层协调
- Crash recovery：各 agent export state 到已知位置，coordinator resume 时 load manifest

**Skills in**
- Subagent 调查具体问题（找 test 文件、trace refund flow），主 agent 协调
- Scratchpad 记录 key findings，后续问题引用
- Phase 间 summarize findings 再 spawn 下一 phase subagent，inject summary
- Crash recovery manifest → resume 时 inject agent prompts
- 探索 session context 满 verbose output 时用 `/compact`

**推荐阅读**
- 课程：[Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action) · [Claude Code 101](https://anthropic.skilljar.com/claude-code-101)
- 文档：[Claude Code overview](https://docs.claude.com/en/docs/claude-code/overview)

**考点速记：** Scratchpad；manifest crash recovery；phase 间 inject summary。

**勾选：** `progress.md` → 5.4

---

### 5.5 Human review and confidence

*Official skill: Design human review workflows and confidence calibration*

**Knowledge of**
- 聚合准确率（97% overall）可能掩盖某 document type/field 差
- Stratified random sampling 测 high-confidence extraction 错误率、发现 novel patterns
- Field-level confidence 用 labeled validation set 校准
- 按 document type + field segment 验证准确率后再减少人工 review

**Skills in**
- High-confidence extraction 分层随机抽样持续测 error rate
- 按 document type + field 分析准确率，确认全 segment 一致后才减 review
- Model 输出 field-level confidence → 用 validation set 校准阈值
- Low confidence 或 ambiguous/contradictory 文档 → 人工 review，优先有限 reviewer 容量

**推荐阅读**
- 课程：[Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api)
- 文档：[Structured outputs SDK](https://code.claude.com/docs/en/agent-sdk/structured-outputs)

**考点速记：** 97% aggregate 可能掩盖 segment 问题；stratified sampling。

**勾选：** `progress.md` → 5.5

---

### 5.6 Information provenance

*Official skill: Preserve information provenance and handle uncertainty in multi-source synthesis*

**Knowledge of**
- Summarization 不保留 claim-source mapping → 丢失 attribution
- Synthesis 须保留 structured claim-source mappings 并 merge
- 冲突统计：annotate 冲突 + source attribution，勿随意选一
- 输出须含 publication/collection dates，防 temporal 差异被误读为矛盾

**Skills in**
- Subagent 输出 claim-source mapping（URL、文档名、excerpt），下游 preserve
- Report 分 well-established vs contested sections，保留方法学 context
- 冲突值 included + annotated，coordinator reconcile 后再 synthesis
- Subagent 输出含 publication/collection dates
- 按内容类型渲染：财务表格、新闻 prose、技术 structured list，勿统一格式

**推荐阅读**
- 课程：[Introduction to subagents](https://anthropic.skilljar.com/introduction-to-subagents)
- 文档：[Subagents SDK](https://code.claude.com/docs/en/agent-sdk/subagents)

**考点速记：** Claim-source mapping；冲突 annotate 不选一；日期防 temporal misread。

**勾选：** `progress.md` → 5.6

---

## 四、8 周学习计划

| 周 | 重点 | 子主题 | 产出 |
|----|------|--------|------|
| W1 | D1 入门 | 1.1–1.2 | 最小 agentic loop + notes |
| W2 | D1 深入 | 1.3–1.7 | subagent 实验 + 勾选 7 项 |
| W3 | D2 | 2.1–2.5 | MCP server + CertSafari D2 |
| W4 | D3 前半 | 3.1–3.3 | CLAUDE.md + Skill |
| W5 | D3 后半 + D4 前半 | 3.4–3.6, 4.1–4.3 | CI 命令 + structured output |
| W6 | D4 后半 + D5 前半 | 4.4–4.6, 5.1–5.3 | Batch API 实验 |
| W7 | D5 后半 | 5.4–5.6 | 综合笔记 |
| W8 | 冲刺 | 全部 | Practice Exam + 错题回顾 |

每周结束：
```bash
git add members/KenLoong
git commit -m "Week N: <domain> progress + notes"
git pull --rebase && git push
```

---

## 五、考前冲刺清单

- [ ] 30/30 子主题已在 `progress.md` 勾选
- [ ] CertSafari 每个 Domain 至少刷一轮
- [ ] 官方 Practice Exam ≥ 900 分
- [ ] `profile.md` 状态改为 `final-prep`

### 高频反模式速查

| ❌ 错误 | ✅ 正确 |
|--------|--------|
| 自然语言判断 loop 终止 | 看 `stop_reason`：`tool_use` 继续，`end_turn` 停 |
| synthesis agent 给 18 个 tools | 每 agent 4–5 个 scoped tools |
| 同 session 自审生成代码 | 独立 reviewer instance |
| 静默吞 subagent 错误 | 结构化 error context 上报 coordinator |
| 盲目 resume stale session | 新 session + injected summary |
| "be conservative" 减 FP | explicit categorical criteria |
| 信息不在文档仍 retry | 识别 retry 无效场景 |
| pre-merge 用 batch API | blocking workflow 用 sync API |
| 多 customer match heuristic 选 | 要求额外 identifier |
| progressive summarization 丢数字 | 持久 case facts block |

---

## 六、进度与打卡

| 操作 | 文件 |
|------|------|
| 勾选学完的子主题 | [progress.md](../progress.md) |
| 每周打卡 | [weekly-log.md](../weekly-log.md) |
| 个人笔记 | `notes/domain-*.md` |
| 刷题 | [CertSafari](https://www.certsafari.com/anthropic/claude-certified-architect) |
| 全组进度 | [PROGRESS.md](../../../PROGRESS.md) |
