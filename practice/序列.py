str = '鼠牛虎兔龙'

print(str[0:2])

base_zodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'

print(base_zodiac[1])  # 按下标获取

base_zodiac_name=('luther','一首歌的时间','自你走后')


# 列表 java逻辑填充元素
list = []
for i in range(1, 10):
    if i % 2 == 0:
        list.append(i * i)
print(list)

# 列表推导式 填充元素
list2 = [i*i for i in range(1, 10) if i % 2 == 0]
print(list2)

#将字典的每个value值设置为0
dict1={}
for name in base_zodiac_name:
    dict1[name]=0
dict1['luther']=200
print(dict1) # {'luther': 0, '一首歌的时间': 0, '自你走后': 0}

#字典推导式 将每个value值设置为0
dict2={n:0 for n in base_zodiac_name}
print(dict2)  # {'luther': 0, '一首歌的时间': 0, '自你走后': 0}

