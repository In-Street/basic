import asyncio, random

"""
	通过信号量，控制同时运行的任务数量
"""

async def handler(sleep_time, name, se):
	async with se:
		print(f'任务- {name} ，开始，延迟：{sleep_time}')
		await asyncio.sleep(sleep_time)  # 使用await 等待异步操作完成，此时会释放事件循环，让其他协程进行操作
		print(f'任务- {name} ，结束')
		return f'任务-{name}, 结果：{random.randint(1, 10)}'


async def main():
	se = asyncio.Semaphore(2)
	tasks = [handler(random.randint(1, 3), i, se) for i in range(5)]
	results = await asyncio.gather(*tasks)
	print(results)


if __name__ == '__main__':
	asyncio.run(main())
