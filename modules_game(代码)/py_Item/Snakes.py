import pygame
import random
import time
import sys
from tkinter import *
from PIL import Image,ImageTk
import os

'''蛇类'''

current_dir = os.getcwd()
current_dir = os.path.dirname(current_dir)
class Snake(object):

    def __init__(self, snake_speed):
        self.snake_speed = snake_speed
        self.snake_head = pygame.image.load(current_dir+'\\All_image\\snake\\snake_head.jpg')
        self.snake_position = [100, 40]
        self.snake_body = [[100, 40],
                           [80, 40],
                           [60, 40],
                           [40, 40]]
        self.snake_body1 = pygame.image.load(current_dir+'\\All_image\\snake\\贪吃蛇图\\杭.png')
        self.snake_body2 = pygame.image.load(current_dir+'\\All_image\\snake\\贪吃蛇图\\州.png')
        self.snake_body3 = pygame.image.load(current_dir+'\\All_image\\snake\\贪吃蛇图\\科.png')
        self.snake_body4 = pygame.image.load(current_dir+'\\All_image\\snake\\贪吃蛇图\\技.png')
        self.snake_body5 = pygame.image.load(current_dir+'\\All_image\\snake\\贪吃蛇图\\职.png')
        self.snake_body6 = pygame.image.load(current_dir+'\\All_image\\snake\\贪吃蛇图\\业.png')
        self.snake_body7 = pygame.image.load(current_dir+'\\All_image\\snake\\贪吃蛇图\\技.png')
        self.snake_body8 = pygame.image.load(current_dir+'\\All_image\\snake\\贪吃蛇图\\术.png')
        self.snake_body9 = pygame.image.load(current_dir+'\\All_image\\snake\\贪吃蛇图\\学.png')
        self.snake_body10 =pygame.image.load(current_dir+'\\All_image\\snake\\贪吃蛇图\\院.png')
        self.snake_bodyli = [self.snake_body1, self.snake_body2, self.snake_body3, self.snake_body4, self.snake_body5, \
                             self.snake_body6, self.snake_body7, self.snake_body8, self.snake_body9, self.snake_body10]
        self.directon = 'Right'
        self.change_to = self.directon

    def snake_move(self):
        if self.directon == 'Right':
            self.snake_position[0] += 20
        if self.directon == 'Left':
            self.snake_position[0] -= 20
        if self.directon == 'Up':
            self.snake_position[1] -= 20
        if self.directon == 'Down':
            self.snake_position[1] += 20
        self.snake_body.insert(0, list(self.snake_position))


'''食物类'''


class Food(object):
    def __init__(self, window, food_color):
        self.food_position = [random.randint(1, (window[0] // 20) - 1) * 20,
                              random.randint(1, (window[1] // 20) - 1) * 20]
        self.food_spawn = True
        self.food_color = food_color
        self.food = pygame.image.load(current_dir+'\\All_image\\snake\\food.jpg')

    def creat_food(self, window):
        self.food_position = [random.randint(1, (window[0] // 20) - 1) * 20,
                              random.randint(1, (window[1] // 20) - 1) * 20]
        self.food_spawn = True


def read_score():
    with open(file=current_dir+'\\py_Item\\snake_score.txt', mode='a', encoding='utf8'):
        with open(file=current_dir+'\\py_Item\\snake_score.txt', mode='r', encoding='utf8') as f:
            info_data = f.readlines()  # 列表
    count = len(info_data)
    return count


def main(window_x, window_y, snake_speed, max_speed):
    # 创建颜色
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 0, 255)

    # 设置窗体参数
    window = [window_x, window_y]
    pygame.init()
    pygame.display.set_caption('贪吃蛇')
    screen = pygame.display.set_mode(window)
    fps = pygame.time.Clock()

    # 初始化分数
    score = 0
    count = read_score()

    '''显示分数函数'''

    def show_socre(color, speed):
        pygame.font.init()
        score_font = pygame.font.SysFont('times new roman', 20)
        # 渲染字体
        score_surface = score_font.render('Score:' + str(score), True, color)
        # 为文本创建矩形坐标
        score_rect = (0, 0)
        # 绘制文本
        screen.blit(score_surface, score_rect)

        # 分数显示
        speed_surface = score_font.render('Speed:' + str(speed), True, color)
        speed_rect = (0, 20)
        screen.blit(speed_surface, speed_rect)

    '''游戏结束函数'''

    def game_over():
        my_font = pygame.font.SysFont('times new roman', 50)
        game_over_surface = my_font.render('You Score Is:' + str(score), True, red)
        game_over_rect = game_over_surface.get_rect()
        # 设置文本位置
        game_over_rect.midtop = (window[0] / 2, window[1] / 2.5)
        # 绘制文本
        screen.blit(game_over_surface, game_over_rect)
        # 更新
        pygame.display.flip()
        # 延迟2秒
        time.sleep(1)
        # 退出pygame环境
        pygame.quit()
        pygame.mixer.init()
        pygame.mixer.music.load(current_dir+'\\All_image\\backgroundmusic.mp3')
        pygame.mixer.music.play(-1)

    def writ_score():
        over_time = time.localtime()  # 获取当地时间
        writ_time = time.strftime('%Y-%m-%d %H:%M:%S', over_time)  # 转换时间格式
        with open(file=current_dir+'\\py_Item\\snake_score.txt', encoding='utf8', mode='a') as f:
            f.write('第' + str(count) + '次:' + str(score) + '分      ' + str(writ_time) + '\n')

    # 实例化类
    snake = Snake(snake_speed)
    food = Food(window, green)
    # 游戏主循环
    while True:
        # 填充背景
        background = pygame.image.load(current_dir+'\\All_image\\snake\\bg.png')
        screen.blit(background, (0, 0))
        # 事件判断
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_to = 'Up'
                if event.key == pygame.K_DOWN:
                    snake.change_to = 'Down'
                if event.key == pygame.K_LEFT:
                    snake.change_to = 'Left'
                if event.key == pygame.K_RIGHT:
                    snake.change_to = 'Right'

        # 判断当前蛇的运动方向与用户移动方向是否冲突
        if snake.change_to == 'Up' and snake.directon != 'Down':
            snake.directon = 'Up'
        if snake.change_to == 'Down' and snake.directon != 'Up':
            snake.directon = 'Down'
        if snake.change_to == 'Left' and snake.directon != 'Right':
            snake.directon = 'Left'
        if snake.change_to == 'Right' and snake.directon != 'Left':
            snake.directon = 'Right'

        # 蛇移动方法
        snake.snake_move()

        # 吃到食物，正常插入snake_body列表并增加分数，否则删除snake_body列表最后一个
        if snake.snake_position[0] == food.food_position[0] and \
                snake.snake_position[1] == food.food_position[1]:
            score += 10
            food.food_spawn = False

            if snake.snake_speed < max_speed:
                if score % 50 == 0:
                    snake.snake_speed += 1
        else:
            snake.snake_body.pop()

        # 判断食物状态，创造食物
        if food.food_spawn == False:
            food.creat_food(window)

        # 绘制蛇
        for index, pos in enumerate(snake.snake_body):
            if index == 0:
                screen.blit(snake.snake_head, [pos[0], pos[1]])
            else:
                if index >= 11:
                    pygame.draw.rect(screen, blue, pygame.Rect(pos[0], pos[1], 20, 20))
                else:
                    screen.blit(snake.snake_bodyli[index-1], [pos[0], pos[1]])

        # 绘制食物
        screen.blit(food.food, food.food_position)

        # 判断蛇头碰到身体
        for block in snake.snake_body[1:]:
            if block[0] == snake.snake_position[0] and block[1] == snake.snake_position[1]:
                game_over()

        # 判断蛇头撞墙
        # 显示分数
        show_socre(red, snake.snake_speed)
        # 更新屏幕
        pygame.display.update()
        # 设置游戏帧率
        fps.tick(snake.snake_speed)
        if snake.snake_position[0] < 0 or snake.snake_position[0] > window[0] - 10:
            count += 1
            writ_score()
            game_over()
        if snake.snake_position[1] < 0 or snake.snake_position[1] > window[1] - 10:
            count += 1
            writ_score()
            game_over()




def get_image(filename,width,height):
    im=Image.open(filename).resize((width,height))
    return ImageTk.PhotoImage(im)


def Snake_main():
 Snakes_myWindow = Tk()
 Snakes_myWindow.title('贪吃蛇')
 Snakes_myWindow.geometry('350x250')
 l10 = Label(Snakes_myWindow, text='填写游戏参数，为空即使用括号内默认参数', fg='green')
 l10.grid(row=0, column=0, pady=5, columnspan=2)
 l1 = Label(Snakes_myWindow, text='窗体长x(800)：')
 l1.grid(row=1, column=0, padx=10, pady=10)
 e1 = Entry(Snakes_myWindow, justify='left', width=20, font=1)
 e1.grid(row=1, column=1, pady=10)

 l2 = Label(Snakes_myWindow, text='窗体宽y(600)：')
 l2.grid(row=2, column=0, padx=10, pady=10)
 e2 = Entry(Snakes_myWindow, justify='left', width=20, font=1)
 e2.grid(row=2, column=1, pady=10)

 l3 = Label(Snakes_myWindow, text='初始速度(15)：')
 l3.grid(row=3, column=0, padx=10, pady=10)
 e3 = Entry(Snakes_myWindow, justify='left', width=20, font=1)
 e3.grid(row=3, column=1, pady=10)

 l4 = Label(Snakes_myWindow, text='最高速度(20)：')
 l4.grid(row=4, column=0, padx=10, pady=10)
 e4 = Entry(Snakes_myWindow, justify='left', width=20, font=1)
 e4.grid(row=4, column=1, pady=10)

 b1 = Button(Snakes_myWindow, text='开始', width=10, height=1, command=lambda: start())
 b1.grid(row=5, column=0, columnspan=2)


 def start():
     if e1.get() == '':
         window_x = 800
     else:
         window_x = int(e1.get())

     if e2.get() == '':
         window_y = 600
     else:
         window_y = int(e2.get())

     if e3.get() == '':
         snake_speed = 15
     else:
         snake_speed = int(e3.get())

     if e4.get() == '':
         max_speed = 20
     else:
         max_speed = int(e4.get())
     Snakes_myWindow.destroy()
     main(window_x, window_y, snake_speed, max_speed)

 # 接口
 Snakes_myWindow.mainloop()
