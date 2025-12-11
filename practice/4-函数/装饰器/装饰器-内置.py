class DataSource:
	ds = '类属性： jdbc:mysql://localhost:3306/jdbc'

	def __init__(self, instance_attr):
		self.instance_attr = instance_attr

	@staticmethod
	def static_get_ds():
		print(f'调用静态方法，访问类属性：{DataSource.ds}')

	@classmethod
	def class_get_ds(cls):
		print(f'调用{cls.__name__}类方法，访问类属性：{cls.ds}')

	@classmethod
	def class_set_ds(cls, param):
		cls.ds = param

	# 普通实例方法，第一个参数是self （指向实例本身）。可访问/修改 实例属性和类属性
	def instance_method(self):
		self.instance_attr = '实例属性'
		print(f'实例方法中，访问类属性: {self.ds}，实例属性：{self.instance_attr}')

	@property
	def property_ds(self):
		return self.ds


DataSource.static_get_ds()
DataSource.class_get_ds()

instance_1 = DataSource('第一个实例')
instance_1.instance_method()

DataSource.class_set_ds('修改类属性：AAAA')
print(' =============  ')

DataSource.static_get_ds()
DataSource.class_get_ds()

instance_2 = DataSource('第二个实例')
instance_1.instance_method()


class  SubDataSource(DataSource):
	ds = '子类的类属性'

SubDataSource.class_get_ds()