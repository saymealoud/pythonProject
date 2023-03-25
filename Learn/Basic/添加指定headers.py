import  urllib.request

url = 'https://www.itcast.cn/'

headers = {
   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url,headers=headers)

request.add_header('Connection','keep-alive')
request.add_header('host','www.itcast.cn')

print(request.get_header('Connection'))

response = urllib.request.urlopen(request)

print(response.read().decode())