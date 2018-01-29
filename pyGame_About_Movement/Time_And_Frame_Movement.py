"""本例主要分析基于帧的运动和基于时间的运动
    (本例宽度为600像素，要求自定义精灵在5秒内横向运动完整个窗口)
    方案一：
        通常我们实现运动均是基于帧来实现的，但是随着精灵数量增加，计算增加等原因，程序实际运行的帧数往往会下降，
    此时往往无法在规定时间完成运动距离要求
    方案二：
        我们可以计算出程序每秒需要运行像素数，在更新时传入时间参数，
    在本例中基于帧的代码后面用#注释，基于时间的代码用##注释
"""

import pygame as pg


WIDTH = 600
HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
DARKGRAY = (40, 40, 40)

#  敌人精灵
MOB_SIZE = 32


class Mob(pg.sprite.Sprite):
    def __init__(self):
        self.groups = all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.Surface((MOB_SIZE, MOB_SIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.centery = HEIGHT / 2
        #self.speedx = 2
        self.speedx = 120## WEIDTH = 600,

    #def update(self):
    #     self.rect.left += self.speedx
    #       if self.rect.left > WIDTH:
    #       self.rect.right = 0

    def update(self, dt):##
        self.rect.left += self.speedx * dt##
        if self.rect.left > WIDTH:##
            self.rect.right = 0##

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
fclock = pg.time.Clock()

all_sprites = pg.sprite.Group()
Mob()

paused = False
running = True
while running:
    dt = fclock.tick(FPS)/1000##
    #fclock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
            if event.key == pg.K_SPACE:
                paused = not paused

    if not paused:
        #all_sprites.update()
        all_sprites.update(dt)##
    pg.display.set_caption("{:.2f}".format(fclock.get_fps()))
    screen.fill(DARKGRAY)
    all_sprites.draw(screen)
    pg.display.flip()