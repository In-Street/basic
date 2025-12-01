"""
1.  reindex: 重新索引顺序 。  当新增索引值，默认值为NaN，填充值：fill_value=xx 、 method = ''ffill / bfill

2. dropna
"""

from pandas import Series

series_a = Series([4.5, 7.2, -2.1], index=['g', 'f', 'e'])
# print(series_a)

# 指定新的索引值
series_a.index = ['c', 'b', 'a']
# print(series_a)

# 重新索引，按给定顺序展示。 新添加的索引的值以100填充
a_reindex = series_a.reindex(index=['a', 'b', 'c', 'H'], fill_value=100)
# print(a_reindex)


# 新索引填充相邻的值
series_b = Series(['蓝色', '紫色', '黄色'], index=[0, 2, 4])
b_reindex = series_b.reindex(index=range(6)) # reindex后，1 NaN  3NaN  5NaN
print(b_reindex)

b_reindex_ffill = series_b.reindex(index=range(6), method='bfill') # ffill： NaN 以上一个索引对应值进行填充。 bfill ： NaN以后一个索引的对应值进行填充
print(b_reindex_ffill)


# 删除NaN的行
b_reindex_dropna = b_reindex.dropna()
print(b_reindex_dropna)