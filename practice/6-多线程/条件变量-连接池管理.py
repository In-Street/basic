"""
	1. 定义通用池管理类
			属性：最大数量、空闲资源列表、正在使用资源列表、资源可用条件（Condition）、初始化资源池的方法
			方法：  获取资源、释放资源、资源池监控：总量、可使用量、正在使用量

	2. 定义数据库连接类：
			属性： 连接id（创建一个自增1）、连接创建时间
			方法： 初始化连接方法，用于初始化资源池 、query 方法模拟业务

	3.  工作任务：
			多个工作线程从池管理中获取数据库连接，执行query 方法

"""
import threading, time
from typing import List, Any, Optional
from contextlib import contextmanager
from itertools import zip_longest


class PoolManager:
	def __init__(self, maxsize, create_resource):
		self.maxsize = maxsize
		self.pool: List[Any] = []
		self.in_use: List[Any] = []
		self.create_resource = create_resource

		"""
			threading.Condition，条件变量传入一个已存在的锁，而不是自己创建一个新的锁：
				1. 
		"""
		self.lock = threading.Lock()
		self.resource_available = threading.Condition(self.lock)

		# 初始化资源池
		for _ in range(maxsize):
			self.pool.append(create_resource())

	"""
		获取连接资源
	"""

	def get_resource(self, timeout: Optional[float] = None):
		with self.resource_available:

			# 最长等待时间
			end_time = time.time() + timeout if timeout else None

			print(f'线程{threading.current_thread().name}，获取可用资源等待中......')
			while not self.pool:  # 资源池为空，进入阻塞等待
				if timeout and time.time() > end_time:
					raise TimeoutError('获取资源超时')

				if timeout:
					remaining_time = end_time - time.time()
					if remaining_time <= 0:
						raise TimeoutError('获取资源超时')

					self.resource_available.wait(remaining_time)
				else:
					self.resource_available.wait()

			connection = self.pool.pop()
			self.in_use.append(connection)
			print(f'线程{threading.current_thread().name}，获取资源成功 {connection}')

		return connection

	"""
		释放资源
	"""

	def release_resource(self, connection: Any):
		with self.resource_available:
			self.in_use.remove(connection)
			self.pool.append(connection)
			self.resource_available.notify()
			print(f'线程{threading.current_thread().name}，释放资源成功 {connection}')

	"""
		对外，使用上下文管理器获取资源
	"""

	@contextmanager
	def fetch_connection(self, timeout: Optional[float] = None):
		resource = self.get_resource(timeout)
		try:
			yield resource
		finally:
			self.release_resource(resource)

	def monitor_pool(self):
		return {
			'总容量': self.maxsize,
			'正在使用资源数': self.in_use,
			'可用资源数': self.pool
		}


class DatasourceConnection:
	_count = 1

	def __init__(self):
		self.connection_id = DatasourceConnection._count
		DatasourceConnection._count += 1

	def query(self, sql: str) -> str:
		time.sleep(0.3)
		return f'连接 {self.connection_id}，执行sql：{sql}'

	@staticmethod
	def create_connection():
		time.sleep(1)
		return DatasourceConnection()

	def __repr__(self):
		return f'数据库连接-{self.connection_id}'


def task_handler(pool_manager: PoolManager,  timeout: Optional[float] = None, task:[Any] = None):
	# 手动调用获取资源、释放资源
	# connection = pool_manager.get_resource(timeout)
	# query_result = connection.query(ordinal)
	# time.sleep(3)
	# print(f'线程{threading.current_thread().name}，查询结果：{query_result}')
	# pool_manager.release_resource(connection)

		with pool_manager.fetch_connection(timeout) as connection:
			query_result = connection.query(task)
			time.sleep(1)
			print(f'线程{threading.current_thread().name}，执行结果：{query_result}')


if __name__ == '__main__':
	pool_manager = PoolManager(maxsize=3, create_resource=DatasourceConnection.create_connection)

	#创建10个查询任务
	queries_task = [f'select * from table_{i}' for i in range(10)]

	#将10个任务，每2个任务分组
	group_task_list = list( zip_longest(*[iter(queries_task)]*2, fillvalue=None) )

	# 创建 5个线程去竞争资源池中的3个连接，每个线程执行2个任务
	threads = [threading.Thread(target=task_handler, args=(pool_manager, 2.0, task), name=f'Worker-{i}') for i,task in enumerate(group_task_list)]

	for t in threads:
		t.start()
	for t in threads:
		t.join()

	print(pool_manager.monitor_pool())
