#  作为迭代器，需实现 __iter__() 、__next__() 两个方法
class MyIter:
	def __init__(self):
		self.c = 0

	def __iter__(self):
		self.c = 1
		return self

	def __next__(self):
		p = self.c
		if p > 50:
			raise StopIteration
		self.c+=3
		return p

my_iter = MyIter()
iter_a = iter(my_iter)

print(next(iter_a)) # 1
print(next(iter_a)) # 4
print(next(iter_a)) # 7

while True:
	print(f'循环产生：   {next(iter_a)}')