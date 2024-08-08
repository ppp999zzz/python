import pygame
import random

class Rect:
    def __init__(self,width,height):
        self.x = random.randint(1,499)
        self.y = 100
        self.ex = random.randint(5,10)
        self.width = width
        self.height = height

screen = pygame.display.set_mode((500, 500))
x = 225
y = 225
dx = 1
#random.randit(a, b) - рандомное число в диапазоне от а до b
num_rects = random.randint(3, 5)
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
    if keys[pygame.K_w] and y >= 0:
        y -= 1
    if keys[pygame.K_s] and y <= 450:
        y += 1
    
    for i in range(len(rects)):
        if rects[i].x >= 450 or rects[i].x <= 0:
            rects[i].ex = -rects[i].ex
        rects[i].x += rects[i].ex  
        pygame.draw.rect(screen, (139,0,0), (rects[i].x, rects[i].y,
                                             rects[i].width, rects[i].height))
    pygame.draw.rect(screen, (255, 255, 255),(x,y, 50, 50))
    pygame.display.update()
    pygame.time.delay(6)
    