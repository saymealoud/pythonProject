import  requests


# zhu
url = 'https://www.google.com.hk/search?'

# 准备字典参数
params = {
    'q': '桥本有菜'
}


# 准备请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

# 发送请求   获取响应数据
response = requests.get(url,params=params,headers=headers)
# 获取响应数据
print(response.text)