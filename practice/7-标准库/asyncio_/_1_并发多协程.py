import asyncio
import random
import time
"""
	注意： await 关键字
"""

async def handler(sleep_time, name):
	print(f'任务- {name} ，开始，延迟：{sleep_time}')
	await asyncio.sleep(sleep_time)  # 使用await 等待异步操作完成，此时会释放事件循环，让其他协程进行操作
	print(f'任务- {name} ，结束')
	return f'任务-{name}, 结果：{random.randint(1, 10)}'


async def main():
	coordination = [handler(random.randint(1, 3), i) for i in range(5)]
	gather_result = await asyncio.gather(*coordination)  # 必须使用await 等待Future对象，事件循环才可以进行调度其他协程执行。若不使用await ，那么执行完后面print语句后主协程结束，事件循环也随之关闭，其他协程无法执行
	print(gather_result)

if __name__ == '__main__':
	start_time = time.time()
	asyncio.run(main())
	print(f'总耗时：{time.time() - start_time}')