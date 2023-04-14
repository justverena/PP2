from pygame.locals import *
import random, sys, time, pygame
pygame.init()
# creating screen
width , height = 332 , 590
speed = 5
score = 0
# creating inscriptions
font = pygame.font.SysFont("Cambria", 60)
font_small = pygame.font.SysFont("Cambria", 30)
game_over = font.render ("Game Over", True, (255, 0, 0))
surface = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
#creating backgrounds
road = pygame.image.load("road.jpg")
music = pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)
# creating classes
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imagee = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.imagee, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0)
    def move(self):
        self.rect.move_ip(0, 5)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, width - 40), 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.imagee = pygame.image.load("enemy.png")
        self.image = pygame.transform.scale(self.imagee, (75, 150))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40),0) 
    def move(self):
        self.rect.move_ip(0,speed)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(60, 340), 0)
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.imagee = pygame.image.load("player.png")
        self.image = pygame.transform.scale(self.imagee, (75, 150))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
 
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-10, 0)
        if self.rect.right < width:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(10, 0)
#creating main variables
c = Coin()
p = Player()
e = Enemy()
#creating sprite groups
enemies = pygame.sprite.Group()
enemies.add(e)
all_sprites = pygame.sprite.Group()
all_sprites.add(p)
all_sprites.add(e)
#creating eservent
inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 1000)

time_collision = time.time()

collision = False
#creating game loop
while True:
    
    for event in pygame.event.get():
        if event.type == inc_speed:
            speed += 0.2

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #creating collection of coins
    surface.blit(road, (0, 0))
    scores = font_small.render("coins:"+str(score), True, (255, 255, 255))
    surface.blit(scores, (480, 6))


    for entity in all_sprites:
        surface.blit(entity.image, entity.rect)
        entity.move()

    current_time = time.time()
    #creating collisions
    if c.rect.colliderect(p.rect):
        if current_time - time_collision > 0.5:
            time_collision = time.time()
            score += 1
            collision = True

    c.move()

    if not collision:
        surface.blit(c.image, c.rect)
        time3 = time.time()

    if current_time - time3 > (0.5):
        time3 = time.time()
        collision = False
    #sound of collisions
    if pygame.sprite.spritecollideany(p, enemies):
        pygame.mixer.music.pause()
        pygame.mixer.Sound("crash.wav").play()
        time.sleep(2)

        surface.fill((0, 0, 0))
        surface.blit(the_end_of_game, (155, 250))
        surface.blit(scores, (250, 330))
        
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(5)
        pygame.quit()
        sys.exit()
    
    pygame.display.update()
    clock.tick(60)