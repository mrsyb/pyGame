#pagame图形绘制

#框架---1.引入pygame库及sys库
import  pygame,sys
from math import pi
#框架---2.初始化initial（）及设置

pygame.init()
screen = pygame.display.set_mode((600,400))#模式设置函数 参数为一个二元元组，表示窗口宽和高
pygame.display.set_caption("pygame图形绘制")#标题设置

GOLD = 255,251,0
RED = pygame.Color("red")
WHITE = 255,255,255
GREEN =pygame.Color("green")

'''#绘制两个矩形
    r1rect = pygame.draw.rect(screen,GOLD,(100,100,200,100),5)#有边框金色
    r2rect = pygame.draw.rect(screen,RED,(210,210,200,100),0)#无边框红色
'''
e1rect = pygame.draw.ellipse(screen,GREEN,(50,50,500,300),3)#绘制一个椭圆
c1rect = pygame.draw.circle(screen,GOLD,(200,180),30,5)#绘制一个圆
c2rect = pygame.draw.circle(screen,GOLD,(400,180),30)#绘制一个圆
r1rect = pygame.draw.rect(screen,RED,(170,130,60,10),3)#绘制一个矩形
r2rect = pygame.draw.rect(screen,RED,(370,130,60,10))#绘制一个矩形
plist = [(295,170),(285,250),(260,280),(340,280),(315,250),(305,170)]#多线位置列表
l1rect = pygame.draw.lines(screen, GOLD, True, plist,2)#绘制一条多线
a1rect = pygame.draw.arc(screen,GREEN,(200,220,200,100),1.4*pi,1.9*pi,3)#绘制一个椭圆弧形
#框架---3.获取事件并诼类响应
    #框架3.4.均处于一个死循环
while True:
    for event in pygame.event.get():#pygame.event.get()--从事件栈中获取事件
        if event.type == pygame.QUIT:
            sys.exit()
#框架---4.刷新屏幕
    pygame.display.update()#刷新屏幕  update（）---只是更新有变化的部分
