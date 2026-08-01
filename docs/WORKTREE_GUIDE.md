# Worktree 指南

> Yuan Layer 角色：控制
> 事实源：YuanForge 的 Worktree 角色、相对路径、流转和清理规则
> 不负责：当前任务进度或功能建设顺序
> 更新时机：角色、分支约定、路径或集成流程改变

## 策略

先定义角色，按任务需要创建实体 Worktree。`git worktree list` 是本机真实拓扑的最终证据；公共文档使用相对路径，避免提交个人目录。

| 角色 | 分支 | 相对主仓库路径 | 状态 |
|---|---|---|---|
| 稳定集成 | `main` | `<repo-root>` | 常驻 |
| 文档与 Skill | `codex/writing` | `../YuanForge-writing` | 当前已创建 |
| 高风险实验 | `codex/experiment` | `../YuanForge-experiment` | 按需 |
| 临时排查 | `codex/agent-debug` | `../YuanForge-agent-debug` | 按需 |

不为匹配表格而创建空闲 Worktree。实际名称或路径发生变化时必须更新本文档，或把差异写入 `progress.txt`。

`git worktree list` 是当前实体拓扑的唯一事实源；表格中的“按需”角色不是已经创建的 Worktree。

## 开工与流转

1. 在主仓库运行 `git worktree list`、`git branch --show-current`、`git status --short`。
2. 普通稳定修改不直接在 `main` 展开；按任务复用或创建对应角色。
3. 保留所有未提交修改；未经明确授权不得移动、Stash 或覆盖。
4. 在角色 Worktree 中完成修改、测试和 Diff 审查。
5. 形成明确提交后再集成到 `main`；集成后重新运行相关验证。

每个物化 Worktree 还必须能回答：独立目标是什么、基于哪个稳定提交、谁负责或授权、退出条件是什么。没有这些信息只能停留在 `planned`，不得为了角色表补建目录。

按需创建示例：

```bash
git worktree add -b codex/experiment ../YuanForge-experiment main
git worktree add -b codex/agent-debug ../YuanForge-agent-debug main
```

## 清理

- 审计或交接时给每个 Worktree 输出 `CONTINUE`、`SPLIT`、`READY_FOR_REVIEW`、`PARK`、`RETIRE` 或 `BLOCKED`。
- `READY_FOR_REVIEW` 只表示提交、Diff、验证和风险足以交给维护者评审，不表示已经授权合并。
- 干净且已提交的候选可以 `PARK`：移除实体 Worktree，保留分支和提交；合并判断与 Worktree 清理是两个独立决策。
- 只有分支成果已集成或明确废弃、状态干净且路径核对无误时才移除 Worktree。
- 不直接删除 Worktree 目录；使用 `git worktree remove <path>`。
- 删除分支是独立操作，不因移除 Worktree 自动获得授权。
- 脏 Worktree 默认保护，不自动移动、Stash、覆盖、合并或删除。

## 集成责任

YuanForge 负责证据检查和 `READY_FOR_REVIEW` 判断；用户或项目维护者负责接受范围和风险；项目交付流程负责实际 Git 合并；稳定分支重新验证后才能把能力写入 `[Done]`。YuanForge 不自动执行 `git merge` 或清理动作。
