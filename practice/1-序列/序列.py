from decimal import Decimal

str = '鼠牛虎兔龙'

print(str[0:2])
print(str[2:])
print('a' not in  str)

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


print(bytes('一首歌', 'utf-8'))


'''
小数处理：
		1.   格式化输出，四舍五入保留2位小数：  f'{a/b:.2f}'
		2.  精确处理， decimal.Decimal(‘xxx’)，  (a/b).quantize()
'''

a = 12
b=7
print(f'{a / b:.2f}') # 四舍五入保留两位小数，输出字符串

f_1 = float(f'{a/b:.2f}')  # 转为float类型
print(f_1)

round_1 = round(a / b, 2)
print(round_1)

# 精准计算
import decimal

d_1 = decimal.Decimal('12')
d_2 = decimal.Decimal('7')
quantize_res = (d_1/d_2).quantize(Decimal('0.000'), rounding=decimal.ROUND_HALF_UP)
print(quantize_res)

# decimal.Decimal.from_float()