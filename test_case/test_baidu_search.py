import os
import sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from time import sleep
import pytest
from page_obj.baidu_page import BaiduPage

# 百度搜索，参数化
@pytest.mark.parametrize(
    ("searchkey"),
    ["python", "pytest", "pytest-html","selenium", "unittest"]
)
def test_baidu_search(searchkey, browser):
    bd = BaiduPage(browser)
    bd.open()
    bd.search_input(searchkey)
    bd.search_button()
    sleep(1)
    title = bd.search_title()
    assert title == searchkey + "_百度搜索"

