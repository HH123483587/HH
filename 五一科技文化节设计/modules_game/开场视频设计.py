''' -*- encoding: utf-8 -*-
 @ModuleName: 主页面设计
 @Function
 @Author : JustDoIt2050
 @Time : 2024-04-21 20:07
 '''
import sys
from tkinter import  *
from PIL import  Image
from PIL import  ImageTk
import cv2
import pygame
def video():
 # 初始化 Pygame
 pygame.init()

 # 设置 Pygame 音频模块
 pygame.mixer.init()

 # 创建 Tkinter 窗口
 root = Tk()
 root.title("开场视频")

 # 创建一个用于显示视频的画布
 canvas = Canvas(root, width=1000, height=800)
 canvas.pack()

 # 打开视频文件
 video = cv2.VideoCapture("../开场视频.mp4")

 # 打开音频文件
 audio_file = "../跳过版开场视频.mp3"
 pygame.mixer.music.load(audio_file)

 # 播放音频
 pygame.mixer.music.play()

 # 循环播放视频
 while True:
     # 读取视频帧
     ret, frame = video.read()

     # 如果视频结束，跳出循环
     if not ret:
         break

     # 将视频帧显示在画布上
     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # OpenCV 读取的图像是 BGR 格式的，需要转换为 RGB 格式
     frame = cv2.resize(frame, (1000, 800))  # 调整视频帧的大小以适应画布
     photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
     canvas.create_image(0, 0, image=photo, anchor=NW)
     root.update()

     # 等待一段时间，保持视频播放的速度
     cv2.waitKey(1)

 # 释放资源
 video.release()
 pygame.mixer.music.stop()
 cv2.destroyAllWindows()
 root.mainloop()

