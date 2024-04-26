import pygame
import sys
import random
from math import sqrt
import time
import os

current_dir = os.getcwd()
current_dir = os.path.dirname(current_dir)

class Color():
    @staticmethod
    def color_random():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return (r, g, b)


class Ball(object):
    def __init__(self, x, y, r, sx, sy, color):
        self.x = x
        self.y = y
        self.r = r
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True

    def move(self, screen):
        self.x += self.sx
        self.y += self.sy
        if self.x - self.r <= 0 \
                or self.x + self.r >= screen.get_width():
            self.sx = -self.sx
        if self.y - self.r <= 0 \
                or self.y + self.r >= screen.get_height():
            self.sy = -self.sy

    def eat(self, other):
        if self.alive and other.alive and self != other:
            '''计算两个球之间的直线距离'''
            dx, dy = self.x - other.x, self.y - other.y
            distance = sqrt(dx ** 2 + dy ** 2)
            if distance < (self.r + other.r) and self.r > other.r:
                other.alive = False
                self.r = self.r + int(other.r * 0.2)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color,
                           (self.x, self.y), self.r, 0)


def main():
    li_balls = []
    pygame.init()
    screen1 = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('大球吃小球')

    red = pygame.Color(255, 0, 0)

    running = True
    start = False

    '''随机生成球，并加入列表'''

    def randon_ball():
        color = Color.color_random()
        x, y = random.randint(20, 780), random.randint(20, 580)
        r = random.randint(5, 30)
        sx, sy = random.randint(-10, 10), random.randint(-10, 10)
        ball = Ball(x, y, r, sx, sy, color)
        li_balls.append(ball)

    def show_socre(screen, score):
        pygame.font.init()
        score_font = pygame.font.SysFont('times new roman', 20)
        # 渲染字体
        score_surface = score_font.render('Score:' + str(score), True, red)
        # 为文本创建矩形坐标
        score_rect = (0, 0)
        # 绘制文本
        screen.blit(score_surface, score_rect)


    '''初始生成6个球'''

    for i in range(7):
        randon_ball()



    while running:
        is_died = False
        screen1.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                my_font = pygame.font.SysFont('times new roman', 50)
                game_over_surface = my_font.render('Game Over!', True, pygame.Color(255, 0, 0))
                game_over_rect = game_over_surface.get_rect()
                # 设置文本位置
                game_over_rect.midtop = (800 / 2, 600 / 2.5)
                # 绘制文本
                screen1.blit(game_over_surface, game_over_rect)

                pygame.display.flip()
                time.sleep(1)
                pygame.quit()
                pygame.mixer.init()
                pygame.mixer.music.load(current_dir + '\\backgroundmusic.mp3')
                pygame.mixer.music.play(-1)
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                color = Color.color_random()
                x, y = event.pos
                # r = random.randint(5, 30)
                r = 20
                sx, sy = 0, 0
                p_ball = Ball(x, y, r, sx, sy, color)
                start = True
        for ball in li_balls:
            if ball.alive:
                ball.draw(screen1)
            else:
                li_balls.remove(ball)

        pygame.display.flip()
        while start:

            screen2 = pygame.display.set_mode((800, 600))
            screen2.fill((255, 255, 255))
            p_ball.draw(screen2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    start = False
                    # running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        p_ball.sy = -5
                        p_ball.sx = 0
                    if event.key == pygame.K_LEFT:
                        p_ball.sx = -5
                        p_ball.sy = 0
                    if event.key == pygame.K_RIGHT:
                        p_ball.sx = 5
                        p_ball.sy = 0
                    if event.key == pygame.K_DOWN:
                        p_ball.sy = 5
                        p_ball.sx = 0
                    if event.key == pygame.K_KP9:
                        p_ball.sy = -5
                        p_ball.sx = 5
                    if event.key == pygame.K_KP7:
                        p_ball.sy = -5
                        p_ball.sx = -5
                    if event.key == pygame.K_KP3:
                        p_ball.sy = 5
                        p_ball.sx = 5
                    if event.key == pygame.K_KP1:
                        p_ball.sy = 5
                        p_ball.sx = -5
            p_ball.move(screen2)

            for ball in li_balls:
                if ball.alive:
                    ball.draw(screen2)
                else:
                    li_balls.remove(ball)

            show_socre(screen2,p_ball.r)

            pygame.display.flip()
            pygame.time.delay(50)

            for ball in li_balls:
                ball.move(screen2)
                p_ball.eat(ball)
                for other in li_balls:
                    ball.eat(other)
                    ball.eat(p_ball)
            # for eat_ball in li_balls:
            #     p_ball.eat(eat_ball)
            '''角色死亡'''
            if p_ball.alive == False:
                # print('Game Over!')
                start = False
                is_died = True
            '''补充球'''
            if len(li_balls) < 7:
                randon_ball()
            if p_ball.r >= 200:
                my_font = pygame.font.SysFont('times new roman', 50)
                game_over_surface = my_font.render('You win', True, pygame.Color(255, 0, 0))
                game_over_rect = game_over_surface.get_rect()
                # 设置文本位置
                game_over_rect.midtop = (800 / 2, 600 / 2.5)
                # 绘制文本
                screen1.blit(game_over_surface, game_over_rect)

                score_surface = my_font.render('You Score Is:' + str(p_ball.r), True, pygame.Color(255, 0, 0))
                score_surface_rect = game_over_surface.get_rect()
                # 设置文本位置
                score_surface_rect.midtop = (800 / 2.25, 600 / 2)
                # 绘制文本
                screen1.blit(score_surface, score_surface_rect)

                pygame.display.flip()
                time.sleep(1)
                pygame.quit()
                pygame.mixer.init()
                pygame.mixer.music.load(current_dir + '\\backgroundmusic.mp3')
                pygame.mixer.music.play(-1)
                start = False
                running = False
        if start == False and is_died == True:
            my_font = pygame.font.SysFont('times new roman', 50)
            game_over_surface = my_font.render('Game Over!', True, pygame.Color(255, 0, 0))
            game_over_rect = game_over_surface.get_rect()
            # 设置文本位置
            game_over_rect.midtop = (800 / 2, 600 / 2.5)
            # 绘制文本
            screen1.blit(game_over_surface, game_over_rect)

            score_surface = my_font.render('You Score Is:' + str(p_ball.r), True, pygame.Color(255, 0, 0))
            score_surface_rect = game_over_surface.get_rect()
            # 设置文本位置
            score_surface_rect.midtop = (800 / 2.25, 600 / 2)
            # 绘制文本
            screen1.blit(score_surface, score_surface_rect)

            pygame.display.flip()
            time.sleep(1)
            pygame.quit()
            pygame.mixer.init()
            pygame.mixer.music.load(current_dir + '\\backgroundmusic.mp3')
            pygame.mixer.music.play(-1)
            running = False






# if __name__ == '__main__':
#  main()