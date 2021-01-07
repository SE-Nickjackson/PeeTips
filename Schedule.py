'''
@date:2021/1/7 16:01
@author: nick_jackson
@description: 定时任务类
'''

from apscheduler.schedulers.blocking import BlockingScheduler

from Tools import Tools
import tkinter_windows


class Schedule():
    def __int__(self):
        print("创建定时任务类")
        self.tools = None
        self.windows = None
        self.scheduler = None

    #初始化变量
    def init(self):
        self.tools = Tools()
        self.windows = tkinter_windows.Windows()
        self.scheduler = BlockingScheduler()

    # 启动定时任务
    def schedule_task(self):
        self.count_down_tip()
        self.scheduler.add_job(self.count_down_tip, 'cron', day_of_week='0-6', hour=20, minute=37)

        self.scheduler.start()


    # 定时任务函数
    def count_down_tip(self):
        now, days, hours = self.tools.calculate()
        output = "现在时间：" + str(now) + "r/n距离22考研还有" + str(days) + "天"
        self.windows.alertTip(output)
