# 资料来源
- https://code.claude.com/docs/en/agent-sdk/agent-loop#keep-context-efficient 
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview


- A turn is one round trip inside the loop

- AssistantMessage: emitted after each Claude response, including the final text-only one. Contains text content blocks and tool call blocks from that turn.

- The effort option controls how much reasoning Claude applies (low/medium/high/xhigh/max)
    - Extended thinking is a separate feature that produces visible chain-of-thought blocks in the output. They are independent: you can set effort: "low" with extended thinking enabled, or effort: "max" without it.

# context window
- When the context window approaches its limit, the SDK automatically compacts the conversation: it summarizes older history to free space, keeping your most recent exchanges and key decisions intact. The SDK emits a message with type: "system" and subtype: "compact_boundary" in the stream when this happens
    - 当上下文窗口接近其上限时，SDK 会自动对对话进行压缩 (compact)：它会总结较旧的历史记录以释放空间，同时确保您最近的对话往来和关键决策保持完整。当此情况发生时，SDK 会在流（stream）中发送一条 type 为 "system" 且 subtype 为 "compact_boundary"

针对长期运行智能体的几种策略：
- 使用子智能体（subagents）处理子任务：每个子智能体都会开启一段全新的对话（没有之前的消息历史，但会加载自身的系统提示词和项目级上下文，如 CLAUDE.md）。子智能体无法看到父智能体的对话轮次，且只有其最终回复会作为工具执行结果返回给父智能体。这样，主智能体的上下文仅会因该“结果摘要”而增加，而不会加载子任务的完整对话记录。详见“子智能体继承内容”获取更多细节。
- 精选工具：每一个工具定义都会占用上下文空间。请利用 AgentDefinition 中的 tools 字段，将子智能体可调用的工具限制在执行任务所需的最小集合内。
- 留意 MCP 服务器开销：默认情况下，MCP 工具搜索会延迟加载 MCP 工具架构（schemas），仅在需要时加载。但在关闭工具搜索、使用 Vertex AI 或使用非官方的 ANTHROPIC_BASE_URL 时，每个 MCP 服务器都会将所有工具架构添加到每次请求中。因此，如果使用了几个包含大量工具的服务器，在智能体开始工作之前，就可能消耗掉大量的上下文空间。
- 对常规任务使用较低的投入（effort）等级：对于只需要读取文件或列出目录的智能体，将 effort 参数设置为 "low"。这可以降低 Token 使用量并减少成本。



- Persistent rules belong in CLAUDE.md (loaded via settingSources) rather than in the initial prompt, because CLAUDE.md content is re-injected on every request.

# Handle the result
When the loop ends, the ResultMessage tells you what happened and gives you the output. The subtype field (available in both SDKs) is the primary way to check termination state.

The result field (the final text output) is only present on the success variant, so always check the subtype before reading it.


The result also includes a stop_reason field (string | null in TypeScript, str | None in Python) indicating why the model stopped generating on its final turn. Common values are end_turn (model finished normally), max_tokens (hit the output token limit), and refusal (the model declined the request). On error result subtypes, stop_reason carries the value from the last assistant response before the loop ended. To detect refusals, check stop_reason === "refusal" (TypeScript) or stop_reason == "refusal" (Python).

# Hooks
Hooks are callbacks that fire at specific points in the loop: before a tool runs, after it returns, when the agent finishes, and so on.

Hooks run in your application process, not inside the agent’s context window, so they don’t consume context.

# code example
```python
import anthropic

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=[{"type": "web_search_20260209", "name": "web_search"}],
    messages=[{"role": "user", "content": "What's the latest on the Mars rover?"}],
)
print(response.content)
```


这段代码展示了如何使用 Anthropic 的 Python SDK 调用 Claude 模型，并赋予它**联网搜索（Web Search）**的能力。

以下是代码的详细解释：

### 1. 导入与初始化
```python
import anthropic

client = anthropic.Anthropic()
```
*   导入 `anthropic` 库。
*   创建一个客户端实例。它会自动从你的环境变量中读取 `ANTHROPIC_API_KEY`。

### 2. 创建消息请求
```python
response = client.messages.create(
    model="claude-opus-4-8", # 使用的模型版本
    max_tokens=1024,         # 最大输出长度
    ...
)
```
*   **`model="claude-opus-4-8"`**: 这里指定了使用 Claude 的 Opus 模型（从命名看这似乎是一个预设的未来版本）。Opus 通常是 Claude 系列中推理能力最强的模型。
*   **`max_tokens=1024`**: 限制 AI 回复的最大长度为 1024 个 Token。

### 3. 配置工具（核心部分）
```python
    tools=[{"type": "web_search_20260209", "name": "web_search"}],
```
*   这是这段代码的关键。它给 Claude 配备了一个**服务端工具（Server Tool）**。
*   **`type: "web_search_20260209"`**: 指定了 Anthropic 内置的联网搜索工具。
*   由于这是一个**服务端工具**（正如你之前翻译的文档所言），你**不需要**自己写爬虫或调用 Google API。Anthropic 的服务器会自动帮你执行搜索。

### 4. 用户输入
```python
    messages=[{"role": "user", "content": "What's the latest on the Mars rover?"}],
```
*   向 Claude 提问：“关于火星车最新的消息是什么？”
*   这是一个实时性问题。如果没有联网工具，Claude 只能根据训练数据回答旧信息；有了这个工具，它可以搜索互联网来回答最新的动态。

### 5. 输出结果
```python
print(response.content)
```
*   打印 Claude 返回的内容。
*   **背后的逻辑**：
    1.  Claude 接收到问题，意识到需要最新信息。
    2.  Claude 决定调用 `web_search` 工具。
    3.  Anthropic 后端执行搜索并返回网页内容给 Claude。
    4.  Claude 整合搜索结果，写出一篇关于火星车的近况总结。
    5.  你拿到的 `response.content` 就是最终生成的总结。

### 总结
这段代码演示了**“增强型生成”（RAG 的变体）**：通过给 AI 挂载一个联网搜索工具，让它能够突破训练数据的截止日期，回答实时发生的新闻。由于使用的是服务端工具，开发者的代码非常简洁，不需要处理复杂的搜索执行逻辑。

# agent实例的理解
在你提供的这段 Python 代码中，**严格来说，并没有一个“Agent 实例”**。

这段代码使用的是 Anthropic 的 **Messages API（基础消息接口）**，而不是你在之前翻译的文档中看到的 **Agent SDK（智能体开发工具包）**。

为了让你彻底理解，我从以下三个维度来拆解：

### 1. 为什么这段代码里没有 Agent 实例？

在这段代码中：
*   `client = anthropic.Anthropic()` 只是一个 **API 客户端**，它负责把你的指令发送给服务器。
*   `client.messages.create(...)` 是一次 **单次的、无状态的请求**。
*   虽然你传入了 `tools`（联网搜索），但处理逻辑是：你发一个请求 -> 模型回一个结果。如果模型想多次调用工具，或者任务没完成，你需要自己写 `while` 循环去处理多次对话。

**它像是一个“接线员”：** 你问一个问题，他查一下，回你一个答案。任务结束后，他就不再管了。

---

### 2. 什么是真正的“Agent 实例”？

根据你之前翻译的文档（提到了 `AgentDefinition`、`ResultMessage`、`subtype: "init"` 等），一个 **Agent 实例（智能体实例）** 通常是指 SDK 中一个更高层的对象（例如在 Anthropic Agent SDK 中的 `Agent` 类）。

一个真正的 **Agent 实例** 具备以下三个核心特征：

*   **自主循环 (The Agent Loop)**：它不仅是“问与答”，它会自动运行。比如它发现搜一次网页不够，它会自动发起第二次搜索，直到解决问题，而不需要你手动写代码去处理中间过程。
*   **状态管理 (State & Memory)**：它拥有“生命周期”。你之前翻译的 `subtype: "init"` 就是它诞生的标志。它会记住这个会话（Session ID），管理上下文的压缩（Compaction）。
*   **权限与回调 (Control)**：它能处理你在翻译中看到的 `tool approval callback`（工具审批回调）。它是一个有生命力的实体，在运行过程中会不断弹出来问你：“我可以执行这个 Bash 命令吗？”

---

### 3. 如何通俗地理解“Agent 实例”？

你可以用“**外包员工**”来类比：

*   **普通的 API 调用（你提供的代码）**：
    这更像是**查字典**。你查一个词，字典给你一个解释。字典本身不动，也不思考，它只是响应你的查询。
*   **Agent 实例（智能体实例）**：
    这更像是**雇佣了一个实习生**。
    1.  **实例化（init）**：你把实习生招进来，给他配了电脑（工具：Bash、搜索）和规章制度（System Prompt）。
    2.  **执行（Agent Loop）**：你跟他说“帮我写个网站并部署”。他会自己去写代码、报错了自己调试、搜资料、最后告诉你做完了。
    3.  **生命周期**：他工作累了（上下文满了）会自动整理笔记（Compaction）；遇到危险操作会问你（Approval）；最后工作结束给你一份总结报告（ResultMessage）。

### 总结

你提供的代码只是**“给模型配了把扳手”**，但**“拿扳手的人”是你（你的 Python 脚本）**。

而在你之前翻译的文档中，**Agent 实例** 是那个**“拿扳手的人”**。它是一个自动化的对象，封装了思考、调用工具、处理错误和管理记忆的全部复杂逻辑。

如果你想在代码中看到 Agent 实例，你通常会看到类似这样的结构（伪代码）：
```python
# 这才是 Agent 实例化的样子
agent = client.agents.create(
    name="MyResearcher",
    model="claude-3-5-sonnet",
    tools=[...]
)

# 启动智能体循环，它会自动处理所有中间步骤
result = agent.run("帮我调研火星车并写一份报告") 
```
