import pygame
import random

class Rect:
    def __init__(self,width,height):
        self.x = random.randint(1,50)
        self.y = 80
        self.ex = random.randint(2,8)
        self.width = width
        self.height = height
        self.s = True
        
    def die(self):
        self.x = -100
        self.y = -100
        self.s = False
        
def kill_rocket():
    global rx, ry, rs
    rx = -100
    ry = -100
    rs = False
    

screen = pygame.display.set_mode((500, 500))
x = 225
y = 430
dx = 1
rx = -100
ry = -100
rs = False
#random.randit(a, b) - рандомное число в диапазоне от а до b
num_rects = random.randint(5, 15)
#0 + 1 500 - ширина квадрата(а - 1)
rects = [Rect(50,50) for i in range (num_rects)]
while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        pass
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] and x <= 450:
        x += 1
    if keys[pygame.K_a] and x >= 0:
        x -= 1
    if keys[pygame.K_SPACE] and rs == False:
       rx = x + 50 // 4
       ry = y
       rs = True
       
    if ry <= 0:
        kill_rocket()
       
    if rs:
        pygame.draw.rect(screen,(255,255,0),(rx,ry,25,25))
        ry -= 5
           
    for i in range(len(rects)):
        if rects[i].x >= 450 or rects[i].x <= 0:
            rects[i].ex = -rects[i].ex
        if (rx >= rects[i].x and rx <= rects[i].x + rects[i].width or \
           rx + 25 <= rects[i].x + rects[i].width and rx + 25 >= rects[i].x) and \
           ry <= rects[i].y + rects[i].height:
               kill_rocket()
               rects[i].die()
        rects[i].x += rects[i].ex
        pygame.draw.rect(screen, (139,0,0), (rects[i].x, rects[i].y,
                                             rects[i].width, rects[i].height))
    pygame.draw.rect(screen, (255, 255, 255),(x,y, 50, 50))
    pygame.display.update()
    pygame.time.delay(6)
    