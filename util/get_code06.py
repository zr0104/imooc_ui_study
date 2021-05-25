from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging
import unittest

from selenium.webdriver.common.action_chains import ActionChains

url = 'https://test.wbfwtop.com/pages/view/register.html'
mobile = '13200001115'
password = '12345678'

# class Getcode06():
#     def __init__(self,driver):
#         self.driver = driver

def open_chrome(url,mobile,password):
    '''
    :param url: 极验证登录页面地址
    :param email: 登录账号
    :param password: 密码
    :return:
    '''
    # options = webdriver.ChromeOptions()
    # options.binary_location = r"C:\Users\KXYL\AppData\Local\Google\Chrome\Application\chrome.exe"
    # browsers = webdriver.Chrome(chrome_options=options)

    browers=webdriver.Chrome()
    browers.get(url)
    time.sleep(3)
    button =browers.find_element_by_class_name('layui-layer-btn0')
    button.click()
    wait=WebDriverWait(browers,5)
    mobile_block=wait.until(EC.presence_of_element_located((By.ID, 'J-mobile')))
    password_block=wait.until((EC.presence_of_element_located((By.ID, 'J-newPassword'))))
    mobile_block.send_keys(mobile)
    password_block.send_keys(password)
    time.sleep(2)
    button =wait.until(EC.element_to_be_clickable((By.ID, 'J-sendAuthCode')))
    button.click()
    return browers,wait

def get_code_massege(self):
    pass

def login(self):
    submit = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'J-submit')))
    submit.click()
    print('登录成功')
    logging.debug('登录成功')

def identify_gap(browers,wait):
    '''

    :param browers: 浏览器对象
    :param wait: wait对象
    :return: 缺口位置x坐标
    '''
    #定位验证码图片
    small_img = wait.until(EC.presence_of_element_located((By.XPATH, '//canvas[@class="geetest_canvas_bg geetest_absolute"]')))
    location = small_img.location  #获取图片位置，及大小
    size = small_img.size
    top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
            'width']    #确定截图位置
    time.sleep(5)
    screenshot = browers.get_screenshot_as_png()
    screenshot = Image.open(BytesIO(screenshot))

    captcha = screenshot.crop((left, top, right, bottom))
    captcha.save(r'first.png')  #保存图片
    first=Image.open(r'first.png')
    xsize,ysize=first.size
    pool=[]        #保存符合条件的像素点的坐标信息的数据池
    pix=first.load()
    for i in range(xsize):            #颜色识别区域
        for j in range(ysize):
            if 159<=(pix[i,j])[0]<=247 and 154<=(pix[i,j])[1] <=249 and 102 <=(pix[i,j])[2]<=231:
                if 0<=abs((pix[i,j])[0]-(pix[i,j])[1])<=10:
                    if  18<=abs((pix[i,j])[1]-(pix[i,j])[2])<=117  :
                        if 1.4<=(pix[i,j])[1]/(pix[i,j])[0]+(pix[i,j])[2]/(pix[i,j])[0]<=1.97:
                            pool.append((i,j))
    #print(pool)
    x,y=(pool[0])[0],(pool[0])[1]     #获取第一个符合条件的像素点的位置
    captcha1=screenshot.crop((left+x,top+y,right,top+y+5))    #进行截图
    captcha1.save(r'second.png')
    Pool=[]         # 第二张截图根据x坐标的每一条竖线的rgb值和的数据池
    second=Image.open(r'second.png')
    Xsize,Ysize=second.size
    pix1=second.load()
    for i in range(Xsize):
        sum=0
        for j in range(Ysize):
             sum+=(pix1[i,j])[0]+(pix1[i,j])[1]+(pix1[i,j])[1]
        Pool.append((i,sum))
    Pool=sorted(Pool,key=lambda x:x[1])      #排序，找出rgb值得和的最低竖线的x坐标
    print(Pool)
    print(i)
    print(x)
    print(y)
    return (Pool[0])[0]+x   #返回偏移值

def get_pool(browers, wait):
    xx0 = identify_gap(browers,wait) + 35
    print(xx0)
    print(xx0)

    # 找到滑动的圆球
    element = browers.find_element_by_xpath('//div[@class="geetest_slider_button"]')
    # 鼠标点击元素并按住不放
    print("第一步，点击元素")
    ActionChains(browers).click_and_hold(on_element=element).perform()
    time.sleep(2)
    print("第二步，拖动元素")
    # 拖动鼠标到指定位置，注意这里位置是相对于元素左上角的值

    # xx0 = self.identify_gap((Pool[0])[0] + x)
    ActionChains(browers).move_to_element_with_offset(to_element=element, xoffset=xx0, yoffset=50).perform()
    time.sleep(1)
    print("第三步，释放鼠标")
    ActionChains(browers).release(on_element=element).perform()
    time.sleep(3)
    #browers.close()
    try:
        success = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_result_box')))
        time.sleep(5)
        login(self=None)
    except:
        time.sleep(5)
        button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_refresh_1')))
        button.click()
        time.sleep(2)
        get_pool(browers,wait)

if __name__=='__main__':

    browers,wait = open_chrome(url=url,mobile=mobile,password=password)

    print(identify_gap(browers,wait))

    get_pool(browers,wait)
