var = 123  # 全局变量

def f():
    var = 456
    print(var)

f() # 456 , 只影响函数内部
print(var) # 123 # 对外部变量不影响


var2 = 789
def f2():
    global var2
    var2= 789
    print(var2)

f2()  # 789
print(var2)  # 789

####################### 嵌套作用域示例1 ###########################

def call_counter(func):
	count = 0
	def wrapper(*args, **kwargs) -> str:
		nonlocal count   # nonlocal ： 允许内部函数修改外部函数的变量
		count += 1
		res = func(*args, **kwargs)
		print(f'函数{func.__name__} 被调用了{count}次')
		return res

	return wrapper


@call_counter
def out_1(name):
	return f'你好，{name}'

print(out_1('Jay'))
print(out_1('JJ'))

####################### 嵌套作用域示例2 ###########################
from typing import Union
print('####################### 嵌套作用域示例2 - 配置管理 ###########################')

def create_change_config():
	config = {
		'debug': False,
		'log_level': 'INFO',
		'timeout': 20
	}
	callback_notification=[]
	str_1 = ''

	def get_config(key):
		return config[key]

	def set_config(key: str, value: Union[bool, str, int]):
		old_value = config[key]
		config[key] = value
		nonlocal str_1  # 使用 nonlocal后，下面对str_1的重新赋值 就会影响外部函数的变量 str_1
		str_1 = value   # 不使用nonlocal时，外部函数的str_1的值未改变。此处的str_1 被视为内部函数的局部变量
		for callback in callback_notification:
			callback(key, old_value, value)

	def register_callback(func):
		callback_notification.append(func)

	def remove_callback(func):
		callback_notification.remove(func)

	def print_str():
		print(f'外部函数str_1：{str_1}')

	return {
		'get': get_config,
		'set': set_config,
		'register': register_callback,
		'remove': remove_callback,
		'print':  print_str
	}

def callback_log(key,old_value,new_value):
	print(f'配置{key}，由{old_value} 更改为 {new_value}')


config_1 = create_change_config()

#注册回调函数
config_1['register'](callback_log)

print(f'获取debug的value值：{config_1['get']('debug')}')  # 获取debug的value值：False

config_1.get('print')()  # 外部函数str_1：
config_1['set']('log_level', 'ERROR')  # 配置log_level，由INFO 更改为 ERROR
config_1.get('print')()  # 外部函数str_1：ERROR
