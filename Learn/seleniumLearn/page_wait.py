from selenium import webdriver

from selenium.webdriver.common.by import By

# 创建Chrome 浏览器驱动

driver = webdriver.Chrome()
# 访问百度首页

driver.get('https://www.baidu.com')

driver.find_element(By.ID, 'kw').send_keys("itcast")

driver.find_element(By.ID, 'su').click()

#  当点击超级链接  跳转到下一个页面，再获取元素的时候，并不会等待页面加载完成
#   三种方案
#         selenium 有两种  1.显式等待    2. 隐式等待
# 获取下一页   a 标签

# 显式等待
# element = WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT,'下一页 >')))
# print(element)


# 隐式等待 指定最大的等待时加你 等待页面完全加载完成，或者时间到了

driver.implicitly_wait(5)

print('-' * 30)

next_page = driver.find_element(By.LINK_TEXT, '下一页 >')

print(next_page)

driver.quit()
