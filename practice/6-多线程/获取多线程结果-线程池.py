import threading
from concurrent.futures import ThreadPoolExecutor, as_completed, Future, wait
import time, random


def task_handler(task_id):
	sleep_time = random.uniform(0.5, 2.5)
	print(f'线程{threading.current_thread().name} 开始执行任务 {task_id}')
	if sleep_time > 1.0:
		time.sleep(sleep_time)
		return f'任务 {task_id} 执行完成'
	else:
		raise Exception(f'任务 {task_id} 异常')

# 多个参数任务，测试map批量提交时参数传递的形式
def task_handler_multi(task_id, number):
	sleep_time = random.uniform(0.5, 2.5)
	print(f'线程{threading.current_thread().name} 开始执行任务 {task_id}，{number} ,{sleep_time}')
	if sleep_time > 1.0:
		time.sleep(sleep_time)
		return f'任务 {task_id} 执行完成, number: {number * 2}'
	else:
		raise Exception(f'任务 {task_id} 异常')


def submit_main():
	result_list = []
	errors = []

	with ThreadPoolExecutor(max_workers=3, thread_name_prefix='Worker_') as executor:
		futures = {executor.submit(task_handler, i): i for i in range(5)}  # 提交5个任务

		for f in as_completed(futures):  # 按完成顺序获取执行结果，耗时最短的先返回
			task_id = futures[f]
			try:
				result_list.append(f'任务{task_id} ，执行结果：{f.result()}')
			except Exception as e:
				errors.append(f'任务{task_id} ，结果异常：{f.exception()}')

	print(result_list)
	print(errors)


def map_main():
	result_list = []
	errors = []
	with ThreadPoolExecutor(max_workers=3, thread_name_prefix='Worker_') as executor:
				executor_result = executor.map(task_handler_multi, list(range(5)),list(range(5,10)), timeout=10)  #批量提交任务，结果顺序 = 提交顺序
				iter_res = iter(executor_result)
				idx = 0
				while True:
					try:
						result_list.append(next(iter_res))  # 只要有一个任务出现异常，遍历就会中断
						print(f'遍历到第 {idx} 个任务')
						idx += 1
					except StopIteration:
						break
					except Exception as e:
						errors.append(e)
	print(result_list)
	print(errors)


def wait_main():
	result_list = []
	errors = []
	with ThreadPoolExecutor(max_workers=3, thread_name_prefix='Worker_') as executor:
		futures = {executor.submit(task_handler, i): i for i in range(5)}

		dones, not_dones = wait(futures, timeout=3, return_when='FIRST_COMPLETED') # 任意一个任务完成就返回

		print(f'已完成任务数：{len(dones)} , 未完成任务数：{len(not_dones)}')
		for future in dones:
			try:
				callback_result = future.add_done_callback(callback)
				print(callback_result)  # None，回调函数的返回值会被忽略。要想获取可通过queue存储
				result_list.append(callback_result)
			except Exception as e:
				errors.append(e)

	print(result_list)
	print(errors)


def callback(future):
	print(f'完成任务的回调')
	try:
		return future.result()
	except Exception as e:
		return future.exception()


if __name__ == '__main__':
	# submit_main()
	map_main()
	# wait_main()
	print('aaaa')
