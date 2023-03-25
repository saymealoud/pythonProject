import json


json_obj = '{"name":"Chester","age":26,"gender":"男"}'

# loads
dic = json.loads(json_obj)
print(dic)
print(type(dic))


# dumps
json_obj = json.dumps(dic)
print(json_obj)

# 禁用 ascii 编码  格式化   indent 缩进

json_obj = json.dumps(dic,ensure_ascii=False,indent=3)
print(json_obj)

with open('person.json','w',encoding='UTF-8') as f:
    json.dump(dic,f,ensure_ascii=False,indent=2)



