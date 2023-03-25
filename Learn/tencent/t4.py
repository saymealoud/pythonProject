from urllib.request import Request,urlopen
from urllib import parse


url = 'http://httpbin.org/post'
url = 'https://movie.douban.com/j/search_subjects'

params =parse.urlencode({
    'tag' : '热门',
    'type': 'tv',
    'page_limit' :5,
    'page_start' : 0
})

url ="{}?{}".format(url,params)

request = Request(url,headers={
    'user-agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
})

with urlopen(request,params.encode()) as response:
    print(response.status,response.reason,'++++++++++++++')
    import  json
    print(json.loads(response.read()))