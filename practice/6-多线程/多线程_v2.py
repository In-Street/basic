from threading import Thread, current_thread
import time

"""
  子类重写run方法需要传入业务参数时，应将业务参数置于 __init__ 方法中
"""


class MyThread(Thread):

	def __init__(self, arg1, *arg2):
		super().__init__()
		self.arg1 = arg1
		self.arg2 = arg2

	def run(self):
		print('子线程：{} ,开始执行  '.format(current_thread().name))
		print("执行业务操作：arg1:{} ， arg2:{}".format(self.arg1, self.arg2))
		time.sleep(2)
		print('子线程：{} ,结束执行  '.format(current_thread().name))


t1 = MyThread('参数A')
t2 = MyThread('参数a','参数b')

t1.start()
t2.start()


t1.join()
t2.join()
print('主线程执行完毕')