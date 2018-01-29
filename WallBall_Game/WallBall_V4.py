'''V4壁球小游戏伸缩版_图标版_最小化感知版
   添加Esc按键响应 line 51
   添加窗体更改事件响应实现窗体调节 line 57
   添加窗体小图标 line 28
   感知最小化，最小化后暂停移动 line 70
   按F1实现全屏
'''

# 框架---1.引入pygame库及sys库
import pygame, sys

# 框架---2.初始化initial（）及设置
pygame.init()
vInfo = pygame.display.Info()#获取当前屏幕分辨率返回值中vInfo.current_w, vInfo.current_h分别表示当前窗口的宽和高
size = width, height = vInfo.current_w, vInfo.current_h

speed = [1, 1]
WHITE = 255, 255, 255
# BLACK = 0,0,0
'''
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)#全屏模式
screen = pygame.display.set_mode(size,pygame.NOFRAME)#无边框模式
'''

screen = pygame.display.set_mode(size,pygame.RESIZABLE)  # 模式设置函数 参数为一个二元元组，表示窗口宽和高--pygame.RESIZABLE为屏幕可调模式
pygame.display.set_caption("pygame壁球_节奏型_伸缩版_图标版_最小化感知版")  # 标题设置
ball = pygame.image.load("turtle.jpg")  # 载入一个图片表示为一个surface对象 pygame使用内部定义的surface对象表示所有载入的图像，其中。get_rect()方法返回一个覆盖图像的矩形Rect对象
ballrect = ball.get_rect()  # 利用get_rect()返回相应的矩形对象
iconimage = pygame.image.load("life.png")#导入图标图片
pygame.display.set_icon(iconimage)#设置图标图片

fps = 300
fclock = pygame.time.Clock()  # 创建一个Clock对象用于操作时间----注意Clock，，C大写

# 框架---3.获取事件并诼类响应
# 框架3.4.均处于一个死循环
while True:
    for event in pygame.event.get():  # pygame.event.get()--从事件栈中获取事件
        if event.type == pygame.QUIT:
            sys.exit()

        # 添加按键响应事件，通过方向键控制壁球对应方向的移动速度
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0]) - 1) * int(speed[0] / abs(speed[0]))
            elif event.key == pygame.K_RIGHT:
                speed[0] = speed[0] + 1 if speed[0] > 0 else speed[0] - 1
            elif event.key == pygame.K_UP:
                speed[1] = speed[1] + 1 if speed[1] > 0 else speed[1] - 1
            elif event.key == pygame.K_DOWN:
                speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1]) - 1) * int(speed[1] / abs(speed[1]))
            # 添加按键响应事件，通过F1键控制壁球游戏全屏，
            elif event.key == pygame.K_F1:
                screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
            elif event.key == pygame.K_ESCAPE:
                sys.exit()
        #添加窗体大小更改事件响应
        #窗口大小发生更改时该事件返回一个event.size元组包含新窗体的宽度和高度
        #size[0]或size.w---表示新窗体的宽度
        #size[1]或size.h---表示新窗体的高度
        elif event.type == pygame.VIDEORESIZE:
            size = width, height =event.w, event.h
            #当调节之后的边框覆盖了当前坐标时修改当前坐标
            if ballrect.left < 0:
                ballrect.left = 0
            if ballrect.right > event.w:
                ballrect.right = event.w
            if ballrect.top < 0:
                ballrect.top = 0
            if ballrect.bottom > event.h:
                ballrect.bottom = event.h
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)#根据新大小重新设置窗体

    if pygame.display.get_active():#感知是否窗体被最小化，是，则暂停移动
        ballrect = ballrect.move(speed[0], speed[1])  # 实现壁球移动使用move()方法
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        # 框架---4.刷新屏幕
        screen.fill(WHITE)  # 背景填充 黑色（BLACK = 0，0，0）白色（WHITE = 255，255，255）
        screen.blit(ball, ballrect)  # screen.blit(src,dest)---将一个图像绘制在另一个图像上，即将src绘制到dest位置上。通过rect对象引导对壁球的绘制。
        fclock.tick(fps)  # Clock.tick(framerate)---tick()是clock的一个方法控制帧速度即窗口刷新速度
        pygame.display.update()  # 刷新屏幕  update（）---只是更新有变化的部分 flip()---重新绘制整个窗口
