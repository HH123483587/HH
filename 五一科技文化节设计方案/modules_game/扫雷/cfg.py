'''配置文件'''
import os

print(os.getcwd())
'''图片素材路径'''
IMAGE_PATHS = {
    '0': os.path.join(os.getcwd(), '扫雷\\resources\\images\\0.bmp'),
    '1': os.path.join(os.getcwd(), '扫雷\\resources\\images\\1.bmp'),
    '2': os.path.join(os.getcwd(), '扫雷\\resources\\images\\2.bmp'),
    '3': os.path.join(os.getcwd(), '扫雷\\resources\\images\\3.bmp'),
    '4': os.path.join(os.getcwd(), '扫雷\\resources\\images\\4.bmp'),
    '5': os.path.join(os.getcwd(), '扫雷\\resources\\images\\5.bmp'),
    '6': os.path.join(os.getcwd(), '扫雷\\resources\\images\\6.bmp'),
    '7': os.path.join(os.getcwd(), '扫雷\\resources\\images\\7.bmp'),
    '8': os.path.join(os.getcwd(), '扫雷\\resources\\images\\8.bmp'),
    'ask': os.path.join(os.getcwd(), '扫雷\\resources\\images\\ask.bmp'),
    'blank': os.path.join(os.getcwd(), '扫雷\\resources\\images\\blank.bmp'),
    'blood': os.path.join(os.getcwd(), '扫雷\\resources\\images\\blood.bmp'),
    'error': os.path.join(os.getcwd(), '扫雷\\resources\\images\\error.bmp'),
    'face_fail': os.path.join(os.getcwd(), '扫雷\\resources\\images\\face_fail.png'),
    'face_normal': os.path.join(os.getcwd(), '扫雷\\resources\\images\\face_normal.png'),
    'face_success': os.path.join(os.getcwd(), '扫雷\\resources\\images\\face_success.png'),
    'flag': os.path.join(os.getcwd(), '扫雷\\resources\\images\\flag.bmp'),
    'mine': os.path.join(os.getcwd(), '扫雷\\resources\\images\\mine.bmp')
}
'''字体路径'''
FONT_PATH = os.path.join(os.getcwd(), '扫雷\\resources\\font\\font.TTF')
FONT_SIZE = 40
'''BGM路径'''
# BGM_PATH = os.path.join(os.getcwd(), 'resources/music/bgm.mp3')
'''游戏相关参数'''
FPS = 60
"窗口大小"
GRIDSIZE = 20
"炸弹数"
NUM_MINES = 80
"窗口尺寸"
GAME_MATRIX_SIZE = (30, 16)
BORDERSIZE = 5
SCREENSIZE = (GAME_MATRIX_SIZE[0] * GRIDSIZE + BORDERSIZE * 2, (GAME_MATRIX_SIZE[1] + 2) * GRIDSIZE + BORDERSIZE)
'''颜色'''
BACKGROUND_COLOR = (225, 225, 225)
RED = (200, 0, 0)