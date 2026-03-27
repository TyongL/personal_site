from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
INDEX = SITE / "index.html"


class ProjectDetailPagesTest(unittest.TestCase):
    def test_homepage_project_links_and_detail_pages(self):
        index_html = INDEX.read_text(encoding="utf-8")

        self.assertIn('href="project-consult-agent.html"', index_html)
        self.assertIn('href="project-sales-training.html"', index_html)
        self.assertIn(
            'href="https://my.feishu.cn/wiki/F2UlwZ2UHiSyGhk9ZqPcimRTnFh?from=from_copylink"',
            index_html,
        )

        consult_detail = SITE / "project-consult-agent.html"
        sales_detail = SITE / "project-sales-training.html"
        self.assertTrue(consult_detail.exists(), "consult detail page should exist")
        self.assertTrue(sales_detail.exists(), "sales detail page should exist")

        consult_html = consult_detail.read_text(encoding="utf-8")
        sales_html = sales_detail.read_text(encoding="utf-8")

        self.assertIn("AI_Consulting_Agent_Matrix_(2).pdf", consult_html)
        self.assertIn("AI_Sales_Traning.pdf", sales_html)
        self.assertIn("联系我", consult_html)
        self.assertIn("联系我", sales_html)
        self.assertIn("查看产品方案文档", consult_html)
        self.assertIn("查看产品方案文档", sales_html)
        self.assertIn("assets/images/weixin.png", consult_html)
        self.assertIn("assets/images/weixin.png", sales_html)
        self.assertIn(
            "https://my.feishu.cn/wiki/E7ENwYnQEi2vRrkfJGFczwaHnTf",
            consult_html,
        )
        self.assertIn(
            "https://my.feishu.cn/wiki/X8nLwn0FcinlHPk8QbZcRj3JnfD?from=from_copylink",
            sales_html,
        )
        self.assertNotIn("Document Access", consult_html)
        self.assertNotIn("Document Access", sales_html)
        self.assertNotIn("Embedded Preview", consult_html)
        self.assertNotIn("Embedded Preview", sales_html)
        self.assertNotIn("打开 PDF", consult_html)
        self.assertNotIn("打开 PDF", sales_html)
        self.assertIn('class="pdf-shell relative', consult_html)
        self.assertIn('class="pdf-shell relative', sales_html)
        self.assertIn('class="project-actions', consult_html)
        self.assertIn('class="project-actions', sales_html)
        self.assertIn("top-4 right-4", consult_html)
        self.assertIn("top-4 right-4", sales_html)
        self.assertNotIn("right-3 top-1/2", consult_html)
        self.assertNotIn("right-3 top-1/2", sales_html)
        self.assertIn("联系我", consult_html)
        self.assertIn("联系我", sales_html)

        self.assertTrue(
            (SITE / "assets" / "docs" / "AI_Consulting_Agent_Matrix_(2).pdf").exists()
        )
        self.assertTrue(
            (SITE / "assets" / "docs" / "AI_Sales_Traning.pdf").exists()
        )


if __name__ == "__main__":
    unittest.main()
