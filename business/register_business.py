# coding:utf-8
from handle.register_handle import RegisterHandle
import time
class RegisterBusiness():
    def __init__(self,driver):
        self.register_h = RegisterHandle(driver)

    def user_base(self, mobile, password, file_name):
        self.register_h.click_user_agreement_button()
        time.sleep(1)
        self.register_h.send_user_mobile(mobile)
        self.register_h.send_user_password(password)
        self.register_h.send_user_code(file_name)
        self.register_h.click_register_button()

    def user_baset(self,useraccount,passwordt):
        self.register_h.click_user_agreement_button()
        time.sleep(2)
        self.register_h.send_user_account(useraccount)
        self.register_h.send_user_passwordt(passwordt)
        self.register_h.click_greetest_button()
        self.register_h.get_register_buttont()

    def register_sucees(self):
        if self.register_h.get_register_text() == None:
            return True
        else:
            False

    #执行操作
    def login_mobile_error(self, mobile, password, file_name):
        self.user_base(mobile,password,file_name)
        if self.register_h.get_user_text('mobile_error', "请填写手机号") == None:
            # print("手机号码格式不正确")
            return True
        else:
            return False

    def register_function(self,mobile,password,file_name,assertCode,assertText):
        self.user_base(mobile,password,file_name)
        if self.register_h.get_user_text(assertCode,assertText) == None:
            # print("手机号码检验不成功")
            return True
        else:
            return False

    # 密码错误
    def login_password_error(self,mobile,password,file_name):
        self.user_base(mobile,password,file_name)
        if self.register_h.get_user_text('password_error', "最少要输入 6 个字符") == None:
            # print("密码检验不成功")
            return True
        else:
            return False

    # 验证码错误
    def login_code_error(self,mobile,password,file_name):
        self.user_base(mobile,password,file_name)
        if self.register_h.get_user_text('code_text_error', "验证码错误") == None:
            # print("验证码检验不成功")
            return True
        else:
            return False

    def login_account_error(self,useraccount, passwordt):
        self.user_baset(useraccount,passwordt)
        if self.register_h.get_user_text('mobile_error', "请填写手机号") == None:
            # print("手机号码格式不正确")
            return True
        else:
            return False

    # 密码错误
    def login_passwordt_error(self,mobile,passwordt):
        self.user_baset(mobile,passwordt)
        if self.register_h.get_user_text('password02_error', "请输入密码") == None:
            # print("密码检验不成功")
            return True
        else:
            return False

