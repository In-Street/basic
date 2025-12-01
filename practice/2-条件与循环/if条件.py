
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
year = 1993
print(chinese_zodiac[year%12])

year_input = int( input('请输入出生年份：') )  # 注意：控制台输入后为字符串，在下面进行取余运算时会报错，所以需要转换为 int
result = chinese_zodiac[year_input%12]
print(result)

if(result == '鸡'):
    print('用户。。。')
else: print('不知道')