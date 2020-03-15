### 使用time库
import time

### datetime字符串转换为时间戳
# datetime类型字符串
datetime = "2020-03-11 19:26:13"
# 先将str转换为时间元组
# time.strptime(str,fmt='...')根据fmt的格式把一个时间字符串str解析为时间元组。	
timetuple = time.strptime(datetime, "%Y-%m-%d %H:%M:%S") # time.struct_time(tm_year=2020, tm_mon=3, tm_mday=11, tm_hour=19, tm_min=26, tm_sec=13, tm_wday=2, tm_yday=71, tm_isdst=-1) <class 'time.struct_time'>
# 将时间元组转换成时间戳
# time.mktime()接受时间元组并返回时间戳（1970纪元后经过的浮点秒数）
timestamp = time.mktime(timetuple) # 1583925973.0 <class 'float'>

### 时间戳转换为datetime字符串
# float类型时间戳，小数点前10位
timestamp = time.time() # 1584278483.256262 <class 'float'>
# 时间戳转换为时间元组
# time.localtime([secs])接收时间戳（1970纪元后经过的浮点秒数），返回当地时间下的时间元组t
timetuple = time.localtime(timestamp) # time.struct_time(tm_year=2020, tm_mon=3, tm_mday=15, tm_hour=21, tm_min=21, tm_sec=23, tm_wday=6, tm_yday=75, tm_isdst=0) <class 'time.struct_time'>
# 时间元组转为datetime字符串
# time.strftime(fmt[,tupletime])接收时间元组，返回以可读字符串表示的当地时间，格式由fmt决定。
datetime = time.strftime("%Y-%m-%d %H:%M:%S", timetuple) # 2020-03-15 21:21:23 <class 'str'>

import datetime
### 使用datetime库显示datetime字符串
# 时间戳转为datetime字符串格式
timeStamp = time.time() # 1584278312.2667465 <class 'float'>
dateArray = datetime.datetime.fromtimestamp(timeStamp) # 2020-03-15 21:18:32.266747 <class 'datetime.datetime'>
# datetime.datetime.strftime()方法接收日期格式返回该格式字符串
otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S") # 2020-03-15 21:18:32 <class 'str'>

# datetime获取当前时间，转为字符串格式
now = datetime.datetime.now() # 2020-03-15 20:58:00.147842 <class 'datetime.datetime'>
otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S") # 2020-03-15 20:58:00 <class 'str'>

### python中时间日期格式化符号：
# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称
# %% %号本身

### struct_time时间元组格式
# tm_year: 公历年
# tm_mon: 月，1-12
# tm_mday: 日，1-31
# tm_hour: 时，0-23
# tm_min: 分，0-59
# tm_sec: 秒，0-61 (60或61 是闰秒)
# tm_wday: 星期，0-6 (0是周一)
# tm_yday: 一年中的第几天，1-366
# tm_isdst: 是否为夏令时，值有：1(夏令时)、0(不是夏令时)、-1(未知)，默认-1
