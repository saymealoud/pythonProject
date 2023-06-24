import time

from selenium import webdriver

# 创建Chrome 浏览器驱动

driver = webdriver.Chrome()
# 访问百度首页

driver.get('https://www.baidu.com')

# 弹出窗口
# 1 准备 弹出窗口 js
js = "alert('hi')"
# 2. 执行 js
driver.execute_script(js)

time.sleep(1)
# 获取弹出窗口对象
alert = driver.switch_to.alert

print(alert.text)

alert.dismiss()

print()

time.sleep(5)

driver.quit()
