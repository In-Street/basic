import threading, time
"""
	信号量： 控制同时访问资源的线程数
"""
se = threading.Semaphore(2)  #最多2个线程同时执行


def task_handler(ordinal):
	with se:
		print(f'线程{threading.current_thread().name} - {ordinal}，开始执行')
		time.sleep(4)
		print(f'线程{threading.current_thread().name} - {ordinal}，结束执行')


threads = [threading.Thread(target=task_handler, args=(i,)) for i in range(7)]

for t in threads:
	t.start()