class ReadOnlyProperty:

	def __set_name__(self, owner, name):
		print(f'调用描述符类的__set_name__ ,设置属性名 {name}')
		self._attr_name = f'_private_{name}'  #

	def __get__(self, instance, owner):
		print(f'调用描述符类的__get__，获取属性值 {self._attr_name}')
		return getattr(instance, self._attr_name)

	def __set__(self, instance, value):
		print(f'调用描述符类的__set__，设置属性值 {self._attr_name}')
		if not hasattr(instance, self._attr_name):
			setattr(instance, self._attr_name, value)
			return
		raise AttributeError(f'属性{self._attr_name} 不允许修改')



class Phone:

	imei  = ReadOnlyProperty() # 仅在描述符类被赋值为类属性时，定义阶段执行一次 __set_name__ ，自动传入 imei , 经过描述符类后，属性名定义为 _private_imei
	number = ReadOnlyProperty()

	def __init__(self, imei, number):
		self.imei = imei
		self.number = number



p1 = Phone('AA','182')
print(p1.imei)

p1.ns = 'BB'
print(vars(p1))

p1.number = '135'
print(p1.number)