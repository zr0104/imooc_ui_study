from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.ymgk.com/account/logon.html?backURL")
driver.find_element_by_id("logonenter").click()
name = driver.find_element_by_id("logonmobile")
actions = ActionChains(driver).move_to_element(name)
driver.execute_script('document.getElementById("logonmobile").value="13888888888"')
