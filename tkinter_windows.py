'''
@date:2021/1/7 17:50
@author: nick_jackson
@description: 窗口类
'''
import tkinter
from tkinter import messagebox


class Windows:
    # 初始化操作
    def __init__(self):
        print("创建tkinter窗口类")
        pass

    # 提示函数
    def alertTip(self, msg):
        tk = tkinter.Tk()
        tk.withdraw()
        messagebox.showinfo('tip', msg)
        tk.destroy()

    # 提示错误函数
    def alertError(self, msg):
        tk = tkinter.Tk()
        tk.withdraw()
        messagebox.showinfo('error', msg)
        tk.destroy()




if __name__=="__main__":
    win = Windows()
    win.alertTip('正在练习')