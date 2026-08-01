# 集成就绪门

> Yuan Layer 角色：交付 / 控制
> 适用范围：审计、修复或演化任务涉及多个分支、Worktree、候选实现或稳定完成声明时
> 核心边界：判断是否具备集成条件，不替用户授权合并，也不代替项目交付流程执行 Git 操作

## 三维证据模型

每项重要完成主张同时检查三个维度：

| 维度 | 工作区或候选状态 | 稳定完成状态 |
|---|---|---|
| 持久性 | 文件存在、未跟踪或未提交 | 有可追溯提交 |
| 归属 | 候选分支或 Worktree | 稳定分支已包含对应变更 |
| 验证 | 未验证或只验证了其他提交 | 对稳定状态有新鲜、适用验证 |

`progress.txt` 是当前事实的摘要，不是独立事实源。稳定快照中的 `[Done]` 或 `READY` 必须同时满足稳定分支包含关系和稳定状态验证。候选分支可以记录自己的进度，但必须明确范围；未跟踪或未提交内容只能描述为进行中事实。

## Worktree 生命周期

Worktree 是执行现场，不是成果仓库。角色按以下状态流转：

```text
planned -> active -> candidate -> integrated -> retired
             ^          |  \
             |          |   -> retired
             |          -> parked
             +------------- parked
```

- `planned`：目标、基线和退出条件已明确，尚未物化 Worktree。
- `active`：正在执行，或包含必须保护的未持久化状态。
- `candidate`：有效改动已提交，Diff、验证和风险可供评审。
- `parked`：分支和提交保留，实体 Worktree 已解除物化。
- `integrated`：稳定分支已包含候选提交或经过审查的等价变更。
- `retired`：成果已集成、被替代或明确放弃，实体 Worktree 不再承担职责。

未合并的干净候选可以 `PARK`；Worktree 移除不等于分支删除。脏状态不能自动进入 `PARK` 或 `RETIRE`。

## 审计判断

每个物化 Worktree 必须得到一个判断和下一步：

| 判断 | 必要条件 | 后续 |
|---|---|---|
| `CONTINUE` | 目标有效但尚未形成可评审候选 | 继续当前任务并保留 Worktree |
| `SPLIT` | 混合多个目标、无关改动或不可独立评审 | 拆分提交或拆分任务 |
| `READY_FOR_REVIEW` | 提交、Diff、验证、依赖和风险已可追溯 | 交由维护者判断是否授权集成 |
| `PARK` | 工作区干净、成果已提交、当前不需执行现场 | 移除 Worktree，保留分支 |
| `RETIRE` | 已集成、被替代或经明确授权放弃，且状态安全 | 按项目规则清理实体 Worktree |
| `BLOCKED` | 归属、基线、验证、冲突或授权无法确认 | 保留现场并披露缺口 |

YuanForge 不输出裸 `MERGE` 作为自动动作。`READY_FOR_REVIEW` 只表示证据门槛满足，不表示维护者已经接受。

## 集成责任边界

集成是四个可审计阶段：

1. `READY_FOR_REVIEW`：YuanForge 检查来源、提交、Diff、验证、依赖、冲突和残余风险。
2. `APPROVED_FOR_INTEGRATION`：用户或项目维护者接受范围、行为和风险。
3. `INTEGRATED`：项目交付流程执行合并或等价集成。
4. `VERIFIED_ON_STABLE`：稳定分支重新验证，完成主张才可写入 `[Done]`。

YuanForge 负责集成就绪判断和稳定事实核对；维护者负责授权；项目交付流程负责 Git 操作。普通功能开发不需要每次重新调用 YuanForge，项目 `AGENTS.md` 和 `docs/WORKTREE_GUIDE.md` 应承载已确认的日常规则。

## 安全底线

- 不自动执行 `git merge`、解决业务冲突、Stash、删除分支或删除 Worktree。
- 脏 Worktree 默认保留，不移动、覆盖或静默清理。
- 候选验证必须绑定候选提交；稳定完成必须重新核对稳定分支和验证结果。
- Worktree 移除、分支删除和成果放弃是相互独立的授权动作。
- 无法确认目标、归属、基线或授权时返回 `BLOCKED` 或 `PARTIAL`。

## 交接格式

报告至少包含：

```text
Worktree/分支：<角色和相对标识>
来源提交：<commit 或未提交>
目标稳定分支：<ref>
工作区：clean | dirty | untracked
验证：<命令、提交和结果>
未决风险：<冲突、缺口、授权或外部条件>
判断：CONTINUE | SPLIT | READY_FOR_REVIEW | PARK | RETIRE | BLOCKED
```
