from dataclasses import dataclass, field,asdict,astuple,replace,fields
@dataclass
class User:
	username: str
@dataclass
class User:
	username: str


@dataclass
class User:
	username: str
	address: str = field(compare=False, repr=False)  # 此字段不参与 __eq__、__repr__  方法
	age: int = 22  # 带默认值
	avatar: str = field(default='default.jpg' ,compare=False)
	scores: list = field(default_factory=list)  # 多个实例之间互不影响
	area: str = field(init=False)

	"""
		后置初始化逻辑，在 __init__ 后执行
	"""
	def __post_init__(self):
		self.area = f'{self.username}，家庭住址：{self.address}'
		if self.age < 18:
			raise Exception('未成年')

u_1 = User('Jay', address='Hong Kong')
u_1.scores.append(66)
print(f'u_1 - {u_1}')

u_2 = User('Jay', age = 22, address='北京')
u_2.scores.append(88)  # scores 相互独立不影响
print(f'u_2 - {u_2}')

print(u_1.scores == u_2.scores)  #False
print(f'将实例转为字典、元组:  {asdict(u_1)} - {astuple(u_1)}')  # 将实例转为字典、元组

u_3 = replace(u_1, avatar='aaa.png',scores = [77,88])  # 拷贝实例，并修改某一字段，若replace时修改了可变对象属性，后续和u_1的可变对象scores列表是相互独立的，修改数据互不影响
# u_3 = replace(u_1, avatar='aaa.png')  # 拷贝实例，并修改某一字段，若replace时没有对scores可变对象修改，那么后续像append修改时，和u_1是共享的scores，两个相互影响
u_3.scores.append(99)
print(f'实例拷贝，u_3 - {u_3}')
print(f'u_1 - {u_1}')
print(f'scores 是否相同：{u_1.scores is u_3.scores}')

all_fields = fields(User)  # 获取所有字段信息





class User2:
	scores : list = []   # 不使用 @dataclass，普通默认值设置后 所有实例共享同一个列表。一个实例修改了列表元素，其他实例的也会跟着变化
	username :str = 'Jay'

	def __repr__(self):
		return f'{self.username}，{self.scores}'

uu = User2()
uu.scores.append(5)
uu.username = 'AA'
print(uu)  #  AA，[5]

uu_2 = User2()
print(uu_2) # Jay，[5]
print(uu.scores == uu_2.scores) #True
