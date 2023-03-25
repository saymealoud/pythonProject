import jsonpath

import json

json_str ='''
{
    "store": {
        "book": [
           {"category": "reference",
            "author": "Nigel Rees",
            "title": "Sayings of the Century",
            "price": 8.95
           }, 
            {"category": "fiction",
            "author": "Chester",
            "title": "Try Everything",
            "price": 22.99
           }
        ],
        "bicycle": {
            "color": "red",
            "price": 9.99
        }
    }
}
'''

# json 字符串转为python对象
store = json.loads(json_str)
print(store)

# 查看store下 bicycle 的 color 属性
# jsonurl = '$.store.bicycle.color'
# ..  跨级查找 要求唯一
jsonurl = '$..color'
result = jsonpath.jsonpath(store,jsonurl)
print(result)

# book的所有对象
# jsonurl = '$.store.book'
# jsonurl = '$.store.book[*]'
jsonurl = '$.store.book[0]'
jsonurl = '$.store.book[*].title'
jsonurl = '$.store.book[?(@.category =="fiction")]'
result =jsonpath.jsonpath(store,jsonurl)
print(result)

