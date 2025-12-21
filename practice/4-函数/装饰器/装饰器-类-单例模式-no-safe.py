# 类装饰器 单例模式
class Singleton:
	"""使目标类变成单例模式"""

	def __init__(self, cls):
		print(f'装饰器类的 init 方法')
		self.instance = None
		self.cls = cls

	def __call__(self, *args, **kwargs):
		if self.instance is None:
			"""拦截实例化过程，确保只创建一个实例"""
			import time
			time.sleep(0.1)
			self.instance = self.cls(*args, **kwargs)  # 真正创建原类实例，触发原类的 __new__ + __init__
		return self.instance


# 类形式的装饰器类
@Singleton
class DataSource:
	def __init__(self):
		import threading
		print(f'初始化数据源，{threading.current_thread().ident}')


# source_1 = DataSource()  # 调用装饰器类的 __call__
# source_2 = DataSource()

# print(source_1 is source_2)  # True，则为同一个实例


class DataSource2:
	_instance = None

	def __new__(cls, *args, **kwargs):
		if cls._instance is None:
			import time
			time.sleep(0.1)
			cls._instance = super().__new__(cls)  # 使用 super()调用，避免递归
		return cls._instance

	def __init__(self, addr):
		import threading
		print(f'初始化数据源-V2，{addr}，{threading.current_thread().ident}')
		self.__addr = addr

	@property
	def addr(self):
		return self.__addr


# ds_1 = DataSource2('链接地址A')
# print(ds_1.addr)
# ds_2 = DataSource2('链接地址B')
# print(ds_1 is ds_2)
# print(ds_1.addr)


################### 线程安全测试  ###################

import threading

ds_list = []


def create_ds(addr=0):
	# ds = DataSource2(addr)
	ds = DataSource()
	ds_list.append(id(ds))


# threads = [threading.Thread(target = create_ds,args=(f'连接地址{i}',)) for i in range(5)]
threads = [threading.Thread(target=create_ds) for _ in range(5)]

for t in threads:
	t.start()

for t in threads:
	t.join()

print(ds_list)  # [4702897648, 4703792320, 4702897648, 4703792320, 4702897648] 存在相同地址，说明装饰器和重写__new__两种方式都线程不安全
