# Yuan Layer

Yuan Layer 是代码仓库的项目元数据层。它让 Coding Agent 能够从持久、可审查的事实源中，重建项目意图、约束、当前状态和执行拓扑。

## 文档职责契约

每份稳定文档应在开头声明一段精炼的职责契约：

```markdown
> Yuan Layer 角色：意图 | 结构 | 交付 | 控制 | 记忆
> 事实源：<本文档拥有的事实>
> 不负责：<由其他文档拥有的事实>
> 更新时机：<需要修订本文档的事件>
```

这份契约用于防止多个文档争夺同一事实的解释权。

## 信息分层

### 意图

- `docs/PRD.md` 负责产品范围和验收条件。
- `docs/APP_FLOW.md` 负责行为、状态、失败路径和恢复方式。

### 结构

- `docs/TECH_STACK.md` 负责技术选择和技术约束。
- `docs/FRONTEND_GUIDELINES.md` 负责客户端约定。
- `docs/BACKEND_STRUCTURE.md` 负责服务端和数据边界。

### 交付

- `docs/IMPLEMENTATION_PLAN.md` 负责建设顺序和验证关卡。

### 控制

- `AGENTS.md` 是精炼的 Agent 入口和阅读路由器。
- `docs/WORKTREE_GUIDE.md` 负责真实 Worktree 拓扑和集成流程。

### 记忆

- `progress.txt` 是当前快照，不是只追加的活动日志。
- `lessons.md` 只记录可复用的症状、根因和预防规则。

## 日常任务生命周期

完成 Bootstrap 后，Coding Agent 应该：

1. 检查 Git 和 Worktree 状态；
2. 阅读 `AGENTS.md`；
3. 阅读 `lessons.md` 和 `progress.txt`；
4. 只阅读与任务有关的稳定规格；
5. 检查目标代码、测试、契约、迁移和配置；
6. 在合适的 Worktree 中工作；
7. 执行新鲜验证；
8. 只有在归属事实发生变化时，才更新进度、教训或稳定文档。

这个日常生命周期不需要再次调用 YuanForge。

## 演化策略

一次纠正只有经过分类，才能晋升为长期指导：

| 观察结果 | 归属位置 |
|---|---|
| 当前阻塞或下一步 | `progress.txt` |
| 可复用的预防规则 | `lessons.md` |
| 稳定的产品偏好 | `docs/PRD.md` 或 `docs/APP_FLOW.md` |
| 稳定的技术偏好 | 对应的结构文档 |
| 稳定的交付规则 | `docs/IMPLEMENTATION_PLAN.md` |
| Agent 阅读或执行规则 | `AGENTS.md` 中的精炼条目 |
| Worktree 规则 | `docs/WORKTREE_GUIDE.md` |

重要规则的晋升必须有证据、可审查。不得静默改写项目的运行性格。

## 语言策略

Yuan Layer 的自然语言应跟随项目，而不是跟随 Skill 内部指令的语言。选择顺序为：用户明确要求、仓库明确规则、当前稳定文档的主导语言、当前对话语言，最后才是英文默认值。

文件名、命令、代码标识符、协议字段和精度敏感术语保持原样。已有文档只有在用户要求或职责修复确有必要时才翻译，避免把语言统一变成无关的大范围改动。
