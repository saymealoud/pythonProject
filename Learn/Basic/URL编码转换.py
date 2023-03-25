import urllib.parse


# 准备字典数据
data = {
    'host':'www.itcast.cn',
    'name': '传智播客'
}

#进行URL编码

data = urllib.parse.urlencode(data)
print(data)

# url  解码
data = urllib.parse.unquote(data)
print(data)


print(urllib.parse.quote(data))



