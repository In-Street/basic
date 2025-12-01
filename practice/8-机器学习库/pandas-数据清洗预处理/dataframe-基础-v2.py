from pandas import DataFrame, NA
from numpy import nan

"""
1. dropna:  删除包含na的整行、 只删除全部是na的整行【how参数控制】、只删除全部是na的整列数据【axis 参数控制】  

2. fillna:  将na 进行填充值。需指定各个列的数据类型，然后依据列的不同类型去设置填充值
"""

# 包含部分值为nan，全部值为nan的数据
data_1 = DataFrame([['北京', 2021, 1.5], ['上海', NA, 1.1], ['深圳', 2023, 3.6], [nan, nan, nan]])
# print(data_1)

data_1_dropna = data_1.dropna()  # 只要包含nan ，就删除整行
# print(data_1_dropna)

dropna_all = data_1.dropna(how='all')  # 只删除 全部值为nan的 整行数据
# print(dropna_all)


data_1[3] = nan
print(data_1)
dropna_all_column = data_1.dropna(how='all', axis=1)  # 通过设置axis参数，只删除 全部值为nan的 整列数据
# print(dropna_all_column)


# 因为数据中包含字符串、整型、浮点型，在使用fillna填充为666时，pandas会进行数据推断，有FutureWarning警告的提示
# data_1.fillna(666, inplace=True)


# 明确指定各个列的数据类型，fillna时依据不同的列分别指定填充值
data_2 = DataFrame([['北京', 2021, 1.5], ['上海', NA, 1.1], ['深圳', 2023, 3.6], [nan, nan, nan],['北京', 2022, 2.5]],
                   columns=['city', 'year', 'pop'])

# 显示指定各个列的数据类型
data_2 = data_2.astype({'city': 'string', 'year': 'Int64', 'pop': 'Float64'})
print(data_2)

#给各个列分别指定值。 inplace=True ，直接修改data_2，否则修改的是data_2的副本
data_2.fillna({'city': '未知', 'year': 666, 'pop': 2.2}, inplace=True)
print(data_2)


#
print(data_2.groupby('city')['pop'].mean())
