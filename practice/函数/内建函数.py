# filter  \  map  \ reduce  \ zip

list_1 = [1, 2, 3, 4]
print(list(filter(lambda x: x > 2, list_1)))

#  map(func, *iterables) : 对迭代器中的每个元素，按参数形式传入func 方法进行计算
l_map = map(lambda x: x + 1, list_1)
print(list(l_map))

# reduce(function, iterable[, initial]) ：初始值可省略。将迭代器中的元素从左向右，作为func的两个参数传入进行累计的运算
from functools import reduce

l_reduce = reduce(lambda x, y: x + y, list_1, 2)
print(l_reduce)  # ( ( (1+2) +2) +3 ) + 4



# zip 对字典的key 和 value 进行调换
dict_1={"a":"aa","b":"bb"}
dict_zip = zip(dict_1.values(), dict_1.keys())
print(dict(dict_zip))  # {'aa': 'a', 'bb': 'b'}


# zip 对 两个列表重组 (a,b,c) 、(d,e,f)  -> (a,d) 、(b,e)、(c,f)
list_2=[5,6,7,8]
list_zip = zip(list_1, list_2)
print(list(list_zip)) #  [(1, 5), (2, 6), (3, 7), (4, 8)]



print(list(range(3)))
print(list(range(4)))