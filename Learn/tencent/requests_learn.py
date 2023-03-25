import requests


base_url = 'https://movie.douban.com/'

with requests.session() as session:
    for url in [base_url,base_url]:
        response = session.get(url,headers={
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"

        })

        with response:
            # print(response.status_code,response.reason)
            # print(response.encoding)
            # print(response.cookies)
            print('=' * 30)
            print(response.request.headers.items(),sep="\n")
            print('=' * 30)
            print(*response.headers.items(),sep='\n')




    # print(response.content)
    # print(response.text)





