class DescriptionObj:

	def __set__(self, instance, value):
		print(f'调用 __set__，属性名:{self._attr_name}，赋值:{value}')
		setattr(instance, self._attr_name, value)

	def __set_name__(self, owner, name):
		print(f'调用DescriptionObj，__set_name__，name:{name}')
		self._attr_name = f'_private_{name}'

	# def __get__(self, instance, owner):
	# 	return getattr(instance, self._attr_name)

class SelfObj:
	username = DescriptionObj()  # 描述符对象作为类属性时，只在类定义阶段执行一次描述符对象内部的 __set_name__ 方法，后续实例化、赋值都不会再执行
	password = DescriptionObj()

	def __init__(self, username, password,age):
		self.username = username   # 触发描述符对象 的 __set__ 方法
		self.password = password
		self.age = age

	def __getstate__(self):
		copy_dict = self.__dict__.copy()
		del copy_dict[self.password._attr_name]  # 脱敏
		return copy_dict

	def __setstate__(self, state):
		print(f'反序列化：{state}')  #  反序列化：{'_private_username': 'abc', 'age': 11}
		print(f'反序列化：{self.__dict__}')  #  {}
		self.__dict__.update(state)  #  将除password 外的属性设置回对象
		self.password='default'  # 脱敏


obj_1 = SelfObj('ABC', '123',11)
obj_2 = SelfObj('DEF', '456',22)

obj_1.username = 'abc'

print(obj_1.__dict__)  # {'_private_username': 'abc', '_private_password': '123'}
print(obj_1.username.__dict__)  # {'_attr_name': '_private_username'}

print('======='*20)

import pickle

dumps = pickle.dumps(obj_1)
loads_res = pickle.loads(dumps)
print(loads_res.__dict__)
