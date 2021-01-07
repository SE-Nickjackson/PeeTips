import os

from apscheduler.schedulers.blocking import BlockingScheduler

from Tools import Tools
from Schedule import Schedule




if __name__ == '__main__':
    m = Schedule()
    m.init()
    m.schedule_task()

