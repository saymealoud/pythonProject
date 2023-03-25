from selenium import webdriver

import time

from selenium.webdriver.common.by import By

# 导入  keys 模块
from selenium.webdriver.common.keys import Keys

# 设置Chrome 无界面浏览器
from selenium.webdriver.chrome.options import Options


# driver = webdriver.PhantomJS()  # 未配置好  已homebrew 下载好了

options = Options()

# 设置无界面
options.add_argument('--headless')
# 使用options 配置Chrome 浏览器
# 创建驱动对象

driver = webdriver.Chrome(options=options)

# 访问网页
driver.get('http://www.baidu.com')

# 保存快照
driver.save_screenshot('baidu.png')


# 获取id 为 s-top-left 元素的文本
print(driver.find_element(By.ID, "s-top-left").text)

# 输入框 输入内容
driver.find_element(By.ID, 'kw').send_keys('itcast')



# 进行搜索
driver.find_element(By.ID, 'su').click()

# 在搜索框里面 按 COMMAND  + A
driver.find_element(By.ID, 'kw').send_keys(Keys.COMMAND, 'a')   # 全选
driver.find_element(By.ID, 'kw').send_keys(Keys.COMMAND, 'x')    # 剪切


driver.find_element(By.ID, 'kw').send_keys('桥本有菜')

driver.find_element(By.ID, 'kw').send_keys(Keys.ENTER)


driver.find_element(By.ID, 'kw').clear()   # 清空搜索框

print(driver.title)

# print(driver.page_source)  # 页面源码


print(driver.current_url)
print(driver.get_cookies())

# 退出当前窗口
driver.close()




time.sleep(5)

#  退出驱动
driver.quit()
