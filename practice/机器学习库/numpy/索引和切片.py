import numpy as np

array_1 = np.arange(10)
print(array_1)  #  [0 1 2 3 4 5 6 7 8 9]

print(array_1[5:8])  # [5 6 7]   左闭右开

# 赋值  [  0   1   2   3   4 666 666 666   8   9]
array_1[5:8]=666
print(array_1)


# 将切片赋值给新变量
copy_array = array_1[5:8].copy()
copy_array[:]=888  # : 表示从第一个元素到最后一个元素


print(copy_array)  # [888 888 888]
print(array_1)  #  [  0   1   2   3   4 666 666 666   8   9]
