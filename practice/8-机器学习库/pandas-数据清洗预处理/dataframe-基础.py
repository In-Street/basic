# dataframe:  多维数组
"""
 1.  创建 DataFrame ： 字典创建、数组创建 、 字典嵌套
 2. 表格排序【index/value】、获取指定一行/多行数据，返回指定一列/多列数据
 3. 现有表格上新增一列： 不可直接使用原生的三元表达式，需使用 numpy.where 或者 Series.apply()
 4.  行、列 互换
"""

import pandas as pd
import numpy as np
from pandas import Series,DataFrame

# 获取pandas 版本号
print(pd.__version__)

# 1 使用字典来创建 DataFrame
data = {'city': ['北京', '上海', '北京', '深圳', '上海'],
        'year': [2021, 2022, 2023, 2022, 2023],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}

frame_a = DataFrame(data,index=['a','b','c','d','e'])
print(frame_a)


# 1 使用数组来创建DataFrame。  columns: 标识表格的列索引
data_2 = [['北京', 2021, 1.5], ['上海', 2022, 1.1], ['深圳', 2023, 3.6]]
frame_columns = DataFrame(data_2, columns=['city', 'year', 'pop'])
# print(frame_sort_columns)

# 1 使用字段嵌套来创建 DataFrame
data_3 = {'beijing':{2008:1.5,2009:2.5},'上海':{2009:1.6,2008:2.6}}
frame_b = DataFrame(data_3)
print(frame_b)

#2 对表格按 value值 进行排序
frame_a_sorted = frame_a.sort_values(by=['year', 'city', 'pop'], ascending=True)
# print(frame_a_sorted)

# 2 loc : 返回指定行的数据，可以一行或多行。若没有设置索引，默认从0 开始
loc_1 = frame_a.loc['d']
loc_2 = frame_a.loc[['d','c']]
# print(loc_2)

# 2 返回指定列数据
single_column = frame_a[['city','pop']]
# print(single_column)



# 3. 新增一列，此处使用原生的三元表达式会报错：ValueError,原生三元表达式只适用于标量逻辑，处理单个值。 DataFrame/Series为向量，需结合使用 numpy.where(判断条件, 条件为True时值, 条件为False时值) 或者 Series.apply()
# frame_a['capital'] = '首都' if frame_a['city'] == '北京' else '城市'
frame_a['capital'] = np.where(frame_a['city'] == '北京', '首都', '直辖市')
# print(frame_a)

#新增一列，使用 Series.apply()
def capital_handler(city):
		return '首都' if city == '北京' else '直辖市'
frame_a['capital_2'] = frame_a['city'].apply(capital_handler)
print(frame_a)



# 4 .  行、列互换（转置）
frame_b_t = frame_b.T
print(frame_b_t)
