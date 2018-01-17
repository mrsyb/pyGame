#本程序测试事件处理函数。
#本程序一秒刷新一次，并产生一个事件

#框架---1.引入pygame库及sys库
import  pygame,sys

#框架---2.初始化initial（）及设置

pygame.init()
screen = pygame.display.set_mode((600,400))#模式设置函数 参数为一个二元元组，表示窗口宽和高
pygame.display.set_caption("pygame事件处理")#标题设置

fps = 1
fclock = pygame.time.Clock()
num = 1

#框架---3.获取事件并诼类响应
    #框架3.4.均处于一个死循环
while True:
    uevent = pygame.event.Event(pygame.KEYDOWN,{"unicode":123, "key":pygame.K_ESCAPE, "mod":pygame.KMOD_ALT})
    pygame.event.post(uevent)
    num = num + 1
    for event in pygame.event.get():#pygame.event.get()--从事件栈中获取事件
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.unicode == "":
                print("[KEYDOWN {}]".format(num),"#",event.key,event.mod)
            else:
                print("[KEYDOWN {}]".format(num),event.unicode,event.key,event.mod)
#框架---4.刷新屏幕

    pygame.display.update()#刷新屏幕  update（）---只是更新有变化的部分
    fclock.tick(fps)