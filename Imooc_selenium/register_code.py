# coding:utf-8
from selenium import webdriver
import time
import random
from PIL import Image
# noinspection PyInterpreter,PyInterpreter
from util.ShowapiRequest import ShowapiRequest
# driver = webdriver.Chrome()
driver = webdriver.Firefox()
#浏览器初始化
def driver_init():
    driver.get("https://test.wbfwtop.com/pages/view/register.html")
    driver.maximize_window()
    time.sleep(5)

#获取element信息
def get_element(id):
    element = driver.find_element_by_id(id)
    return element

#获取随机数
def get_range_user():
    user_mobile = ''.join(random.sample('1234567890abcdefg', 10))
    return user_mobile

#获取极验验证码...


#运行主程序
def run_main():
    user_mobile_info = get_range_user()
    user_mobile = "1" + user_mobile_info
    file_name = r"C:\Users\KXYL\PycharmProjects\imooc_study\Image"
    driver_init()
    get_element("layui-layer-btn0").click()
    get_element("mobile").send_keys(user_mobile)
    get_element("J-newPassword").send_keys("111111")
    #极验代码...
    get_element("J-submit").click()
    driver.close()
