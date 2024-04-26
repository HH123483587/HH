from tkinter import *
from tkinter import messagebox
import time
import random
import numpy as np


class BLOCK_1():
    '''
    “田”字形方块
    '''

    def __init__(self):
        self.BLOCK_LOCATION = [[[0, 0], [0, 1], [1, 0], [1, 1]]]
        self.BLOCK_COLOR = 'blue'
        self.BLOCK_NUM = 1


class BLOCK_2():
    '''
    “一”字型方块
    '''

    def __init__(self):
        self.BLOCK_LOCATION = [[[0, 0], [0, 1], [0, 2], [0, 3]],
                               [[-1, 0], [0, 0], [1, 0], [2, 0]]]
        self.BLOCK_COLOR = 'yellow'
        self.BLOCK_NUM = 2


class BLOCK_3():
    '''
    反“Z”字型方块
    '''

    def __init__(self):
        self.BLOCK_LOCATION = [[[0, 0], [0, 1], [1, 0], [-1, 1]],
                               [[0, 1], [0, 2], [-1, 0], [-1, 1]]]
        self.BLOCK_COLOR = 'pink'
        self.BLOCK_NUM = 3


class BLOCK_4():
    '''
    “L”字型方块
    '''

    def __init__(self):
        self.BLOCK_LOCATION = [[[0, 0], [0, 1], [0, 2], [1, 2]],
                               [[-1, 0], [-1, 1], [0, 0], [1, 0]],
                               [[1, 0], [1, 1], [1, 2], [0, 0]],
                               [[1, 0], [1, 1], [0, 1], [-1, 1]]]
        self.BLOCK_COLOR = 'green'
        self.BLOCK_NUM = 4


class BLOCK_5():
    '''
    “Z”字型方块
    '''

    def __init__(self):
        self.BLOCK_LOCATION = [[[0, 0], [0, 1], [1, 1], [-1, 0]],
                               [[0, 0], [0, 1], [-1, 1], [-1, 2]]]
        self.BLOCK_COLOR = 'purple'
        self.BLOCK_NUM = 5


class BLOCK_6():
    '''
    反“L”字型方块
    '''

    def __init__(self):
        self.BLOCK_LOCATION = [[[0, 0], [0, 1], [0, 2], [-1, 2]],
                               [[-1, 0], [-1, 1], [0, 1], [1, 1]],
                               [[-1, 0], [-1, 1], [-1, 2], [0, 0]],
                               [[-1, 0], [0, 0], [1, 0], [1, 1]]]
        self.BLOCK_COLOR = 'orange'
        self.BLOCK_NUM = 6


class BLOCK_7():
    '''
    “T”字型方块
    '''

    def __init__(self):
        self.BLOCK_LOCATION = [[[0, 0], [0, 1], [0, 2], [-1, 1]],
                               [[0, 0], [0, 1], [1, 1], [-1, 1]],
                               [[0, 0], [0, 1], [1, 1], [0, 2]],
                               [[-1, 1], [0, 1], [1, 1], [0, 2]]]
        self.BLOCK_COLOR = 'white'
        self.BLOCK_NUM = 7


class Tetris():
    def __init__(self):
        self.width = 360  # 界面宽度
        self.height = 700  # 界面高度
        self.grid_size = 30  # 单格子边长
        self.row_num = 20  # 行数
        self.col_num = 12  # 列数

        self.speed = 500  # 格子下降速度
        self.total_score = 0  # 总分数

        self.inner_row_num = self.row_num - 2  # 内部格子空间行数
        self.inner_col_num = self.col_num - 2  # 内部格子空间列数

        self.grid = np.full((self.row_num, self.col_num), 0)  # 记录格子空间的矩阵
        self.grid_init()

        self.BLOCK_1 = BLOCK_1()
        self.BLOCK_2 = BLOCK_2()
        self.BLOCK_3 = BLOCK_3()
        self.BLOCK_4 = BLOCK_4()
        self.BLOCK_5 = BLOCK_5()
        self.BLOCK_6 = BLOCK_6()
        self.BLOCK_7 = BLOCK_7()
        self.block_list = [self.BLOCK_1, self.BLOCK_2, self.BLOCK_3, self.BLOCK_4, self.BLOCK_5, self.BLOCK_6,
                           self.BLOCK_7]
        self.color_dic = {1: self.BLOCK_1.BLOCK_COLOR, 2: self.BLOCK_2.BLOCK_COLOR, 3: self.BLOCK_3.BLOCK_COLOR,
                          4: self.BLOCK_4.BLOCK_COLOR, 5: self.BLOCK_5.BLOCK_COLOR, 6: self.BLOCK_6.BLOCK_COLOR,
                          7: self.BLOCK_7.BLOCK_COLOR, 0: 'black', -1: 'grey'}  # 颜色对照表

        self.tk = Tk()
        self.tk.title('俄罗斯方块')
        self.tk.geometry(f'{self.width}x{self.height}')

        self.canvas = Canvas(self.tk, width=self.width, height=self.height, background='#FFFFFF')
        self.canvas.pack()
        self.canvas.focus_set()  # 聚焦
        self.canvas.bind("<KeyPress-Left>", self.move)
        self.canvas.bind("<KeyPress-Right>", self.move)
        self.canvas.bind("<KeyPress-Down>", self.move)
        self.canvas.bind("<KeyPress-Up>", self.block_change)

        self.draw_grid()

        self.start_game()
        self.tk.mainloop()

    def grid_init(self):
        # 墙体赋值
        for i in range(0, self.row_num):
            self.grid[i][0] = -1
            self.grid[i][self.col_num - 1] = -1
        for i in range(0, self.col_num):
            self.grid[0][i] = -1
            self.grid[self.row_num - 1][i] = -1

    def draw_grid(self):
        # 画格子
        for i in range(0, self.row_num):
            for j in range(0, self.col_num):
                self.canvas.create_rectangle(j * self.grid_size + 2, i * self.grid_size + 2,
                                             (j + 1) * self.grid_size - 2, (i + 1) * self.grid_size - 2,
                                             fill=self.color_dic[self.grid[i][j]])
        self.label_text = StringVar()
        self.label_text.set('当前分数：' + str(self.total_score))
        self.label_score = Label(self.tk, textvariable=self.label_text, font=('宋体', 20), foreground='#000000',
                                 background='#FFFFFF').place_configure(x=70, y=620)

    def block_change(self, event):
        # 方块变形
        tmp_change_num = self.change_num + 1
        tmp_choose_one = tmp_change_num % len(self.this_block.BLOCK_LOCATION)
        tmp_block_location = [[i[0] + self.block_col_offset, i[1] + self.block_row_offset] for i in
                              self.this_block.BLOCK_LOCATION[tmp_choose_one]]
        for i in tmp_block_location:
            if self.grid[i[1], i[0]] != 0 and i not in self.this_block_location:
                return

        self.change_num += 1
        self.choose_one = self.change_num % len(self.this_block.BLOCK_LOCATION)
        for i in self.this_block_location:
            self.grid[i[1], i[0]] = 0
        self.this_block_location = [[i[0] + self.block_col_offset, i[1] + self.block_row_offset] for i in
                                    self.this_block.BLOCK_LOCATION[self.choose_one]]
        self.canvas.delete('all')

        for i in self.this_block_location:
            self.grid[i[1], i[0]] = self.this_block.BLOCK_NUM

        self.draw_grid()

    def get_random_block(self):
        # 获取随机的格子，开始下落
        self.this_block = self.block_list[random.randint(0, len(self.block_list) - 1)]
        self.block_col_offset = 5
        self.block_row_offset = 1
        self.choose_one = 0
        self.this_block_location = [[i[0] + self.block_col_offset, i[1] + self.block_row_offset] for i in
                                    self.this_block.BLOCK_LOCATION[self.choose_one]]
        self.start_judge = True
        self.change_num = 0
        if self.if_game_end():
            messagebox.showinfo('提示', '游戏结束')
            self.tk.destroy()

    def move(self, event):
        # 键盘事件，移动
        if event.keysym == 'Left':
            next_block_location = [[i[0] - 1, i[1]] for i in self.this_block_location]
            for i in next_block_location:
                if i not in self.this_block_location and self.grid[i[1], i[0]] != 0:
                    return
            for i in self.this_block_location:
                self.grid[i[1], i[0]] = 0
            self.block_col_offset -= 1
            self.this_block_location = [[i[0] + self.block_col_offset, i[1] + self.block_row_offset] for i in
                                        self.this_block.BLOCK_LOCATION[self.choose_one]]
        elif event.keysym == 'Right':
            next_block_location = [[i[0] + 1, i[1]] for i in self.this_block_location]
            for i in next_block_location:
                if i not in self.this_block_location and self.grid[i[1], i[0]] != 0:
                    return
            for i in self.this_block_location:
                self.grid[i[1], i[0]] = 0
            self.block_col_offset += 1
            self.this_block_location = [[i[0] + self.block_col_offset, i[1] + self.block_row_offset] for i in
                                        self.this_block.BLOCK_LOCATION[self.choose_one]]
        elif event.keysym == 'Down':
            for i in self.this_block_location:
                self.grid[i[1], i[0]] = 0
            while self.if_block_end() == False:
                self.block_row_offset += 1
                self.this_block_location = [[i[0] + self.block_col_offset, i[1] + self.block_row_offset] for i in
                                            self.this_block.BLOCK_LOCATION[self.choose_one]]
        self.canvas.delete('all')

        for i in self.this_block_location:
            self.grid[i[1], i[0]] = self.this_block.BLOCK_NUM

        self.draw_grid()

    def start_game(self):
        # 开始游戏
        self.get_random_block()
        self.block_move()

    def block_eliminate(self):
        # 方块清除
        tmplist = self.grid.tolist()
        continuous_row = 0
        score = 0
        for i in range(1, self.inner_row_num + 1):
            tmpls = tmplist[i][1: self.inner_col_num + 1]
            if min(tmpls) > 0:
                continuous_row += 1
                for j in range(i, 1, -1):
                    self.grid[j] = self.grid[j - 1]
            else:
                if continuous_row == 1:
                    score += 100
                elif continuous_row == 2:
                    score += 200
                elif continuous_row == 3:
                    score += 400
                elif continuous_row >= 4:
                    score += 800
                continuous_row = 0
        if continuous_row == 1:
            score += 100
        elif continuous_row == 2:
            score += 200
        elif continuous_row == 3:
            score += 400
        elif continuous_row >= 4:
            score += 800
        continuous_row = 0
        return score

    def if_game_end(self):
        # 判断游戏是否结束
        for i in self.this_block_location:
            if self.grid[i[1], i[0]] > 0:
                return True
        return False

    def if_block_end(self):
        # 判断方块是否下落完毕
        next_block_location = [[i[0], i[1] + 1] for i in self.this_block_location]
        for i in next_block_location:
            next_block_x = i[1]
            next_block_y = i[0]
            if i not in self.this_block_location and self.grid[next_block_x, next_block_y] != 0:
                return True
        return False

    def block_move(self):
        # 方块的自动下落
        if self.if_block_end() == True:
            self.total_score += self.block_eliminate()
            self.get_random_block()

        for i in self.this_block_location:
            self.grid[i[1], i[0]] = 0

        if self.start_judge != True:
            self.block_row_offset += 1
            self.this_block_location = [[i[0] + self.block_col_offset, i[1] + self.block_row_offset] for i in
                                        self.this_block.BLOCK_LOCATION[self.choose_one]]

        self.canvas.delete('all')

        for i in self.this_block_location:
            self.grid[i[1], i[0]] = self.this_block.BLOCK_NUM

        self.draw_grid()
        self.start_judge = False

        if self.if_block_end() == False:
            self.canvas.after(self.speed, self.block_move)
        else:
            self.get_random_block()
            self.canvas.after(self.speed, self.block_move)


def tetris_start():
        tetris = Tetris()
        tetris.start_game()



