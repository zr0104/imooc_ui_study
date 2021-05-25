# coding:utf-8
import unittest
from threading import Thread

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC
import time
import random
from PIL import Image
import HTMLTestRunner
import os
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Firefox()
# driver = webdriver.Chrome()
driver.get("https://test.wbfwtop.com/pages/view/register.html")
time.sleep(5)
print(EC.title_contains("注册"))
driver.find_element_by_class_name("layui-layer-btn0").click()
mobile_element = driver.find_element_by_name("mobile")

'''
# 2.如何生成随机手机号码，便于后期填值
for i in range(5):
    user_mobile = ''.join(random.sample('1234567890abcdefg', 11))
    print(user_mobile)

#获取图片验证码
driver.save_screenshot("D:\Sen\imooc.png")
code_element = driver.find_element_by_id("J-sendAuthCode")
print(code_element.location)#{"x":123,"y":345}
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width']+left
height = code_element.size['height']+top
Image.open("D:\Sen\imooc.png")
im = Image.open("D:\Sen\imooc.png")
img = im.crop((left, top, right, height))
img.save("D:\Sen\imooc.png")
'''

# 协议弹窗确认
# driver.find_element_by_class_name("layui-layer-btn0").click()


'''
# 1.如何生成用户名：输入用户名及获取用户信息
element = driver.find_element_by_class_name("form-box")
locator = (By.CLASS_NAME, "form-box")
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))

print(mobile_element.get_attribute("placeholder"))
mobile_element.send_keys("13246001301")
print(mobile_element.get_attribute("value"))
print()
driver.close()
'''

    #
    # driver.find_element_by_class_name("layui-layer-btn0").click()
    # driver.find_element_by_name("mobile").send_keys("13246001300")
    # user_name_element = driver.find_element_by_name("authCode").send_keys("1234")
    #
    # # user_name_element_node = driver.find_element_by_class_name("confrols")[1]
    # # user_name_element = find_element_node.find_element_by_name("form-control")
    # # user_element.send_keys("qerqewre")
    #
    # driver.find_element_by_id("J-newPassword").send_keys("88888888")
    # driver.find_element_by_id("J-submit").click()
    # # driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys("111111")


# if __name__ = '__main__':
#     suite = unittest.TestSuite()
#     suite.
