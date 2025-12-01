#  外部函数的变量 被 内部函数引用，这种方式称为闭包
def sum_f(a):
    def add(b):
        return a + b

    return add  # 返回内部函数名称 或 函数的引用


sum_ = sum_f(10)
print(type(sum_)) #  <class 'function'>
print(sum_(2)) # 12
print(sum_(3)) # 13


print(sum([2, 3]))


#计数器： 每调用一次进行增加
def counter(a):
    count_=[0]
    def add():
        count_[0]+=a
        return count_[0]
    return add

num_ = counter(1)
print(num_()) # 1
print(num_()) # 2
print(num_()) # 3

num_2 = counter(10)
print(num_2()) # 10
print(num_2()) # 20