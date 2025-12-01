#   pip3 install numpy

import numpy as np

array_1 = np.array([1, 2, 3, 4, 5, 6])
print(array_1.dtype)


# 数组与标量计算
print(array_1 * 10)  #  [10 20 30 40 50 60]


# 定义一维全是0的数组
zeros_array = np.zeros(10)
print(zeros_array)  #  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]


# 定义全是1 的 2行3列 的二维数组
ones_array = np.ones((2, 3))
print(ones_array)


# 创建一维数组，等差结构
"""
	np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
		num:  要生成的等步长的样本数量
		endpoint:  True-包含stop值
		restep:  True-生成的数组中会显示间距
"""
linspace_a = np.linspace(10, 20, 5,endpoint=False,retstep=True) # 在 10～20 不包括20的区间，取5个数组，那么间隔步长则为2
print(linspace_a)
