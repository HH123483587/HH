import pygame
import sys
import os
import time

current_dir = os.path.dirname(__file__)
class Bird(object):
    def __init__(self):
        '''小鸟的矩形有四个参数，前两个为小鸟左上角的坐标，后两个为矩形的长宽'''
        self.birdRect = pygame.Rect(65, 50, 50, 50)
        '''定义鸟的状态图片'''
        self.birdStatus = [pygame.image.load(current_dir+'\\image\\up.png'),
                           pygame.image.load(current_dir+'\\image\\down.png'),
                           pygame.image.load(current_dir+'\\image\\dead.png')]
        '''默认飞行状态'''
        self.status = 0
        '''鸟所在X轴，即向右飞行的速度'''
        self.birdX = 120
        '''鸟所在Y轴，即上下飞行的高度'''
        self.birdY = 350
        '''默认鸟为下降'''
        self.jump = False
        '''跳跃高度'''
        self.jumpSpeed = 10
        '''重力，即下降速度'''
        self.gravity = 2
        '''默认鸟的状态为活着'''
        self.dead = False

    def birdUpdate(self):
        '''鸟跳跃'''
        if self.jump:
            '''速度递减，上升越来越慢'''
            self.jumpSpeed -= 1
            '''鸟Y轴坐标减小，实现鸟上升'''
            self.birdY -= self.jumpSpeed

        else:
            '''鸟下降'''
            '''重力递增，下降越来越快'''
            self.gravity += 0.01
            '''鸟Y轴坐标增加，实现鸟下降'''
            self.birdY += self.gravity
        '''更改鸟的Y轴坐标'''
        self.birdRect[1] = self.birdY


class Pipeline(object):
    '''定义管道类'''

    def __init__(self):
        '''管道X轴坐标，在地图最右侧'''
        self.wallx = 400
        '''加载上管道图片'''
        self.pineUp = pygame.image.load(current_dir+'\\image\\shang_guandao.png')
        '''加载下管道图片'''
        self.pineDown = pygame.image.load(current_dir+'\\image\\xia_guandao.png')

    def updatePipeline(self):
        '''管道移动方法'''
        '''管道X轴递减，即向左移动'''
        self.wallx -= 5
        '''管道宽度为94，当管道快移除屏幕外时重置管道位置'''
        if self.wallx < -80:
            '''声明全局变量，设置得分并加一'''
            global score
            score += 1
            self.wallx = 400


def birds_fly():
    def createMap():
        '''定义创建地图方法'''
        screen.fill((255, 255, 255))  # 填充颜色
        screen.blit(background, (0, 0))  # 填入到背景
        # 显示管道
        # 因为管道长度为495几乎占满屏幕了，为了让管道小一点设置为屏幕外的上下方
        screen.blit(pipeline.pineUp, (pipeline.wallx, -300))  # 上管道坐标位置
        screen.blit(pipeline.pineDown, (pipeline.wallx, 500))  # 下管道坐标位置
        pipeline.updatePipeline()  # 管道移动
        if bird.dead:  # 撞管道
            bird.status = 2
        elif bird.jump:  # 起飞状态
            bird.status = 1
        '''设置鸟的状态和坐标'''
        screen.blit(bird.birdStatus[bird.status], (bird.birdX, bird.birdY))
        '''鸟移动'''
        bird.birdUpdate()
        # 显示分数
        # font.render（）用于显示字体有三个参数：字符串、是否平滑、颜色
        screen.blit(font.render(str(score), -1, (255, 255, 255)), (200, 50))  # 设置字体颜色及坐标位置
        pygame.display.update()  # 更新显示

    def checkDead():
        '''上管道矩形位置'''
        upRect = pygame.Rect(pipeline.wallx, -300,
                             pipeline.pineUp.get_width() - 10,
                             pipeline.pineUp.get_height())
        '''下管道矩形位置'''
        downRect = pygame.Rect(pipeline.wallx, 500,
                               pipeline.pineDown.get_width() - 10,
                               pipeline.pineDown.get_height())
        '''碰撞检测'''
        if upRect.colliderect(bird.birdRect) or downRect.colliderect(bird.birdRect):
            bird.dead = True
        '''检测鸟是否飞出上下边界'''
        if not 0 < bird.birdRect[1] < height:
            bird.dead = True
            return True
        else:
            return False

    def getResult1():
        final_text1 = 'Game Over'
        final_text2 = 'Your Final Score Is:' + str(score)
        ft1_font = pygame.font.SysFont('Arial', 70)  # 设置第一行文字字体
        ft1_surf = font.render(final_text1, 1, (242, 3, 36))  # 设置第一行文字颜色
        ft2_font = pygame.font.SysFont('Arial', 50)  # 设置第二行文字字体
        ft2_surf = font.render(final_text2, 1, (253, 177, 6))  # 设置第二行文字颜色
        screen.blit(ft1_surf, [screen.get_width() / 2 - ft1_surf.get_width() / 2, 100])  # 设置第一
        screen.blit(ft2_surf, [screen.get_width() / 2 - ft2_surf.get_width() / 2, 200])  # 设置第二
        pygame.display.flip()  # 更新整个待显示的Surface对象到屏幕上

    '''主程序'''
    pygame.init()  # 初始化pygame
    pygame.font.init()  # 初始化字体
    '''设置字体大小'''
    font = pygame.font.SysFont('Arila', 50)
    '''显示窗口'''
    pygame.display.set_caption('笨鸟先飞')
    size = width, height = 400, 680
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()  # 设置时钟
    '''实例化类'''
    pipeline = Pipeline()
    bird = Bird()
    global score
    score = 0
    running = True
    while running:
        clock.tick(60)  # 每秒执行60次
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        '''如果触发键盘和鼠标事件并且小鸟状态不是死亡,则Bird.jump值为True并且初始化跳跃跟坠落速度'''
        if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not bird.dead:
             bird.jump = True
             bird.gravity = 2
             bird.jumpSpeed = 10
        '''绘制背景'''
        background = pygame.image.load(current_dir+'\\image\\background.png')
        if checkDead():  # 检测小鸟生命状态
            getResult1()  # 如果小鸟死亡，显示游戏总分数
            pygame.display.flip()
            time.sleep(1)
            pygame.quit()
        else:
            createMap()  # 创建地图

def birds_start():
    if __name__ == '__main__':
        birds_fly()

birds_start()
