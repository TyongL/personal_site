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


class ProjectsTabUITest(unittest.TestCase):
    def test_tab_buttons_exist(self):
        html = INDEX.read_text(encoding="utf-8")
        self.assertIn('data-tab="all"', html)
        self.assertIn('data-tab="project"', html)
        self.assertIn('data-tab="article"', html)

    def test_four_project_cards_have_data_type(self):
        html = INDEX.read_text(encoding="utf-8")
        self.assertEqual(
            html.count('data-type="project"'), 4,
            "4 个项目卡片都应有 data-type=\"project\"",
        )

    def test_projects_grid_id_exists(self):
        html = INDEX.read_text(encoding="utf-8")
        self.assertIn('id="projects-grid"', html)

    def test_articles_container_exists(self):
        html = INDEX.read_text(encoding="utf-8")
        self.assertIn('id="articles-container"', html)


class ArticleRenderingTest(unittest.TestCase):
    def test_fetch_articles_json_in_script(self):
        html = INDEX.read_text(encoding="utf-8")
        self.assertIn("fetch('articles.json')", html)

    def test_wechat_feed_label_in_script(self):
        html = INDEX.read_text(encoding="utf-8")
        self.assertIn("WECHAT_FEED", html)

    def test_read_original_link_in_script(self):
        html = INDEX.read_text(encoding="utf-8")
        self.assertIn("阅读原文", html)

    def test_switch_tab_function_in_script(self):
        html = INDEX.read_text(encoding="utf-8")
        self.assertIn("switchTab", html)

    def test_article_data_type_attribute_in_script(self):
        html = INDEX.read_text(encoding="utf-8")
        self.assertIn('data-type="article"', html)


if __name__ == "__main__":
    unittest.main()
