#coding=utf-8
try:
    from webdriver2 import WebDriver
except ImportError:
    from .webdriver2 import WebDriver
from time import sleep


class BaiduPage(WebDriver):
    """
    百度首页
    """
    url = '/'   

    # 百度输入框
    def search_input(self, searchkey):
        self.type("#kw", searchkey)

    # 百度按钮
    def search_button(self):
        self.click("#su")
        sleep(1)

    # 搜索标题
    def search_title(self):
        return self.get_title()

    # 设置
    def settings(self):
        self.click("link_text=>设置")

    # 搜索设置
    def search_setting(self):
        self.click("#wrapper > div.bdpfmenu > a.setpref")

    # 保存设置
    def save_setting(self):
        self.click(".prefpanelgo")
        self.accept_alert()
