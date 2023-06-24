
from pymongo import MongoClient

from pymongo.database import  Database


url = "mongodb://127.0.0.1:27017"

client = MongoClient(url)
print(client)

db:Database = client['users']

table = db['users']

# r = table.insert_one({'id':1,'name':'Chester','age':26})
# print(r.inserted_id)
#
# r = table.insert_many([
#   {'id':2,'name':'ZhaoMO','age':25},
#   {'id':3,'name':'Kelly','age':27}
# ])
# print(r.inserted_ids)
#
# r = table.insert_one({'id':4,'name':'Sam','age':18})
# print(r.inserted_id)




# result = table.find({'name':'Chester'})    # select * from users.users where name = 'Chester'
# print(type(result),*result)
# result = table.find_one({'name':'Chester'})    # select * from users.users where name = 'Chester'
# result = table.find({'age':{'$gte': 20}})
# print(type(result),*result)
# result = table.find()    # select * from users.users
# print(type(result),*result,sep="\n")


# result = table.find().sort('age',DESCENDING)
# print(*result,sep="\n")

# r = table.update_many({'name':'Chester'},{'$inc':{'age': -5}})
# print(type(r),r.upserted_id,r.modified_count,r.matched_count)
# print(*table.find(),sep="\n")

# table.update_many({},{'$set' :{'comment':'form '}})

#  创建全文索引
# r =table.create_index([('name','text'),('comment','text')])
# print(type(r),r)


r = table.find({'$text': {'$search': 'Chester'}})
print(*r,sep="\n")


# https://www.mongodb.com/docs/manual/crud/   官方文档



client.close()