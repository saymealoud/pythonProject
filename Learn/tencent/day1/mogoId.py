import  datetime

id = "6427d436b41b6b36604e5764"
x = id[:8]
print(x)
print(0x6427d436)
print(int('0x6427d436',16))

print(datetime.datetime.fromtimestamp(0x6427d436))

print('='*30)

y = int.from_bytes(bytes.fromhex(x),'big')
print(y)

import bson

z = bson.ObjectId(id)
print(z)
print(z.generation_time)