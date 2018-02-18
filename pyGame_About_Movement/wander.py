# Steering Behavior Examples
# Seek & Approach
"""本例主要解决自动寻找目标和接近目标之后的处理过程，
    主要原理是向量的运算。
    按V显示当前速度和所需速度
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
CYAN = (0, 255, 255)
#  敌人精灵（尺寸，最大速度，目标向量的最大系数---用于控制接近速度，接近半径）
MOB_SIZE = 32
MAX_SPEED = 5
MAX_FORCE = 0.1
APPROACH_RADIUS = 120
PRODICT_DISTANCE = 200
PRODICT_RADIUS = 100
TARGET_TYPE = 2

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
        self.target = vec(randint(0, WIDTH), randint(0, HEIGHT))
        self.last_target = 0
        self.www =1



    def seek(self, target):
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

    def wander(self):
        now = pg.time.get_ticks()
        if now - self.last_target > 3000:
            self.last_target = now
            self.target = vec(randint(0, WIDTH), randint(0, HEIGHT))
        return self.seek(self.target)

    def wander_imporve(self):
        now = pg.time.get_ticks()
        if now - self.last_target >0:
            self.last_target = now
            prodict_pos = self.pos + self.vel.normalize() * PRODICT_DISTANCE
            self.target = prodict_pos + vec(PRODICT_RADIUS,0).rotate(uniform(0,360))
        return self.seek(self.target)

    def update(self):
        #self.acc = self.wander()
        self.acc = self.wander_imporve()
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
        scale = 15
        # vel
        pg.draw.line(screen, GREEN, self.pos, (self.pos + self.vel * scale), 3)
        # desired
        pg.draw.line(screen, RED, self.pos, (self.pos + self.desired * scale), 3)
        # random target
        if TARGET_TYPE == 1:
            pg.draw.circle(screen, YELLOW,(int(self.target[0]), int(self.target[1])), 1)
        else:
            prodict_pos = self.pos + self.vel.normalize() * PRODICT_DISTANCE
            pg.draw.circle(screen, WHITE,(int(prodict_pos[0]), int(prodict_pos[1])), PRODICT_RADIUS,1)
            pg.draw.line(screen, CYAN ,prodict_pos ,self.target,3 )
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