import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
import pytest
from page_obj.baidu_page import BaiduPage


# 百度搜索设置
def test_baidu_a_setting(browser):
    bd = BaiduPage(browser, time_out=10)
    bd.open()
    bd.settings()
    bd.search_setting()
    bd.save_setting()


