'''V5壁球小游戏伸缩版_节奏版_图标版_最小化感知版_鼠标型_缩放型
   添加Esc按键响应 line 51
   添加窗体更改事件响应实现窗体调节 line 57
   添加窗体小图标 line 28
   感知最小化，最小化后暂停移动 line 70
   按F1实现全屏
   鼠标型功能定义：
                通过鼠标左键摆放壁球，按键按下时壁球停止移动，左键释放时重新于鼠标处绘制壁球。按下右键下并移动时，壁球跟随移动。
   缩放型功能定义：
                添加按键响应事件，按“+”放大壁球，按“-”缩小壁球，按“空格”恢复原状，扩大和缩小的比例范围为“0.5-2.0”
'''
"""此处可以用这种方式实现同一程序不同精灵的不同刷新速度的要求
last_update = pygame.time.get_ticks()
now = pygame.time.get_ticks()
        if now - last_update > 1000:
            last_update = now
            direction = random.randint(-8, 8)
            ball = pygame.transform.rotate(old_ball, direction)
"""


'''设置png图片透明度的函数,----因为png图像带有alpha通道，load（）后会生成一个带有alph属性的surface对象，
                              而调用convert()之后会转换成不带alph的surface对象，并且set_alpha(int)只能由不带alph属性的surface对象使用，
                              所以引入了temp进行转换
from pygame.locals import*
def bilt_alpha(target,source,location,opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(),source.get_height())).convert()
    temp.blit(target,(-x,-y))
    temp.blit(source,(0,0))
    temp.set_alpha(opacity)
    target.blit(temp,location)
'''
"""防止旋转后抖动
 old_center = ballrect.center
 ball = pygame.transform.rotate(old_ball,direction)
 ballrect = ball.get_rect()
 ballrect.center = old_center
"""


# 框架---1.引入pygame库及sys库
import pygame, sys
from math import atan,pi


# 框架---2.初始化initial（）及设置
pygame.init()
vInfo = pygame.display.Info()#获取当前屏幕分辨率返回值中vInfo.current_w, vInfo.current_h分别表示当前窗口的宽和高
size = width, height = vInfo.current_w, vInfo.current_h

speed = [1, 1]
WHITE = 255, 255, 255
still = False
# BLACK = 0,0,0
'''
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)#全屏模式
screen = pygame.display.set_mode(size,pygame.NOFRAME)#无边框模式
'''

screen = pygame.display.set_mode(size,pygame.RESIZABLE)  # 模式设置函数 参数为一个二元元组，表示窗口宽和高--pygame.RESIZABLE为屏幕可调模式
pygame.display.set_caption("pygame壁球_缩放型")  # 标题设置
old_ball = pygame.image.load("turtle.jpg").convert()  # 载入一个图片表示为一个surface对象 pygame使用内部定义的surface对象表示所有载入的图像，其中。get_rect()方法返回一个覆盖图像的矩形Rect对象
old_ball.set_colorkey((WHITE))
ball = old_ball         #备份用于缩放壁球
old_ballrect = old_ball.get_rect()  # 利用get_rect()返回相应的矩形对象
ballrect = old_ballrect  #备份用于缩放
iconimage = pygame.image.load("life.png")#导入图标图片
pygame.display.set_icon(iconimage)#设置图标图片

ratio = 1.0#壁球缩放比例
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
            #添加按键响应事件，按“+”放大壁球，按“-”缩小壁球，按“空格”恢复原状，扩大和缩小的比例范围为“0.5-2.0”
            elif event.key == pygame.K_EQUALS or event.key == pygame.K_MINUS or event.key == pygame.K_SPACE:
                if event.key == pygame.K_EQUALS and ratio < 2:
                    ratio += 0.1
                    print(ratio)
                if event.key == pygame.K_MINUS and ratio > 0.5:
                    ratio -= 0.1
                    print(ratio)
                if event.key == pygame.K_SPACE:
                    ratio = 1.0
                    print(ratio)
                #改变surface对象的大小，和相应rect对象的大小，---“\”符号表示另起一行继续写本行代码
                ball = pygame.transform.smoothscale(old_ball,\
                       (int(old_ballrect.width*ratio),int(old_ballrect.height*ratio)))
                ballrect.width, ballrect.height = ball.get_rect().width,ball.get_rect().height
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
        #添加鼠标按键按下事件响应，实现按下停止
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                still = True
        #添加鼠标释放事件响应，实现鼠标抬起时重新在鼠标处绘制壁球
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                still = False
                ballrect = ballrect.move(event.pos[0] - ballrect.left, event.pos[1] - ballrect.top)
        #添加鼠标移动事件，实现鼠标右键拖动壁球
        #event.buttons[0],event.buttons[1],event.buttons[2]分别表示鼠标移动时左，右，中，三个按键的状态---按下为1，抬起为0
        elif event.type == pygame.MOUSEMOTION:
            if event.buttons[2] == 1:
                ballrect = ballrect.move(event.pos[0] - ballrect.left, event.pos[1] - ballrect.top)

    if pygame.display.get_active() and not still:  # 感知是否窗体被最小化，是，则暂停移动

        #direction = atan(int((speed[0]/speed[1])))*(180/pi)
        #print(direction)
        #ball = pygame.transform.rotate(ball,direction)
        #ballrect.width, ballrect.height = ball.get_rect().width, ball.get_rect().height


        ballrect = ballrect.move(speed[0], speed[1])  # 实现壁球移动使用move()方法
        if ballrect.left < 0 or ballrect.right > width:
            if ballrect.right > width:
                ballrect.right = width
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            if ballrect.bottom > height:
                ballrect.bottom = height
            speed[1] = -speed[1]


        # 框架---4.刷新屏幕
        screen.fill(WHITE)  # 背景填充 黑色（BLACK = 0，0，0）白色（WHITE = 255，255，255）
        screen.blit(ball, ballrect)  # screen.blit(src,dest)---将一个图像绘制在另一个图像上，即将src绘制到dest位置上。通过rect对象引导对壁球的绘制。
        fclock.tick(fps)  # Clock.tick(framerate)---tick()是clock的一个方法控制帧速度即窗口刷新速度
        pygame.display.update()  # 刷新屏幕  update（）---只是更新有变化的部分 flip()---重新绘制整个窗口
