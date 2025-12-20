# 从字典中动态映射属性，无需预先全部定义
class DynamicClass:

	def __init__(self, name, **kwargs):
		self.name = name
		self.kwargs = kwargs

	def __getattr__(self, attr_name):
		if attr_name in self.kwargs:
			return self.kwargs[attr_name]
		return f'未找到：{attr_name}'


d_1 = DynamicClass('nameA', age=12, addr='我睁开双眼看着空白')

print(d_1.name)
print(d_1.age)
print(d_1.addr)

print(d_1.gender)

# 延迟加载重量级属性

print(vars(d_1))

print(round(2.675,2)) # 输出2.67  而非2.68

print(f'{2.675:.20f}') # 末尾有非0数 -> 二进制不能精确表示，浮点数有误差

print(f'{0.5:.20f}')  # 末尾全是0 -> 二进制精确表示