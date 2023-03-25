import urllib.request
import urllib.parse

# 准备URL
# url = 'http://www.google.com/s?'
url = 'https://www.google.com.hk/search?'
# http://www.baidu.com/s?wd=%E6%A1%A5%E6%9C%AC%E6%9C%89%E8%8F%9C&oq=%25E6%25A1%25A5%25E6%259C%25AC%25E6%259C%2589%25E8%258F%259C
# https://www.google.com.hk/search?q=%E6%A1%A5%E6%9C%AC%E6%9C%89%E8%8F%9C&oq=%E6%A1%A5%E6%9C%AC%E6%9C%89%E8%8F%9C&aqs=chrome..69i57j69i60.3120j0j15&sourceid=chrome&ie=UTF-8


# 准备字典参数
param = {
    'q': '桥本有菜'
}
# 对参数进行URL编码
param_str = urllib.parse.urlencode(param)

# 把参数拼接到原来的URL上
url = url + param_str
print(url)

# 准备请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

# 构造request
request = urllib.request.Request(url, headers=headers)


#发送请求
response = urllib.request.urlopen(request)
print(response)

# 打印结果
print(response.read().decode())