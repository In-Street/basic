# 计算函数执行时间
import time
from curses import wrapper


# 传统方式：每个方法执行前后都需要手动加开始时间、结束时间
def _sleep():
    time.sleep(3)


start_time = time.time()
_sleep()
end_time = time.time()
print("函数执行了 %s 秒" % (end_time - start_time))


# 装饰器方式： @xxx 称为装饰函数 ， 被标注的函数称为被修饰函数

def timer(func):  # 错误的方式
    s_time = time.time()
    func()
    e_time = time.time()
    print("函数执行了 %s 秒" % (e_time - s_time))


def timer_2(func):  # 正确方式，使用闭包
    def wrapper(a, b):
        print("开始执行")
        s_time = time.time()
        result = func(a, b)
        e_time = time.time()
        print("结束执行")
        print("函数执行了 %s 秒" % (e_time - s_time))
        return result

    return wrapper


# @timer  # 报错： TypeError: 'NoneType' object is not callable。如果一个函数没有显式的 return 语句（或 return 后没有值），它的默认返回值是 None。如果将这个函数的返回值赋值给变量，再对变量进行调用，就会报错
@timer_2  # 修饰带参数的函数时，函数的参数需传入装饰函数的内部函数中
def sleep_1(a, b):
    time.sleep(4)
    return a + b

print(sleep_1(1, 3))




# 装饰函数带参数，标记不同的函数，并获取被装饰函数名
def timer_3(arg):
    def time_4(func):
        def wrap(a, b):
            print("装饰方法："+ arg)
            s_time = time.time()
            result = func(a, b)
            e_time = time.time()
            print("函数: %s 执行了 %s 秒" % (func.__name__ , e_time - s_time))  # 获取函数名称
            return result

        return wrap

    return time_4

@timer_3("add module")
def add(a, b):
    time.sleep(1)
    return a + b

@timer_3("sub module")
def sub(a, b):
    time.sleep(1)
    return a - b

print(add(7, 3))
print(sub(10, 3))

