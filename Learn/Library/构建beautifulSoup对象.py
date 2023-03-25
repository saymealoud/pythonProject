from bs4 import BeautifulSoup

from lxml import etree

import re

html_doc = '''
<html><head><title> The Dormouse's story</title></head>
<body>
</body></html>
'''


# 构建BeautifulSoup对象
bs = BeautifulSoup(html_doc,'lxml')
print(bs)

# 1.2 传入 HTML文件对象
bs = BeautifulSoup(open('hello.html'),'lxml')
print(bs)


print('-'*100)

print(bs.prettify())