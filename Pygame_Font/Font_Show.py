#文字展示
'''
surface和rect的区别
pygame.surface----绘图层或图层，，用于表示图形，文字或图像的绘图效果，与当前屏幕主图层可以并列存在。
                 如果不绘制在主图层上则不会被显示。
pygame.rect-----表示当前主图层的一个矩形区域
主图层-----------由pygame.display.set_mode()生成的surface对象就叫主图层
                在主图层上绘制其它图层使用.blit()方法
'''

#框架---1.引入pygame库及sys库
import  pygame,sys
import  pygame.freetype#文字绘制的增强模块---向屏幕上绘制指定字体和字号的文字

#框架---2.初始化initial（）及设置

pygame.init()
screen = pygame.display.set_mode((600,400))#模式设置函数 参数为一个二元元组，表示窗口宽和高
pygame.display.set_caption("pygame文字展示")#标题设置
GOLD = 255,251,0

f1 = pygame.freetype.Font("c://Windows//Fonts//msyh.ttc",36)#根据字体和字号生成一个Font对象
#f1rect = f1.render_to(screen,(200,160),"中国制造",fgcolor = GOLD,size = 50)#返回一个rect对象
f1surf,f1rect = f1.render("中国制造",fgcolor = GOLD,size = 50)#通过render（）返回一个已绘制的surface对象和一个rect对象需要与blit()方法结合使用

#f2 = pygame.freetype.Font(".//font.ttf",36)
#f2rect = f2.render_to(screen,(200,160),"score 12345",fgcolor = GOLD,size = 50)


#框架---3.获取事件并诼类响应
    #框架3.4.均处于一个死循环
while True:
    for event in pygame.event.get():#pygame.event.get()--从事件栈中获取事件
        if event.type == pygame.QUIT:
            sys.exit()
#框架---4.刷新屏幕
    screen.blit(f1surf,(200,160))
    pygame.display.update()#刷新屏幕  update（）---只是更新有变化的部分
