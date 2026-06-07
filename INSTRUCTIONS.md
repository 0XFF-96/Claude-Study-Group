# Instructions (TL;DR)

**Claude Certified Architect – Foundations (CCA-F)** study group. Progress is tracked automatically — you only edit your own folder.

## Join (once)

```bash
git clone git@github.com:0XFF-96/Claude-Study-Group.git
cd Claude-Study-Group
cp -r members/_TEMPLATE members/<your-github-username>   # lowercase
# edit profile.md → name, target exam date, status
git add . && git commit -m "join" && git pull --rebase && git push
```

## Every week

1. Tick boxes in `members/<you>/progress.md` (`- [ ]` → `- [x]`) as you learn.
2. Add a `## YYYY-MM-DD` entry to `members/<you>/weekly-log.md`.
3. Push:
   ```bash
   git add . && git commit -m "weekly update" && git pull --rebase && git push
   ```

A bot regenerates [PROGRESS.md](PROGRESS.md) from your checkboxes — **never edit it by hand.**

## Rules

- Only edit files under your own `members/<you>/` folder.
- Always `git pull --rebase` before you push.
- Keep headers intact: `## Domain 1`–`## Domain 5` in progress.md, `**Status**:` / `**Target exam date**:` in profile.md.

Full details → [GUIDE.md](GUIDE.md).
