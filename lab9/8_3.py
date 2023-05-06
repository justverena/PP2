import pygame  
pygame.init()
#creating variables 
width = 600
height = 700
points = []
color = pygame.Color('black')
clock = pygame.time.Clock()
#creating colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
darkblue = (0, 0, 255)
purple = (221,160,221)
yellow=(255, 255, 0)
blue = (0, 255, 255)
#creating screen
screen = pygame.display.set_mode((width, height))
screen.fill(white)
pygame.display.set_caption('PAINT')
img = pygame.transform.scale(pygame.image.load('paint.jpg'), (150, 150))
#creating functions to shapes
def drawRect(color, pos, width, height):
    pygame.draw.rect(screen, color, (pos[0], pos[1], width, height), 4)


def drawCircle(color, pos, RAD):
    pygame.draw.circle(screen, color, pos, RAD, 4)

def eraser(pos):
    pygame.draw.circle(screen, white, pos, RAD)

#boolean variables
finished = False
drawing = False
#beginning and end points
start_pos = 0
end_pos = 0
RAD = 30
cnt = 0
#creating main
while not finished:
    clock.tick(60)

    #creating the mouse cursors position
    pos = pygame.mouse.get_pos()

    screen.blit(img, (10, 10)) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = pos
            if pos[0]>10 and pos[0]<160 and pos[1]>10 and pos[1]<160:
                color = screen.get_at(pos)

        if event.type==pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = pos 

            #coordinates for a rectangle
            rect_x=abs(start_pos[0]-end_pos[0])#width
            rect_y=abs(start_pos[1]-end_pos[1])#height

            #coordinates for a circle
            circ_x=abs(start_pos[0]+rect_x//2)#center 
            circ_y=abs(start_pos[1]+rect_y//2)
            #creating the keyboard control
            if cnt == 0:
                drawRect(color, start_pos, rect_x, rect_y)
            if cnt == 1: 
                drawCircle(color, (circ_x, circ_y), rect_x//2)
       #creating eraser
        if event.type == pygame.MOUSEMOTION and drawing:
            if cnt == 3:
                eraser(pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                cnt+=1 #if we type the buttom space, the value of cnt will be increased by 1
                cnt%=3 #and we will divide it by 3, it will count it from the begining 

    pygame.display.flip()