from pygame.locals import *
import random, sys, time, pygame
pygame.init()
# creating screen
FPS = 60
FramePerSec = pygame.time.Clock()
width , height = 332 , 590
speed = 5
score = 0
# creating inscriptions
font = pygame.font.SysFont("Cambria", 60)
font_small = pygame.font.SysFont("Cambria", 30)
game_over = font.render ("Game Over", True, (255, 0, 0))
surface = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
surface = pygame.display.set_mode((width,height))
surface.fill((255, 255, 255))
pygame.display.set_caption("Game")
#creating backgrounds
road = pygame.image.load("road.jpg")
music = pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)
coin_image1 = pygame.image.load('coin_1.png')
coin_image2 = pygame.image.load('coin_2.png')
coin_image3 = pygame.image.load('coin_3.png')
# creating classes
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        random_coin = random.randint(1, 3)
        image = pygame.transform.scale(pygame.image.load('coin_1.png'), (40, 40))
        self.image = pygame.transform.scale(pygame.image.load('coin_1.png'), (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width-40), 0)
        self.random_coin = random_coin
        

    def move(self):
        self.rect.move_ip(0, 5)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, width - 40), 0)

 #randomly generating coins with different weights on the road
    def reset(self):
        self.rect.top = 0
        self.rect.center = (random.randint(40, width - 40), 0)
    def set_random_coin(self, value):
        self.random_coin = value
    def get_random_coin():
        return self.random_coin
    def change_photo(self, value):
        if value == 1:
            self.image = pygame.transform.scale(coin_image1, (40, 40))
        elif value == 2:
            self.image = pygame.transform.scale(coin_image2, (40, 40))
        elif value == 3:
            self.image = pygame.transform.scale(coin_image3, (40, 40))

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
p = Player()
e = Enemy()
c = Coin()

#creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(e)
friends = pygame.sprite.Group()
friends.add(c)
all_sprites = pygame.sprite.Group()
all_sprites.add(p)
all_sprites.add(e)
all_sprites.add(c)
#creating eserevent 
inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 1000)
time_collision = time.time()
current_time = time.time()
collision = False
#creating game loop
while True:         
    for event in pygame.event.get():
        #increasing the speed of Enemy when the player earns N coins
        if event.type == inc_speed and score >= 10:
              speed += 1    
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    surface.blit(road, (0,0))
    scores = font_small.render("coins:"+str(score), True, (255, 255, 255))
    surface.blit(scores, (10, 10))

    for entity in all_sprites:
        surface.blit(entity.image, entity.rect)
        entity.move()
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
        time.sleep(1)

        surface.fill((0, 0, 0))
        surface.blit(game_over, (40, 40))
        surface.blit(scores, (90, 90))
        
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
            time.sleep(2)
            pygame.quit()
            sys.exit()
    #randomly generating coins with different weights on the road 2
    elif pygame.sprite.spritecollideany(p, friends):
        score += c.random_coin
        c.change_photo(c.random_coin)
        c.set_random_coin(random.randint(1, 3))

        for coin in friends:
            coin.reset()

    pygame.display.update()
    clock.tick(60)