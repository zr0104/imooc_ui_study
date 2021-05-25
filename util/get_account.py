#coding=utf-8
from io import BytesIO

import wait as wait
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging
import unittest
from selenium.webdriver.common.action_chains import ActionChains

class GetAccount:
    def __init__(self,driver):
        self.driver = driver

    def get_chrome02(self):
        browers = webdriver.Chrome()
        browers.get("https://test.wbfwtop.com/pages/view/register.html")
        time.sleep(3)
        button = browers.find_element_by_class_name('layui-layer-btn0')
        button.click()
        wait = WebDriverWait(browers, 5)
        mobile_block = wait.until(EC.presence_of_element_located((By.ID, 'J-mobile')))
        password_block = wait.until((EC.presence_of_element_located((By.ID, 'J-newPassword'))))
        mobile_block.send_keys(mobile)
        password_block.send_keys(password)
        time.sleep(2)
        button = wait.until(EC.element_to_be_clickable((By.ID, 'J-sendAuthCode')))
        button.click()
        return browers, wait
