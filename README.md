# Cloud Study Group — AWS SAA-C03

A study group working toward the **AWS Certified Solutions Architect – Associate (SAA-C03)**.
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
| [syllabus/SAA-C03.md](syllabus/SAA-C03.md) | The exam blueprint & master topic checklist |
| [members/](members/) | One folder per person: profile, progress, notes, weekly log |
| [members/_TEMPLATE/](members/_TEMPLATE/) | Copy this to create your folder |
| [resources/](resources/) | Shared courses, docs, practice exams |
| [scripts/update_progress.py](scripts/update_progress.py) | Builds the progress table from everyone's checkboxes |

## ⚙️ How tracking works

Each person ticks `- [ ]` → `- [x]` boxes in their own `progress.md`. A
[GitHub Action](.github/workflows/update-progress.yml) runs weekly (and on every push) to count
the boxes per domain and regenerate [PROGRESS.md](PROGRESS.md). Nobody edits the shared table —
so direct pushes to `main` rarely conflict.

## 🎯 The exam: SAA-C03 domains

1. Design Secure Architectures (30%)
2. Design Resilient Architectures (26%)
3. Design High-Performing Architectures (24%)
4. Design Cost-Optimized Architectures (20%)

Happy studying — see you on the leaderboard. 🟢🎯✅
