import calendar

# 打印某月的日历
cl = calendar.month(2025, 12)
print(cl)


#是否闰年
print(calendar.isleap(2025))

a,b = calendar.monthrange(2025, 12)
print(a)  # 2025年12月 的第一天是星期几。 星期一0～6星期日
print(b) # 2025年12月 总共有多少天

weekday = calendar.weekday(2025, 12, 24)
print(weekday)  # 返回给定日期的星期数，0～6  星期一～星期日
