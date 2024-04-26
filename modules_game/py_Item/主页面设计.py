''' -*- encoding: utf-8 -*-
 @ModuleName: 主页面设计
 @Function
 @Author : JustDoIt2050
 @Time : 2024-04-21 21:16
 '''
import tkinter
# from tkinter import *
# from PIL import Image, ImageTk
from Snakes import *
from Snakes import Snake_main
import pygame.mixer
from big_eats_small import main
from birds_fly import birds_fly
from Russia_block import tetris_start


current_dir = os.getcwd()
current_dir = os.path.dirname(current_dir)


def give_label_with_picture(master, image) -> Label:
    """ 给一个包含图片的 Label，可以直接布局 """
    image = Image.open(image)
    new_width = 300
    new_height = 180
    resize_image = image.resize((new_width, new_height))
    resize_image.save(current_dir + "\\resized_image.png")
    #
    photo = ImageTk.PhotoImage(file=current_dir + "\\resized_image.png")
    lab = Label(master)
    lab.config(image=photo)
    lab.image = photo
    return lab


def get_image(filename, width, height):
    im = Image.open(filename).resize((width, height))
    return ImageTk.PhotoImage(im)


pygame.mixer.init()
pygame.mixer.music.load(current_dir + '\\backgroundmusic.mp3')
pygame.mixer.music.play(-1)
maintask = Tk()
maintask.title("主界面")
maintask.geometry('800x500')  # 设置根
# 本窗口整体大小
canvas_maintask = tkinter.Canvas(maintask, width=1000, height=800)  # 不知道？
photo = get_image(current_dir + "\\All_image\\bg.png", 1000, 800)
canvas_maintask.create_image(400, 150, image=photo)  # 设置相应位置
canvas_maintask.pack()
l1 = give_label_with_picture(maintask, current_dir+"\\All_image\\snake\\游戏概览图.png").place(x=50, y=10)
l2 = Button(maintask, text='贪吃蛇', command=Snake_main).place(x=160, y=200)

l3=give_label_with_picture(maintask,current_dir+"\\All_image\\big_eat_small.png").place(x=430,y=10)
l4 = Button(maintask, text='大球吃小球', command=main).place(x=530, y=200)

l5 = give_label_with_picture(maintask,current_dir+"\\All_image\\birds_fly.png").place(x=50,y=260)
l6 = Button(maintask, text='笨鸟先飞', command=birds_fly).place(x=160, y=450)

l7 = give_label_with_picture(maintask,current_dir+"\\All_image\\Russia_block.png").place(x=430,y=260)
l8 = Button(maintask, text='俄罗斯方块', command=tetris_start).place(x=530, y=450)

maintask.mainloop()
