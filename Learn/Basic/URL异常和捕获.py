import urllib.request
import urllib.error

# 构建请求对象
request = urllib.request.Request("http://www.adawwwwdas.com")

try:
    response = urllib.request.urlopen(request,timeout=3)
    print(response)
except urllib.error.URLError as error:
    print(error)



