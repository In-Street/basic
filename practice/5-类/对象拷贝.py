"""
	浅拷贝：
		1. dataclasses 模块：  replace ，参考: practice/7-标准库/装饰器/dataclasses_.py
		2. yy = copy.copy(xx) ，浅拷贝

	深拷贝：
		1. copy.deepcopy()
		2. 通过 asdict 创建的新对象
"""
import copy
from dataclasses import dataclass, field,astuple,asdict


@dataclass
class User:
	username: str
	age: int
	address: list[str] = field(default_factory=list, compare=False)
	desc: list[list[str]] = field(default_factory=list, compare=False)  # 存在嵌套容器
	hobby : dict[str, str|list] = field(default_factory=dict, compare=False)



u_1 = User('Jay', 18, ['北京', '上海'],[['大兴区'],['朝阳区']],{'company':'人民在线','scores':[85,90]})
print(f'原始u_1 - {u_1}')  #  User(username='Jay', age=18, address=['北京', '上海'])

######################### 手动构造新实例 #########################
u_3 = User(**asdict(u_1))
u_3.address.append('纽约')
u_3.desc[0].append('dxq')  # 针对嵌套容器，修改内层列表中的数据，仍然不影响原对象
u_3.hobby['company'] = 'rmzx'
u_3.hobby['scores'].append(95)  # 针对字典修改，仍然不影响原对象
u_3.hobby['AA']='aa'
print(f'asdict u_3 - {u_3}')
print(f'asdict 后修改，u_1 - {u_1}')
print(f'asdict 针对可变对象是否相同：address: {u_1.address is u_3.address}，desc: {u_1.desc[0] is u_3.desc[0]}，hobby：{u_1.hobby is u_3.hobby}')  #False
print(f'hobby-scores: {u_1.hobby['scores'] is u_3.hobby['scores']}')


######################### copy.copy  #########################
u_4 = copy.copy(u_1)
u_4.username='国际化'
u_4.address.append('芝加哥')
print(f'copy u_4 - {u_4.address is u_1.address}')  #True ,属于浅拷贝

u_5 = copy.deepcopy(u_1)
print(f'copy u_5 - {u_5.address is u_1.address}') # False ，属于深拷贝