import numpy as np
from pandas import Series, DataFrame

"""
	a  1    6
        2    6
        3    6
	b  1    6
        2    6
        3    6
	c  1    6
        2    6
	d  1    6
"""


series_a = Series(np.random.randint(1, 10),
                  index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd'], [1, 2, 3, 1, 2, 3, 1, 2, 1]])
print(series_a)

print(series_a['a'])
print(series_a['a':'c'])

print(series_a['a',3])


#  转换为 DataFrame 结构格式
unstack_a = series_a.unstack()
print(unstack_a)

print(unstack_a.stack())  # 转为层次化索引结构
