# coding:utf-8

from page.register_page import RegisterPage
from util.get_code import GetCode
from log.user_log import UserLog
from selenium import webdriver
import time

class RegisterHandle():
    def __init__(self,driver):
        self.driver = driver
        self.register_p = RegisterPage(self.driver)
        get_user_log = UserLog()
        self.logger = get_user_log.get_log()

    #点击同意协议
    def click_user_agreement_button(self):
        self.logger.info("确认协议成功：")
        self.register_p.get_agreement_element().click()

    #输入手机号
    def send_user_mobile(self, usermobile):
        self.logger.info("请输入手机号码：" + usermobile)
        self.register_p.get_mobile_element().send_keys(usermobile)

    #输入密码
    def send_user_password(self, password):
        self.logger.info("输入的密码是：" + password)
        self.register_p.get_password_element().send_keys(password)

    #输入验证码
    def send_user_code(self, file_name):
        get_code_text = GetCode(self.driver)
        code = get_code_text.code_online(file_name)
        self.register_p.get_code_error_element().send_keys(code)

    #获取文字信息
    def get_user_text(self, info, user_info):
        try:
            if info == "user_mobile_error":
                text = self.register_p.get_mobile_error_element().text
            elif info == "user_password_error":
                text = self.register_p.get_mobile_error_element().text
            else:
                text = self.register_p.get_code_error_element().text
        except:
            text = None
        return text

    #点击注册按钮
    def click_register_button(self):
        self.register_p.get_button_element().click()

    #获取注册按钮文字
    def get_register_text(self):
        return self.register_p.get_button_element().text


    #切换账号登录元素
    def click_current_element(self):
        self.driver.find_element_by_link_text("账号密码登录").click()
        # return self.register_p.get_current_element()

        # data = {'name': self.register_p.get_current_element()}
        # self.SWITCH_TO_WINDOW(data)

    #输入手机、邮箱账号
    def send_user_account(self, usaccount):
        self.logger.info("请输入手机号码/邮箱：" + str(usaccount))
        self.register_p.get_account_element().send_keys(usaccount)
        print(usaccount)

    #输入密码02
    def send_user_passwordt(self, passwordt):
        self.logger.info("输入的密码是：" + str(passwordt))
        self.register_p.get_passwordt_element().send_keys(passwordt)

    #点击极验验证码按钮
    def click_greetest_button(self):
        self.register_p.get_greetest_element().click()
        # print(self.register_p.get_greetest_element())

    #点击登录02按钮
    def get_register_buttont(self):
        self.register_p.get_buttont_element().click()

    #获取文字信息
    def get_user_textt(self, infot, user_info02):
        try:
            if infot == "user_account_error":
                text = self.register_p.get_account_error_element().text
            elif infot == "user_password02_error":
                text = self.register_p.get_passwordt_error_element().text
            else:
                text = self.register_p.get_code_error_element().text
        except:
            text = None
        return text
