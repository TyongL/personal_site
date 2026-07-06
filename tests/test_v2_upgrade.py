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


if __name__ == "__main__":
    unittest.main()
