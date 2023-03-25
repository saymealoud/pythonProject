import urllib.request

# 发送请求
try:
    response = urllib.request.urlopen("http://202.183.32.173:80",timeout=3)
    print(response)
except Exception as ex:
    print(ex)
