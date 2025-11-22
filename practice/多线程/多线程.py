from threading import Thread, current_thread
import time

"""
Thread: 
	target 是用于 run() 方法调用的可调用对象。默认是 None，表示不需要调用任何方法。
	args 是用于唤起目标函数的参数列表或元组。 默认为 ()
"""


def custom_thread_run(arg1, arg2):
	print('子线程：{}，开始执行  '.format(current_thread().name))
	print('%s - %s' % (arg1, arg2))
	time.sleep(3)
	print('子线程：{}，结束执行  '.format(current_thread().name))


for i in range(1, 3):
	t1 = Thread(target=custom_thread_run, args=(i, i + 1))
	t1.start()

print('主线程执行结束：', current_thread().name)
