class Monster:
	def __init__(self, name, hp=100):
		self.hp = hp
		self.name = name

	def run_(self):
		print('%s 正在移动' % self.name)


class Boss(Monster):
	def __init__(self, name, career, hp):
		super().__init__(name, hp)
		self.career = career  # 子类可定义父类中不存在的新属性


	# 子类覆盖父类中同名的方法
	def run_(self):
		print("我是子类的run_方法")


class Animal(Monster):
	pass


a1 = Animal("Jimmy")
print('%s , %s HP' % (a1.name, a1.hp))
a1.run_()

a2 = Boss("Boss", '最强', 2000)
print('%s , %s HP , %s' % (a2.name, a2.hp,a2.career))
a2.run_()
