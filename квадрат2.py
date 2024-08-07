import pygame

screen = pygame.display.set_mode((500, 500))
x = 225
y = 225
z = 300
v = 300
dx = 1
while True:
    screen.fill((0,0,0))
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
        
        
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        pass
    if z >= 450 or z <= 0:
        dx *= -1
    pygame.draw.rect(screen, (225,0,0), (z, v, 50, 50))
    z += dx

    
    pygame.draw.rect(screen, (255, 255, 255), (x, y, 50, 50))
    pygame.display.update()
    pygame.time.delay(1)
    