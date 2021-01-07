'''
@date:2021/1/7 16:01
@author: nick_jackson
@description: 定时任务类
'''

from apscheduler.schedulers.blocking import BlockingScheduler

from Tools import Tools
from Speaker import Speaker
from tkinter_windows import Windows


class Schedule():
    def __int__(self):
        print("创建定时任务类")
        self.tools = None
        self.windows = None
        self.scheduler = None
        self.speaker = None

    #初始化变量
    def init(self):
        self.tools = Tools()
        self.windows = Windows()
        self.scheduler = BlockingScheduler()
        self.speaker = Speaker()

    # 启动定时任务
    def schedule_task(self):
        self.count_down_tip()
        self.scheduler.add_job(self.count_down_tip, 'cron', day_of_week='0-6', hour=20, minute=35)
        self.scheduler.add_job(self.wake_up, 'cron', day_of_week='0-6', hour=21, minute=35)


        self.scheduler.start()


    # 定时任务函数
    def count_down_tip(self):
        now, days, hours = self.tools.calculate()
        output = "现在时间：" + str(now) + "\r\n距离22考研还有" + str(days) + "天\r\n"
        self.windows.alertTip(output)

    def wake_up(self):
        i = 3
        while i > 0:
            i -= 1
            self.speaker.speak("It's time to sleep, Nick Jackson!")
        self.speaker.speak("Let's go to bed, It's necessary to say something important three times")

