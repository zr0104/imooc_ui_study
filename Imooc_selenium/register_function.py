import sys
sys.path.append(r'C:\Users\KXYL\PycharmProjects\imooc_study')
from selenium import webdriver
import time
from PIL import Image
from base.find_element import FindElement
from ShowapiRequest import ShowapiRequest
class RegisterFunction(object):
    def __init__(self, url, i):
        self.driver = self.get_driver(url, i)
    #获取url并且打开url
    def get_driver(self, url, i):
        if i == 1:
            driver = webdriver.Chrome()
        elif i == 2:
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Edge()
        driver.get(url)
        driver.maximize_window()
        return driver

    # 输入用户信息
    def send_mobile_info(self, key, data):
        self.get_mobile_element(key).send_keys(data)
