# Cloud Study Group — Claude Certified Architect (CCA-F)

A study group working toward the **Claude Certified Architect – Foundations (CCA-F)**.
We track everyone's progress in one place, keep our own notes, and check in weekly.

## 📊 Where is everyone?

→ **[PROGRESS.md](PROGRESS.md)** — auto-generated overview of every member's progress per domain.

## 🚀 Quick start (3 steps)

```bash
git clone <repo-url> && cd Claude-Study-Group
cp -r members/_TEMPLATE members/<your-github-username>   # 1. make your folder
# 2. fill in profile.md, then tick boxes in progress.md as you learn
git add members/<your-github-username> && git commit -m "join" && git pull --rebase && git push   # 3. push
```

The bot adds you to the overview automatically. Full instructions: **[GUIDE.md](GUIDE.md)**.

## 🗂️ Repo layout

| Path | What |
|------|------|
| [GUIDE.md](GUIDE.md) | How to participate — read this first |
| [PROGRESS.md](PROGRESS.md) | Auto-generated group progress table (don't edit by hand) |
| [syllabus/CCA-F.md](syllabus/CCA-F.md) | The 30-subdomain master checklist (tick boxes in your own `progress.md`) |
| [syllabus/domains/](syllabus/domains/) | Detailed per-domain reference (Knowledge of / Skills in for each subdomain) |
| [members/](members/) | One folder per person: profile, progress, notes, weekly log |
| [members/_TEMPLATE/](members/_TEMPLATE/) | Copy this to create your folder |
| [resources/](resources/) | Shared docs, courses, practice questions |
| [scripts/update_progress.py](scripts/update_progress.py) | Builds the progress table from everyone's checkboxes |

## ⚙️ How tracking works

Each person ticks `- [ ]` → `- [x]` boxes in their own `progress.md`. A
[GitHub Action](.github/workflows/update-progress.yml) runs weekly (and on every push) to count
the boxes per domain and regenerate [PROGRESS.md](PROGRESS.md). Nobody edits the shared table —
so direct pushes to `main` rarely conflict.

## 🎯 The exam: CCA-F domains

1. Agentic Architecture & Orchestration (27%)
2. Tool Design & MCP Integration (18%)
3. Claude Code Configuration & Workflows (20%)
4. Prompt Engineering & Structured Output (20%)
5. Context Management & Reliability (15%)

60 multiple-choice questions · 120 minutes · closed-book · pass = 720 / 1000.

Blueprint & practice questions: **[CertSafari CCA-F](https://www.certsafari.com/anthropic/claude-certified-architect)**.

Happy studying — see you on the leaderboard. 🟢🎯✅
