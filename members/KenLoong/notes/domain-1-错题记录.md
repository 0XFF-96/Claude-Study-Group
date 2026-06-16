以下是针对这道 **Claude 认证架构师 — 基础认证 (CCA-F)** 模拟题及其解析的完整中英双语翻译：
---

### **Question (题目)**

**English:**
A travel application uses a Claude-powered agent to call a `search_flights` tool. The external flight API requires the `date` parameter to be in a strict `YYYY-MM-DD` format and will fail otherwise. Despite prompt engineering, the model occasionally provides natural language dates (e.g., 'tomorrow'). Which of the following is the most robust and recommended method to ensure the model provides a correctly formatted date string to the tool?

**中文：**
一个旅游应用程序使用由 Claude 驱动的智能体来调用 `search_flights`（搜索航班）工具。外部航班 API 要求 `date`（日期）参数必须采用严格的 `YYYY-MM-DD` 格式，否则会调用失败。尽管进行了提示词工程（prompt engineering），模型偶尔仍会提供自然语言日期（例如“明天”）。以下哪项是确保模型向工具提供正确格式日期字符串的最**鲁棒（稳健）**且**推荐**的方法？

---

### **Options & Explanations (选项与解析)**

#### **A) Validation Function (验证函数)**
*   **Option (选项):**
    *   **En:** In the application code, implement a validation function that checks the date format *after* receiving the tool call from Claude but *before* calling the external API. If validation fails, return an error message to the model.
    *   **中：** 在应用程序代码中实现一个验证函数，在接收到 Claude 的工具调用**之后**但在调用外部 API **之前**检查日期格式。如果验证失败，则向模型返回错误消息。
*   **Explanation (解析):**
    *   **En:** **Incorrect.** While this is a valid **defensive** programming pattern, it is not the most **robust** or efficient method. This approach is **reactive**, requiring an additional round-trip with the model to correct the error after it has already occurred. This increases latency and cost, **whereas** using `strict: true` prevents the error **proactively**.
    *   **中：** **错误。** 虽然这是一种有效的**防御性（defensive）**编程模式，但它不是最**鲁棒（robust）**或最高效的方法。这种方法是**响应式（reactive）**的，需要与模型进行额外的回合交互才能在错误发生后对其进行纠正。这增加了延迟和成本，**而**使用 `strict: true` 可以**主动地（proactively）**防止错误发生。

#### **B) System Prompt Refinement (优化系统提示词)**
*   **Option (选项):**
    *   **En:** **Refine** the system prompt with a stronger negative constraint, such as: 'CRITICAL: The date parameter must always be in YYYY-MM-DD format. Failure to **comply** will result in an error.'
    *   **中：** **细化（Refine）**系统提示词，加入更强的负面约束，例如：“关键要求：date 参数必须始终采用 YYYY-MM-DD 格式。未能**遵守（comply）**将导致错误。”
*   **Explanation (解析):**
    *   **En:** **Incorrect.** The scenario **explicitly** states that prompt engineering has already proven **insufficient**. While providing clear instructions and examples in the prompt is a best practice, it does not provide a hard guarantee of **compliance**. The `strict: true` tool property is the recommended **mechanism** for **enforcing** schema **adherence**.
    *   **中：** **错误。** 场景中**显式（explicitly）**说明了提示词工程已被证明是**不足够的（insufficient）**。虽然在提示词中提供清晰的指令和示例是最佳实践，但它不能提供**合规性（compliance）**的硬性保证。`strict: true` 工具属性才是**强制执行（enforcing）**架构**坚持/遵循（adherence）**的推荐**机制（mechanism）**。

#### **C) PostToolUse Hook (使用 PostToolUse 钩子)**
*   **Option (选项):**
    *   **En:** Implement a `PostToolUse` hook that catches the API crash, parses the natural language date into the correct format, and automatically re-triggers the `search_flights` tool call.
    *   **中：** 实现一个 `PostToolUse` 钩子来捕获 API 崩溃，将自然语言日期解析为正确格式，并自动重新触发 `search_flights` 工具调用。
*   **Explanation (解析):**
    *   **En:** **Incorrect.** This is a complex and **brittle** error-handling strategy. It relies on the external API failing in a **predictable** way and requires building and maintaining custom parsing logic for various natural language formats. It is far more **robust** and efficient to **enforce** the correct format **proactively** at the model generation step using the `strict: true` tool property.
    *   **中：** **错误。** 这是一种复杂且**脆弱的（brittle）**错误处理策略。它依赖于外部 API 以**可预测（predictable）**的方式报错，并且需要针对各种自然语言格式构建和维护自定义解析逻辑。使用 `strict: true` 工具属性在模型生成步骤中**主动（proactively）**且**强制执行（enforce）**正确格式要鲁棒和高效得多。

#### **D) JSON Schema with `strict: true` (使用 JSON 架构及严格模式) —— [正确答案]**
*   **Option (选项):**
    *   **En:** In the tool's `input_schema`, define the `date` parameter with a `type` of `string` and a `pattern` property containing a regex for `YYYY-MM-DD`. To guarantee **compliance**, also set `strict: true` in the tool definition.
    *   **中：** 在工具的 `input_schema`（输入架构）中，将 `date` 参数定义为 `string` 类型，并使用包含 `YYYY-MM-DD` 正则表达式的 `pattern` 属性。为了确保**合规性（compliance）**，还要在工具定义中设置 `strict: true`。
*   **Explanation (解析):**
    *   **En:** **Correct.** According to **Anthropic**'s documentation, setting `strict: true` on a tool definition guarantees that Claude's tool inputs will match the provided JSON Schema. This is achieved by **constraining** the model's token sampling to only generate schema-valid outputs. This is the most **robust** and recommended method as it prevents the invalid tool call from ever being generated, ensuring reliability without extra application logic.
    *   **中：** **正确。** 根据 **Anthropic** 的文档，在工具定义上设置 `strict: true` 可以保证 Claude 的工具输入将符合提供的 JSON Schema。这是通过**制约（constraining）**模型的 Token 采样，使其仅生成符合架构要求的输出来实现的。这是最**鲁棒（robust）**且最受推荐的方法，因为它从源头上防止了无效工具调用的生成，无需额外的应用程序逻辑即可确保可靠性。