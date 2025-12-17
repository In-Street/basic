"""
描述符类，不存储属性具体值，仅定义只读规则
"""
class PrivateProperty:
	def __init__(self, attr_name):
		# 接收实例的私有属性名
		self._attr_name = attr_name

	#读取属性时触发
	def __get__(self, instance, owner):

		# 类访问时，如 Phone.imei ,返回描述符自身
		if instance is None:
			return self

		#从实例的 __dict__ 中取值
		if self._attr_name in instance.__dict__:
			return instance.__dict__[self._attr_name]

		return f'未找到属性{self._attr_name}定义'

	# 修改属性时触发
	def __set__(self, instance, value):
		if instance is None:
			raise AttributeError("实例不存在")

		# 若实例已存在该属性，则禁止修改
		if self._attr_name in instance.__dict__:
			raise AttributeError("禁止修改属性值")

		# 首次设置，存入实例的__dict__
		instance.__dict__[self._attr_name] = value

	def __delete__(self, instance):
		raise AttributeError("禁止删除属性值")

class Phone:

	#将描述符作为类属性
	imei = PrivateProperty('_imei')

	def __init__(self, imei):
		self.imei = imei  # 初始化实例，给 _imei赋值时，触发描述符的__set__

	@property
	def mei(self):
		return self.imei

	@mei.setter
	def mei(self, value):
		raise AttributeError("禁止修改属性值>")

p_1 = Phone('aaa')
print(p_1.imei)

p_2 = Phone('BBB')
print(p_2.mei)

print(vars(p_1))

p_1.imei = 'CC'
print(p_1.mei)  #  AttributeError: 禁止修改属性值
