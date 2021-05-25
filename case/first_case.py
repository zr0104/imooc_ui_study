# coding:utf-8
import sys
sys.path.append("E:\\Sen\\Sen\\study\\Python\\imooc_study")
import traceback
from business.register_business import RegisterBusiness
from handle.register_handle import RegisterHandle
import unittest
from log.user_log import UserLog
from selenium import webdriver
import HTMLTestRunner
import os
import time

class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
        cls.file_name = os.path.join(os.getcwd() + "/Image/" + "test001.png")
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://test.wbfwtop.com/pages/view/register.html")

        cls.driver.maximize_window()

    def setUp(self):

        self.driver.refresh()  # 页面刷新

        self.logger.info("this is  chrome")

        self.login = RegisterBusiness(self.driver)
        # self.login01 = RegisterHandle(self.driver)
        # self.login01.click_user_agreement_button()

    def tearDown(self):
        time.sleep(2)
        # if sys.exc_info()[0]:
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.getcwd()+"/report/"+case_name+".png")
                self.driver.save_screenshot(file_path)
        # print("这个是case的后置条件1")

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()
        cls.driver.close()

    # def test_login_agreement(self):
    #     agreement = self.login.login_agreement_button().click()

    # 手机号码、密码、验证码、错误信息定位元素、错误提示信息

    # def click_greetest_agreement(self):
    #     time.sleep(2)
    #     self.driver.find_elements_by_class_name('layui-layer-btn0').click()

    def test_login_mobile_error(self):
        mobile_error = self.login.login_mobile_error(132000011, 123456,self.file_name)
        return self.assertFalse(mobile_error, "测试失败")

    def test_login_code_error(self):
        code_error = self.login.login_code_error(13200001111, 123456,self.file_name)
        return self.assertFalse(code_error)

    def test_login_password_error(self):
        password_error = self.login.login_password_error(13200001111, 123456,self.file_name)
        return self.assertFalse(password_error)

    def test_login_success(self):
        success = self.login.user_base(13200001111, 123456,self.file_name)
        return self.assertFalse(success)
        #self.assert

'''
def main():
    first = FirstCase()
    first.test_login_code_error()
    first.test_login_email_error()
    first.test_login_password_error()
    first.test_login_username_error()
    first.test_login_success()
'''

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite)
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstCase)
    file_path = os.path.join(os.getcwd()+"/report/"+"first_case.html")
    f = open(file_path,'wb')
    suite = unittest.TestSuite()
    suite = addTest(FirstCase)
    suite = addTest(FirstCase('test_login_success'))
    suite = addTest(FirstCase('test_login_code_error'))
    suite = addTest(FirstCase('test_login_password_error'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="This is first report", description=u'这是我的第一次测试报告',verbosity=2)
    runner.run(suite)
