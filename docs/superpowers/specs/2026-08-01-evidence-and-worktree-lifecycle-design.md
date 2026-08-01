# 事实晋升与 Worktree 生命周期设计

## 背景

一次真实仓库审计发现，候选 Worktree 中未提交、未完整验证的实验实现被 `progress.txt` 写入 `[Done]`，而稳定分支并不包含该能力。同一仓库还长期保留了大量目标重叠、状态不明或已经可以解除物化的 Worktree。

这两个现象来自同一缺口：YuanForge 规定了如何创建基线和 Worktree，却没有完整定义候选事实如何晋升、Worktree 何时退出，以及“具备合并条件”“获得合并授权”“已经进入稳定分支”之间的责任边界。

## 目标

- 防止未跟踪文件、未提交改动或候选分支能力冒充稳定分支事实。
- 为每个物化 Worktree 给出可审计的继续、拆分、评审、暂停或退役判断。
- 区分集成就绪判断、维护者授权、Git 合并执行和稳定分支验证。
- 允许解除干净候选 Worktree 的物化，同时保留未合并分支及其提交。
- 保持 YuanForge 为基线治理 Skill，不扩张为自动合并器、发布系统或第二套 Git 状态数据库。

## 非目标

- 不自动执行 `git merge`、解决业务冲突、删除分支或删除 Worktree。
- 不根据测试结果替用户接受产品、架构、安全或发布风险。
- 不要求所有项目维护机器可读的 Worktree 注册表。
- 不把 Worktree 数量上限当作健康度判据。

## 第一性模型

### 事实主张

每项重要完成主张必须同时说明三个维度：

| 维度 | 值 | 含义 |
|---|---|---|
| 持久性 | 工作区 / 提交 | 改动只存在于可变现场，还是已经形成可追溯快照 |
| 归属 | 候选 / 稳定 | 改动属于实验或评审分支，还是已进入项目稳定基线 |
| 验证 | 未验证 / 已验证 | 对应提交和环境是否产生了新鲜、适用的证据 |

`progress.txt` 是这些事实的摘要视图，不是独立权威来源。稳定分支中的 `[Done]` 或 `READY` 只允许描述稳定分支已经包含、并在该稳定状态上完成适用验证的能力。

候选分支可以记录自身工作，但必须带范围限定：

- 未提交改动只能描述为正在进行的实验或原型；
- 已提交且验证通过的候选只能描述为等待集成评审；
- 已集成但未完成稳定分支验证的能力只能描述为已集成、待验证；
- 只有稳定分支验证通过后才能晋升为完成事实。

### Worktree

Worktree 是执行现场，不是长期成果容器。Worktree 继续物化，当且仅当它仍承担至少一种职责：

- 当前任务正在其中执行；
- 其中存在尚未持久化、必须保护的本地状态；
- 其中运行无法安全迁移的验证或环境。

分支负责保存已提交候选成果。一个干净、已提交但尚未合并的候选可以解除 Worktree 物化并保留分支；解除 Worktree 物化和删除分支是两个独立决策。

## 生命周期与判断结果

Worktree 角色使用以下生命周期；`planned` 表示尚未物化，`parked` 表示已经解除物化：

```text
planned -> active -> candidate -> integrated -> retired
             ^          |  \
             |          |   -> retired
             |          -> parked
             +------------- parked
```

- `planned`：已有独立目标、基线和退出条件，但尚未创建 Worktree。
- `active`：正在执行，或包含必须保护的未持久化状态。
- `candidate`：有效改动已提交，范围和验证证据可供评审。
- `parked`：分支和提交保留，实体 Worktree 可以安全解除物化。
- `integrated`：目标稳定分支已经包含候选提交或等价变更。
- `retired`：成果已集成、被替代或经授权放弃，实体 Worktree 不再承担职责。

审计或交接时，YuanForge 为每个 Worktree 给出一个判断：

| 判断 | 条件与后续 |
|---|---|
| `CONTINUE` | 目标仍有效，工作尚未形成完整候选 |
| `SPLIT` | 混合了多个目标、无关改动或不可独立评审的内容 |
| `READY_FOR_REVIEW` | 提交、Diff、验证和风险披露完整，可交由维护者决定 |
| `PARK` | 工作区干净且成果已提交，当前不需占用实体 Worktree；保留分支 |
| `RETIRE` | 已集成、被替代或经明确授权放弃；清理仍需独立安全检查 |
| `BLOCKED` | 脏状态归属不明、基线冲突、验证缺失或授权不足，不能安全推进 |

YuanForge 不输出会混淆判断和授权的裸 `MERGE`。`READY_FOR_REVIEW` 只表示证据门槛满足，不表示维护者已经接受。

## 集成责任边界

集成分为四步：

1. `READY_FOR_REVIEW`：YuanForge 检查来源、提交、Diff、验证、依赖、冲突和残余风险。
2. `APPROVED_FOR_INTEGRATION`：用户或项目维护者接受范围与风险。
3. `INTEGRATED`：项目交付流程执行合并或等价集成。
4. `VERIFIED_ON_STABLE`：稳定分支产生新鲜验证，完成主张才可进入 `[Done]`。

YuanForge 拥有集成就绪判断和稳定事实校验职责；维护者拥有接受权；项目交付流程拥有实际 Git 操作权。

## Skill 与项目基线的分工

Skill 内核定义通用证据维度、生命周期、判断结果和安全底线。项目自己的 `docs/WORKTREE_GUIDE.md` 负责稳定分支、角色、验证命令、授权人和集成方式。日常任务直接执行项目规则，不需要反复调用 YuanForge。

YuanForge 在 `audit`、`repair` 和 `evolve` 中共用这道集成就绪门，不增加第五个顶层操作。

实现应保持单一事实来源：Git 提供 Worktree、分支、提交和祖先关系，测试输出提供验证事实，项目文档提供目标与授权规则，`progress.txt` 只汇总当前状态和决策。

## 安全与失败处理

- 任何脏 Worktree 默认保护，不自动移动、Stash、覆盖或删除。
- 未跟踪文件与未提交改动不得支持稳定完成主张。
- 候选验证必须绑定当前候选提交；稳定完成必须重新核对稳定分支包含关系和适用验证。
- 工作区干净不等于可以删除分支；Worktree 移除、分支删除和成果放弃分别授权。
- 无法确认目标、归属、基线或授权时返回 `BLOCKED` 或 `PARTIAL`，并指出缺失证据。
- 多个候选修改同一责任或目标时，先报告重叠和依赖，不能仅按最近提交自动选胜者。

## 产物调整

- `skills/yuanforge/SKILL.md`：在检查、验证和交接阶段接入集成就绪门。
- `skills/yuanforge/references/evidence.md`：增加完成主张的持久性、归属和验证维度。
- `skills/yuanforge/references/integration-readiness.md`：新增完整生命周期、判断清单和安全边界。
- `skills/yuanforge/references/bootstrap.md`：创建 Worktree 前要求独立目标、稳定基线和退出条件。
- `docs/WORKTREE_GUIDE.md`：让 YuanForge 项目自身采用同一生命周期和职责边界。
- `AGENTS.md`、`lessons.md`、`progress.txt`：分别保存精炼执行门、可复用事故预防和当前实现状态。
- `README.md`、`docs/YUAN_LAYER.md`、`docs/IMPLEMENTATION_PLAN.md`：同步用户承诺、治理模型和验收顺序；检查 UI 元数据，仅在发现触发描述缺失时修改。
- `evals/cases.json` 与仓库契约测试：覆盖候选事实误报和 Worktree 膨胀场景。

## 验证场景

### 候选事实不得晋升

给定候选 Worktree 中存在未跟踪 `progress.txt`、未提交实现和部分单元测试，且稳定分支不包含该实现，YuanForge 必须：

- 把能力限定为候选 Worktree 的进行中事实；
- 拒绝 `[Done]`、`READY` 或“主线已实现”；
- 报告持久性、归属和验证缺口；
- 对混合改动返回 `SPLIT` 或 `CONTINUE`。

### Worktree 生命周期审计

给定多个 Worktree，包括脏实验、干净已提交候选、已集成分支和被替代分支，YuanForge 必须：

- 逐一给出 `CONTINUE`、`SPLIT`、`READY_FOR_REVIEW`、`PARK`、`RETIRE` 或 `BLOCKED`；
- 对干净未合并候选允许 `PARK`，同时明确保留分支；
- 对脏 Worktree 拒绝自动清理；
- 不因 Worktree 数量本身判定失败；
- 不执行合并、删除或 Stash。

## 验收条件

- Skill 明确区分工作区存在、候选提交、稳定集成和稳定验证。
- `[Done]` 与 `READY` 不能由未提交或候选分支证据支持。
- 所有 Worktree 审计均有生命周期判断和下一步，不再只有拓扑清单。
- 集成就绪、维护者授权、实际合并和稳定验证职责唯一。
- 仓库测试、Skill 校验、相对链接、UTF-8 和 Worktree 拓扑检查通过。
- YuanForge 项目自身不新增无任务的 Worktree，也不触碰其他仓库的脏状态。
