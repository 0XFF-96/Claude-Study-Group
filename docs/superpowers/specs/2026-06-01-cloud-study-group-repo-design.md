# Cloud Study Group Repo Design

- **Date**: 2026-06-01
- **Certification target**: AWS Certified Solutions Architect – Associate (SAA-C03)
- **Group size**: 7–15 people
- **Collaboration model**: Direct push to `main` (designed around "everyone edits only their own files" to minimize conflicts)

## Goals

Build a clear, low-friction, sustainable GitHub repo for a cloud certification study group that lets us:

1. See **every member's progress and study status at a glance** (motivation + peer accountability).
2. Give each member a private space for **study notes** and **weekly check-ins / logs**.
3. Provide a clear **participation guide** so a new member can get started in ~5 minutes.

## Chosen approach: Central table + per-member folders (Approach A)

- One `PROGRESS.md` overview table, **one row per person** → whole-group progress at a glance. Row-level edits merge cleanly in git.
- Each member gets a `members/<github-username>/` folder for notes, detailed checklist, and weekly log → fully isolated, zero conflicts on direct push.

**Rejected alternatives**:
- Fully decentralized (no central table): zero conflicts but no group overview or motivation.
- GitHub Issues/Projects board: ruled out by user (prefers Markdown).

## Conventions

- **Member folder naming**: lowercase GitHub username, e.g. `members/jimmyli/`. Matches PR/commit authors.
- **Progress quantification**: each domain shown as "completed topics / total topics" percentage, e.g. `Domain 1: 60%`. Topic lists come from `syllabus/SAA-C03.md`.
- **Check-in cadence**: at least once per week, recorded in each member's `weekly-log.md`.
- **Conflict minimization**: aside from editing **your own row** in `PROGRESS.md`, only edit files under your own `members/<name>/` folder.

## Directory structure

```
Claude-Study-Group/
├── README.md                  # Landing page: intro + quick start + link to progress overview
├── GUIDE.md                   # Detailed participation guide (step by step for each member)
├── PROGRESS.md                # Group-wide progress overview table (one row per person)
├── syllabus/
│   └── SAA-C03.md             # Exam blueprint: 4 domains + topic checklist template
├── members/
│   ├── _TEMPLATE/             # New members copy this folder to start
│   │   ├── profile.md         #   Personal info + target exam date + study plan
│   │   ├── progress.md        #   Personal detailed domain topic checklist
│   │   ├── notes/
│   │   │   └── domain-1-security.md   # Example note
│   │   └── weekly-log.md      #   Weekly check-in: hours + what was done + reflection
│   └── jimmyli/               # Example member folder (copied from _TEMPLATE)
│       ├── profile.md
│       ├── progress.md
│       ├── notes/
│       │   └── domain-1-security.md
│       └── weekly-log.md
└── resources/
    └── README.md              # Shared study resources list (courses/docs/practice exams)
```

## File responsibilities

| File | Maintained by | Content |
|------|---------------|---------|
| `README.md` | Maintainer | Group intro, 3-step quick start, links to GUIDE/PROGRESS |
| `GUIDE.md` | Maintainer | Full participation flow: join, get started, daily/weekly tasks, commit rules |
| `PROGRESS.md` | Each edits own row | Overview table: name · target exam date · D1–D4 progress · last check-in · notes link |
| `syllabus/SAA-C03.md` | Maintainer | Authoritative 4-domain topic checklist, source for personal progress.md |
| `members/_TEMPLATE/` | Maintainer | Starter template with all placeholder files |
| `members/<name>/` | The member | Personal profile, detailed checklist, notes, weekly log |
| `resources/README.md` | Everyone | Shared courses/docs/practice-exam links |

### PROGRESS.md overview table columns

| Column | Meaning |
|--------|---------|
| Member | GitHub username (links to their folder) |
| Target exam date | Planned exam date |
| D1 Secure | Domain 1 completion % |
| D2 Resilient | Domain 2 completion % |
| D3 Performance | Domain 3 completion % |
| D4 Cost | Domain 4 completion % |
| Last check-in | Date of latest weekly-log entry |
| Status | 🟢 In progress / 🎯 Final prep / ✅ Passed |

### SAA-C03 exam domains (official weights)

1. **Domain 1: Design Secure Architectures** (30%)
2. **Domain 2: Design Resilient Architectures** (26%)
3. **Domain 3: Design High-Performing Architectures** (24%)
4. **Domain 4: Design Cost-Optimized Architectures** (20%)

## New member onboarding flow (goes into GUIDE.md)

1. `git clone` the repo.
2. `cp -r members/_TEMPLATE members/<your-github-username>`.
3. Fill in `profile.md` (target exam date, study plan).
4. Add **your own row** at the bottom of the `PROGRESS.md` table.
5. Weekly: update `progress.md` checkboxes, write a `weekly-log.md` entry, update your row's percentages in `PROGRESS.md`.
6. `git add . && git commit && git pull --rebase && git push` (pull-rebase before push to reduce conflicts).

## Success criteria

- Anyone opening the repo can see every member's progress within 30 seconds via `PROGRESS.md`.
- A new member can follow `GUIDE.md`, get set up, and make their first commit within 5 minutes.
- Personal notes/logs never interfere with each other; direct push rarely produces conflicts.

## Out of scope (YAGNI)

- No GitHub Actions auto-aggregation / dashboard (not requested, high upfront cost).
- No automated practice-exam scoring system.
- No Issues/Projects board.
