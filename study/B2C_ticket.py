# coding=utf-8
from selenium import webdriver
import time
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class B2C(object):
    def open_Chrome(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.csair.com/cn/")
        self.driver.maximize_window()
        time.sleep(5)  # 等待元素加载玩时间

# title = driver.switch_to("zsl-unlogin")
# title = EC.title_is("登录")
# title = EC.title_contains("登录")
# title = EC.presence_of_element_located("zsl-unlogin")
    def click_title(self):
        title = self.driver.find_element_by_link_text("登录")
        title.click()
        time.sleep(5)

# user = driver.find_element_by_class_name("memberBox")
# user = driver.find_element_by_link_text("会员登录")
# WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_name('memberBox')).click()
# user = driver.find_element_by_css_selector("memberBox")
# EC.title_contains("会员登录")
# EC.frame_to_be_available_and_switch_to_it("memberBox")
# print(EC.title_contains("会员登录"))
# EC.title_contains.frame("tab-title")
# driver.find_element_by_class_name("left member-login").click()
# locator = (By.CLASS_NAME,"left member-login")
# WebDriverWait(driver,5).until(EC.visibility_of_element_located(locator))
# locator.click()
# user.click()
    def send_username(self):
        self.driver.find_element_by_xpath("//*[@data-boxname='memberBox']").click()
        time.sleep(2)
        self.driver.find_element_by_id("userId").send_keys("13229914751")
        time.sleep(3)
# driver.find_element_by_name("passWordPH").send_keys("210523")
# driver.find_element_by_xpath("//*[@id='passWordPH']").send_keys("210523")
# passw=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='passWordPH']"))).click()
# driver.find_element_by_css_selector(EC.visibility_of_element_located("passWordPH")).send_keys("210523")

    def send_keys(self):
        '''
        点击输入框输入数据
        '''
        element = self.driver.find_element(By.XPATH,"//*[@id='passWordPH']")  #单击按钮
        # doubleclick_btn = self.driver.find_element_by_xpath('//*[@id="dbl passWordPH"]')  # 双击按钮
        # rightclick_btn = self.driver.find_element_by_xpath('//input[@id="right passWordPH"]')  # 右键单击按钮
        # EC.visibility_of_element_located(element)
        # element.clear()
        # ActionChself.driver).click(element).double_click(doubleclick_btn).context_click(rightclick_btn).perform()

        # element = self.driver.find_element_by_xpath('//*[@id="passWordPH"]')
        # hidden_submenu = self.driver.find_element_by_xpath('//*[@id="passWord"]')
        #
        # wait = WebDriverWait(self.driver, 5)
        # wait.until(lambda driver: driver.find_element_by_id("passWord"))
        # ActionChains(self.driver).move_to_element(element).click(hidden_submenu).perform()
        # element.send_keys("210523")

        # name = self.driver.find_element_by_id("passWordPH")
        # action = ActionChains(self.driver).move_to_element(name)
        # action.execute_script('document.getElementById("passWordPH").value="210523"')

# locator = (By.CLASS_NAME,"passWordPH")
# WebDriverWait(driver,5).until(EC.visibility_of_element_located(locator))
# print(locaa)
# driver.close()

# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='passWordPH']"))).send_keys("210523")
    def click_login(self):
        self.driver.find_element_by_id("loginProtocol").click()
        self.driver.find_element_by_id("mem_btn_login").click()
        print("登录成功")


# driver.find_element_by_class_name("zsl-unlogin").click()
# driver.close()

if __name__ == '__main__':
    test = B2C()
    test.open_Chrome()
    test.click_title()
    test.send_username()
    test.send_keys()
    test.click_login()
