# coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://test.wbfwtop.com/pages/view/login.html")

time.sleep(2)
#driver.find_element_by_link_text("账号密码登录").click()
#driver.find_elements_by_class_name("layui-nav-item").click()
driver.find_element_by_css_selector("div#ul>a:last-child").click()
time.sleep(2)
driver.find_element_by_class_name("geetest_radar_tip").click()


# ...句柄切换窗口实例...
'''
driver = webdriver.Chrome()
#第一个标签页打开百度
url = "http://www.baidu.com"
driver.get(url)
#A=百度，当前窗口
current_window_handle = driver.current_window_handle
#使用js打开新标签
#B=163邮箱，现在当前窗口是163邮箱
js="window.open('http://mail.163.com/')"
driver.execute_script(js)
all_window_handles = driver.window_handles
sleep(2)
for handle in all_window_handles:
    if handle == current_window_handle: #切换回第一个窗口
        driver.switch_to.window(handle)
sleep(2)
driver.quit()
'''


#八大元素定位方法
'''
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# 1）绝对路径（一般不推荐使用，此处不介绍）
# 2）id选择器
# driver.find_element_by_css_selector("#kw").send_keys("ethon")

# 3）class选择器
# driver.find_element_by_css_selector(".s_ipt").send_keys("ethon")

# 4）其他属性定位
# driver.find_element_by_css_selector("[autocomplete='off']").send_keys("ethon")

# 5）通过部分属性定位
#      * 包含某个字符
#      ^ 以某个字符开关
#      $ 以某个字符结尾

# driver.find_element_by_css_selector("[autocomplete*='f']").send_keys("ethon")
# driver.find_element_by_css_selector("[autocomplete^='o']").send_keys("ethon")
# driver.find_element_by_css_selector("[autocomplete$='f']").send_keys("ethon")

# 6）通过层级定位
# driver.find_element_by_css_selector("form>span>input").send_keys("ethon")
# driver.find_element_by_css_selector("form#form>span>input").send_keys("ethon")  # 层级与id组合定位
# driver.find_element_by_css_selector("form.fm>span>input").send_keys("ethon")  # 层级与class组合定位

# 7）通过兄弟节点定位
# driver.find_element_by_css_selector("div#u1>a:first-child").click()
# driver.find_element_by_css_selector("div#u1>a:nth-child(2)").click()
driver.find_element_by_css_selector("div#u1>a:last-child").click()
'''
