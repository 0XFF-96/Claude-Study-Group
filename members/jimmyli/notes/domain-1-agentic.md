# Domain 1 — Agentic Architecture & Orchestration Notes

Your own notes for Domain 1. Add one file per domain (or per topic) under `notes/`.
Notes are free-form — write whatever helps you remember. Diagrams, gotchas, exam tips.

## Example topic: the agentic loop

- Continue the loop while `stop_reason == "tool_use"`; stop when `end_turn`.
- Tool results get appended to conversation history so the model reasons about the next step.

## Gotchas / exam traps

- Don't terminate by parsing natural-language signals or by a hard iteration cap.
- Subagents do **not** inherit the coordinator's context — pass findings explicitly in the prompt.
