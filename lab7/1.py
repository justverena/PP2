import pygame, datetime
pygame.init()
size = (800, 800)
screen = pygame.display.set_mode(size)
x = 400
y = 400
clock = pygame.time.Clock()
mickey = pygame.image.load("mickey.png")
l_hand = pygame.image.load("l-hand.png")
r_hand = pygame.image.load("r-hand.png")
mickeyrect = mickey.get_rect()
def rotate(surf, image, angle, x, y):
    rot_image = pygame.transform.rotate(image, angle)
    new_rect = rot_image.get_rect(center = image.get_rect(center = (x, y)).center)
    surf.blit(rot_image, new_rect)

ok = True
while ok:
    screen.blit(mickey, (0, 0))
    time = datetime.datetime.now()
    clock.tick(30)
    rotate(screen, l_hand, -time.second * 6, x, y)
    rotate(screen, r_hand, -time.minute * 6 - 42, x, y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ok = False
    pygame.display.update()