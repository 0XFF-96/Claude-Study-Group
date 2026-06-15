# 阅读材料
- https://code.claude.com/docs/en/agent-sdk/subagents#tool-restrictions-2


## Benefits of using subagents

### Context isolation
Each subagent runs in its own fresh conversation. Intermediate tool calls and results stay inside the subagent; only its final message returns to the parent.

## Creating subagents

```python
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition


async def main():
    async for message in query(
        prompt="Review the authentication module for security issues",
        options=ClaudeAgentOptions(
            # Auto-approve these tools, including Agent for subagent invocation
            allowed_tools=["Read", "Grep", "Glob", "Agent"],
            agents={
                "code-reviewer": AgentDefinition(
                    # description tells Claude when to use this subagent
                    description="Expert code review specialist. Use for quality, security, and maintainability reviews.",
                    # prompt defines the subagent's behavior and expertise
                    prompt="""You are a code review specialist with expertise in security, performance, and best practices.

When reviewing code:
- Identify security vulnerabilities
- Check for performance issues
- Verify adherence to coding standards
- Suggest specific improvements

Be thorough but concise in your feedback.""",
                    # tools restricts what the subagent can do (read-only here)
                    tools=["Read", "Grep", "Glob"],
                    # model overrides the default model for this subagent
                    model="sonnet",
                ),
                "test-runner": AgentDefinition(
                    description="Runs and analyzes test suites. Use for test execution and coverage analysis.",
                    prompt="""You are a test execution specialist. Run tests and provide clear analysis of results.

Focus on:
- Running test commands
- Analyzing test output
- Identifying failing tests
- Suggesting fixes for failures""",
                    # Bash access lets this subagent run test commands
                    tools=["Bash", "Read", "Grep"],
                ),
            },
        ),
    ):
        if hasattr(message, "result"):
            print(message.result)


asyncio.run(main())
```

## 代码解释
这段代码演示了如何使用 `claude_agent_sdk`（一个用于构建 Claude 智能体的 SDK）来创建一个**多智能体系统（Multi-Agent System）**。

其核心目标是：**通过主智能体协调多个“专家”子智能体，对代码库中的身份验证模块（Authentication Module）进行安全审查。**

以下是代码的详细拆解：

### 1. 核心流程概述
这段代码启动了一个异步任务，向 Claude 发送了一个任务指令：“审查身份验证模块的安全问题”。
为了完成这个任务，Claude 不仅可以使用基本的文件操作工具，还可以根据需要**调用两个专门定义的子智能体**：一个负责代码审计，一个负责运行测试。

---

### 2. 代码组件详解

#### A. 主查询入口 (`query`)
```python
async for message in query(
    prompt="Review the authentication module for security issues",
    options=ClaudeAgentOptions(...)
)
```
*   **`prompt`**: 这是给主智能体的最高指令。
*   **`allowed_tools`**: 规定了主智能体可以直接使用的工具。特别注意 **`"Agent"`** 也是一个工具，这允许主智能体去“雇用”或“调用”下面定义的子智能体。

#### B. 子智能体定义 (`AgentDefinition`)
代码定义了两个“专家”角色：

1.  **`code-reviewer` (代码审查专家)**
    *   **职责**: 专注于安全性、性能和代码规范。
    *   **限制**: 它只被赋予了 `Read`、`Grep`、`Glob` 工具。这意味着它**只能看代码**，不能修改代码或运行系统命令，确保了审查过程的安全性（Read-only）。
    *   **模型**: 指定使用 `sonnet` 模型（通常指 Claude 3.5 Sonnet），因为它在逻辑推理和代码分析方面表现出色。

2.  **`test-runner` (测试执行专家)**
    *   **职责**: 运行测试套件、分析输出、定位失败的测试。
    *   **能力**: 它拥有 **`Bash`** 工具。这意味着它可以执行终端命令，实际运行项目中的单元测试或安全扫描工具。

#### C. 工作流逻辑
当代码运行时，Claude 内部的决策逻辑通常如下：
1.  **分析任务**：主智能体接收到“审查安全”的任务。
2.  **指派子任务**：
    *   它可能会先调用 `code-reviewer`，让它用 `Grep` 搜索代码中的敏感关键词（如 `password`, `token`, `secret`）。
    *   如果需要验证某个安全漏洞是否真的存在，它可能会调用 `test-runner` 编写并运行一个测试用例。
3.  **汇总结果**：主智能体收集各个专家的反馈，最后给出一个综合的审查报告。

#### D. 异步迭代与输出
```python
async for message in query(...):
    if hasattr(message, "result"):
        print(message.result)
```
*   这是一个异步生成器。随着任务的进展（例如某个子智能体完成了分析），SDK 会不断推送到消息。
*   当消息包含 `result` 时，将其打印出来。这通常是最终的审查报告或中间的关键结论。

---

### 3. 这段代码体现的架构思想

*   **关注点分离 (Separation of Concerns)**：不同的智能体负责不同的任务。安全专家不负责跑测试，跑测试的专家不负责深度架构分析。
*   **最小权限原则 (Least Privilege)**：给 `code-reviewer` 只读权限，防止 AI 在审查过程中意外破坏代码；而 `test-runner` 拥有 `Bash` 权限，但其 Prompt 限制它仅用于测试分析。
*   **工具化 (Tool Use)**：AI 不仅仅是聊天，而是通过 `Grep`（搜索）、`Read`（阅读）、`Bash`（执行）等工具与真实文件系统交互。

### 4. 运行前提
要运行这段代码，你通常需要：
1.  安装了该 SDK (`pip install claude_agent_sdk`)。
2.  配置了 Anthropic 的 API Key。
3.  处于一个包含代码库的工作目录中，这样 `Read`、`Grep` 等工具才有内容可以操作。

**总结：** 这是一个自动化的、基于 AI 角色的代码安全审计工作流。它模拟了人类团队中“主架构师 + 安全审计员 + 测试工程师”协作的模式。


# AgentDefinition conf
As of Claude Code v2.1.172, subagents can spawn their own subagents. A background subagent five levels below the main agent cannot spawn further subagents; foreground subagents can spawn at any depth. To prevent a subagent from spawning others, omit Agent from its tools array or add it to disallowedTools. See nested subagents for the full depth rules.

自 Claude Code v2.1.172 版本起，子智能体（Subagents）可以创建自己的子智能体。位于主智能体下方第五层的“后台子智能体”无法再进一步创建子智能体；而“前台子智能体”可以在任何深度进行创建。若要禁止某个子智能体创建其他智能体，请在其工具数组（tools array）中移除 Agent 工具，或将其添加到 disallowedTools 列表中。完整的深度规则请参阅“嵌套子智能体（nested subagents）”相关说明。
关键点解析：
递归创建：现在支持“子生孙、孙生曾孙”的模式。
后台限制 (Background Subagents)：为了防止无限循环或过度消耗资源，后台运行的子智能体在达到主智能体之下的 5 层深度后将被禁止再创建新的智能体。
前台无限制 (Foreground Subagents)：直接与用户交互或在前台运行的智能体不受此深度限制。
权限控制：
如果你希望一个子智能体能创建自己的下属，必须在它的 tools 里包含 "Agent"（正如你之前代码里写的那样）。
如果你希望禁止它创建下属，删掉 "Agent" 即可。



## Filesystem-based definition (alternative)
You can also define subagents as markdown files in .claude/agents/ directories. See the Claude Code subagents documentation for details on this approach. Programmatically defined agents take precedence over filesystem-based agents with the same name.

## Invoking subagent

### Automatic invocation
Claude automatically decides when to invoke subagents based on the task and each subagent’s description. For example, if you define a performance-optimizer.



### Explicit invocation
To guarantee Claude uses a specific subagent, mention it by name in your prompt:

```python
"Use the code-reviewer agent to check the authentication module"
```

### Dynamic agent configuration

```python
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition


# Factory function that returns an AgentDefinition
# This pattern lets you customize agents based on runtime conditions
def create_security_agent(security_level: str) -> AgentDefinition:
    is_strict = security_level == "strict"
    return AgentDefinition(
        description="Security code reviewer",
        # Customize the prompt based on strictness level
        prompt=f"You are a {'strict' if is_strict else 'balanced'} security reviewer...",
        tools=["Read", "Grep", "Glob"],
        # Key insight: use a more capable model for high-stakes reviews
        model="opus" if is_strict else "sonnet",
    )


async def main():
    # The agent is created at query time, so each request can use different settings
    async for message in query(
        prompt="Review this PR for security issues",
        options=ClaudeAgentOptions(
            allowed_tools=["Read", "Grep", "Glob", "Agent"],
            agents={
                # Call the factory with your desired configuration
                "security-reviewer": create_security_agent("strict")
            },
        ),
    ):
        if hasattr(message, "result"):
            print(message.result)


asyncio.run(main())
```

这段代码在之前“多智能体系统”的基础上，引入了**工厂模式（Factory Pattern）**。其核心目的是实现**动态配置智能体**，让智能体能够根据不同的运行环境或需求（比如安全级别）来调整自己的行为和性能。

以下是代码的详细拆解：

### 1. 核心亮点：工厂函数 `create_security_agent`
这是这段代码与之前静态定义最大的不同。

```python
def create_security_agent(security_level: str) -> AgentDefinition:
    is_strict = security_level == "strict"
    return AgentDefinition(
        description="Security code reviewer",
        # 1. 动态提示词：根据 security_level 改变 AI 的审查风格
        prompt=f"You are a {'strict' if is_strict else 'balanced'} security reviewer...",
        tools=["Read", "Grep", "Glob"],
        # 2. 动态模型选择：
        # 如果是严苛模式(strict)，使用更强大的 Opus 模型（推理能力最强，但更贵/稍慢）
        # 如果是平衡模式，使用性价比更高的 Sonnet 模型
        model="opus" if is_strict else "sonnet",
    )
```

*   **灵活切换模型**：这是一个非常实用的技巧。在处理关键任务（如生产环境的安全审查）时切换到顶级模型 `Opus`，而在日常开发中为了降低成本和提高响应速度切换到 `Sonnet`。
*   **参数化 Prompt**：通过代码逻辑动态生成 `prompt`，而不是把提示词写死。

### 2. 主查询中的应用
在调用 `query` 时，它直接在配置字典中调用了这个工厂函数：

```python
options=ClaudeAgentOptions(
    allowed_tools=["Read", "Grep", "Glob", "Agent"],
    agents={
        # 调用工厂函数，传入 "strict" 参数
        "security-reviewer": create_security_agent("strict")
    },
)
```

这样做的好处是：你可以根据外部输入（比如命令行参数、环境变量或上游逻辑）来决定这一步是要创建一个“严格的审查员”还是一个“普通的审查员”。

### 3. 这段代码展示的设计模式优势

1.  **逻辑解耦**：将“如何定义一个审查专家”的逻辑从“主流程（main）”中剥离出来。主流程只需要知道它需要一个名为 `security-reviewer` 的专家，而具体的专家配置由工厂函数负责。
2.  **资源优化**：通过模型分层（Model Tiering），在保证质量的同时控制 API 成本。
3.  **可维护性**：如果以后要增加新的安全级别（比如 `fast` 或 `compliance-only`），只需要修改工厂函数即可，不需要动到 `main` 逻辑。

### 4. 结合你之前提到的“嵌套智能体”规则
结合你之前提供的 v2.1.172 规则，这段代码在实际运行时会遵循以下逻辑：
*   **主智能体 (Main Agent)**：拥有 `Agent` 工具，它可以“生出”这个 `security-reviewer` 子智能体。
*   **子智能体 (Security Reviewer)**：注意看它的定义，它的 `tools` 数组里 **没有 `Agent`**。
    *   **结果**：这意味着这个 `security-reviewer` 是一个**末端节点**，它不能再进一步创建下属子智能体了。这符合“最小权限”和“防止失控嵌套”的安全实践。

### 总结
这段代码演示了**如何通过 Python 代码逻辑来动态控制 AI 的大脑（模型）和灵魂（Prompt）**，是构建企业级 AI Agent 工作流的推荐做法。



## Detecting subagent invocation

```python
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition, ToolUseBlock


async def main():
    async for message in query(
        prompt="Use the code-reviewer agent to review this codebase",
        options=ClaudeAgentOptions(
            allowed_tools=["Read", "Glob", "Grep", "Agent"],
            agents={
                "code-reviewer": AgentDefinition(
                    description="Expert code reviewer.",
                    prompt="Analyze code quality and suggest improvements.",
                    tools=["Read", "Glob", "Grep"],
                )
            },
        ),
    ):
        # Check for subagent invocation. Match both names: older SDK
        # versions emitted "Task", current versions emit "Agent".
        if hasattr(message, "content") and message.content:
            for block in message.content:
                if isinstance(block, ToolUseBlock) and block.name in (
                    "Task",
                    "Agent",
                ):
                    print(f"Subagent invoked: {block.input.get('subagent_type')}")

        # Check if this message is from within a subagent's context
        if hasattr(message, "parent_tool_use_id") and message.parent_tool_use_id:
            print("  (running inside subagent)")

        if hasattr(message, "result"):
            print(message.result)


asyncio.run(main())
```

这段代码的主要目的是演示**如何监控和追踪主智能体与子智能体之间的交互过程**。

与之前的代码相比，这段代码不仅关注最终结果（result），还深入到了消息的内部结构，实时观察 Claude 是如何决定调用子智能体，以及当前任务是否正在子智能体内部运行。

以下是代码的详细拆解：

### 1. 监控子智能体的调用 (Subagent Invocation)
这段代码检查了 Claude 发出的每一条消息的内容块（content blocks）：

```python
if isinstance(block, ToolUseBlock) and block.name in ("Task", "Agent"):
    print(f"Subagent invoked: {block.input.get('subagent_type')}")
```

*   **`ToolUseBlock`**: 当 Claude 决定使用一个工具时，它会生成一个“工具调用块”。
*   **`block.name in ("Task", "Agent")`**: 
    *   这是为了**兼容性**。在旧版 SDK 中，调用子智能体的工具名为 `Task`；在新版中，它被统一称为 `Agent`。
*   **作用**：一旦主智能体说“我需要 `code-reviewer` 来帮我看这段代码”，这段逻辑就会立即捕获这个意图并打印出来，让你知道子智能体被“雇佣”了。

### 2. 追踪执行上下文 (Context Tracking)
这是这段代码最核心的进阶功能：

```python
if hasattr(message, "parent_tool_use_id") and message.parent_tool_use_id:
    print("  (running inside subagent)")
```

*   **`parent_tool_use_id`**: 这是 SDK 用来标识“父级工具调用”的 ID。
*   **原理**：
    *   如果这条消息是主智能体直接发出的，这个字段通常为空。
    *   如果这条消息是**子智能体**在工作（例如 `code-reviewer` 正在读取文件或输出分析），SDK 会标记这条消息属于哪个父级任务。
*   **作用**：它可以让你在控制台中清晰地分辨出：哪些操作是主智能体做的，哪些操作是正在运行的子智能体在“后台”执行的。

### 3. 结构化的多智能体协作流
代码定义的逻辑如下：
1.  **用户指令**：“使用 code-reviewer 审查代码库”。
2.  **主智能体**：识别到它有 `Agent` 工具，并且配置里有一个叫 `code-reviewer` 的专家。
3.  **分发任务**：主智能体调用 `Agent` 工具。
4.  **实时监控**（代码逻辑）：
    *   捕获到 `ToolUseBlock` -> 打印 "Subagent invoked: code-reviewer"。
    *   接下来的消息带有 `parent_tool_use_id` -> 打印 "(running inside subagent)"。
5.  **汇总**：最后子智能体完成任务，主智能体整理结果。

### 4. 为什么要这么写？（应用场景）

*   **调试 (Debugging)**：在开发复杂的多智能体系统时，很难分清哪句话是谁说的。通过检查 `parent_tool_use_id`，你可以像查看分布式追踪（Tracing）一样，理清调用链路。
*   **用户界面反馈**：如果你在做一个 Web UI，你可以根据这些信息给用户展示动态：“主智能体正在思考...” -> “已启动代码审查专家...” -> “专家正在读取文件...”。
*   **审计与日志**：保留子智能体调用的记录，用于分析 AI 的任务分配逻辑是否合理。

### 总结
这段代码不仅是让 AI 干活，更是**给 AI 的思考过程加装了“监控探针”**。它展示了如何通过 `ToolUseBlock` 和 `parent_tool_use_id` 来实现多智能体协作的**可见性（Observability）**。

## Resuming subagents

When a subagent completes, the Agent tool result includes a text block containing agentId: <id>. The built-in Explore and Plan agents are one-shot and do not return an agentId, so use a custom agent or general-purpose when you need to resume. To resume a subagent programmatically:
1. Capture the session ID: Extract session_id from messages during the first query
2. Extract the agent ID: Parse agentId from the Agent tool result text
3. Resume the session: Pass resume: sessionId in the second query’s options, and include the agent ID in your prompt

```python
import asyncio
import re
from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition, ToolResultBlock

AGENTS = {
    "endpoint-finder": AgentDefinition(
        description="Locates and catalogs API endpoints in a codebase.",
        prompt="You find and document API endpoints. Report each endpoint's path, method, and handler.",
        tools=["Read", "Grep", "Glob"],
    )
}


def extract_agent_id(block: ToolResultBlock) -> str | None:
    """Extract agentId from an Agent tool result's text content."""
    parts = block.content if isinstance(block.content, list) else [{"text": block.content}]
    for part in parts:
        if match := re.search(r"agentId:\s*([\w-]+)", part.get("text") or ""):
            return match.group(1)
    return None


async def main():
    agent_id = None
    session_id = None

    # First invocation - run the endpoint-finder subagent
    async for message in query(
        prompt="Use the endpoint-finder agent to find all API endpoints in this codebase",
        options=ClaudeAgentOptions(allowed_tools=["Read", "Grep", "Glob", "Agent"], agents=AGENTS),
    ):
        # Capture session_id from ResultMessage (needed to resume this session)
        if hasattr(message, "session_id"):
            session_id = message.session_id
        # Search tool results for the agentId trailer
        for block in getattr(message, "content", None) or []:
            if isinstance(block, ToolResultBlock):
                agent_id = extract_agent_id(block) or agent_id
        # Print the final result
        if hasattr(message, "result"):
            print(message.result)

    # Second invocation - resume and ask follow-up
    if agent_id and session_id:
        async for message in query(
            prompt=f"Resume agent {agent_id} and list the top 3 most complex endpoints",
            options=ClaudeAgentOptions(
                allowed_tools=["Read", "Grep", "Glob", "Agent"], agents=AGENTS, resume=session_id
            ),
        ):
            if hasattr(message, "result"):
                print(message.result)


asyncio.run(main())
```

这段代码是 `claude_agent_sdk` 的进阶用法，核心演示了**如何跨请求“复活（Resume）”一个已经运行过的子智能体**。

通过保存子智能体的状态 ID，你可以在第二个请求中让 AI 接着之前的思路继续工作，而不需要重新扫描代码库。

以下是代码的详细分析：

### 1. 核心组件：`agentId` 提取器
```python
def extract_agent_id(block: ToolResultBlock) -> str | None:
    """从 Agent 工具结果的文本内容中提取 agentId。"""
    # ... 使用正则表达式查找 "agentId: xxxx-xxxx" ...
```
*   **背景**：当主智能体调用子智能体并运行结束时，SDK 会在工具结果的末尾附加一段类似 `agentId: 550e8400-e29b...` 的文本。
*   **作用**：这个 ID 就像是这个子智能体的“存档点（Checkpoint）”。有了它，你就能在以后重新找回这个特定的“大脑状态”。

### 2. 第一次调用：建立上下文并保存状态
在第一个 `query` 块中，代码做了三件事：
1.  **启动任务**：让 `endpoint-finder` 查找所有 API 端点。
2.  **获取 `session_id`**：这是整个主对话的 ID。
    ```python
    if hasattr(message, "session_id"):
        session_id = message.session_id
    ```
3.  **捕获 `agent_id`**：当子智能体扫描完代码，代码通过 `extract_agent_id` 把存档 ID 存下来。

### 3. 第二次调用：断点续传（Resume）
这是整段代码最关键的部分：
```python
if agent_id and session_id:
    async for message in query(
        prompt=f"Resume agent {agent_id} and list the top 3 most complex endpoints",
        options=ClaudeAgentOptions(
            # 关键点 1: 传入之前的 session_id，恢复对话流
            resume=session_id,
            # ... 其他配置 ...
        ),
    ):
        # ...
```
*   **`resume=session_id`**：这告诉 SDK，“不要开启新对话，请加载我之前的那个 session”。
*   **Prompt 引用**：提示词里明确说 `Resume agent {agent_id}`。此时，主智能体会去查找存档中对应 ID 的子智能体。
*   **状态继承**：**非常重要！** 在第二次调用时，`endpoint-finder` **不需要**再次运行 `Grep` 或 `Read`。它已经记得第一次调用时找到的所有端点信息。它直接基于之前的记忆，分析并回答“哪三个最复杂”。

---

### 4. 为什么要这样设计？（架构优势）

1.  **节省 Token 和成本**：
    如果代码库很大，扫描一次可能消耗成千上万个 Token。通过恢复（Resume），你只需要扫描一次。后续所有的提问（比如“分析性能”、“检查权限”）都基于第一次扫描的结果，无需重复读取文件。

2.  **保持逻辑连贯性**：
    AI 的推理过程也会被保存。如果子智能体在第一次任务中产生了一些中间结论，在恢复后，这些结论依然有效。

3.  **解决“长对话”压力**：
    相比于把所有东西都塞进一个巨大的 Prompt，这种方式允许你把任务分解成多个步骤，每个步骤只在需要时恢复相关的子智能体。

### 5. 总结流程
1.  **执行任务** -> **获取 SessionID 和 AgentID**。
2.  **保存 IDs**（可以存在数据库或变量里）。
3.  **后续请求** -> **传入 SessionID** -> **指名道姓恢复 AgentID**。
4.  **结果**：AI 带着之前的记忆直接回答新问题。

**一句话总结：** 这段代码展示了如何给 AI Agent 加上“存档”和“读档”功能，从而实现高效的、跨会话的复杂任务处理。



## Tool restrictions

```python
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition


async def main():
    async for message in query(
        prompt="Analyze the architecture of this codebase",
        options=ClaudeAgentOptions(
            allowed_tools=["Read", "Grep", "Glob", "Agent"],
            agents={
                "code-analyzer": AgentDefinition(
                    description="Static code analysis and architecture review",
                    prompt="""You are a code architecture analyst. Analyze code structure,
identify patterns, and suggest improvements without making changes.""",
                    # Read-only tools: no Edit, Write, or Bash access
                    tools=["Read", "Grep", "Glob"],
                )
            },
        ),
    ):
        if hasattr(message, "result"):
            print(message.result)


asyncio.run(main())

```

这段代码展示了如何利用 `claude_agent_sdk` 构建一个**受限的、专注于只读分析的专家子智能体**，来完成代码库架构分析任务。

这是多智能体架构中最经典、最安全的一个应用场景。以下是详细分析：

### 1. 核心设计：职责分离与安全约束
这段代码最值得关注的地方在于其**权限控制**：

*   **只读工具集（Read-only tools）**：
    在 `code-analyzer` 的定义中，只给了 `Read`（读文件）、`Grep`（正则搜索）和 `Glob`（列出文件列表）三个工具。
    *   **分析**：它被明确剥夺了 `Write`（写）、`Edit`（编辑）或 `Bash`（执行系统命令）的权限。
    *   **意义**：这确保了即便 AI 对架构有非常大胆的改进想法，它也**绝对无法修改你的任何一行代码**，从而保证了代码库的安全和纯净。

### 2. 角色定位：架构分析专家
```python
prompt="""You are a code architecture analyst. Analyze code structure, 
identify patterns, and suggest improvements without making changes."""
```
*   **Prompt 设定**：通过系统提示词，将该子智能体定位为“架构分析师”。
*   **任务目标**：它会寻找设计模式（如 MVC、微服务、依赖注入等），并从宏观角度提供改进建议，而不是纠结于小的语法错误。

### 3. 工作流程模拟
当你运行这段代码时，后台会发生以下步骤：

1.  **任务下发**：用户向主智能体发出指令：“分析这个代码库的架构”。
2.  **专家委派**：主智能体意识到这是一个专业的架构任务，于是通过 `Agent` 工具调用 `code-analyzer`。
3.  **信息收集**：
    *   `code-analyzer` 首先会使用 `Glob` 遍历目录，了解项目整体结构（如 `/src`, `/tests`, `/api` 等）。
    *   它可能会用 `Grep` 搜索特定的框架关键词（如 `React`, `Django`, `Spring`）。
    *   它会用 `Read` 读取关键的配置文件（如 `package.json`, `pom.xml`, `requirements.txt`）。
4.  **架构推理**：基于收集到的信息，子智能体在内部构建起对项目逻辑流转和组件关系的理解。
5.  **生成报告**：最后汇总成一份架构文档，返回给主智能体，主智能体再输出给用户。

### 4. 代码结构亮点
*   **封装性**：`code-analyzer` 的所有分析逻辑都封装在 `AgentDefinition` 中。如果以后你想把架构分析换成性能分析，只需要换一个专家定义，而不需要改动 `main` 函数。
*   **异步流**：使用 `async for message in query(...)` 能够让你在主程序中实时感知任务的进度，而不是死等结果。

### 5. 适用场景建议
这段代码非常适合集成到：
*   **CI/CD 流水线**：在代码提交后，自动生成一份架构变动报告。
*   **新入职开发者辅助**：帮助新人快速理清庞大遗留代码（Legacy Code）的项目结构。
*   **重构前调研**：在进行大规模重构前，让 AI 评估当前的耦合度和模式问题。

### 总结
与你之前看过的“自动测试”或“动态创建”不同，这段代码强调的是 **“专家系统的专业性”** 和 **“操作的安全性”**。它是一个低风险、高收益的 AI 辅助开发工具示例。


