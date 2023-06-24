import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建Chrome 浏览器驱动

driver = webdriver.Chrome()
# 访问百度首页

driver.get('https://www.baidu.com')

# 点击新闻
xw = driver.find_element(By.LINK_TEXT, '新闻').click()

time.sleep(1)

# 页面后退

driver.back()
time.sleep(1)
driver.forward()

time.sleep(5)

driver.quit()
