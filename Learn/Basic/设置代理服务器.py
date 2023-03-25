import random
import urllib.request

# 1. 创建ProxyHandler 对象
#  定义变量是否启用代理
# proxy_switch = True
#
# if proxy_switch:
#     proxies = {'http': '110.238.113.119:80'}
# else:
#     proxies = {}
#
#
# proxy_handler = urllib.request.ProxyHandler(proxies)
#
# # 2. 创建opener 对象
# opener = urllib.request.build_opener(proxy_handler)
#
# #  3. 发送请求获取响应对象
#
# response = opener.open("https://www.itcast.cn/")
#
# print(response.read().decode())

#  1. 准备代理列表
proxies_list = [

    {'http': '110.238.113.119:80'},
    {'http': '121.13.252.60:41564'},
    {'http': '47.243.242.70:3128'},
]

#  2. 随机选取一个代理
proxy = random.choice(proxies_list)
print(proxy)
# 3. 通过随机代理  创建处理器对象
proxy_handler = urllib.request.ProxyHandler(proxy)

# 4. 通过代理器对象 创建opener
opener = urllib.request.build_opener(proxy_handler)

# 5. 使用opener 发送请求  通过随机代理器发送的
response = opener.open("https://www.itcast.cn/")
print(response.read().decode())
