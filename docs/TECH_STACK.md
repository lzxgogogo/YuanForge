# 技术约束

> Yuan Layer 角色：方法 | 结构
> 事实源：YuanForge 的文件格式、运行依赖、目录边界和验证命令
> 不负责：产品介绍、Agent 执行流程和当前进度
> 更新时机：运行依赖、目录结构或验证方式发生变化

## 当前技术形态

- YuanForge 是 Codex Skill 仓库，不包含应用运行时、数据库或在线服务。
- Skill 本体位于 `skills/yuanforge/`，必须保留 `SKILL.md` 和 `agents/openai.yaml`。
- 机器执行规则使用 Markdown；UI 元数据使用 YAML；品牌图使用 SVG。
- 仓库契约测试只依赖 Python 标准库，避免为轻量校验引入包管理器。
- Git 和 Git Worktree 负责版本、隔离和集成。
- Browser、Documents、PDF、Presentations、Spreadsheets 和外部连接器均为可选组合，不是 YuanForge 的运行依赖。

## 目录边界

- `skills/yuanforge/SKILL.md` 只保留核心流程与引用路由。
- `skills/yuanforge/references/` 保存按需加载的详细规则。
- `skills/yuanforge/agents/openai.yaml` 保存用户可见的 Skill 元数据。
- `docs/` 保存 YuanForge 项目自身的稳定事实，不随 Skill 安装。
- `evals/` 保存前向验证场景；`tests/` 验证可确定的仓库契约。

## 验证命令

```powershell
python -m unittest discover -s tests -v
python C:/Users/ystg_/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/yuanforge
```

第二条命令依赖本机 Codex 自带的 `skill-creator`。其他环境应使用其 Codex 安装中对应的 `quick_validate.py`，不得把个人绝对路径写进脚本或公共配置。

## 不支持的选择

- 不为项目中不存在的系统、参与者或交付面创建空规格。
- 不把项目特有偏好静默写回全局安装的 Skill。
- 不用自动化测试冒充真实 Agent 前向验证。
- 不把 UI 运行、文档解析、数据分析或外部研究实现进 YuanForge 核心；能力不足时给出组合建议并披露证据缺口。
