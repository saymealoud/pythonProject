import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get('https://weibo.com/signup/signup.php')

year = driver.find_element(By.CSS_SELECTOR, 'select.sel.year')
# print(year)

# Select(year).select_by_index(1)  # 按index 选择
# Select(year).select_by_value("1997")  # 按 value 选择
Select(year).select_by_visible_text("1998")  # 按 可见文本 选择

# 取消选择   单选  select 中不支持 任何的取消选择
#  You may only deselect all options of a multi-select
# Select(year).deselect_all()


time.sleep(5)
