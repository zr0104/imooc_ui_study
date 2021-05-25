# coding:utf-8
from base.find_element import FindElement
class RegisterPage(object):
    def __init__(self,driver):
        self.fd = FindElement(driver)

    #同意协议
    def get_agreement_element(self):
        return self.fd.get_element("user_agreement")

    #获取手机元素
    def get_mobile_element(self):
        return self.fd.get_element("user_mobile")

    # #获取用户名元素
    # def get_email_element(self):
    #     return self.fd.get_element("user_name")

    #获取密码元素
    def get_password_element(self):
        return self.fd.get_element("user_password")

    #获取验证码元素
    def get_code_element(self):
        return self.fd.get_element("code_text")

    #获取注册按钮元素
    def get_button_element(self):
        return self.fd.get_element("register-button")

    #获取手机错误元素
    def get_mobile_error_element(self):
        return self.fd.get_element("user_mobile_error")

    # #获取用户名错误元素
    # def get_mobile_error(self):
    #     return self.fd.get_element("user_name_error")

    #获取密码错误元素
    def get_password_error_element(self):
        return self.fd.get_element("user_password_error")

    #获取验证码错误元素
    def get_code_error_element(self):
        return self.fd.get_element("code_text_error")

    #切换账号密码登录元素
    def get_current_element(self):
        return self.fd.get_element("user_current")

    #获取手机账号元素
    def get_account_element(self):
        return self.fd.get_element("user_account")

    #获取密码02元素
    def get_passwordt_element(self):
        return self.fd.get_element("user_passwordt")

    #获取极验验证码元素
    def get_greetest_element(self):
        return self.fd.get_element("greetest_code")

    #获取登录按钮元素
    def get_buttont_element(self):
        return self.fd.get_element("register_buttont")

    #获取手机账号错误元素
    def get_account_error_element(self):
        return self.fd.get_element("user_account_error")

    #获取手机账号错误元素
    def get_passwordt_error_element(self):
        return self.fd.get_element("user_passwordt_error")
