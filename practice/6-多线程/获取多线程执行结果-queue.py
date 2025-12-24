import queue, threading, time, random


def task_handler(task_id, result_queue):
	try:
		print(f'线程 {threading.current_thread().name} 开始任务')
		time.sleep(random.uniform(0.5, 1.5))
		result = f'任务{task_id}执行结果'

		if task_id in (1, 2):
			1 / 0

		res_dict = {
			'task_id': task_id,
			'result': result,
			'thread_name': threading.current_thread().name,
			'status': 'success',
		}
		result_queue.put(res_dict)  # 使用队列收集各个线程的执行结果
	except Exception as e:
		res_dict = {
			'task_id': f'task_{task_id}',
			'result': None,
			'thread_name': threading.current_thread().name,
			'status': 'error',
			'error_msg': str(e),
		}
		result_queue.put(res_dict)
	finally:
		print(f'线程 {threading.current_thread().name} 结束任务')


def execute():
	result_queue = queue.Queue()
	threads = [threading.Thread(target=task_handler, args=(i, result_queue), name=f'Worker-{i}') for i in range(3)]
	for t in threads:
		t.start()
	for t in threads:
		t.join()

	result_list = []
	while not result_queue.empty():
		result_list.append(result_queue.get())

	print(
		f'任务成功数：{len(list(filter(lambda r: r.get('status') == 'success', result_list)))}，结果：{[i.get('result') for i in result_list if i.get('status') == 'success']}')
	print(
		f'任务失败数：{len(list(filter(lambda r: r.get('status') == 'error', result_list)))} ,异常：{ {r.get('task_id'): r.get('error_msg') for r in result_list} }')

if __name__ == '__main__':
	execute()
