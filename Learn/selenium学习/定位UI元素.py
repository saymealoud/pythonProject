from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()

options.add_argument('--headless')

driver = webdriver.Chrome(options=options)

driver.get('https://www.baidu.com')


input = driver.find_element(By.ID,'kw')
print(input.get_attribute('name'))


input = driver.find_element(By.ID)




driver.quit()