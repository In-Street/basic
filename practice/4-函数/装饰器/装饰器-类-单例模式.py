# 类装饰器 单例模式
class Singleton:

	"""使目标类变成单例模式"""
	def __init__(self, cls):
		self.instance = None
		self.cls = cls

	def __call__(self, *args, **kwargs):
		if self.instance is None:
			"""拦截实例化过程，确保只创建一个实例"""
			self.instance = self.cls(*args, **kwargs)
		return self.instance


#类形式的装饰器类
@Singleton
class DataSource:
	def __init__(self):
		print('初始化数据源')


source_1 = DataSource()
source_2 = DataSource()

print(source_1 is source_2)  # True，则为同一个实例
