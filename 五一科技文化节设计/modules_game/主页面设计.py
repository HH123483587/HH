''' -*- encoding: utf-8 -*-
 @ModuleName: 主页面设计
 @Function
 @Author : JustDoIt2050
 @Time : 2024-04-21 21:16
 '''
import tkinter
from tkinter import *
from PIL import Image,ImageTk
from Gluttonous_snake import *
from Gluttonous_snake.Snakes import Snake, Snake_main
import pygame.mixer
from 大球吃小球.big_eats_small import main
from 笨鸟先飞.birds_fly import birds_fly
# from modules_game.开场视频设计 import video
from 俄罗斯方块.Russia_block import tetris_start

# from 扫雷.minesweeper import emain


def give_label_with_picture(master, image) -> Label:
    """ 给一个包含图片的 Label，可以直接布局 """
    image=Image.open(image)
    new_width=50
    new_height=50
    resize_image=image.resize((new_width,new_height))
    resize_image.save("resized_image.jpg")

    photo = ImageTk.PhotoImage(file="resized_image.jpg")
    lab = Label(master)
    lab.config(image=photo)
    lab.image = photo
    return lab


def get_image(filename,width,height):
    im=Image.open(filename).resize((width,height))
    return ImageTk.PhotoImage(im)

pygame.mixer.init()
pygame.mixer.music.load('backgroundmusic.mp3')
pygame.mixer.music.play(-1)
maintask=Tk()
maintask.title("主界面")
maintask.geometry('800x500')  #设置根
# 本窗口整体大小
canvas_maintask=tkinter.Canvas(maintask,width=1000,height=800)  #不知道？
photo=get_image("Gluttonous_snake/试验品.png", 1000, 800)
canvas_maintask.create_image(400,150,image=photo)   #设置相应位置
canvas_maintask.pack()
l1=give_label_with_picture(maintask,"0034034892281415_b.jpg").place(x=10,y=10)
l2=Button(maintask,text='第一关',command=Snake_main).place(x=10,y=80)
l3=Label(maintask,text='第二关').place(x=200,y=10)
l4=Button(maintask,text='第二关',command=main).place(x=200,y=50)
l5=Label(maintask,text='第三关').place(x=400,y=10)
l6=Button(maintask,text='第三关',command=birds_fly).place(x=400,y=50)
l7=Label(maintask,text='第四关').place(x=600,y=10)
l8=Button(maintask,text='第四关',command=tetris_start).place(x=600,y=50)
# l9=Label(maintask,text='第五关').place(x=10,y=200)
# l10=Button(maintask,text='第五关',command=emain).place(x=10,y=250)
maintask.mainloop()
