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
        self.assertIn("角色、入口、页面、动作、状态", expected)
        self.assertIn("不把后端业务流水线或 API 清单", expected)
        self.assertIn("统一领域证据报告", expected)
        self.assertIn("UI 画像只负责取证", expected)

    def test_optional_domain_evidence_profiles_are_wired(self):
        skill = (ROOT / "skills/yuanforge/SKILL.md").read_text(encoding="utf-8")
        required = [
            "skills/yuanforge/references/domain-evidence.md",
            "skills/yuanforge/references/ui-evidence.md",
        ]
        for path in required:
            self.assertTrue((ROOT / path).is_file(), path)
        self.assertIn("references/domain-evidence.md", skill)
        self.assertIn("references/ui-evidence.md", skill)

        contract = (ROOT / required[0]).read_text(encoding="utf-8")
        self.assertIn("领域画像负责发现、分类和引用证据", contract)
        self.assertIn("YuanForge 负责判断就绪", contract)
        self.assertIn("项目稳定文档负责保存", contract)
        self.assertIn("不是 YuanForge 的硬依赖", contract)

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
