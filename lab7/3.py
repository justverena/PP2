import pygame
pygame.init()
size = (500, 500)
screen = pygame.display.set_mode((size))
r = 25
x, y = 500 // 2, 500 // 2
color = (255, 0, 0)
ok = True
while ok:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            ok = False
         elif event.type == pygame.KEYDOWN:
             if event.key == pygame.K_UP:
                y = max(y - 20, r)
             elif event.key == pygame.K_DOWN:
                y = min(y + 20, 500 - r)
             elif event.key == pygame.K_LEFT:
                x = max(x - 20, r)
             elif event.key == pygame.K_RIGHT:
                x = min(x + 20, 500 - r)
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, color, (x, y), r)
    pygame.display.update()