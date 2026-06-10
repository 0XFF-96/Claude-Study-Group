# Domain 4: Prompt Engineering & Structured Output (20%)

> Reference detail for the [CCA-F checklist](../CCA-F.md). Source: official study guide skills breakdown.

## 推荐阅读

**考试权重：20%**

### 本 Domain 总览

| 类型 | 资源 | 说明 |
|------|------|------|
| 课程 | [Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api) | Prompting、structured output、tool use — 覆盖 4.1–4.5 |
| 课程 | [Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action) | Multi-pass review、CI structured output — 覆盖 4.6 |
| 文档 | [Prompt engineering](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview) | Explicit criteria、few-shot、examples |
| 文档 | [Tool use](https://docs.claude.com/en/docs/build-with-claude/tool-use) | `tool_use` + JSON schema、`tool_choice` |
| 文档 | [Structured outputs (SDK)](https://code.claude.com/docs/en/agent-sdk/structured-outputs) | `outputFormat`、validation retry |
| 文档 | [Batch processing](https://docs.claude.com/en/docs/build-with-claude/batch-processing) | Message Batches API、50% 成本、`custom_id` |
| 文档 | [Messages Batch API reference](https://docs.claude.com/en/api/messages-batch) | API 参数、限制 |
| 刷题 | [CertSafari — Domain 4](https://www.certsafari.com/anthropic/claude-certified-architect) | 选 Domain Mode → Prompt Engineering |

**建议学习顺序：** 4.1 → 4.2 → 4.3 → 4.4 → 4.5 → 4.6

### 按子主题

#### [4.1 Explicit criteria](#41-explicit-criteria)

- 课程：[Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api) — review criteria 设计
- 文档：[Prompt engineering](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview) — 具体标准 vs 模糊指令
- 考点速记："be conservative" 无效；高 FP 类别先 disable 恢复信任；severity 用代码示例定义

#### [4.2 Few-shot prompting](#42-few-shot-prompting)

- 课程：[Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api) — few-shot 模块
- 文档：[Prompt engineering](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview) — 2–4 个 targeted examples
- 考点速记：ambiguous case 展示 reasoning；extraction 任务减少 hallucination；格式一致性

#### [4.3 Structured output](#43-structured-output)

- 课程：[Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api) — tool use + schema
- 文档：[Tool use](https://docs.claude.com/en/docs/build-with-claude/tool-use) — `tool_choice` auto / any / forced
- 文档：[Structured outputs (SDK)](https://code.claude.com/docs/en/agent-sdk/structured-outputs) — JSON Schema、Zod/Pydantic
- 考点速记：schema 消除 syntax error 不防 semantic error；nullable 字段防 fabrication；enum + "other"

#### [4.4 Validation, retry, and feedback loops](#44-validation-retry-and-feedback-loops)

- 课程：[Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api) — validation flows
- 文档：[Structured outputs (SDK)](https://code.claude.com/docs/en/agent-sdk/structured-outputs) — retry limit、error handling
- 文档：[Prompt engineering](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview) — 反馈循环设计
- 考点速记：信息根本不在文档里 → retry 无效；`detected_pattern` 分析 FP；`calculated_total` vs `stated_total`

#### [4.5 Batch processing](#45-batch-processing)

- 课程：[Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api) — batch 策略
- 文档：[Batch processing](https://docs.claude.com/en/docs/build-with-claude/batch-processing) — 50% 折扣、≤24h、无 SLA
- 文档：[Messages Batch API](https://docs.claude.com/en/api/messages-batch) — `custom_id` 关联
- 考点速记：blocking pre-merge → sync API；overnight audit → batch；单 request 不支持 multi-turn tool calling

#### [4.6 Multi-pass review](#46-multi-pass-review)

- 课程：[Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action) — 独立 review instance
- 文档：[Structured outputs (SDK)](https://code.claude.com/docs/en/agent-sdk/structured-outputs) — multi-step tool use 后结构化输出
- 文档：[Agent SDK Overview](https://docs.claude.com/en/api/agent-sdk/overview) — 多 instance 架构
- 考点速记：同 session 自审 < 独立 reviewer；大 review → per-file local + cross-file integration 两 pass

---

## 4.1 Explicit criteria

*Official skill: Design prompts with explicit criteria to improve precision and reduce false positives*

**Knowledge of**

- The importance of explicit criteria over vague instructions (e.g., "flag comments only when claimed behavior contradicts actual code behavior" vs "check that comments are accurate")
- How general instructions like "be conservative" or "only report high-confidence findings" fail to improve precision compared to specific categorical criteria
- The impact of false positive rates on developer trust: high false positive categories undermine confidence in accurate categories

**Skills in**

- Writing specific review criteria that define which issues to report (bugs, security) versus skip (minor style, local patterns) rather than relying on confidence-based filtering
- Temporarily disabling high false-positive categories to restore developer trust while improving prompts for those categories
- Defining explicit severity criteria with concrete code examples for each severity level to achieve consistent classification

## 4.2 Few-shot prompting

*Official skill: Apply few-shot prompting to improve output consistency and quality*

**Knowledge of**

- Few-shot examples as the most effective technique for achieving consistently formatted, actionable output when detailed instructions alone produce inconsistent results
- The role of few-shot examples in demonstrating ambiguous-case handling (e.g., tool selection for ambiguous requests, branch-level test coverage gaps)
- How few-shot examples enable the model to generalize judgment to novel patterns rather than matching only pre-specified cases
- The effectiveness of few-shot examples for reducing hallucination in extraction tasks (e.g., handling informal measurements, varied document structures)

**Skills in**

- Creating 2-4 targeted few-shot examples for ambiguous scenarios that show reasoning for why one action was chosen over plausible alternatives
- Including few-shot examples that demonstrate specific desired output format (location, issue, severity, suggested fix) to achieve consistency
- Providing few-shot examples distinguishing acceptable code patterns from genuine issues to reduce false positives while enabling generalization
- Using few-shot examples to demonstrate correct handling of varied document structures (inline citations vs bibliographies, methodology sections vs embedded details)
- Adding few-shot examples showing correct extraction from documents with varied formats to address empty/null extraction of required fields

## 4.3 Structured output

*Official skill: Enforce structured output using tool use and JSON schemas*

**Knowledge of**

- Tool use (tool_use) with JSON schemas as the most reliable approach for guaranteed schema-compliant structured output, eliminating JSON syntax errors
- The distinction between tool_choice: "auto" (model may return text instead of calling a tool), "any" (model must call a tool but can choose which), and forced tool selection (model must call a specific named tool)
- That strict JSON schemas via tool use eliminate syntax errors but do not prevent semantic errors (e.g., line items that don't sum to total, values in wrong fields)
- Schema design considerations: required vs optional fields, enum fields with "other" + detail string patterns for extensible categories

**Skills in**

- Defining extraction tools with JSON schemas as input parameters and extracting structured data from the tool_use response
- Setting tool_choice: "any" to guarantee structured output when multiple extraction schemas exist and the document type is unknown
- Forcing a specific tool with tool_choice: {"type": "tool", "name": "extract_metadata"} to ensure a particular extraction runs before enrichment steps
- Designing schema fields as optional (nullable) when source documents may not contain the information, preventing the model from fabricating values to satisfy required fields
- Adding enum values like "unclear" for ambiguous cases and "other" + detail fields for extensible categorization
- Including format normalization rules in prompts alongside strict output schemas to handle inconsistent source formatting

## 4.4 Validation, retry, and feedback loops

*Official skill: Implement validation, retry, and feedback loops for extraction quality*

**Knowledge of**

- Retry-with-error-feedback: appending specific validation errors to the prompt on retry to guide the model toward correction
- The limits of retry: retries are ineffective when the required information is simply absent from the source document (vs format or structural errors)
- Feedback loop design: tracking which code constructs trigger findings (detected_pattern field) to enable systematic analysis of dismissal patterns
- The difference between semantic validation errors (values don't sum, wrong field placement) and schema syntax errors (eliminated by tool use)

**Skills in**

- Implementing follow-up requests that include the original document, the failed extraction, and specific validation errors for model self-correction
- Identifying when retries will be ineffective (e.g., information exists only in an external document not provided) versus when they will succeed (format mismatches, structural output errors)
- Adding detected_pattern fields to structured findings to enable analysis of false positive patterns when developers dismiss findings
- Designing self-correction validation flows: extracting "calculated_total" alongside "stated_total" to flag discrepancies, adding "conflict_detected" booleans for inconsistent source data

## 4.5 Batch processing

*Official skill: Design efficient batch processing strategies*

**Knowledge of**

- The Message Batches API: 50% cost savings, up to 24-hour processing window, no guaranteed latency SLA
- Batch processing is appropriate for non-blocking, latency-tolerant workloads (overnight reports, weekly audits, nightly test generation) and inappropriate for blocking workflows (pre-merge checks)
- The batch API does not support multi-turn tool calling within a single request (cannot execute tools mid-request and return results)
- custom_id fields for correlating batch request/response pairs

**Skills in**

- Matching API approach to workflow latency requirements: synchronous API for blocking pre-merge checks, batch API for overnight/weekly analysis
- Calculating batch submission frequency based on SLA constraints (e.g., 4-hour windows to guarantee 30-hour SLA with 24-hour batch processing)
- Handling batch failures: resubmitting only failed documents (identified by custom_id) with appropriate modifications (e.g., chunking documents that exceeded context limits)
- Using prompt refinement on a sample set before batch-processing large volumes to maximize first-pass success rates and reduce iterative resubmission costs

## 4.6 Multi-pass review

*Official skill: Design multi-instance and multi-pass review architectures*

**Knowledge of**

- Self-review limitations: a model retains reasoning context from generation, making it less likely to question its own decisions in the same session
- Independent review instances (without prior reasoning context) are more effective at catching subtle issues than self-review instructions or extended thinking
- Multi-pass review: splitting large reviews into per-file local analysis passes plus cross-file integration passes to avoid attention dilution and contradictory findings

**Skills in**

- Using a second independent Claude instance to review generated code without the generator's reasoning context
- Splitting large multi-file reviews into focused per-file passes for local issues plus separate integration passes for cross-file data flow analysis
- Running verification passes where the model self-reports confidence alongside each finding to enable calibrated review routing
