import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PluginTests(unittest.TestCase):
    def test_manifests_and_skill_are_consistent(self):
        manifest = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text())
        claude = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text())
        skill = (ROOT / "skills" / "focus-flow" / "SKILL.md").read_text()
        self.assertEqual(manifest["name"], claude["name"])
        self.assertEqual(manifest["name"], "focus-flow")
        self.assertIn("Modern Standard Arabic", skill)
        self.assertIn("Egyptian Arabic", skill)
        self.assertIn("English", skill)


    def test_eval_cases_are_valid_jsonl(self):
        lines = (ROOT / "evals" / "cases.jsonl").read_text().splitlines()
        cases = [json.loads(line) for line in lines if line.strip()]
        self.assertGreaterEqual(len(cases), 8)
        self.assertEqual(len({case["id"] for case in cases}), len(cases))
        self.assertTrue(all(case["criteria"] for case in cases))


if __name__ == "__main__":
    unittest.main()
