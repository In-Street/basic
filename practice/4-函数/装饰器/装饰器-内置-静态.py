class User:
	def __init__(self, name, age, phone):
		self.name = name
		self.age = age
		self.phone = phone

	# 静态方法验证手机号，和User相关，但不依赖类属性/实例属性
	@staticmethod
	def check_phone(phone):
		return len(phone) == 11 and phone.isdigit()


print(User.check_phone('0123456789a'))

# 实例化时验证
phone = '18211112222'
if User.check_phone(phone):
	user_1 = User('Jay', 10, phone)
