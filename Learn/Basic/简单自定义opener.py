import urllib.request

# 发送请求 请求谷歌首页


#  1.创建一个用于处理http 请求的handler对象
http_handler = urllib.request.HTTPHandler(debuglevel=1)

# 2. 使用http_handler 创建一个opener对象
opener = urllib.request.build_opener((http_handler))

# 将 opener 对象设置为全局
# urllib.request.install_opener(opener)

# 3.构造一个request对象

request = urllib.request.Request('http://www.baidu.com')
# 4.发送请求
response = opener.open(request)
# 5.输出内容
print(response.read().decode())


