"""
线程等待/触发，实现单向通信，线程间简单通知
	event.wait():  阻塞，直到 event.set()
"""
import threading,time

event = threading.Event()

def task_1():
	print(f'线程{threading.current_thread().name} ，开始执行')
	time.sleep(2)
	event.wait()
	print(f'线程{threading.current_thread().name} ，正在执行.....')
	print(f'线程{threading.current_thread().name} ，结束执行')


def task_2():
	print(f'触发线程{threading.current_thread().name} ，开始执行')
	time.sleep(2)
	event.set()
	print(f'触发线程{threading.current_thread().name} ，结束执行')


threading.Thread(target=task_1, args=()).start()
threading.Thread(target=task_2, args=()).start()