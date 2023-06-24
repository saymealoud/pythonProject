from urllib3 import PoolManager, HTTPResponse

pool = PoolManager()



with PoolManager() as http:
    url = 'https://movie.douban.com/'
    res:HTTPResponse = http.request('GET', url ,headers={
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    })

    with open('/Users/mesay/Downloads/movie.html','wb') as f:
        f.write(res.data)