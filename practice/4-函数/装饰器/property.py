class Demo:

	def __init__(self, name, **kwargs):
		self.kwargs = kwargs
		self._name = name

	def __getattr__(self, attr_name):
		if attr_name in self.kwargs:
			return self.kwargs[attr_name]
		return f'未找到属性：{attr_name}'

	def __str__(self):
		return f'{self.name}'

	@property
	def name(self):
		return self._name



d_1 = Demo('nameA', age=10, addr='地址A')
print(d_1.name)
d_1._name = 'nameB'
print(d_1.name)