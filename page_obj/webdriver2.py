# coding=utf-8
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select


class WebDriver(object):
    """
    PO模型基础类，对原生webdriver类进行二次封装‘
    """
    BASE_URL = "https://www.baidu.com"  # 定义项目基本URL
    TIME_OUT = 10 # 定位元素定位超时时间 
    url = None
    driver = None
    domain = None


    def __init__(self, selenium_webdriver, base_url=BASE_URL, time_out=TIME_OUT):
        self.driver = selenium_webdriver
        self.base_url = base_url
        self.time_out = time_out

    def _open(self, url):
        """
        根据页面提供的路径和基本url得到完整路径
        :param url: 
        :return: 
        """
        url = self.base_url + url
        self.driver.get(url)

    def open(self):
        """
        打开url
        :return: 
        """
        self._open(self.url)

    def element_wait(self, by, value, secs=TIME_OUT):
        """
        设置元素显示等待
        :return: 
        """
        if by == "id":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.ID, value)))
        elif by == "name":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.NAME, value)))
        elif by == "class":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
        elif by == "link_text":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.LINK_TEXT, value)))
        elif by == "xpath":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.XPATH, value)))
        elif by == "css":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
        else:
            raise NoSuchElementException("Not find element, Please check the syntax error.")

    def get_element(self, css):
        """
        判断元素定位方式，返回元素
        :param css: 
        :return: 
        """
        if "=>" not in css:
            by = "css"
            value = css
            self.element_wait(by, css)
        else:
            by = css.split("=>")[0]
            value = css.spilt("=>")[1]
            if by == "" or value == "":
                raise  NameError("Grammatical errors,reference: 'id=>useranme'.")
            self.element_wait(by, value)

        if by == "id":
            element = self.driver.find_element_by_id(value)
        elif by == "name":
            element = self.driver.find_element_by_name(value)
        elif by == "class":
            element = self.driver.find_element_by_class_name(value)
        elif by == "link_text":
            element = self.driver.find_element_by_link_text(value)
        elif by == "xpath":
            element = self.driver.find_element_by_xpath(value)
        elif by == "css":
            element = self.driver.find_element_by_css_selector(value)
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")
        return element

    def max_window(self):
        """
        将浏览器最大化
        :return: 
        """
        self.driver.maximize_window()

    def set_window(self, wide, high):
        """
        设置浏览器的大小
        :param wide: 
        :param high: 
        :return: 
        """
        self.driver.set_window_size(wide, high)

    def type(self, css, text):
        """
        操作输入框
        :param css: 
        :param text: 
        :return: 
        """
        e1 = self.get_element(css)
        e1.send_keys(text)

    def clear(self, css):
        """
        清除文本输入框中的内容
        :param css: 
        :return: 
        """
        e1 = self.get_element(css)
        e1.clear()

    def click(self, css):
        """
        对所有能左键点击的控件执行点击操作
        :param css: 
        :return: 
        """
        e1 = self.get_element(css)
        e1.click()

    def right_click(self, css):
        """
        对控件进行右键操作
        :param css: 
        :return: 
        """
        e1 = self.get_element(css)
        ActionChains(self.driver).context_click(e1).perform()

    def move_to_element(self, css):
        """
        鼠标移动到元素上
        :param css: 
        :return: 
        """
        e1 = self.get_element(css)
        ActionChains(self.driver).move_to_element(e1).perform()

    def double_click(self, css):
        """
        鼠标双击元素
        :param css: 
        :return: 
        """
        e1 = self.get_element(css)
        ActionChains(self.driver).double_click(e1).perform()

    def drag_and_drop(self, el_css, ta_css):
        """
         拖拽功能
        :param el_css: 
        :param ta_css: 
        :return: 
        """
        element = self.get_element(el_css)
        target = self.get_element(ta_css)
        ActionChains(self.driver).drag_and_drop(element, target).perform()

    def click_text(self, text):
        """
        点击链接的文本
        :param text: 
        :return: 
        """
        self.driver.find_element_by_partial_link_text(text).click()

    def close(self):
        """
        关闭页面
        :return: 
        """
        self.driver.close()

    def quit(self):
        """
        退出浏览器
        :return: 
        """
        self.driver.quit()

    def submit(self, css):
        """
        提交表单
        :param css: 
        :return: 
        """
        e1 = self.get_element(css)
        e1.submit()

    def F5(self):
        """
        刷新页面
        :return: 
        """
        self.driver.refresh()

    def js(self, script):
        """
        执行js脚本
        :param script: 
        :return: 
        """
        self.driver.execute_script(script)

    def get_attribute(self, css, attribute):
        """
        得到一个元素的指定属性
        :param css: 
        :param attribute: 
        :return: 
        """
        e1 = self.get_element(css)
        return e1.get_attribute(attribute)

    def get_text(self, css):
        """
        得到text文本信息
        :param css: 
        :param attribute: 
        :return: 
        """
        e1 = self.get_element(css)
        return e1.text

    def get_display(self, css):
        """
        判断一个元素是否可见
        :param css: 
        :return: 
        """
        e1 = self.get_element(css)
        return e1.is_displayed()

    def get_title(self):
        """
        得到窗口的标题
        :return: 
        """
        return self.driver.title

    def get_url(self):
        """
        得到页面的url地址
        :return: 
        """
        return self.driver.current_url()

    def get_alert_text(self):
        """
        获取对话框的提示信息
        :return: 
        """
        return self.driver.switch_to.alert.text

    def get_window_img(self, file_path):
        """
        当前窗口的截图
        :param file_path: 
        :return: 
        """
        self.driver.get_screenshot_as_file(file_path)

    def wait(self, secs):
        """
        设置隐性等待
        :param secs: 
        :return: 
        """
        self.driver.implicitly_wait(secs)

    def accept_alert(self):
        """
        接受警告框
        :return: 
        """
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        """
        取消对话框
        :return: 
        """
        self.driver.switch_to.alert.dismiss()

    def switch_to_frame(self, css):
        """
        切换到frame框
        :param css: 
        :return: 
        """
        iframe_e1 = self.get_element(css)
        self.driver.switch_to.frame(iframe_e1)

    def switch_to_frame_out(self):
        """
        跳出frame框
        :return: 
        """
        self.driver.switch_to.default_content()

    def open_new_window(self, css):
        """
        打开新的窗口
        :param css: 
        :return: 
        """
        original_window = self.driver.current_window_handle
        e1 = self.get_element(css)
        e1.click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != original_window:
                self.driver.switch_to.window(handle)

    def get_screenshot(self, file_path):
        """
        
        :param file_path: 
        :return: 
        """
        self.driver.get_screenshot_as_file(file_path)

    def select(self, css, value):
        """
        下拉框选择
        :param css: 
        :param value: 
        :return: 
        """
        e1 = self.get_element(css)
        Select(e1).select_by_value(value)

    def screenshot_on_exception(self, locator):
        """
        元素动态等待与截图
        :param css: 
        :param value: 
        :return: 
        """
        try:
            WebDriverWait(self.driver, DEFAULT_SECONDS).until(EC.visibility_of_element_located(locator))
        except TimeoutException as e:
            # print(self.gen_screenshot_path(locator))
            self.driver.get_screenshot_as_file(self.gen_screenshot_path(locator))
            msg = "Time out when locate element using %s: %s" %(locator[0], locator[-1])
            raise TimeoutException(msg)




