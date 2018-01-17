#测试游戏最小开发框架

#框架---1.引入pygame库及sys库
import  pygame,sys

#框架---2.初始化initial（）及设置

pygame.init()
screen = pygame.display.set_mode((600,400))#模式设置函数 参数为一个二元元组，表示窗口宽和高
pygame.display.set_caption("pygame游戏之旅")#标题设置

#框架---3.获取事件并诼类响应
    #框架3.4.均处于一个死循环
while True:
    for event in pygame.event.get():#pygame.event.get()--从事件栈中获取事件
        if event.type == pygame.QUIT:
            sys.exit()
#框架---4.刷新屏幕
    pygame.display.update()#刷新屏幕  update（）---只是更新有变化的部分
