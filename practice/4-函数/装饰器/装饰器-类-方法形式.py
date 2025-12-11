"""方法形式的类装饰器"""
def decoration(cls):
	class Wrapper:
		def __init__(self, *args, **kwargs):
			self.wrapper = cls(*args, **kwargs)  # 实例化原始类

		#  AttributeError: 'Wrapper' object has no attribute 'handler_test'
		"""
		不定义__getattr__ 方法时 ， 下面方法名定义成 handler_test_1 时，报错：AttributeError：hsa no attribute xx  
		此方法属于兜底方法，在找不到属性/方法时被调用
		"""
		def __getattr__(self, item):
			print('未找到属性/方法时，会调用此方法进行兜底')
			return getattr(self.wrapper, item)

		# def handler_test_1(self, param):
		def handler_test(self, param):
			print('>>> 前置处理')
			self.wrapper.handler_test(param)
			print('<<<  后置处理')

	return Wrapper


@decoration
class Test:

	def handler_test(self, param):
		print(f'正在处理：{param}')


t_1 = Test()
t_1.handler_test('AAA')
