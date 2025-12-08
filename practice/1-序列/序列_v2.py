
######################################################  字符串   ######################################################

#  字符串下标从0开始
base_zodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'

print(base_zodiac[1])  # 按下标获取
print(base_zodiac[0:3])  # 鼠牛虎，左闭右开，字符串切片操作
print(base_zodiac[-1])  # 狗，按下标 逆向获取

# 根据年份获取生肖
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
year = 1993
print(chinese_zodiac[year % 12])

# 字符串操作： 成员关系in 、not in
print('鸡' in base_zodiac)

# 字符串操作： 连接
print(base_zodiac + 'ABC')

# 字符串操作： 重复
print(base_zodiac * 2)

######################################################  元组   ######################################################


# u 代表unicode ，防止乱码。 元组定义
zodiac_name = (
    '摩羯座', '水瓶座', '双鱼座', '白羊座', '金牛座', '双子座', '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座',
    '射手座')

# 元组嵌套 ：  月份和日期同时以元组形式存储 (月份, 日期)   。将所有的月份和日期的元组再次包装成新的元组，形成嵌套关系
zodiac_day = (
    (1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

# 定义变量：用户的出生月份、日期
(month, day) = (3, 15)
# 找出用户出生日期在日期元组中符合条件的个数
zodiac_day = filter(lambda x:x<=(month, day), zodiac_day)
filter_result_count = len(list(zodiac_day))
# 根据下标获取用户对应的星座
print('用户星座是：'+ zodiac_name[filter_result_count%12])
print(month)


# 元组中单个数字比较
print((4) > (3))

# 元组中多个数字比较，相当于 120 > 119
print((1, 20) > (1, 19))

# filter ： 元组中筛选数据
a = (1, 3, 5, 7)
b = 4
result = filter(lambda x: x < 4, a)  # 从a中取出小于4的元素
c= list(result)
print(c)  # 使用 list 打印
result_count = len(c) # 从a中取出小于4的元素的个数
print(result_count)



######################################################  列表   ######################################################
a_list=['A','B','C','A']
a_list.append('E')  #在列表尾部添加元素
print(a_list, 'C' in a_list)

a_list.insert(1,'aaaa')
print(a_list)

param = a_list.pop(2)
print(a_list)

a_list.remove('C')
print(a_list)

print(a_list[-2])

list_b = [1,2,3]
print(a_list + list_b)

print(max(list_b))
print(a_list.count('A'))

list_c = ['一首歌的时间','爱错','一首歌的时间']
a_list.extend(list_c)
print(a_list)

print(a_list.index('E'))

a_list.sort(key=lambda x:x == '一首歌的时间',reverse=True)
print(a_list)


######################################################  集合  ######################################################

set_a= {1,2,3,4,3}
set_b = set([4,5,6,7])
print(f'去重：{set_a}')  # 去重

#差集
print(set_a - set_b) #  {1, 2, 3}   集合a包含且集合b不包含的元素 , 差集
print(f'差集：{set_a.difference(set_b)}') # 差集
set_a.difference_update(set_b)  # 移除集合a中的元素，该元素在集合b中也存在
print(f'difference_update：{set_a}') #  {1, 2, 3}

# 交集
set_a.add(4)
print(set_a & set_b)  # {4}  集合a 和 集合b 都包含的元素 ， 交集
print(f'交集: {set_a.intersection(set_b)}')
# set_a.intersection_update(set_b)
# print(set_a)

# 判断两个集合是否相交，若没有相同的元素返回True
print(set_a.isdisjoint(set_b))


# 并集
print(set_a | set_b) #  {1, 2, 3, 4, 5, 6, 7}  集合a b中包含的所有元素 ， 并集
print(f'并集：{set_a.union(set_b)}')

print(set_a ^ set_b) # {1, 2, 3, 5, 6, 7}  不同时包含于集合a和b的元素， 除交集外的元素
print(f'两个集合中不重复的元素：{set_a.symmetric_difference(set_b)}')
print(set_a)
set_a.symmetric_difference_update(set_b)
print(set_a)


# 添加元素
set_c = {'七里香','说好的幸福呢'}
set_c.add('枫')
set_c.update(['晴天','蒲公英的约定'],['一首歌的时间','青花瓷'])
print(set_c)

# 删除元素
set_c.remove('枫')  # 元素不存在时会报错
set_c.discard('青花瓷') # 元素不存在时不会报错
print(set_c)