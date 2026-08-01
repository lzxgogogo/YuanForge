import json
import re
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class RepositoryContractTests(unittest.TestCase):
    def test_minimum_baseline_exists(self):
        required = [
            "AGENTS.md",
            "progress.txt",
            "lessons.md",
            "docs/TECH_STACK.md",
            "docs/IMPLEMENTATION_PLAN.md",
            "docs/WORKTREE_GUIDE.md",
        ]
        missing = [path for path in required if not (ROOT / path).is_file()]
        self.assertEqual([], missing)

    def test_local_markdown_links_resolve(self):
        pattern = re.compile(r"\[[^\]]+\]\((?!https?://|#)([^)]+)\)")
        failures = []
        for document in ROOT.rglob("*.md"):
            if ".git" in document.parts:
                continue
            text = document.read_text(encoding="utf-8")
            for target in pattern.findall(text):
                clean_target = target.strip("<>").split("#", 1)[0]
                resolved = (document.parent / clean_target).resolve()
                if not resolved.exists():
                    failures.append(f"{document.relative_to(ROOT)} -> {target}")
        self.assertEqual([], failures)

    def test_eval_cases_cover_core_operations(self):
        cases = json.loads((ROOT / "evals/cases.json").read_text(encoding="utf-8"))
        operations = {case["operation"] for case in cases}
        self.assertEqual({"bootstrap", "audit", "repair", "evolve"}, operations)
        profiles = {case["profile"] for case in cases}
        self.assertEqual({"software", "research", "documentation"}, profiles)
        self.assertEqual(len(cases), len({case["id"] for case in cases}))
        for case in cases:
            self.assertTrue(case["prompt"])
            self.assertTrue(case["fixture"])
            self.assertGreaterEqual(len(case["expected"]), 3)

    def test_ui_flow_regression_case_guards_intent(self):
        cases = json.loads((ROOT / "evals/cases.json").read_text(encoding="utf-8"))
        case = next(
            item for item in cases if item["id"] == "brownfield-ui-current-is-not-target"
        )
        expected = "\n".join(case["expected"])
        self.assertIn("当前实现、目标意图和候选方案", expected)
        self.assertIn("角色、触发情境、用户目标、完成信号", expected)
        self.assertIn("不把后端业务流水线或 API 清单", expected)
        self.assertIn("不从页面、路由、组件或当前运行界面反推", expected)

    def test_intent_discovery_is_wired(self):
        skill = (ROOT / "skills/yuanforge/SKILL.md").read_text(encoding="utf-8")
        required = [
            "skills/yuanforge/references/domain-evidence.md",
            "skills/yuanforge/references/intent-discovery.md",
            "skills/yuanforge/references/capability-combinations.md",
        ]
        for path in required:
            self.assertTrue((ROOT / path).is_file(), path)
        self.assertIn("references/domain-evidence.md", skill)
        self.assertIn("references/intent-discovery.md", skill)
        self.assertIn("references/capability-combinations.md", skill)
        self.assertNotIn("references/ui-evidence.md", skill)

        intent = (ROOT / required[1]).read_text(encoding="utf-8")
        self.assertIn("用户不必一开始知道完整意图", intent)
        self.assertIn("关键取舍经用户确认", intent)
        self.assertIn("To confirm", intent)

    def test_greenfield_intent_requires_confirmation(self):
        cases = json.loads((ROOT / "evals/cases.json").read_text(encoding="utf-8"))
        case = next(item for item in cases if item["id"] == "greenfield-intent-emergence")
        expected = "\n".join(case["expected"])
        self.assertIn("目标意图素材，而不是已有项目事实", expected)
        self.assertIn("用户不知道完整答案", expected)
        self.assertIn("经用户确认后才写入稳定目标文档", expected)

    def test_capability_recommendations_preserve_scope(self):
        recommendations = (
            ROOT / "skills/yuanforge/references/capability-combinations.md"
        ).read_text(
            encoding="utf-8"
        )
        for expected in [
            "不内置领域执行能力",
            "推荐不等于已安装或可用",
            "PARTIAL",
            "仍写入项目稳定文档",
        ]:
            self.assertIn(expected, recommendations)

        cases = json.loads((ROOT / "evals/cases.json").read_text(encoding="utf-8"))
        case = next(
            item for item in cases if item["id"] == "capability-recommendation-fallback"
        )
        expected = "\n".join(case["expected"])
        self.assertIn("不声称已经安装", expected)
        self.assertIn("不把 UI 运行、讲义解析或领域执行实现进 YuanForge 核心", expected)

    def test_integration_readiness_cases_are_recorded(self):
        cases = json.loads((ROOT / "evals/cases.json").read_text(encoding="utf-8"))
        by_id = {case["id"]: case for case in cases}
        for case_id in (
            "candidate-evidence-cannot-be-done",
            "worktree-lifecycle-review",
        ):
            self.assertIn(case_id, by_id)
            self.assertEqual("audit", by_id[case_id]["operation"])
            self.assertGreaterEqual(len(by_id[case_id]["expected"]), 5)

    def test_integration_readiness_reference_is_wired(self):
        skill = (ROOT / "skills/yuanforge/SKILL.md").read_text(encoding="utf-8")
        reference_path = ROOT / "skills/yuanforge/references/integration-readiness.md"
        self.assertTrue(reference_path.is_file())
        self.assertIn("references/integration-readiness.md", skill)
        reference = reference_path.read_text(encoding="utf-8")
        for expected in [
            "READY_FOR_REVIEW",
            "PARK",
            "RETIRE",
            "BLOCKED",
            "不自动执行 `git merge`",
        ]:
            self.assertIn(expected, reference)

    def test_skill_scope_is_finite(self):
        skill = (ROOT / "skills/yuanforge/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Keep the promise finite", skill)
        self.assertIn("does not perform domain work", skill)
        self.assertIn("does not have, recommend a suitable Skill combination", skill)
        self.assertLess(len(skill.splitlines()), 180)

    def test_cross_repo_forward_eval_is_recorded(self):
        result = (
            ROOT / "evals/results/2026-07-29-cross-repo-audit.md"
        ).read_text(encoding="utf-8")
        for expected in [
            "样本 A",
            "样本 B",
            "样本 C",
            "真实新项目",
            "Spreadsheets + Browser",
        ]:
            self.assertIn(expected, result)
        self.assertNotRegex(result, r"`[^`\n]+@[0-9a-f]{7,40}`")
        self.assertNotRegex(result, r"(?i)(?:[a-z]:\\|\\\\wsl|/home/)")
        sample_rows = re.findall(r"^\| 样本 [A-Z] \|", result, flags=re.MULTILINE)
        self.assertEqual(3, len(sample_rows))

    def test_install_command_copies_contents_not_container(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("skills/yuanforge/.", readme)
        self.assertNotIn(
            "cp -R YuanForge/skills/yuanforge ~/.codex/skills/yuanforge",
            readme,
        )

    def test_skill_ui_metadata_matches_project_language(self):
        metadata = (ROOT / "skills/yuanforge/agents/openai.yaml").read_text(
            encoding="utf-8"
        )
        self.assertRegex(metadata, r"[\u4e00-\u9fff]")
        self.assertIn("$yuanforge", metadata)

    def test_maintained_text_is_utf8_and_svg_is_well_formed(self):
        suffixes = {".md", ".txt", ".yaml", ".json", ".py", ".svg"}
        for artifact in ROOT.rglob("*"):
            if artifact.is_file() and artifact.suffix in suffixes:
                with self.subTest(path=artifact.relative_to(ROOT)):
                    artifact.read_text(encoding="utf-8")
        ET.parse(ROOT / "assets/yuanforge-hero.svg")


if __name__ == "__main__":
    unittest.main()
