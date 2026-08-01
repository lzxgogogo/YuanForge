# YuanForge Agent 指南

本文件是 Coding Agent 的精炼入口，只保存执行约束和事实路由。

## 开工顺序

1. 运行 `git worktree list`、`git branch --show-current`、`git status --short`。
2. 阅读 `docs/WORKTREE_GUIDE.md`，按任务选择或创建 Worktree。
3. 阅读 `lessons.md` 和 `progress.txt`。
4. 按任务读取稳定事实源：
   - 意图、流程和外部交互：`README.md`
   - Yuan Layer 职责模型：`docs/YUAN_LAYER.md`
   - 方法、内部结构与验证：`docs/TECH_STACK.md`
   - 建设顺序：`docs/IMPLEMENTATION_PLAN.md`
   - Skill 执行规则：`skills/yuanforge/SKILL.md`

## Worktree 路由

- `main` 只保留已验证的稳定基线。
- 文档、Skill 指令和评测在 `writing` 角色中修改。
- 高风险原型使用 `experiment`；一次性排查使用 `agent-debug`。
- 角色先规划、Worktree 按需创建；不得为凑齐拓扑建立空闲 Worktree。
- 每个物化 Worktree 必须有独立目标、稳定基线和退出条件；交接时必须给出生命周期判断。

## 关键约束

- 仓库自然语言默认使用中文；命令、文件名、代码标识符和协议字段保持原样。
- README 负责面向人的介绍，不复制 Skill 的完整机器指令。
- 六类规格是意图、流程、方法、交互、结构和交付职责，不是软件专属文件名或六个空模板。
- `AGENTS.md` 保持精炼；约 60 行是膨胀审查信号，不是截断规则。
- `progress.txt` 是当前快照，`lessons.md` 只保存可复用的预防规则。
- `[Done]`/`READY` 必须有稳定分支归属和稳定状态的新鲜验证；候选或未提交改动只能写入进行中/风险。
- `READY_FOR_REVIEW` 不等于授权合并；YuanForge 不自动 merge、Stash 或删除 Worktree，清理与分支删除必须分开授权。
- 不覆盖用户未提交修改，不把 Stash 当长期工作区，不提交个人绝对路径或敏感信息。
- 真实仓库评测的原始输出只留本地；可提交案例必须匿名化项目名、提交哈希、绝对路径和可识别业务细节。
- 修改 Skill 内核必须同步检查参考文档、UI 元数据、README 和评测场景。

## 最小验证

- `python -m unittest discover -s tests -v`
- `python C:/Users/ystg_/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/yuanforge`
- 检查 README 和文档相对链接。
- 检查 `git worktree list` 与 `docs/WORKTREE_GUIDE.md` 的角色和真实拓扑一致。

## 完成标准

职责归属唯一；Skill 校验和仓库测试通过；安装命令可重复执行；Worktree 状态已披露；稳定文档、评测场景与 Skill 行为同步。
