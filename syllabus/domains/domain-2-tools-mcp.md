# Domain 2: Tool Design & MCP Integration (18%)

> Reference detail for the [CCA-F checklist](../CCA-F.md). Source: official study guide skills breakdown.

## 推荐阅读

**考试权重：18%**

### 本 Domain 总览

| 类型 | 资源 | 说明 |
|------|------|------|
| 课程 | [Introduction to Model Context Protocol](https://anthropic.skilljar.com/introduction-to-model-context-protocol) | MCP tools/resources/prompts 三原语 — 覆盖 2.2、2.4 |
| 课程 | [Model Context Protocol: Advanced Topics](https://anthropic.skilljar.com/model-context-protocol-advanced-topics) | 生产级 MCP、transport、notifications — 覆盖 2.4 |
| 课程 | [Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api) | Defining tools、MCP servers、tool_choice — 覆盖 2.1–2.3 |
| 课程 | [Claude Code 101](https://anthropic.skilljar.com/claude-code-101) | MCP 连接、built-in tools — 覆盖 2.4–2.5 |
| 文档 | [Tool use](https://docs.claude.com/en/docs/build-with-claude/tool-use) | Tool 描述、`tool_choice` auto/any/forced |
| 文档 | [Claude Code — MCP](https://docs.claude.com/en/docs/claude-code/mcp) | `.mcp.json`、`~/.claude.json`、env 变量 |
| 文档 | [MCP 规范 — Tools](https://modelcontextprotocol.io/docs/concepts/tools) | `isError`、结构化错误 |
| 文档 | [MCP 规范 — Resources](https://modelcontextprotocol.io/docs/concepts/resources) | 内容目录、减少 exploratory calls |
| 文档 | [Claude Code overview](https://docs.claude.com/en/docs/claude-code/overview) | Grep/Glob/Read/Write/Edit 内置工具 |
| 刷题 | [CertSafari — Domain 2](https://www.certsafari.com/anthropic/claude-certified-architect) | 选 Domain Mode → Tool Design & MCP |

**建议学习顺序：** 2.1 → 2.3 → 2.2 → 2.4 → 2.5

### 按子主题

#### [2.1 Tool interface design](#21-tool-interface-design)

- 课程：[Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api) — *Defining tools with MCP*
- 文档：[Tool use](https://docs.claude.com/en/docs/build-with-claude/tool-use) — description 是 LLM 选 tool 的主要依据
- 文档：[MCP Tools spec](https://modelcontextprotocol.io/docs/concepts/tools) — input schema、description 最佳实践
- 考点速记：重叠 tool 要 rename/split；system prompt 关键词勿覆盖 tool description

#### [2.2 Structured MCP errors](#22-structured-mcp-errors)

- 课程：[Introduction to Model Context Protocol](https://anthropic.skilljar.com/introduction-to-model-context-protocol) — 错误处理模式
- 文档：[MCP Tools spec](https://modelcontextprotocol.io/docs/concepts/tools) — `isError` flag
- 文档：[Subagents in the SDK](https://code.claude.com/docs/en/agent-sdk/subagents) — subagent 本地恢复 transient error
- 考点速记：返回 `errorCategory` + `isRetryable`；区分 access failure vs valid empty result

#### [2.3 Tool distribution and tool_choice](#23-tool-distribution-and-tool_choice)

- 课程：[Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api) — tool distribution 章节
- 文档：[Tool use](https://docs.claude.com/en/docs/build-with-claude/tool-use) — `tool_choice`: `auto` / `any` / forced
- 文档：[Subagents in the SDK](https://code.claude.com/docs/en/agent-sdk/subagents) — 每 subagent scoped tools
- 考点速记：每 agent 4–5 个 tools 而非 18 个；synthesis agent 不应有 web search tools

#### [2.4 MCP server integration](#24-mcp-server-integration)

- 课程：[Introduction to Model Context Protocol](https://anthropic.skilljar.com/introduction-to-model-context-protocol) — server/client 搭建
- 课程：[Model Context Protocol: Advanced Topics](https://anthropic.skilljar.com/model-context-protocol-advanced-topics) — 生产部署
- 课程：[Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action) — *MCP servers with Claude Code*
- 文档：[Claude Code — MCP](https://docs.claude.com/en/docs/claude-code/mcp) — project vs user scope、`${GITHUB_TOKEN}`
- 文档：[MCP Resources](https://modelcontextprotocol.io/docs/concepts/resources) — 暴露 catalog 减少探索性调用
- 考点速记：团队共享 → `.mcp.json`；个人实验 → `~/.claude.json`；优先社区 server 而非重复造轮子

#### [2.5 Built-in tools](#25-built-in-tools)

- 课程：[Claude Code 101](https://anthropic.skilljar.com/claude-code-101) — 内置工具日常用法
- 文档：[Claude Code overview](https://docs.claude.com/en/docs/claude-code/overview) — Read/Write/Edit/Bash/Grep/Glob
- 考点速记：搜内容用 Grep，搜文件名用 Glob；Edit 锚点不唯一时 Read + Write；增量探索勿一次 Read 全库

---

## 2.1 Tool interface design

*Official skill: Design effective tool interfaces with clear descriptions and boundaries*

**Knowledge of**

- Tool descriptions as the primary mechanism LLMs use for tool selection; minimal descriptions lead to unreliable selection among similar tools
- The importance of including input formats, example queries, edge cases, and boundary explanations in tool descriptions
- How ambiguous or overlapping tool descriptions cause misrouting (e.g., analyze_content vs analyze_document with near-identical descriptions)
- The impact of system prompt wording on tool selection: keyword-sensitive instructions can create unintended tool associations

**Skills in**

- Writing tool descriptions that clearly differentiate each tool's purpose, expected inputs, outputs, and when to use it versus similar alternatives
- Renaming tools and updating descriptions to eliminate functional overlap (e.g., renaming analyze_content to extract_web_results with a web-specific description)
- Splitting generic tools into purpose-specific tools with defined input/output contracts (e.g., splitting a generic analyze_document into extract_data_points, summarize_content, and verify_claim_against_source)
- Reviewing system prompts for keyword-sensitive instructions that might override well-written tool descriptions

## 2.2 Structured MCP errors

*Official skill: Implement structured error responses for MCP tools*

**Knowledge of**

- The MCP isError flag pattern for communicating tool failures back to the agent
- The distinction between transient errors (timeouts, service unavailability), validation errors (invalid input), business errors (policy violations), and permission errors
- Why uniform error responses (generic "Operation failed") prevent the agent from making appropriate recovery decisions
- The difference between retryable and non-retryable errors, and how returning structured metadata prevents wasted retry attempts

**Skills in**

- Returning structured error metadata including errorCategory (transient/validation/permission), isRetryable boolean, and human-readable descriptions
- Including retriable: false flags and customer-friendly explanations for business rule violations so the agent can communicate appropriately
- Implementing local error recovery within subagents for transient failures, propagating to the coordinator only errors that cannot be resolved locally along with partial results and what was attempted
- Distinguishing between access failures (needing retry decisions) and valid empty results (representing successful queries with no matches)

## 2.3 Tool distribution and tool_choice

*Official skill: Distribute tools appropriately across agents and configure tool choice*

**Knowledge of**

- The principle that giving an agent access to too many tools (e.g., 18 instead of 4-5) degrades tool selection reliability by increasing decision complexity
- Why agents with tools outside their specialization tend to misuse them (e.g., a synthesis agent attempting web searches)
- Scoped tool access: giving agents only the tools needed for their role, with limited cross-role tools for specific high-frequency needs
- tool_choice configuration options: "auto", "any", and forced tool selection ({"type": "tool", "name": "..."})

**Skills in**

- Restricting each subagent's tool set to those relevant to its role, preventing cross-specialization misuse
- Replacing generic tools with constrained alternatives (e.g., replacing fetch_url with load_document that validates document URLs)
- Providing scoped cross-role tools for high-frequency needs (e.g., a verify_fact tool for the synthesis agent) while routing complex cases through the coordinator
- Using tool_choice forced selection to ensure a specific tool is called first (e.g., forcing extract_metadata before enrichment tools), then processing subsequent steps in follow-up turns
- Setting tool_choice: "any" to guarantee the model calls a tool rather than returning conversational text

## 2.4 MCP server integration

*Official skill: Integrate MCP servers into Claude Code and agent workflows*

**Knowledge of**

- MCP server scoping: project-level (.mcp.json) for shared team tooling vs user-level (~/.claude.json) for personal/experimental servers
- Environment variable expansion in .mcp.json (e.g., ${GITHUB_TOKEN}) for credential management without committing secrets
- That tools from all configured MCP servers are discovered at connection time and available simultaneously to the agent
- MCP resources as a mechanism for exposing content catalogs (e.g., issue summaries, documentation hierarchies, database schemas) to reduce exploratory tool calls

**Skills in**

- Configuring shared MCP servers in project-scoped .mcp.json with environment variable expansion for authentication tokens
- Configuring personal/experimental MCP servers in user-scoped ~/.claude.json
- Enhancing MCP tool descriptions to explain capabilities and outputs in detail, preventing the agent from preferring built-in tools (like Grep) over more capable MCP tools
- Choosing existing community MCP servers over custom implementations for standard integrations (e.g., Jira), reserving custom servers for team-specific workflows
- Exposing content catalogs as MCP resources to give agents visibility into available data without requiring exploratory tool calls

## 2.5 Built-in tools

*Official skill: Select and apply built-in tools (Read, Write, Edit, Bash, Grep, Glob) effectively*

**Knowledge of**

- Grep for content search (searching file contents for patterns like function names, error messages, or import statements)
- Glob for file path pattern matching (finding files by name or extension patterns)
- Read/Write for full file operations; Edit for targeted modifications using unique text matching
- When Edit fails due to non-unique text matches, using Read + Write as a fallback for reliable file modifications

**Skills in**

- Selecting Grep for searching code content across a codebase (e.g., finding all callers of a function, locating error messages)
- Selecting Glob for finding files matching naming patterns (e.g., **/*.test.tsx)
- Using Read to load full file contents followed by Write when Edit cannot find unique anchor text
- Building codebase understanding incrementally: starting with Grep to find entry points, then using Read to follow imports and trace flows, rather than reading all files upfront
- Tracing function usage across wrapper modules by first identifying all exported names, then searching for each name across the codebase
