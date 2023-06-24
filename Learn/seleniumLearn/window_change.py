import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建Chrome 浏览器驱动

driver = webdriver.Chrome()
# 访问百度首页

driver.get('https://www.baidu.com')

driver.find_element(By.ID, 'lg').click()

time.sleep(1)

# window_handles  所有窗口名称列表
# for win in driver.window_handles:
#     print(win)
#     print(type(win))

#  切换窗口
driver.switch_to.window(driver.window_handles[0])

time.sleep(5)

driver.quit()
