import os

from apscheduler.schedulers.blocking import BlockingScheduler

from Tools import Tools


class Windows:
    pass


if __name__ == '__main__':
    os.environ['TZ'] = 'Asia/Shanghai'
    tools = Tools()
    print("开始")
    scheduler = BlockingScheduler()
    scheduler.add_job(tools.calculate, 'cron', day_of_week='0-6', hour=16, minute=37)
    scheduler.add_job(tools.shutDown, 'cron', day_of_week='0-6', hour=16, minute=37)
    scheduler.start()
