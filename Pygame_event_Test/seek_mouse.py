# Steering Behavior Examples
# Seek & Approach
# KidsCanCode 2016
"""本例主要解决自动寻找目标和接近目标之后的处理过程，
    主要原理是向量的运算。
"""

import pygame as pg
from random import randint, uniform
vec = pg.math.Vector2

WIDTH = 800
HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
DARKGRAY = (40, 40, 40)

#  敌人精灵（尺寸，最大速度，目标向量的最大系数---用于控制接近速度，接近半径）
MOB_SIZE = 32
MAX_SPEED = 5
MAX_FORCE = 0.1
APPROACH_RADIUS = 120

class Mob(pg.sprite.Sprite):
    def __init__(self):
        self.groups = all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.Surface((MOB_SIZE, MOB_SIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.pos = vec(randint(0, WIDTH), randint(0, HEIGHT))
        self.vel = vec(MAX_SPEED, 0).rotate(uniform(0, 360))#当前速度
        self.acc = vec(0, 0)#施加速度
        self.rect.center = self.pos

    """ 方案一，
        直接计算出需要的向量，设置为self.acc
        主要有两个不足，
        1.由于目标位置一定时施加的速度向量也是一定的，所以敌人精灵会一直在目标位置附近抖动
        2.由于是直接施加最终所需的向量给敌人精灵，所以运动轨迹会显得机械，生硬
    """
    def follow_mouse(self):
        mpos = pg.mouse.get_pos()
        self.acc = (mpos - self.pos).normalize() * 0.5

    """方案二，
        通过设置最大施加向量速度MAX_SPEED使转向更加“圆润”
        缺陷：会继续出现方案一中的抖动现象
        normalize()---使向量标准化
    """
    def seek(self, target):
        self.desired = (target - self.pos).normalize() * MAX_SPEED
        steer = (self.desired - self.vel)
        if steer.length() > MAX_FORCE:
            steer.scale_to_length(MAX_FORCE)
        return steer
    """方案三，
        以目标位置为圆心，以APPROACH_RADIUS为半径，超过界限后以"全速"接近目标位置，
        在距离之内，逐渐减小施加向量的大小，到达目标位置后减为零，
    """
    def seek_with_approach(self, target):
        self.desired = (target - self.pos)#需要目标向量
        dist = self.desired.length()#目标向量大小
        self.desired.normalize_ip()
        if dist < APPROACH_RADIUS:
            self.desired *= dist / APPROACH_RADIUS * MAX_SPEED
        else:
            self.desired *= MAX_SPEED
        steer = (self.desired - self.vel)
        if steer.length() > MAX_FORCE:
            steer.scale_to_length(MAX_FORCE)
        return steer

    def update(self):
        #self.follow_mouse()
        #self.acc = self.seek(pg.mouse.get_pos())
        self.acc = self.seek_with_approach(pg.mouse.get_pos())
        # equations of motion
        self.vel += self.acc
        if self.vel.length() > MAX_SPEED:
            self.vel.scale_to_length(MAX_SPEED)
        self.pos += self.vel
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        if self.pos.y > HEIGHT:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = HEIGHT
        self.rect.center = self.pos

    def draw_vectors(self):
        scale = 25
        # vel
        pg.draw.line(screen, GREEN, self.pos, (self.pos + self.vel * scale), 5)
        # desired
        pg.draw.line(screen, RED, self.pos, (self.pos + self.desired * scale), 5)
        # approach radius
        pg.draw.circle(screen, WHITE, pg.mouse.get_pos(), APPROACH_RADIUS, 1)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
Mob()
paused = False
show_vectors = False
running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
            if event.key == pg.K_SPACE:
                paused = not paused
            if event.key == pg.K_v:
                show_vectors = not show_vectors
            if event.key == pg.K_m:
                Mob()

    if not paused:
        all_sprites.update()
    pg.display.set_caption("{:.2f}".format(clock.get_fps()))
    screen.fill(DARKGRAY)
    all_sprites.draw(screen)
    if show_vectors:
        for sprite in all_sprites:
            sprite.draw_vectors()
    pg.display.flip()