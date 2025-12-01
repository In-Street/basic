import  re

#匹配年月日
p1 = re.compile(r'\d{4}-\d{1,2}-\d+')
print(p1.match('2025-1-13'))

# () 进行分组
p2 = re.compile(r'(\d{4})-(\d+)-(\d+)')
print(p2.match('2025-01-13').group(1))  # 2025

# groups 返回分组结果： ('2025', '01', '13')
year,month,day = p2.match('2025-01-13').groups()
print(month) # 直接返回月份
