# 各个数据类型比较

"""
1. int、float、bool、str 等基本类型都使用 == 进行值相等性判断.
		float有精度问题

2.  ==  和 is
		== :  判断两个对象的值是否相等
		is:   用于判断两个变量是否指向同一个对象（即它们的内存地址是否相同)。最常见的用途是检查一个变量是否为 None (if x is None:)。
			   不要依赖 is 来比较整数是否相等， 尤其是超出 -5 ~ 256 范围的整数，原因是可能会因书写格式（单行/多行）、运行环境（交互式、py文件）不同产生不同的结果。
				a. 在交互式环境中（终端）：
					如果在同一行代码中创建并比较两个相同的大整数，Python 的解释器可能会进行优化，让它们指向同一个对象。
					如果在不同行代码中创建并比较，Python 则会创建两个不同的对象

				b. 在.py 文件中：
					当 Python 执行一个脚本文件时，它会在编译阶段对整个文件的代码进行解析和优化。
					在这种情况下，即使是在不同行创建的、超出缓存范围的相同整数，Python 编译器也可能会发现它们是同一个值，并优化为使用同一个对象


3. 列表数据判断：
		a. 遵循 值和顺序 完全相同
		b. 若仅看元素值，忽略顺序的话：sorted() : 适用可排序的数据 、 collections.Counter : 计数比较，适用可哈希的元素【一个对象如果具有在其生命期内绝不改变的哈希值（它需要有 __hash__() 方法），并可以同其他对象进行比较（它需要有 __eq__() 方法）就被称为 可哈希 对象】
"""
from collections import Counter

str_a = '一首歌的时间'
str_b = '一首歌的时间'
print(str_a == str_b)

print(0.1 + 0.2 == 0.3)  # False 因为0.1+0.2实际是0.30000000000000004）

print(True == 1)  # True 的本质是1


# python 会缓存 -5 ～ 256 间的整数
int_a = 110
int_b = 110
print(int_a == int_b) # True
print(int_a is int_b) # True 。

int_c = 666
int_d = 666
print(int_c == int_d)
print(int_c is int_d)


# 可排序的元素，使用 sorted 后比较
list_a = [1,2,3]
list_b = [1,3,2]
print(list_a == list_b)
print(list_a.sort() == list_b.sort())

# 可哈希的元素，Counter()后在比较
list_c  =['一首歌的时间','说好的幸福呢']
list_d  =['说好的幸福呢','一首歌的时间']
print(Counter(list_c) == Counter(list_d))


# 不可重复、无序
set_a = {1,12,14,1,5}
print(set_a )