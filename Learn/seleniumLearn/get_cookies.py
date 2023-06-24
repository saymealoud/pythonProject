from selenium import webdriver

# 创建Chrome 浏览器驱动

driver = webdriver.Chrome()
# 访问百度首页

driver.get('https://www.baidu.com')

for cookie in driver.get_cookies():
    print("%s=%s" % (cookie['name'], cookie['value']))

# print(driver.get_cookies())

# 删除 cookies  根据名称

driver.delete_cookie('H_PS_PSSID')

# 删除所有cookie
driver.delete_all_cookies()

driver.quit()
