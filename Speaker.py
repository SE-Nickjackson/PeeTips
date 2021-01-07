'''
@date:2021/1/7 21:14
@author: nick_jackson
@description: 语音功能类
'''
import win32com.client

class Speaker:
    def __init__(self):
        pass

    # 语音读出语句
    def speak(self, sth):
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        speaker.Speak(sth)

if __name__=="__main__":
    speaker = Speaker()
    speaker.speak("")
    

