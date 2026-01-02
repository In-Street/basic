import asyncio,random


"""
	
"""
async def long_handler(name):
	try:
		print(f'任务- {name} ，开始，延迟：{10}')
		await asyncio.sleep(10)  # 使用await 等待异步操作完成，此时会释放事件循环，让其他协程进行操作
		print(f'任务- {name} ，结束')
		return f'任务-{name}, 结果：{random.randint(1, 10)}'
	except asyncio.CancelledError:
		print(f'任务- {name} 被取消')
		raise


async def main():

	try:
		task = asyncio.create_task(long_handler('长任务'))
		await task
		await asyncio.sleep(2)
		task.cancel()

	except asyncio.CancelledError:
		print(f'主协程任务取消')

if __name__ == '__main__':
	asyncio.run(main())