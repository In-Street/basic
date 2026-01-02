import asyncio
import random


async def handler(sleep_time, name):
	print(f'任务- {name} ，开始，延迟：{sleep_time}')
	await asyncio.sleep(sleep_time)  # 使用await 等待异步操作完成，此时会释放事件循环，让其他协程进行操作
	print(f'任务- {name} ，结束')
	return f'任务-{name}, 结果：{random.randint(1, 10)}'


async def main():
	task_1 = asyncio.create_task(handler(1, 1))
	task_2 = asyncio.create_task(handler(3, 2))
	task_3 = asyncio.create_task(handler(2.5, 3))

	result_3 = await task_3
	print(f'任务-3 完成，结果：{result_3}')

	result_1 = await task_1
	result_2 = await task_2
	print(f'所有任务完成，所有结果：{[result_1, result_2, result_3]}')


async def main2():
	task_1 = asyncio.create_task(handler(1, 1))
	task_2 = asyncio.create_task(handler(4, 2))
	task_3 = asyncio.create_task(handler(2.5, 3))
	tasks = [task_1, task_2, task_3]

	done, not_done = await asyncio.wait(tasks, timeout=3)
	print(f'已完成任务结果：{done}')
	print(f'未完成任务结果：{not_done}')

if __name__ == '__main__':
	asyncio.run(main2())
