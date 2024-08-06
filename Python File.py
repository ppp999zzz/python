import pygame

screen = pygame.display.set_mode((500, 500))
x = 225
y = 225
dx = 1
while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        pass
    if x >= 450 or x <= 0:
        dx *= -1
    pygame.draw.rect(screen, (225,0,0), (x, y, 50, 50))
    x += dx
    pygame.display.update()
    pygame.time.delay(1)
    