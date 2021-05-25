'''
import os
from time import sleep
class SSH(object):
    def __init__(self,host,port,user,pwd):
        self.host='39.108.51.97'
        self.port=22
        self.user=13246001119
        self.pwd=123456
    """此方法是统计在登陆之前获取的服务日志code的数量"""
    def before_count(self, logfile_absolute_path, paramiko):
        logfile_parentdir,logfile_name=os.path.split(logfile_absolute_path)
        shell="cd {}; cat {}|grep 动态验证码为".format(logfile_parentdir,logfile_name)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.host,self.port,self.user,self.pwd)
        self.ssh=ssh
        stdin, stdout, stderr = self.ssh.exec_command(shell)
        res,err = stdout.readlines(),stderr.readlines()
        result = res if res else err
        return len(result)

'''


import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#from util.get_code06 import Getcode06
import unittest

# 设置代理
proxy = '220.191.64.149'
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--proxy-server = http://' + proxy)

broswer = webdriver.Chrome()
# 测试代理
# broswer.get('http://httpbin.org/get')

# 输入即将收到短信的手机号码
tel = 13246821387

class GetMobileCode(unittest.TestCase):

    def __init__(self,driver):
        self.fc = Getcode06(driver)

    def get_loin1(self):
        self.fc.open_chrome()



if __name__ == '__main__':
    GetMobileCode(driver=None)

