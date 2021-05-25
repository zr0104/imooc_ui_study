# -*- coding: utf-8 -*-
"""
@author：你们的龙哥
@2018-06-21
规则只匹配极验的官网，若使用破解验证码的规则，仍需要根据实际项目情况做调整
建议：本程序提供的是思路，无需修改本程序代码
写代码过程中遇到的问题：
1、chrome driver要下载，并配置好，过程忘记了，请百度。driver的版本一定要和chrome的版本对应。。。
2、chrome浏览器不在环境变量的，要把第32行（大概位置）注释解开，并填入自己电脑chrome的位置。要不就会报错，二进制文件找不到之类的。
3、reload（sys)要加，不然不能识别中文
4、location定位的时候，经常出白图，是因为save_screenshot()截屏的时候，保存的图片像素为实际像素的2倍，这个百度了一下，有人说是高分屏的原因,因为我用的mac？
5、第一次识别失败后，经常会报错，好像是时间超时之类的，我try掉了。想踩雷的，可以去掉所有的try自己玩一下。
6、本代码经过本机的极限测试，连续尝试40多次后依然可以正常运行，然后我就手动结束了测试。
"""
from importlib import reload

from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import os
import logging
import time
import sys
reload(sys)
#sys.setdefaultencoding('utf-8')

# 本段为指定chrome浏览器的位置，如果chrome安装的时候放到了环境变量中，应该用不到这样写,注释掉就可以
# 果然，把chrome移动到应用程序里面后，自动就配置到环境变量了（mac本）
#chrome_options = Options()
# chrome_options.binary_location = r"/Users/qmp/Downloads/Google Chrome.app/Contents/MacOS/Google Chrome"

class CrackGeetest():
    """
    实现了正常登陆、错误重试、多次重试后刷新图片的功能。。。除非规则和页面结构变更，要不基本走不到多次刷新图片重试这一步
    没有对crack()和fail_again()这两个类方法进行精简，是希望程序的运行步骤清晰明了。。。
    """
    def __init__(self,url,mobile,password,threshold=60,left=57,deviation=6):
        self.url = url
        self.driver = webdriver.Chrome()  # 前面注释掉参数（chrome_options=chrome_options）
        self.driver.get(url)
        self.wait = WebDriverWait(self.driver,5)
        self.mobile = mobile
        self.password = password
        self.threshold = threshold #验证码图片对比中RGB的差值，可调
        self.left = left #验证码图片的对比中的起始坐标，即拖动模块的右边线位置
        self.deviation = deviation # 偏移量，这个值是多次测试得出的经验值
        self.count = 1

    def close_win(self):
        self.driver.close()

    def get_agreement_element(self):
        self.driver.find_element_by_class_name('layui-layer-btn0').click()

    def get_geetest_button(self):
        """
        点击按钮，弹出没有缺口的图片
        :return: 返回按钮对象
        """
        button = self.wait.until(EC.presence_of_element_located((By.ID, 'J-sendAuthCode')))
        return button

    # # 点击弹窗极验验证码
    # def click_gee_button(self):
    #     self.driver.find_element_by_id("J-sendAuthCode").click()


    def get_slider(self):
        """
        获取滑块
        :return: 滑块对象
        """
        slider = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,'geetest_slider_button')))
        return slider

    def get_snap(self):
        """
        对整个网页截图，保存图片，然后用PIL.Image拿到图片对象
        :return: 图片对象
        """
        # 新增保存路径
        #img_path = os.path.join(os.getcwd() + '/Image/' + '极验验证过程中产生的图片.png')
        #保存图片
        self.driver.save_screenshot('极验验证过程中产生的图片.png')
        page_snap_obj = Image.open('极验验证过程中产生的图片.png')
        return page_snap_obj

    def get_image(self,name='captcha.png'):
        """
        从网页的网站截图中，截取验证码图片
        :return: 验证码图片对象
        """
        img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_img')))
        time.sleep(2)  # 保证图片刷新出来
        location = img.location
        size = img.size
        top = location['y']
        bottom = location['y'] + size['height']
        left = location['x']
        right = location['x'] + size['width']
        page_snap_obj = self.get_snap()

        #这里强调一下：大概由于高分屏的原因，网页的截图是实际像素的2倍，所以验证码定位也要相应*2
        # crop_imag_obj = page_snap_obj.crop((left,top,right,bottom))
        crop_imag_obj = page_snap_obj.crop((2 * left, 2 * top, 2 * right, 2 * bottom))
        size = 258, 159
        crop_imag_obj.thumbnail(size)
        #实际生产环境下就不需要保存这张图片了
        # crop_imag_obj.save(name)
        return crop_imag_obj

    def open(self):
        """
        打开网页输入用户名和密码
        :return:
        """
        self.driver.get(self.url)
        time.sleep(3)
        mobile = self.wait.until(EC.presence_of_element_located((By.ID, 'J-mobile')))
        password = self.wait.until(EC.presence_of_element_located((By.ID, 'J-newPassword')))
        mobile.send_keys(self.mobile)
        password.send_keys(self.password)

    def get_distance(self,image1, image2):
        """
        拿到滑动验证码需要移动的距离
        :param image1: 没有缺口的图片对象
        :param image2: 带缺口的图片对象
        :return: 需要移动的距离
        """
        i = 0
        for i in range(self.left, image1.size[0]):
            for j in range(image1.size[1]):
                rgb1 = image1.load()[i, j]
                rgb2 = image2.load()[i, j]
                res1 = abs(rgb1[0] - rgb2[0])
                res2 = abs(rgb1[1] - rgb2[1])
                res3 = abs(rgb1[2] - rgb2[2])
                if not (res1 < self.threshold and res2 < self.threshold and res3 < self.threshold):
                    return i - self.deviation  # 误差矫正
        logging.debug('未识别出验证码中的不同位置，或图片定位出现异常')
        return i  # 如果没有识别出不同位置，则象征性的滑动，以刷新下一张验证码

    def get_tracks(self,distance):
        """
        拿到移动轨迹，模仿人的滑动行为，先匀加速后均减速
        匀变速运动基本公式：
        ①：v=v0+at
        ②：s=v0t+½at²
        ③：v²-v0²=2as
        :param distance:需要移动的距离
        :return:存放每0.3秒移动的距离
        """
        distance += 20  # 先滑过一点，最后再反着滑动回来
        # 初速度
        v = 0
        # 单位时间为0.3s来统计轨迹，轨迹即0.3s内的位移
        t = 0.3
        # 位移/轨迹列表，列表内的一个元素代表0.3s的位移
        forward_tracks = []
        # 当前位移
        current = 0
        # 到达mid值开始减速
        mid = distance * 4 / 5
        while current < distance:
            if current < mid:
                # 加速度越小，单位时间的位移越小，模拟的轨迹就越多越详细
                a = 2
            else:
                a = -3
            # 初速度
            v0 = v
            # 0.3秒时间内的位移
            s = v0 * t + 0.5 * a * (t ** 2)
            # 当前的位置
            current += s
            # 添加到轨迹列表,round()为保留一位小数且该小数要进行四舍五入
            forward_tracks.append(round(s))
            # 速度已经达到v，该速度作为下次的初速度
            v = v0 + a * t

        # 反着滑动到准确位置
        back_tracks = [-3, -3, -2, -2, -2, -2, -2, -1, -1, -1]  # 总共等于-20
        return {'forward_tracks': forward_tracks, 'back_tracks': back_tracks}

    def login(self):
        """
        登录
        :return: None
        """
        submit = self.wait.until(EC.element_to_be_clickable((By.ID, 'J-submit')))
        submit.click()
        print('登录成功')
        logging.debug('登陆成功')

    def crack(self):
        """
        程序运行流程。。。
        :return:
        """
        #步骤一：输入用户名密码
        self.open()

        # 点击按钮前同意协议agreement
        self.get_agreement_element()
        time.sleep(2)

        #步骤二：点击按钮，弹出没有缺口的图片（方法1）
        button = self.get_geetest_button()
        button.click()
        time.sleep(1)
        #步骤二：点击按钮，弹出没有缺口的图片（方法2）
        #self.click_gee_button()

        # 步骤三：拿到没有缺口的图片
        image1 = self.get_image('captcha1.png')

        # 步骤四：点击托送按钮，弹出有缺口的图片
        slider = self.get_slider()
        slider.click()

        #步骤五：拿到有缺口的图片
        image2 = self.get_image('captcha2.png')

        #步骤六：对比两张图片的所有RBG像素点，得到不一样像素点间的差值，即要移动的距离
        distance = self.get_distance(image1, image2)

        print(distance)

        time.sleep(1)
        # 步骤七：模拟人的行为习惯（先匀加速拖动后匀减速拖动），把需要拖动的总距离分成一段一段小的轨迹
        tracks = self.get_tracks(distance)

        print(tracks)

        # 步骤八：按照轨迹拖动，完成验证
        button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_slider_button')))
        ActionChains(self.driver).click_and_hold(slider).perform()

        # 正常人类总是自信满满地开始正向滑动，自信地表现是疯狂加速
        for track in tracks['forward_tracks']:
            ActionChains(self.driver).move_by_offset(xoffset=track, yoffset=0).perform()

        # 结果傻逼了，正常的人类停顿了一下，回过神来发现，卧槽，滑过了,然后开始反向滑动
        time.sleep(0.6)
        for back_track in tracks['back_tracks']:
            ActionChains(self.driver).move_by_offset(xoffset=back_track, yoffset=0).perform()

        # 小范围震荡一下，进一步迷惑极验后台，这一步可以极大地提高成功率
        time.sleep(0.5)
        ActionChains(self.driver).move_by_offset(xoffset=3, yoffset=0).perform()  # 先移动去一点
        time.sleep(0.6)
        ActionChains(self.driver).move_by_offset(xoffset=-3, yoffset=0).perform()  # 再退回来，模仿人的行为习惯

        time.sleep(0.6)  # 0.6秒后释放鼠标
        ActionChains(self.driver).release().perform()

        time.sleep(5)
        try:
            success = self.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'geetest_result_content'), '验证成功'))
            self.login()
            time.sleep(5)
            self.close_win()
        except:
            # 位置没定位好，或者时间太长了，所以本次失败，进入下一轮
            self.fail_again()


    def fail_again(self):
        """
        失败重试功能，加了好几个try，防止报错，使程序运行下去。在故意改变误差值（偏移量）的情况下，目前只尝试到40多次，遇到的报错都位于步骤三，程序暂无问题
        :return:
        """

        # 步骤二：点击刷新按钮，弹出没有缺口的图片，其实貌似也许大概，无需手动点刷新，失败后自动就刷新了，但我就这么写了。。。
        try:
            button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_refresh_1')))
            button.click()
        except Exception as e:
            print(e)
            print('尝试次数过多，刷新一次图片-步骤二')
            button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_reset_tip_content')))
            button.click()
            time.sleep(2)
            self.fail_again()


        # 步骤三：拿到没有缺口的图片
        try:
            time.sleep(0.5)
            image1 = self.get_image('captcha1.png')
        except Exception as e:
            print(e)
            print('尝试次数过多，刷新一次图片-步骤三')
            button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_reset_tip_content')))
            button.click()
            time.sleep(2)
            self.fail_again()

        # 步骤四：点击托送按钮，弹出有缺口的图片
        try:
            slider = self.get_slider()
            slider.click()
        except Exception as e:
            print(e)
            print('尝试次数过多，刷新一次图片-步骤四')
            button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_reset_tip_content')))
            button.click()
            time.sleep(2)
            self.fail_again()

        # 步骤五：拿到有缺口的图片
        try:
            image2 = self.get_image('captcha2.png')
        except Exception as e:
            print(e)
            print('尝试次数过多，刷新一次图片-步骤五')
            button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_reset_tip_content')))
            button.click()
            time.sleep(2)
            self.fail_again()

        # 步骤六：对比两张图片的所有RBG像素点，得到不一样像素点间的差值，即要移动的距离
        distance = self.get_distance(image1, image2)

        # 步骤七：模拟人的行为习惯（先匀加速拖动后匀减速拖动），把需要拖动的总距离分成一段一段小的轨迹
        tracks = self.get_tracks(distance)

        # 步骤八：按照轨迹拖动，完全验证
        button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_slider_button')))
        ActionChains(self.driver).click_and_hold(slider).perform()

        # 正常人类总是自信满满地开始正向滑动，自信地表现是疯狂加速
        for track in tracks['forward_tracks']:
            ActionChains(self.driver).move_by_offset(xoffset=track, yoffset=0).perform()

        # 结果傻逼了，正常的人类停顿了一下，回过神来发现，卧槽，滑过了,然后开始反向滑动
        time.sleep(0.6)
        for back_track in tracks['back_tracks']:
            ActionChains(self.driver).move_by_offset(xoffset=back_track, yoffset=0).perform()

        # 小范围震荡一下，进一步迷惑极验后台，这一步可以极大地提高成功率
        time.sleep(0.3)
        ActionChains(self.driver).move_by_offset(xoffset=-4, yoffset=0).perform()  # 先移动去一点
        time.sleep(0.4)
        ActionChains(self.driver).move_by_offset(xoffset=4, yoffset=0).perform()  # 再退回来，模仿人的行为习惯

        time.sleep(0.6)  # 0.5秒后释放鼠标
        ActionChains(self.driver).release().perform()
        print(self.count)
        try:
            success = self.wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, 'geetest_result_content'), '验证成功'))
            self.login()
            time.sleep(5)
            self.close_win()
        except:
            self.count+=1
            if self.count<100:
                self.fail_again()
            else:
                self.close_win()


if __name__ == '__main__':
    url = 'https://test.wbfwtop.com/pages/view/register.html'
    mobile = '13200001115'
    password = '12345678'
    threshold = 60 #RGB色差
    left = 57 #起始位置
    deviation = 7 #偏移量，误差
    crack = CrackGeetest(url, mobile, password, threshold, left, deviation)
    crack.crack()
