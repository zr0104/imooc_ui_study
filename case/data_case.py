# coding:utf-8
import ddt
import unittest
from base.find_element import FindElement
@ddt.ddt
class DataTest(unittest.TestCase):
    def setUp(self):
        print("这个是setup")
    def tearDown(self):
        print("这个是teardown")
    #手机号码，密码，验证码
    @ddt.data(
        [13246821387,12345678]
    )
    @ddt.unpack
    def test_add(self,mobile,password):
        print(mobile,password)

if __name__ == '__main__':
        unittest.main()
