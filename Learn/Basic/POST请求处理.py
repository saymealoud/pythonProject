import urllib.request
import urllib.parse

# 准备URL
url = 'https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'

#  准备数据 （参数）

data = {
    'i': '英语',                   
    'from': 'auto',
    'to': 'auto',
    'dictResult': 'true',
    # 'keyid': 'webfanyi',
    # 'sign': '5d427a5a63e2c99a8a04c92a9bb1a1eb',
    'client': 'fanyideskweb',
    'product': 'webfanyi',
    'appVersion': '1.0.0',
    'vendor': 'web',
    'pointParam': 'client,mysticTime,product',                         
    'mysticTime': '1676793405592',
    'keyfrom': 'fanyi.web'
}
                                                                  
data = urllib.parse.urlencode(data)
# 转换为bytes对象
data = bytes(data.encode())

# 准备请求头
headers = {
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
      'X-Requested-With': 'XMLHttpRequest'
}

# 构造request对象
request = urllib.request.Request(url,data=data,headers=headers)

# 发送请求获取响应数据
response = urllib.request.urlopen(request)

# 打印响应结果
print(response.read().decode())