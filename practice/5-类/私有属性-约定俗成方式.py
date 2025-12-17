class Phone:
	def __init__(self,imei):
		self.__imei = imei  # __xxx 私有属性。约定俗成的一种方式，并没有语法层面的强制性

	@property
	def imei(self):
		return self.__imei

phone = Phone('AAA')
print(phone.imei)

# print(phone.__imei)    no attribute '__imei'

phone._Phone__imei = 'BBB'
print(phone.imei) # 成功修改，BBB
