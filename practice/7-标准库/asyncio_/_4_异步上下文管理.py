import asyncio

class AsyncManager:

	async def __aenter__(self):
		print(f'获取异步资源')
		await asyncio.sleep(2)
		return self

	async def __aexit__(self, exc_type, exc, tb):
		print(f'释放资源')
		await asyncio.sleep(1)

	async def handler_task(self):
		print('业务操作')


async def main():

	async with AsyncManager() as manager:
		await manager.handler_task()

if __name__ == '__main__':
	asyncio.run(main())