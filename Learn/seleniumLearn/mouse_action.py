import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# 创建Chrome 浏览器驱动

driver = webdriver.Chrome()
# 访问百度首页

driver.get('https://www.baidu.com')

# 获取新闻 a 标签元素
xw = driver.find_element(By.LINK_TEXT, '新闻')
# 鼠标移动到新闻的位置
#  ActionChains 鼠标动作链  move_to_element 只是移动 没有执行 perform 执行
# ActionChains(driver).move_to_element(xw).perform()

# 单击新闻
# ActionChains(driver).move_to_element(xw).click(xw).perform()
# ActionChains(driver).click(xw).perform()


# 双击新闻
# ActionChains(driver).move_to_element(xw).double_click(xw).perform()
# ActionChains(driver).double_click(xw).perform()


# 按住不动

ActionChains(driver).move_to_element(xw).click_and_hold(xw).perform()

# todo 拖拽验证  要获取的元素在iframe中 要切换到 此iframe 中才能获取
#  frame()  可以传入索引： 从 0 开始 frame 的name属性值，要切换iframe 元素  然后再获取
# driver.switch_to.frame(0)

#
#

time.sleep(5)
# 退出浏览器
driver.quit()
