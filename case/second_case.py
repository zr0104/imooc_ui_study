# coding:utf-8
import sys
sys.path.append("E:\\Sen\\Sen\\study\\Python\\imooc_study")
import traceback
from business.register_business02 import RegisterBusiness02
from handle.register_handle import RegisterHandle
import unittest
from log.user_log import UserLog
from selenium import webdriver
import HTMLTestRunner
import os
import time

class SecondCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://test.wbfwtop.com/pages/view/login.html")

        cls.driver.maximize_window()
        time.sleep(2)

    def setUp(self):
        time.sleep(20)
        self.driver.refresh()  # 页面刷新

        self.logger.info("this is  chrome")

        self.logint = RegisterBusiness02(self.driver)

    def tearDown(self):
        time.sleep(10)
        # if sys.exc_info()[0]:
        #     for method_name,error in self._outcome.errors:
        #         if error:
        #             case_name = self._testMethodName
        #             file_path = os.path.join(os.getcwd()+"/report/"+case_name+".png")
        #             self.driver.save_screenshot(file_path)
        #     print("这个是case的后置条件1")

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()
        time.sleep(20)
        cls.driver.close()

    # def test_login_agreement(self):
    #     agreement = self.login.login_agreement_button().click()

    # 手机号码、密码、验证码、错误信息定位元素、错误提示信息

    # def click_greetest_agreement(self):
    #     time.sleep(2)
    #     self.driver.find_elements_by_class_name('layui-layer-btn0').click()

    def test_login_account_error(self):
        account_error = self.logint.login_account_error(1320000, 12345678)
        return self.assertFalse(account_error)

    def test_login_passwordt_error(self):
        passwordt_error = self.logint.login_passwordt_error(13200001111, 12345)
        return self.assertFalse(passwordt_error)

    def test_login_successt(self):
        successt = self.logint.user_baset(13246821387, 12345678)
        return self.assertFalse(successt)
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
    suite = unittest.TestSuite()
    #unittest.TextTestRunner().run(suite)
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(SecondCase))
    file_path = os.path.join(os.getcwd()+"/report/" + "Second_case.html")
    f = open(file_path,'wb')
    suite = unittest.TestSuite()
    #suite.suite.addTest(SecondtCase)
    suite.addTest(SecondCase('test_login_success'))
    # suite = addTest(SecondCase('test_login_code_error'))
    # suite = addTest(SecondCase('test_login_password_error'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="This is first report", description=u'这是我的第二次测试报告',verbosity=2)
    runner.run(suite)
