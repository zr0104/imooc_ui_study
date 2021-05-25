# coding=utf8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from PIL import Image
import time
from io import BytesIO


def main(self):
    driver = webdriver.Chrome()
    driver.get("https://test.wbfwtop.com/pages/view/register.html")
    driver.maximize_window()

    #等待极验验证码弹窗元素加载完
    WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_xpath('//div[@class="form-box"]').is_displayed())

    driver.find_element_by_class_name("layui-layer-btn0").click()
    driver.find_element_by_id("J-mobile").send_keys("13200001111")
    driver.find_element_by_id("J-sendAuthCode").click()
    time.sleep(3)

    # 找到滑动的圆球
    element = driver.find_element_by_xpath('//div[@class="geetest_slider_button"]')

    # 1 把鼠标放到按钮上
    # ActionChains(driver).move_to_element(button).perform()
    ActionChains(driver).click_and_hold(on_element=element).perform()

    # 2 获取整个页面截图
    screeshot = driver.get_screenshot_as_png()
    screeshot = Image.open(BytesIO(screeshot))

    # 3 获取验证码坐标
    img = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'geetest_slider_track')))
    time.sleep(2)
    location = img.location
    size = img.size
    top,button,left,right = location['y'],location[y]+size['height'],location['x'],location['x']+size['width']

    # 4 获取带缺口的验证码图片
    #   获取滑块对象
    slider = WebDriverWait(driver, 5, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'geetest_canvas_img')))
    #  获取缺口位置
    gap = self.get_gap(image1, image2)
    #  减去缺口的位移
    gap -= BORDER

    # 5 移动轨迹
    track = []
    # 当前位移
    current = 0
    # 减速阈值
    mid = distance * 4 / 5
    # 计算间隔
    t = 0.2
    # 初速度
    v = 0
    while current < distance:
        if current < mid:
            # 加速度为正2
            a = 2
        else:
            # 加速度为负3
            a = -3
        # 初速度v0
        v0 = v
        # 当前速度v = v0 + at
        v = v0 + a * t
        # 移动距离
        move = v0 * t + 1 / 2 * a * t * t
        # 当前位移
        current += move
        # 加入轨迹
        track.append(round(move))

    # 6 拖动滑块
    ActionChains(driver).click_and_hold(on_element=button).perform()
    for x in track:
        # ActionChains(driver).move_by_offset(xoffset=x, yoffset=0).perform()
        ActionChains(driver).move_to_element_with_offset(to_element=element, xoffset=x, yoffset=50).perform()
    time.sleep(0.5)
    ActionChains(driver).release().perform()


'''
    # 鼠标点击元素并按住不放
    print("第一步，点击元素")
    ActionChains(driver).click_and_hold(on_element=button).perform()
    time.sleep(2)
    print("第二步，拖动元素")
    # 拖动鼠标到指定位置，注意这里位置是相对于元素左上角的值
    ActionChains(driver).move_to_element_with_offset(to_element=element, xoffset=200, yoffset=50).perform()

    time.sleep(10)
    print("第三步，释放鼠标")
    ActionChains(driver).release(on_element=element).perform()
    time.sleep(3)
    driver.close()
'''

if __name__ == '__main__':
    main()
