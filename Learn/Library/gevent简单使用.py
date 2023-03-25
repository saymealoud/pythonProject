# 打猴子补丁  实现在遇到阻塞的时候 协程间多个任务自动切换
from gevent import monkey
monkey.patch_all()
import gevent
import time


def task(msg):
    for i in range(10):
        print(msg)
        time.sleep(0.5)


# 默认情况下 spawn方法遇到阻塞不会自动切换
#  需要遇到阻塞自动切换  需要打 猴子布丁
#  一般 猴子布丁 都会打在最开头
g1 = gevent.spawn(task,"协程1")
g2 = gevent.spawn(task,"协程2")

gevent.joinall((
    g1,g2
))