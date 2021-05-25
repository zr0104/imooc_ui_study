# coding:utf-8
from handle.register_handle import RegisterHandle
import time
from util.get_code import GetCode

class RegisterBusiness02():
    def __init__(self,driver):
        self.register_ht = RegisterHandle(driver)
        self.register_hc = GetCode(driver)

    def user_baset(self,usaccount,passwordt):
        self.register_ht.click_current_element()
        time.sleep(2)
        self.register_ht.send_user_account(usaccount)
        time.sleep(2)
        self.register_ht.send_user_passwordt(passwordt)
        time.sleep(2)
        self.register_ht.click_greetest_button()
        self.register_hc.get_pool()
        time.sleep(20)
        self.register_ht.get_register_buttont()

    def register_sucees(self,usaccount,passwordt):
        self.user_baset(usaccount,passwordt)
        if self.register_ht.get_register_buttont() == None:
            return True
        else:
            return False

    def login_account_error(self,usaccount, passwordt):
        self.user_baset(usaccount,passwordt)
        if self.register_ht.get_user_text('account_error', "请填写手机号/邮箱") == None:
            print("手机号码格式不正确")
            return True
        else:
            return False

    # 密码错误
    def login_passwordt_error(self,usaccount,passwordt):
        self.user_baset(usaccount,passwordt)
        if self.register_ht.get_user_text('passwordt_error', "请输入密码") == None:
            print("密码检验不成功")
            return True
        else:
            return False

