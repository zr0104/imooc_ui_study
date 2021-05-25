# coding:utf-8
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from log.path_os import record_dir
from log.user_log import UserLog
import time
# import win32gui
# import win32con

log = UserLog()


class Base:

    # 引入驱动
    def __init__(self, drivers):
        self.driver = drivers

    # 截图
    def record(self, model_name="error"):
        RecordPath = record_dir + "/{}_{}.png".format(model_name,
                                                      time.strftime("%Y-%m-%d-""%H-%M-%S", time.localtime()))
        try:
            self.driver.get_screenshot_as_file(RecordPath)
        except Exception as e:
            log.error("截图失败：{}".format(e))

    # 等待元素 - 默认等待30秒，每0.5秒找一次
    def wait_elevisible(self, locator, timeout=30, poll_frequency=0.5, model_name="model"):
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(
                expected_conditions.visibility_of_element_located(locator))
        except Exception as e:
            self.record(model_name)
            log.error("等待超时，未找到元素：{}".format(e))

    # 查找元素
    def get_element(self, locator, model_name="model"):
        try:
            return self.driver.find_element(*locator)
        except Exception as e:
            self.record(model_name)
            log.error("未找到元素：{}".format(e))

    # 点击元素
    def click_elemet(self, locator, model_name="model"):
        ele = self.get_element(locator, model_name)
        try:
            ele.click()
        except Exception as e:
            self.record(model_name)
            log.error("点击元素失败：{}".format(e))

    # 输入框 - 输入内容
    def input_text(self, locator, value, model_name="model"):
        ele = self.get_element(locator, model_name)
        try:
            ele.send_keys(value)
        except Exception as e:
            self.record(model_name)
            log.error("输入内容失败：{}".format(e))

    # 输入框 - 清空内容
    def clear_text(self, locator, model_name="model"):
        ele = self.get_element(locator, model_name)
        try:
            ele.clear()
        except Exception as e:
            self.record(model_name)
            log.error("清空输入框内容失败：{}".format(e))

    # 获取元素的文本内容
    def get_text(self, locator, model_name="model"):
        ele = self.get_element(locator, model_name)
        try:
            return ele.text
        except Exception as e:
            self.record(model_name)
            log.error("获取元素文本内容失败：{}".format(e))

    # 获取元素属性
    def get_ele_attribute(self, locator, attribute, model_name="model"):
        ele = self.get_element(locator, model_name)
        try:
            return ele.get_attribute(attribute)
        except Exception as e:
            self.record(model_name)
            log.error("获取元素属性失败：{}".format(e))

    # 元素存在则为True，否则为False
    def is_eleExist(self, locator, model_name="model"):
        try:
            self.wait_elevisible(locator, model_name=model_name)
            return True
        except Exception as e:
            self.record(model_name)
            log.error("元素不存在：{}".format(e))
            return False

    # 切换alert弹框
    def switch_to_alert(self, action="accept", content="请输入内容", model_name="model"):
        try:
            WebDriverWait(self.driver, timeout=30, poll_frequency=0.5).until(expected_conditions.alert_is_present())
            # 切换到alert
            alert = self.driver.switch_to.alert
            # 确定按钮
            if action == "accept":
                alert.accept()
            # 输入框
            elif action == "value":
                alert.send_keys(content)
            # 取消按钮
            else:
                alert.dismiss()
        except Exception as e:
            self.record(model_name)
            log.error("alert操作失败：{}".format(e))

    # windows窗口切换
    def switch_window(self, str_wd="", index=None, model_name="mode1"):
        try:
            time.sleep(2)
            # 获取所有窗口
            windows = self.driver.window_handles
            if str_wd == "new":
                self.driver.switch_to.window(windows[-1])
            else:
                if index is not None and 0 <= int(index) < len(windows):
                    self.driver.switch_to.window(windows[int(index)])
        except Exception as e:
            self.record(model_name)
            log.error("切换浏览器窗口失败：{}".format(e))

    # iframe切换
    def switch_to_iframe(self, locator, model_name="mode1"):
        try:
            # 切过去
            ele = self.get_element(locator)
            WebDriverWait(self.driver, timeout=30, poll_frequency=0.5).until(
                expected_conditions.frame_to_be_available_and_switch_to_it(ele))
            # 执行命令后切回来
            self.driver.switch_to.default_content()
        except Exception as e:
            self.record(model_name)
            log.error("切换iframe失败：{}".format(e))

    # 上传文件  每个系统不一样，一般是这种
    def upload(self, file, browser_type="chrome", model_name="mode1"):
        try:
            if browser_type == "chrome":
                title = "打开"
            else:
                title = ""
            # 一级窗口
            dialog = win32gui.FindWindow("#32770", title)
            # 二级窗口
            ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
            comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)
            # 三级窗口 - 输入框
            edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)
            # 四级窗口 - 打开按钮
            open_button = win32gui.FindWindowEx(dialog, 0, 'Button', "打开(&O)")
            # 输入文件路径
            win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, file)
            # 上传
            win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, open_button)
        except Exception as e:
            self.record(model_name)
            log.error("上传文件失败：{}".format(e))

    # 滚动条操作
    def move_to_see(self, locator, type_ele="will", model_name="mode1"):
        try:
            if type_ele == "will":
                self.driver.execute_script("arguments[0].scrollIntoView();", locator)
                time.sleep(2)
            elif type_ele == "top":
                self.driver.execute_script("window.scrollTo(0,0)")
                time.sleep(2)
            else:
                self.driver.execute_script("var q=document.documentElement.scrollTop=10000")
                time.sleep(2)
        except Exception as e:
            self.record(model_name)
            log.error("滚动条操作失败：{}".format(e))
