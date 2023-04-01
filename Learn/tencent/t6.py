from lxml import  etree

import requests

url = 'https://movie.douban.com'
ua ='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'


with requests.get(url,headers={'user-agent': ua}) as response:
    content = response.text



    html = etree.HTML(content)
    titles = html.xpath("//div[@class='billboard-bd']//tr/td/a/text()")

    for t in titles:
        print(t)