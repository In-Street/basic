import asyncio, random,requests
import time

#  同步函数
def handler(sleep_time, name, url):
	print(f'任务- {name} ，开始，延迟：{sleep_time}')
	time.sleep(sleep_time)
	response = requests.get(url)
	return f'任务-{name}, 结果：{response.status_code}'


"""
	协程中调用同步函数，会阻塞整个事件循环，导致并发失效。可将同步函数提交到线程池，实现异步化
"""
async def main():

	loop = asyncio.get_running_loop()
	task_1 = loop.run_in_executor(None, handler, random.randint(1, 3), 1, 'https://www.qq.com')
	task_2 = loop.run_in_executor(None, handler, random.randint(1, 3), 2, 'https://www.qq.com')
	task_3 = loop.run_in_executor(None, handler, random.randint(1, 3), 3, 'https://www.qq.com')

	result = await asyncio.gather(task_1, task_2, task_3)
	print(result)

if __name__ == '__main__':
	start_time = time.time()
	asyncio.run(main())
	print(f'总耗时：{time.time() - start_time}')