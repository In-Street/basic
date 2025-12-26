import time

time.time()  # 时间戳

# localtime() :  time.struct_time(tm_year=2025, tm_mon=11, tm_mday=22, tm_hour=11, tm_min=39, tm_sec=22, tm_wday=5, tm_yday=326, tm_isdst=0)
print(time.localtime())
print(time.localtime().tm_mon)  # 月份： 11

# 格式化
time_strftime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
print(time_strftime)

from datetime import datetime,timedelta,date

# now = datetime.datetime.now().timestamp()
now = datetime.now()
print(now)  # 2025-11-22 11:45:51.258691

# timedelta: 获取20分钟后的时间
datetime_timedelta = timedelta(minutes=20)
now_plus = datetime.now() + datetime_timedelta
print(now_plus)


# 指定时间
print(datetime(2015,1,15,14,10,20))

# 指定时区
import pytz
print(f'指定时区：{datetime.now(pytz.timezone('America/New_York'))}')
print(f'指定时区：{datetime.now().astimezone(pytz.timezone('America/New_York'))}')


print(datetime.now().strftime('%Y年%m月%d日 %H:%M:%S'))

print(datetime.strptime('2025年12月26日','%Y年%m月%d日').date())