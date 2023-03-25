
import requests

url = 'https://www.google.com.hk/search?'

# requests.request()   构造一个请求，支撑以下各方法的基础方法
# response = requests.request('get', url)
#
# # 打印编码方式
# print(response.encoding)
# # 修改编码方式
# response.encoding = 'UTF-8'
# # 打印响应内容
# print(response.text)

response = requests.get(url)
# response.encoding = 'Big5'
# print(response.text)
# print(response.content)
print(response.headers)


