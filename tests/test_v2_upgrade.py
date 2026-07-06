# tests/test_v2_upgrade.py
from pathlib import Path
import unittest
import json

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
INDEX = SITE / "index.html"


class BaiduAnalyticsTest(unittest.TestCase):
    def test_baidu_script_in_head(self):
        html = INDEX.read_text(encoding="utf-8")
        self.assertIn(
            "hm.baidu.com/hm.js?627da0e9a787ddbeacb52a04791bf278",
            html,
        )
        script_pos = html.find("627da0e9a787ddbeacb52a04791bf278")
        head_close_pos = html.find("</head>")
        self.assertLess(script_pos, head_close_pos, "百度统计脚本必须在 </head> 之前")


class ArticlesDataTest(unittest.TestCase):
    def test_articles_json_exists(self):
        self.assertTrue(
            (SITE / "articles.json").exists(),
            "site/articles.json 应存在",
        )

    def test_articles_json_valid_structure(self):
        data = json.loads((SITE / "articles.json").read_text(encoding="utf-8"))
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0, "articles.json 至少需要一条示例记录")
        required = ["id", "title", "date", "excerpt", "cover", "url"]
        for field in required:
            self.assertIn(field, data[0], f"字段缺失: {field}")

    def test_articles_image_dir_exists(self):
        self.assertTrue(
            (SITE / "assets" / "images" / "articles").exists(),
            "site/assets/images/articles/ 目录应存在",
        )


if __name__ == "__main__":
    unittest.main()
