#V7实现文字型壁球小游戏，使用rend方法绘制
'''
Font.render(text, fgcolor=None, bgcolor=None,rotation=0, size=0) —> (Surface, Rect)
• text 绘制的文字内容
• fgcolor, bgcolor 字体颜色、背景颜色
• rotation 逆时针的旋转角度，取值0-359，部分字体可旋转
• size 文字大小，赋值该参数将覆盖Font中的设定值
----返回一个已绘制的surface对象和一个rect对象，需要结合blit()方法才能绘制到主图层上
'''

#框架---1.引入pygame库及sys库
import  pygame,sys
import pygame.freetype#文字渲染模块，主要使用Font()方法

#框架---2.初始化init()及设置
pygame.init()
size = width, height = 600,400
speed = [1,1]
WHITE = 255,255,255
GOLD = 255,251,0
pos = [230,160]

fps = 300
ftick = pygame.time.Clock()

screen = pygame.display.set_mode(size)#模式设置函数 参数为一个二元元组，表示窗口宽和高
pygame.display.set_caption("pygame壁球_文字型")#标题设置
f1 = pygame.freetype.Font("C://Windows//Fonts//msyh.ttc",36)
f1surf, f1rect= f1.render("中国制造",fgcolor=GOLD,size=50)


#框架---3.获取事件并诼类响应
    #框架3.4.均处于一个死循环
while True:
    for event in pygame.event.get():#pygame.event.get()--从事件栈中获取事件
        if event.type == pygame.QUIT:
            sys.exit()
    if pos[0] < 0 or pos[0] + f1rect.width > width:
        speed[0] = -speed[0]
    if pos[1] < 0 or pos[1] + f1rect.bottom > height:
        speed[1] = -speed[1]
    pos[0] = pos[0] + speed[0]
    pos[1] = pos[1] + speed[1]
#框架---4.刷新屏幕
    screen.fill(WHITE)#背景填充 黑色（BLACK = 0，0，0）白色（WHITE = 255，255，255）
    f1surf, f1rect = f1.render("中国制造", fgcolor=GOLD, size=50)
    screen.blit(f1surf,(pos[0],pos[1]))
    pygame.display.update()#刷新屏幕  update（）---只是更新有变化的部分 flip()---重新绘制整个窗口
    ftick.tick(fps)