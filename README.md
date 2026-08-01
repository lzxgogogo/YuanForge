# YuanForge

<p align="center">
  <img src="assets/yuanforge-hero.svg" alt="YuanForge 为项目建立 Yuan Layer" width="900">
</p>

<p align="center">
  <strong>Forge the metadata your agents build by.</strong><br>
  锻造项目元数据，让 Agent 有据可循。
</p>

让 Agent 第一次走进项目仓库，就能回答三件事：

**这个项目要做什么？哪些约束不能碰？下一步从哪里继续？**

YuanForge 为长期 Agent 协作的 Git 仓库建立项目基线。它从代码、文档、测试、数据、来源、产物和历史中找回事实，把散落的上下文锻造成一层可维护的项目元数据：**Yuan Layer**。

它也会区分“项目现在怎样工作”和“项目应该怎样工作”。代码可以证明现状，却不能替你决定目标。用户不必一开始就知道完整意图；YuanForge 会从问题情境出发，通过提问、候选方案和确认帮助意图浮现，再写入稳定基线。

它不替你开发、研究或管理项目，也不要求每个任务都走一遍流程。基线建好以后，仓库自己的文档会接管日常协作，YuanForge 就可以退场了。

## 为什么叫 Yuan

`Yuan` 指向“元”：项目的起点，也是描述项目的元数据。

代码负责运行，Yuan Layer 负责告诉人和 Agent：代码为什么这样运行、应该怎样继续演化。

## 它怎么工作

```mermaid
flowchart LR
    U["用户与目标素材"] --> Q["提问 · 候选 · 确认"]
    R["仓库当前事实"] --> Y["YuanForge"]
    Q --> Y
    Y --> L["Yuan Layer<br/>规格 · 约束 · 记忆"]
    L --> A["Agent<br/>少猜 · 可交接 · 可验证"]
```

YuanForge 只做四件事：

| 操作 | 什么时候用 |
|---|---|
| `bootstrap` | 项目还没有一套可信基线 |
| `audit` | 怀疑文档和代码已经对不上 |
| `repair` | 已确认基线缺失、冲突或失真 |
| `evolve` | 项目经验需要沉淀成长期规则 |

新项目和已有项目走不同路径：

- 新项目把链接、PPT、原型、草稿和对话作为目标素材，通过用户确认建立初始规范；这些素材不是已有项目事实。
- 已有项目先从代码、测试、运行结果、数据和历史中还原现状，再与确认目标对照。

## 它会留下什么

| 层次 | 规范归属 |
|---|---|
| 意图与流程 | `PROJECT_BRIEF.md`、`WORKFLOW.md`，或已有 PRD、研究方案 |
| 方法与结构 | `METHODS.md`、`PROJECT_STRUCTURE.md`，或已有技术、证据结构文档 |
| 交互与交付 | `INTERACTION_GUIDE.md`、`DELIVERY_PLAN.md`，或项目已有等价物 |
| 控制 | 精炼的 `AGENTS.md`、`WORKTREE_GUIDE.md` |
| 记忆 | 当前快照 `progress.txt`、经验规则 `lessons.md` |

固定的是意图、流程、方法、交互、结构、交付六类职责，不是文件名。软件、研究、数据、文档和混合项目会选择不同表达；已有文档稳定承担职责时，YuanForge 会复用它。

对用户交互型项目，YuanForge 先确认角色、触发情境、用户目标、完成信号和关键失败责任。页面、路由、组件、API 和运行界面可以证明当前实现，却不能单独还原产品意图。

YuanForge 不内置 UI 运行、文档解析、数据分析或外部研究能力。遇到证据缺口时，它只推荐合适的 Browser、Documents、PDF、Presentations、Spreadsheets 或 Web 能力组合；未安装时继续基础检查并准确披露缺口。

默认会规划四类 Worktree：稳定集成、实验、文档和临时排查。角色预先定义，实体按需创建；真实名称、路径和数量以项目现状为准。

Worktree 只是执行现场，分支和提交才保存候选成果。YuanForge 会检查来源、提交、稳定分支归属和新鲜验证，并给出 `CONTINUE`、`SPLIT`、`READY_FOR_REVIEW`、`PARK`、`RETIRE` 或 `BLOCKED` 判断；`READY_FOR_REVIEW` 不等于维护者授权合并。实际 Git 合并、冲突处理和 Worktree 清理仍由项目交付流程和明确授权负责，稳定分支重新验证后才会进入 `[Done]`。

## 安装

```bash
git clone https://github.com/lzxgogogo/YuanForge.git
mkdir -p ~/.codex/skills/yuanforge
cp -R YuanForge/skills/yuanforge/. ~/.codex/skills/yuanforge/
```

PowerShell：

```powershell
git clone https://github.com/lzxgogogo/YuanForge.git
$target = "$env:USERPROFILE\.codex\skills\yuanforge"
New-Item -ItemType Directory -Force $target | Out-Null
Get-ChildItem -Force .\YuanForge\skills\yuanforge | Copy-Item -Destination $target -Recurse -Force
```

安装后新建一个 Codex 任务，让 Codex 重新发现 Skill。

## 使用

建立或补齐项目基线：

```text
$yuanforge bootstrap 当前仓库。
以仓库证据为准，实际创建或映射项目基线，不要覆盖已有事实源。
```

只做审计，不改文件：

```text
$yuanforge audit 当前 Yuan Layer。
对照代码、测试、契约、迁移、Git 和真实 Worktree，找出缺失与漂移。
```

修复已确认的问题：

```text
$yuanforge repair 已确认的基线问题，并验证链接、命令和 Worktree。
```

沉淀项目偏好：

```text
$yuanforge 从用户纠正、评审、progress.txt 和 lessons.md 中，
提出有证据、可审查的 Yuan Layer 演化方案。
```

## 适用边界

YuanForge 面向让 Agent 在 Git 仓库中持续工作的个人与团队，尤其适合上下文已经分散、文档可能漂移的中途项目。

软件、研究、数据、文档和混合项目都可以使用，前提是主要产物、约束和验证证据能够保存在仓库中。六类职责可以组合项目画像，不要求项目只能属于一种类型。

一次性任务、主要状态存在外部业务系统或线下执行中的项目，不是当前承诺范围。YuanForge 不会把仓库中不存在的事实猜成完整项目状态。

## 几条底线

- 仓库证据优先于聊天记忆和合理猜测。
- 当前实现证明“是什么”，不能单独决定“应该是什么”。
- 一个长期事实只保留一个规范归属。
- `AGENTS.md` 是入口，不是项目百科；约 60 行只是膨胀提醒。
- 文档语言跟随用户和项目，代码标识符与协议字段保持原样。
- 项目偏好留在项目里，不让一个仓库静默改写全局 Skill。
- 没有新鲜验证，就不声称基线已经完成。
- 基线稳定后，普通开发、研究和项目任务不再需要调用 YuanForge。

更完整的职责模型见 [Yuan Layer](docs/YUAN_LAYER.md)。Skill 的执行细节在 [skills/yuanforge](skills/yuanforge)。

## 可选能力组合

YuanForge 自己只管基线，不为每个领域预置大型探针。需要额外证据时，按 [可选能力组合](skills/yuanforge/references/capability-combinations.md) 给出安装建议；其他能力返回的证据按 [统一领域证据报告](skills/yuanforge/references/domain-evidence.md) 交接，确认后的事实仍归档到项目已有规范文档。

## 状态

YuanForge 仍是早期自用版本。结构已经通过 Codex Skill 校验，并用自身仓库完成首轮 Bootstrap；减法重构后已对三个现有真实仓库完成独立只读评测，结果均为 `PARTIAL`。真实新项目的意图发现路径仍待验证，详见 [前向评测记录](evals/results/2026-07-29-cross-repo-audit.md)。

MIT License
