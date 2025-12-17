def create_phone(imei):

	class Phone:
		def get_imei(self):
			return imei

	return Phone()


# 外部无法修改
p_1 = create_phone('AAA')
print(p_1.get_imei())

