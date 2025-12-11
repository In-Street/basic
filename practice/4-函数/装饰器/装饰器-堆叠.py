def decoration_1(func):
	def wrapper():
		print('第一个装饰器前置')
		result = func()
		print('第一个装饰器后置')
		return result
	return wrapper


def decoration_2(func):
	def wrapper():
		print('第二个装饰器前置')
		result = func()
		print('第二个装饰器后置')
		return result
	return wrapper


@decoration_1
@decoration_2
def hello():
	print('hello')


hello()