import os
from datetime import datetime
import time
from tzlocal import get_localzone
import pytz


class Tools:

    # 创建工具类
    def __init__(self):
        print("创建工具类")

    # 计算天数
    def calculate(self):
        # Python实现天数倒计时计算
        # tips：在datetime模块里有一个计算时间差的 timedelta。
        # 让两个datetime对象相减就得到timedelta
        # 构造一个将来的时间
        future = datetime.strptime('2021-12-26 00:00:00', '%Y-%m-%d %H:%M:%S')
        # 当前时间
        now = datetime.now()
        # 求时间差
        delta = future - now
        hour = delta.seconds / 60 / 60
        minute = (delta.seconds - hour * 60 * 60) / 60
        seconds = delta.seconds - hour * 60 * 60 - minute * 60
        print_now = now.strftime('%Y-%m-%d %H:%M:%S')
        print("今天是：", print_now)
        print("距离 2021-12-26 \"考研\" 还剩下：%d天" % delta.days)
        print(delta.days, hour, minute, seconds)
        return print_now, delta.days, hour

    # 获取时区
    def get_correct_localzone(self):
        try:
            return get_localzone()
        except pytz.UnknownTimeZoneError:
            return pytz.timezone("Asia/Shanghai")

    def job(self):
        print("hello world!")

    # 关机
    def shutDown(self):
        print("时间已到，将在5秒后自动关机")
        os.system('shutdown -s -t 5')
