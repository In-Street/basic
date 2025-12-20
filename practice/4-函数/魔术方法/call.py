# 自定义元类重写 __call__
class SelfMeta(type):
	def __call__(cls, *args, **kwargs):
		print(f'元类__call__前置，{cls.__name__}')

		# 创建实例
		instance = cls.__new__(cls, *args, **kwargs)
		if instance is not None:
			#初始化
			cls.__init__(instance,*args, **kwargs)
		print(f'元类__call__后置，{cls.__name__}')
		return instance


# 使用自定义元类来创建普通类，监控实例化普通类的过程
class SelfClass(metaclass=SelfMeta):
	def __init__(self, name, age):
		print(f'自定义类实例初始化')
		self.name = name
		self.age = age

	def __new__(cls, *args, **kwargs):
		print(f'自定义类创建实例')
		# return cls.__new__(cls, *args, **kwargs) # 出现递归，报错。 应使用super调用
		return super().__new__(cls)

	def __call__(self):
		print(f'调用显式定义__call__')


s_1 = SelfClass('我睁开双眼看着空白', 22)

print(s_1.name)
print(callable(s_1))
print(s_1())
