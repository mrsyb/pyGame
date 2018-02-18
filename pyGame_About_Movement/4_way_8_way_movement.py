"""本例主要分析四个方向的运动和八个方向的运动
    方案一：
        朝上下左右四个方向的运动
    方案二：
        加上对角线的方向共八个方向的运动
"""

import pygame as pg


WIDTH = 600
HEIGHT = 600
FPS = 60
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
        self.rect.center = WIDTH/2 , HEIGHT / 2

    """这个函数是四向运动的update()函数"""
    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_UP]:
            self.speedy = -5
        elif keystate[pg.K_DOWN]:
            self.speedy = 5
        elif keystate[pg.K_RIGHT]:
            self.speedx = 5
        elif keystate[pg.K_LEFT]:
            self.speedx = -5

        self.rect.centerx += self.speedx
        self.rect.centery += self.speedy
    """这个函数是基于八向运动的update()函数
       与四向运动的区别是将elif改为if，并添加的对角线运功的速度转换（勾股定理）   
    """
    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_UP]:
            self.speedy = -5
        if keystate[pg.K_DOWN]:
            self.speedy = 5
        if keystate[pg.K_RIGHT]:
            self.speedx = 5
        if keystate[pg.K_LEFT]:
            self.speedx = -5
        if self.speedx != 0 and self.speedy != 0:#根据勾股定理对对角线运动速度处理
            self.speedx /= 1.414
            self.speedy /= 1.414

        self.rect.centerx += self.speedx
        self.rect.centery += self.speedy


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
fclock = pg.time.Clock()

all_sprites = pg.sprite.Group()
Mob()

paused = False
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
            if event.key == pg.K_SPACE:
                paused = not paused


    all_sprites.update()
    pg.display.set_caption("FPS {:.2f}".format(fclock.get_fps()))
    screen.fill(DARKGRAY)
    all_sprites.draw(screen)
    fclock.tick(FPS)
    pg.display.update()