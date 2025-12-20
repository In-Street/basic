import threading, time

"""
使用Lock 并 双重校验，实现线程安全。 装饰器类也可采用 此方式来实现线程安全的单例模式
"""
class DataSource:
	_instance = None
	lock = threading.Lock()
	# lock = threading.RLock() # 可重入锁

	def __new__(cls, *args, **kwargs):

		if cls._instance is None:
			with cls.lock:
				if cls._instance is None:
					time.sleep(0.1)
					cls._instance = super().__new__(cls)
		return cls._instance

	def __init__(self, addr):
		import threading
		print(f'初始化数据源，{addr}，{threading.current_thread().ident}')
		self.addr = addr


res=[]
def create_ds(addr):
	ds = DataSource(addr)
	res.append(id(ds))
	return ds

threads = [threading.Thread(target=create_ds, args=(i,)) for i in range(10)]
for t in threads:
	t.start()

for t in threads:
	t.join()

print(res)



##########  通过模块引入 ##########
"""
模块在程序运行中仅加载一次，且加载过程是线程安全的
"""
from MySingleton import instance
import queue

result_queue = queue.Queue()  # 接收多线程的执行结果

def create_ds_module_wrapper(addr: str | None =None) ->None:
	ds = instance  # 模块在加载时创建唯一实例，天然线程安全
	result_queue.put(ds)

threads = [threading.Thread(target=create_ds_module_wrapper, args=(i,)) for i in range(7)]
for t in threads:
	t.start()
for t in threads:
	t.join()


result_id_list = []
while not result_queue.empty():
	result_id_list.append(id(result_queue.get()))

print(f'模块引入，{result_id_list}')