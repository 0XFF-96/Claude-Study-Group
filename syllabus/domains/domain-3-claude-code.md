# Domain 3: Claude Code Configuration & Workflows (20%)

> Reference detail for the [CCA-F checklist](../CCA-F.md). Source: official study guide skills breakdown.

## 推荐阅读

**考试权重：20%**

### 本 Domain 总览

| 类型 | 资源 | 说明 |
|------|------|------|
| 课程 | [Claude Code 101](https://anthropic.skilljar.com/claude-code-101) | CLAUDE.md、Plan Mode、hooks、context — 覆盖 3.1、3.4、3.5 |
| 课程 | [Introduction to agent skills](https://anthropic.skilljar.com/introduction-to-agent-skills) | SKILL.md、slash commands、rules — 覆盖 3.2、3.3 |
| 课程 | [Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action) | CI/CD、GitHub、SDK — 覆盖 3.5、3.6 |
| 课程 | [Introduction to subagents](https://anthropic.skilljar.com/introduction-to-subagents) | Explore subagent、context 隔离 — 覆盖 3.4 |
| 文档 | [CLAUDE.md / Memory](https://docs.claude.com/en/docs/claude-code/memory) | 层级、`@import`、`.claude/rules/`、`/memory` |
| 文档 | [Skills](https://docs.claude.com/en/docs/claude-code/skills) | `SKILL.md` frontmatter、`context: fork` |
| 文档 | [Slash commands](https://docs.claude.com/en/docs/claude-code/slash-commands) | `.claude/commands/` vs `~/` |
| 文档 | [Hooks](https://docs.claude.com/en/docs/claude-code/hooks) | 与 skills 对比、确定性控制 |
| 文档 | [Common workflows](https://docs.claude.com/en/docs/claude-code/common-workflows) | Explore → Plan → Code → Commit |
| 文档 | [Headless / CI mode](https://docs.claude.com/en/docs/claude-code/headless) | `-p`、`--output-format json`、`--json-schema` |
| 博客 | [Agent Skills 工程文](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) | Skills 设计理念 |
| 刷题 | [CertSafari — Domain 3](https://www.certsafari.com/anthropic/claude-certified-architect) | 选 Domain Mode → Claude Code Config |

**建议学习顺序：** 3.1 → 3.2 → 3.3 → 3.4 → 3.5 → 3.6

### 按子主题

#### [3.1 CLAUDE.md hierarchy](#31-claudemd-hierarchy)

- 课程：[Claude Code 101](https://anthropic.skilljar.com/claude-code-101) — CLAUDE.md 创建与维护
- 文档：[Memory / CLAUDE.md](https://docs.claude.com/en/docs/claude-code/memory) — user / project / directory 三级
- 文档：[Introduction to agent skills](https://anthropic.skilljar.com/introduction-to-agent-skills) — CLAUDE.md vs Skills 选型
- 考点速记：团队共享放 project-level；`@import` 模块化；大文件拆到 `.claude/rules/`；`/memory` 诊断加载

#### [3.2 Slash commands and skills](#32-slash-commands-and-skills)

- 课程：[Introduction to agent skills](https://anthropic.skilljar.com/introduction-to-agent-skills) — 从零创建 Skill
- 文档：[Skills](https://docs.claude.com/en/docs/claude-code/skills) — `context: fork`、`allowed-tools`、`argument-hint`
- 文档：[Slash commands](https://docs.claude.com/en/docs/claude-code/slash-commands) — project vs user scope
- 博客：[Agent Skills 工程文](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- 考点速记：verbose 输出 skill 用 `context: fork`；个人定制放 `~/.claude/skills/` 换名避免冲突

#### [3.3 Path-specific rules](#33-path-specific-rules)

- 课程：[Introduction to agent skills](https://anthropic.skilljar.com/introduction-to-agent-skills) — rules 组织
- 文档：[Memory § rules](https://docs.claude.com/en/docs/claude-code/memory) — YAML `paths` glob
- 考点速记：`**/*.test.tsx` 跨目录比 subdirectory CLAUDE.md 更合适；仅编辑匹配文件时加载

#### [3.4 Plan mode vs direct execution](#34-plan-mode-vs-direct-execution)

- 课程：[Claude Code 101](https://anthropic.skilljar.com/claude-code-101) — Plan Mode、Explore → Plan → Code
- 课程：[Introduction to subagents](https://anthropic.skilljar.com/introduction-to-subagents) — Explore subagent 隔离发现阶段
- 文档：[Common workflows](https://docs.claude.com/en/docs/claude-code/common-workflows) — 何时 plan vs 直接执行
- 考点速记：架构级/多文件/多方案 → Plan；单文件明确 bug → direct；verbose discovery 用 Explore subagent

#### [3.5 Iterative refinement](#35-iterative-refinement)

- 课程：[Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action) — 迭代工作流
- 文档：[Prompt engineering](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview) — 具体 I/O 示例优于纯 prose
- 考点速记：2–3 个 input/output 示例；TDD 先写 test 再迭代；interview pattern 先问再写；交互问题一次 message 修

#### [3.6 CI/CD integration](#36-cicd-integration)

- 课程：[Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action) — GitHub 集成、自动化 review
- 文档：[Headless / CI mode](https://docs.claude.com/en/docs/claude-code/headless) — `-p`、`--output-format json`、`--json-schema`
- 文档：[Memory / CLAUDE.md](https://docs.claude.com/en/docs/claude-code/memory) — CI 上下文注入
- 考点速记：CI 用 `-p` 防 hang；review 用独立 instance 非生成者自审；重跑时只报新/未解决问题

---

## 3.1 CLAUDE.md hierarchy

*Official skill: Configure CLAUDE.md files with appropriate hierarchy, scoping, and modular organization*

**Knowledge of**

- The CLAUDE.md configuration hierarchy: user-level (~/.claude/CLAUDE.md), project-level (.claude/CLAUDE.md or root CLAUDE.md), and directory-level (subdirectory CLAUDE.md files)
- That user-level settings apply only to that user—instructions in ~/.claude/CLAUDE.md are not shared with teammates via version control
- The @import syntax for referencing external files to keep CLAUDE.md modular (e.g., importing specific standards files relevant to each package)
- .claude/rules/ directory for organizing topic-specific rule files as an alternative to a monolithic CLAUDE.md

**Skills in**

- Diagnosing configuration hierarchy issues (e.g., a new team member not receiving instructions because they're in user-level rather than project-level configuration)
- Using @import to selectively include relevant standards files in each package's CLAUDE.md based on maintainer domain knowledge
- Splitting large CLAUDE.md files into focused topic-specific files in .claude/rules/ (e.g., testing.md, api-conventions.md, deployment.md)
- Using the /memory command to verify which memory files are loaded and diagnose inconsistent behavior across sessions

## 3.2 Slash commands and skills

*Official skill: Create and configure custom slash commands and skills*

**Knowledge of**

- Project-scoped commands in .claude/commands/ (shared via version control) vs user-scoped commands in ~/.claude/commands/ (personal)
- Skills in .claude/skills/ with SKILL.md files that support frontmatter configuration including context: fork, allowed-tools, and argument-hint
- The context: fork frontmatter option for running skills in an isolated sub-agent context, preventing skill outputs from polluting the main conversation
- Personal skill customization: creating personal variants in ~/.claude/skills/ with different names to avoid affecting teammates

**Skills in**

- Creating project-scoped slash commands in .claude/commands/ for team-wide availability via version control
- Using context: fork to isolate skills that produce verbose output (e.g., codebase analysis) or exploratory context (e.g., brainstorming alternatives) from the main session
- Configuring allowed-tools in skill frontmatter to restrict tool access during skill execution (e.g., limiting to file write operations to prevent destructive actions)
- Using argument-hint frontmatter to prompt developers for required parameters when they invoke the skill without arguments
- Choosing between skills (on-demand invocation for task-specific workflows) and CLAUDE.md (always-loaded universal standards)

## 3.3 Path-specific rules

*Official skill: Apply path-specific rules for conditional convention loading*

**Knowledge of**

- .claude/rules/ files with YAML frontmatter paths fields containing glob patterns for conditional rule activation
- How path-scoped rules load only when editing matching files, reducing irrelevant context and token usage
- The advantage of glob-pattern rules over directory-level CLAUDE.md files for conventions that span multiple directories (e.g., test files spread throughout a codebase)

**Skills in**

- Creating .claude/rules/ files with YAML frontmatter path scoping (e.g., paths: ["terraform/**/*"]) so rules load only when editing matching files
- Using glob patterns in path-specific rules to apply conventions to files by type regardless of directory location (e.g., **/*.test.tsx for all test files)
- Choosing path-specific rules over subdirectory CLAUDE.md files when conventions must apply to files spread across the codebase

## 3.4 Plan mode vs direct execution

*Official skill: Determine when to use plan mode vs direct execution*

**Knowledge of**

- Plan mode is designed for complex tasks involving large-scale changes, multiple valid approaches, architectural decisions, and multi-file modifications
- Direct execution is appropriate for simple, well-scoped changes (e.g., adding a single validation check to one function)
- Plan mode enables safe codebase exploration and design before committing to changes, preventing costly rework
- The Explore subagent for isolating verbose discovery output and returning summaries to preserve main conversation context

**Skills in**

- Selecting plan mode for tasks with architectural implications (e.g., microservice restructuring, library migrations affecting 45+ files, choosing between integration approaches with different infrastructure requirements)
- Selecting direct execution for well-understood changes with clear scope (e.g., a single-file bug fix with a clear stack trace, adding a date validation conditional)
- Using the Explore subagent for verbose discovery phases to prevent context window exhaustion during multi-phase tasks
- Combining plan mode for investigation with direct execution for implementation (e.g., planning a library migration, then executing the planned approach)

## 3.5 Iterative refinement

*Official skill: Apply iterative refinement techniques for progressive improvement*

**Knowledge of**

- Concrete input/output examples as the most effective way to communicate expected transformations when prose descriptions are interpreted inconsistently
- Test-driven iteration: writing test suites first, then iterating by sharing test failures to guide progressive improvement
- The interview pattern: having Claude ask questions to surface considerations the developer may not have anticipated before implementing
- When to provide all issues in a single message (interacting problems) versus fixing them sequentially (independent problems)

**Skills in**

- Providing 2-3 concrete input/output examples to clarify transformation requirements when natural language descriptions produce inconsistent results
- Writing test suites covering expected behavior, edge cases, and performance requirements before implementation, then iterating by sharing test failures
- Using the interview pattern to surface design considerations (e.g., cache invalidation strategies, failure modes) before implementing solutions in unfamiliar domains
- Providing specific test cases with example input and expected output to fix edge case handling (e.g., null values in migration scripts)
- Addressing multiple interacting issues in a single detailed message when fixes interact, versus sequential iteration for independent issues

## 3.6 CI/CD integration

*Official skill: Integrate Claude Code into CI/CD pipelines*

**Knowledge of**

- The -p (or --print) flag for running Claude Code in non-interactive mode in automated pipelines
- --output-format json and --json-schema CLI flags for enforcing structured output in CI contexts
- CLAUDE.md as the mechanism for providing project context (testing standards, fixture conventions, review criteria) to CI-invoked Claude Code
- Session context isolation: why the same Claude session that generated code is less effective at reviewing its own changes compared to an independent review instance

**Skills in**

- Running Claude Code in CI with the -p flag to prevent interactive input hangs
- Using --output-format json with --json-schema to produce machine-parseable structured findings for automated posting as inline PR comments
- Including prior review findings in context when re-running reviews after new commits, instructing Claude to report only new or still-unaddressed issues to avoid duplicate comments
- Providing existing test files in context so test generation avoids suggesting duplicate scenarios already covered by the test suite
- Documenting testing standards, valuable test criteria, and available fixtures in CLAUDE.md to improve test generation quality and reduce low-value test output
