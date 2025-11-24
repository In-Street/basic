class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age


p1 = Person('纽约', 18)
p2 = Person('纽约', 18)
p3 = Person('里斯本', 20)

print(p1 == p2)  # False 默认比较内存地址，不同的对象内存地址不同
print(p1 is p2)  # False ， is 明确比较内存地址
print(p1 == p3)


class Song:
	def __init__(self, name, year):
		self.name = name
		self.year = year

	def __eq__(self, other):
		# 类型比较
		if not isinstance(other, Song):
			return False

		# 2 类属性值比较
		return self.name == other.name and self.year == other.year

	def __hash__(self):
		return hash((self.name, self.year))


song_a = Song('七里香',2004)
song_b = Song('七里香',2004)
song_c = Song('说好的幸福呢',2008)

print(song_a == song_b)  # True
print(song_a == song_c)