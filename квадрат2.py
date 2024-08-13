import pygame
import random

class Rect:
    def __init__(self, x, y, ex, width, height, s):
        self.x = x
        self.y = y
        self.ex = ex
        self.width = width
        self.height = height
        self.s = s
        
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
hp = 3

rx = -100
ry = -100
rs = False
#random.randit(a, b) - рандомное число в диапазоне от а до b
num_rects = random.randint(5, 10)
#0 + 1 500 - ширина квадрата(а - 1)
rects = [Rect(random.randint(1, 499), 50, random.randint(1, 2), 50, 50, True) for i in range (num_rects)]
bullets = [Rect(-100,-100, 3, 25, 25, False) for i in range (num_rects)]

pygame.init()
font = pygame.font.Font(None, 60)

while True:
    screen.fill((0, 0, 0))
    hp_text = font.render(str(hp), True, (255, 255, 255))
    screen.blit(hp_text,(450,10))
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
        
    if hp <= 0:
        break
           
    for i in range(len(rects)):
        if rects[i].x > x and rects[i].x < x + 50 and bullets [i].s == False:
            bullets[i].x = rects[i].x + rects[i].width // 4
            bullets[i].y = rects[i].y
            bullets[i].s = True
        if bullets[i].y >=500:
            bullets[i].die()
            
        if (x < bullets[i].x < x + 50 or \
            x < bullets[i].x + bullets[i].width < x + 50) and \
            bullets[i].y + bullets[i].height >= y:
            bullets[i].die()
            hp -= 1
        
        if bullets[i].s:
            bullets[i].y += bullets[i].ex
            pygame.draw.rect(screen, (0, 0, 255),(bullets[i].x, bullets[i].y, bullets[i].width, bullets[i].height))
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
   
text = font.render ("GAME OVER", True (225, 225, 225))
screen.blit(Text, (100, 200))
pygame.display.update()
