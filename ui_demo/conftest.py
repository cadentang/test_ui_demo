from selenium import webdriver
from selenium.webdriver import Remote
import pytest
import os
from py._xmlgen import html

"""
pytest 命令行参数：
1.pytest -v:可以输出用例更加详细的执行信息，比如用例所在的文件及用例名称等。
2.pytest -s:输入我们用例中的调式信息，比如print的打印信息等，我们在上面用例8行加上一句 print(driver.title)。
3.pytest -m "标记":执行特定的测试用例。
4.pytest -k "关键字": 执行用例包含“关键字”的用例。
5.pytest -q：执行用例包含“关键字”的用例。
6.pytest --collect-only：罗列出所有当前目录下所有的测试模块，测试类及测试函数。
7.pytest --tb=style：屏蔽测试用例执行输出的回溯信息，可以简化用例失败时的输出信息。style可以是 on，line，short。
8.pytest --lf：当一次用例执行完成后，如果其中存在失败的测试用例，那么我们可以使用此命令重新运行失败的测试用例。
9.pytest --ff：如果上次测试用例出现失败的用例，当使用--ff后，失败的测试用例会首先执行，剩余的用例也会再次执行一次。
"""

# driver = None

# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#     :param item:
#     :return:
#     """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_") + ".png"
#             _capture_screenshot(file_name)
#             file_name = file_name.replace('test_case/', 'image/')
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                         'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
#
# def _capture_screenshot(name):
#     try:
#         file_name = name.split("test_case/")[1]
#     except IndexError:
#         file_name = name
#     base_dir = str(os.getcwd()).replace('\\', '/').split('test_case/')[0]
#     file_path = base_dir + "/report/image/" + file_name
#     driver.get_screenshot(file_path)



# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#     当测试失败的时候，自动截图，展示到html报告中
#     :param item:
#     """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#            file_name = report.nodeid.replace("::", "_")+".png"
#            screen_img = _capture_screenshot()
#            if file_name:
#                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
#                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
#                extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#         report.description = str(item.function.__doc__)
#         report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")
#
# @pytest.mark.optionalhook
# def pytest_html_results_table_header(cells):
#      cells.insert(1, html.th('Description'))
#      cells.insert(2, html.th('Test_nodeid'))
#      cells.pop(2)

# @pytest.mark.optionalhook
# def pytest_html_results_table_row(report, cells):
#     cells.insert(1, html.td(report.description))
#     cells.insert(2, html.td(report.nodeid))
#     cells.pop(2)
#
# def _capture_screenshot():
#     return driver.get_screenshot_as_base64()

driver = None

@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver
    if driver is None:
        driver = webdriver.Chrome()

    yield(driver)
    driver.quit()
    return driver

