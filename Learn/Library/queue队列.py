from queue import Queue

#  先进先出队列   火车站排队


q = Queue(maxsize=20)

# 存储元素
# q.put(1)
# q.put(2)
# q.put(3)
# print(q.qsize())
# print(q.get(1))

print(q.full())
print(q.empty())

for i in range(4):
    q.put(i)

#   取出所有元素
while not q.empty():
    print(q.get())

# LifeQueue: 后进先出队列   类似栈
from queue import LifoQueue

lifeQ = LifoQueue(maxsize=20)
for i in range(4):
    lifeQ.put(i)

#   取出所有元素
while not lifeQ.empty():
    print(lifeQ.get())

# PriorityQueue    优先级队列 在存储数据的时候,会对元素进行排序

from queue import PriorityQueue


class Job(object):

    def __int__(self, level, name):
        self.level = level
        self.name = name
    def __lt__(self, other):
        return self.level < other.level


pq = PriorityQueue()

pq.put((1, 'code'))
pq.put((2,'eat'))
pq.put((3,'sleep'))
# pq.put(Job(2,'不重要的'))

while not pq.empty():
    next_item = pq.get()
    print(next_item)
