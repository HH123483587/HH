''' -*- encoding: utf-8 -*-
 @ModuleName: test
 @Function
 @Author : JustDoIt2050
 @Time : 2024-04-23 19:48
 '''
from tkinter import *
from PIL import  ImageTk
def blank():
    pass
def give_label_with_picture(master, image) -> Label:
    """ 给一个包含图片的 Label，可以直接布局 """
    photo = ImageTk.PhotoImage(file=image)
    lab = Label(master)
    lab.config(image=photo)
    lab.image = photo
    return lab

root=Tk()
ce=give_label_with_picture(root, '0034034892281415_b.jpg').place(x=10,y=10)
l1=Label(text=ce)
root.mainloop()