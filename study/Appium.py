#coding=utf-8
import time
from appium import webdriver

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']="5.1.1"
desired_caps['deviceName']='Android Emulator'
desired_caps['appPackage']='wbfwtop_buyer_v1.9.0_2020-12-02_ali'
desired_caps['appActivity']='wbfwtop_buyer_v1.9.0_2020-12-02_ali'
driver=webdriver.Remote("http://test.portal.lvdatong.com/#/index",desired_caps)
time.sleep(1)
el1 = driver.find_element_by_id("android:id/button2")
el1.click()
time.sleep(1)
el2 = driver.find_element_by_id("com.tal.kaoyan:id/tv_skip")
el2.click()
