from selenium import webdriver
from selenium.webdriver import Remote
import pytest
import os
from py._xmlgen import html

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



@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    当测试失败的时候，自动截图，展示到html报告中
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
           file_name = report.nodeid.replace("::", "_")+".png"
           screen_img = _capture_screenshot()
           if file_name:
               html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                      'onclick="window.open(this.src)" align="right"/></div>' % screen_img
               extra.append(pytest_html.extras.html(html))
        report.extra = extra
        report.description = str(item.function.__doc__)
        report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")

@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
     cells.insert(1, html.th('Description'))
     cells.insert(2, html.th('Test_nodeid'))
     cells.pop(2)

@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    cells.insert(2, html.td(report.nodeid))
    cells.pop(2)

def _capture_screenshot():
    return driver.get_screenshot_as_base64()

driver = None

@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver
    if driver is None:
        driver = webdriver.Chrome()

    yield(driver)
    driver.quit()
    return driver