'''
@date:2021/1/7 20:55
@author: nick_jackson
@description: 音乐播放器类
'''
import mp3
import pygame
import time
class MP3Player:
    def __init__(self):
        pass

    #播放mp3音乐
    def play_mp3(self, path):
        pygame.mixer.init()  # 初始化
        track = pygame.mixer.music.load(path)  # 加载音乐
        pygame.mixer.music.play()  # 播放

        userIn = input()  # 输入空格暂停
        if userIn == ' ':
            pygame.mixer.music.pause()
        else:
            time.sleep(207)  # 表示音频的长度
        pygame.mixer.music.stop()


if __name__=="__main__":
    mp3 = MP3Player()
    mp3.play_mp3('mp3/wuding.mp3')