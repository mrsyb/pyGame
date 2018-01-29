#将事件显示到窗口中，同时记录到指定的文件中

#框架---1.引入pygame库及sys库
import  pygame,sys
import pygame.freetype

#框架---2.初始化initial（）及设置

pygame.init()
vInfo = pygame.display.Info()#获取当前屏幕分辨率返回值中vInfo.current_w, vInfo.current_h分别表示当前窗口的宽和高
size = width, height = vInfo.current_w, vInfo.current_h
screen = pygame.display.set_mode(size)#模式设置函数 参数为一个二元元组，表示窗口宽和高
pygame.display.set_caption("pygame游戏之旅")#标题设置


font = pygame.freetype.Font("C://Windows//Fonts//msyh.ttc",36)
file = open("record.txt","a")

green = pygame.Color("green")
position_y = 0
line_height = font.get_sized_glyph_height()
#框架---3.获取事件并诼类响应
    #框架3.4.均处于一个死循环
while True:
    for event in pygame.event.get():#pygame.event.get()--从事件栈中获取事件
        file.write(str(event)+ '\n')


        if event.type == pygame.QUIT:
            file.close()
            sys.exit()

        font_surf, front_rect = font.render(str(event), (0, 255, 0))

        screen.blit(font_surf,(0,position_y))
        position_y += line_height


        if position_y > height:
            position_y = 0
            screen.fill((0,0,0))



#框架---4.刷新屏幕
    pygame.display.update()#刷新屏幕  update（）---只是更新有变化的部分
