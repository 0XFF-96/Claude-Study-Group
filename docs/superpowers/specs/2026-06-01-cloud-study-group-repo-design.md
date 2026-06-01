# Cloud Study Group Repo 设计文档

- **日期**：2026-06-01
- **认证目标**：AWS Certified Solutions Architect – Associate (SAA-C03)
- **小组规模**：7–15 人
- **协作方式**：直接 push 到 `main`（设计以"每人只改自己文件"为原则，最大化避免冲突）

## 目标

为云认证学习小组建立一个清晰、低门槛、可持续的 GitHub repo，用来：

1. 一眼看到**全组每个人的进度和学习状态**（激励 + 互相监督）。
2. 让每个人有独立空间记录**学习笔记**和**每周打卡/周报**。
3. 提供一份清晰的**参与指南**，让新成员 5 分钟内能上手。

## 采用方案：集中式单表 + 个人文件夹（方案 A）

- 一个 `PROGRESS.md` 总览表，**每人占一行** → 全组进度一目了然。表格按行编辑，git 行级合并几乎不冲突。
- 每人一个 `members/<github-username>/` 文件夹放笔记、详细 checklist、周报 → 完全隔离，直接 push 零冲突。

**被否决的方案**：
- 完全分散式（无总表）：零冲突但缺少全组总览与激励感。
- GitHub Issues/Projects 看板：用户已排除（偏好 Markdown）。

## 约定（Conventions）

- **个人文件夹命名**：GitHub 用户名小写，如 `members/jimmyli/`。与 PR/commit 作者对得上。
- **进度量化**：每个 domain 用「已完成知识点 / 该 domain 总知识点」的百分比表示，如 `Domain 1: 60%`。知识点清单来自 `syllabus/SAA-C03.md`。
- **打卡频率**：每周至少一次，记录在个人 `weekly-log.md`。
- **冲突最小化**：除了在 `PROGRESS.md` 修改**自己那一行**，其余只改自己 `members/<name>/` 下的文件。

## 目录结构

```
Claude-Study-Group/
├── README.md                  # 项目首页：小组介绍 + 快速开始 + 进度总览链接
├── GUIDE.md                   # 详细参与指南（每个人分步骤怎么做）
├── PROGRESS.md                # 全组进度总览表（每人一行）
├── syllabus/
│   └── SAA-C03.md             # 考试大纲：4 个 domain + 知识点 checklist 模板
├── members/
│   ├── _TEMPLATE/             # 新成员复制此文件夹起步
│   │   ├── profile.md         #   个人信息 + 目标考试日期 + 学习计划
│   │   ├── progress.md        #   个人详细 domain 知识点 checklist
│   │   ├── notes/
│   │   │   └── domain-1-security.md   # 笔记示例
│   │   └── weekly-log.md      #   每周打卡：时长 + 完成内容 + 反思
│   └── jimmyli/               # 示例成员文件夹（从 _TEMPLATE 复制）
│       ├── profile.md
│       ├── progress.md
│       ├── notes/
│       │   └── domain-1-security.md
│       └── weekly-log.md
└── resources/
    └── README.md              # 共享学习资源清单（课程/文档/题库链接）
```

## 各文件职责

| 文件 | 谁维护 | 内容 |
|------|--------|------|
| `README.md` | 维护者 | 小组介绍、3 步快速开始、指向 GUIDE/PROGRESS 的链接 |
| `GUIDE.md` | 维护者 | 完整参与流程：加入、起步、每日/每周该做什么、提交规范 |
| `PROGRESS.md` | 每人改自己那行 | 总览表：姓名·目标考试日期·D1–D4 进度·上次打卡·笔记链接 |
| `syllabus/SAA-C03.md` | 维护者 | 官方 4 domain 权威知识点清单，作为个人 progress.md 模板源 |
| `members/_TEMPLATE/` | 维护者 | 新人起步模板，含全部占位文件 |
| `members/<name>/` | 本人 | 个人 profile、详细 checklist、笔记、周报 |
| `resources/README.md` | 大家共建 | 共享课程/文档/题库链接 |

### PROGRESS.md 总览表列设计

| 列 | 说明 |
|----|------|
| 成员 | GitHub 用户名（链接到个人文件夹） |
| 目标考试日期 | 计划考试日期 |
| D1 安全 | Domain 1 完成百分比 |
| D2 弹性 | Domain 2 完成百分比 |
| D3 高性能 | Domain 3 完成百分比 |
| D4 成本优化 | Domain 4 完成百分比 |
| 上次打卡 | 最近一次 weekly-log 日期 |
| 状态 | 🟢 进行中 / 🎯 备考冲刺 / ✅ 已通过 |

### SAA-C03 四个考试域（官方权重）

1. **Domain 1: Design Secure Architectures**（30%）
2. **Domain 2: Design Resilient Architectures**（26%）
3. **Domain 3: Design High-Performing Architectures**（24%）
4. **Domain 4: Design Cost-Optimized Architectures**（20%）

## 新成员上手流程（写进 GUIDE.md）

1. `git clone` 仓库。
2. `cp -r members/_TEMPLATE members/<你的github用户名>`。
3. 填写 `profile.md`（目标考试日期、学习计划）。
4. 在 `PROGRESS.md` 表格底部加上**自己这一行**。
5. 每周：更新 `progress.md` 勾选知识点、写 `weekly-log.md` 打卡、更新 `PROGRESS.md` 自己那行的百分比。
6. `git add . && git commit && git pull --rebase && git push`（push 前先 pull rebase，减少冲突）。

## 成功标准

- 任何人打开 repo，30 秒内通过 `PROGRESS.md` 看到全组每个人的进度。
- 新成员照着 `GUIDE.md` 能在 5 分钟内完成起步并提交第一次。
- 每个人的笔记/打卡互不干扰，直接 push 基本不产生冲突。

## 范围之外（YAGNI）

- 不做 GitHub Actions 自动汇总/dashboard（用户未要求，前期成本高）。
- 不做题库自动评分系统。
- 不引入 Issues/Projects 看板。
