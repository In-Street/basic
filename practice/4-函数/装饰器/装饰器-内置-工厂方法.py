import time, datetime

'''
	python 不支持重载 __init__ 方法。可通过 @classmethod 装饰为类方法，来创建不同参数的实例，替代多构造器
'''

class SelfData:
	def __init__(self, year, month, day):
		self.year = year
		self.month = month
		self.day = day

	def __str__(self):
		return f'{self.year} / {self.month} / {self.day}'

	@classmethod
	def from_timestamp(cls, timestamp):
		# time_localtime = time.localtime(timestamp)
		# return cls(time_localtime.tm_year, time_localtime.tm_mon, time_localtime.tm_mday)

		d = datetime.datetime.fromtimestamp(timestamp)
		return cls(d.year, d.month, d.day)

	@classmethod
	def from_string(cls, string):
		s = datetime.datetime.strptime(string, '%Y-%m-%d')
		return cls(s.year, s.month, s.day)


data_1 = SelfData(2025, 10, 10)

data_2 = SelfData.from_timestamp(1757426948)

data_3 = SelfData.from_string('2025-08-11')

print(data_1.__str__())
print(data_2.__str__())
print(data_3.__str__())