#  pip3 install pandas
# Series :一维数组

from pandas import Series, DataFrame

series_1 = Series([7, 8, 9, 10])  # 默认索引值0 1 2 3
print(series_1)

print(series_1[3]) # 10

print(series_1.index) # 所有索引值
print(series_1.values) # 所有value


# 明确指定索引值
series_2 = Series([7, 8, 9, 10], index=['d', 'b', 'c', 'a'])
print(series_2)

print(series_2['c'])

# 指定具体索引，设置其value
series_2['c'] = 100
print(series_2)

# 判断索引值是否存在
print('b' in series_2)


# 将字典转换为 Series
dict_1 = {'beijing': 100, 'shanghai': 90, 'nanjing': 120}
series_3 = Series(dict_1)
print(series_3)

series_3.index = ['bj','sh','nj']  # 重新设置索引值
print(series_3)