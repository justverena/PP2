import pygame, time, random
pygame.init()
#creating screen and colors
width = 720
height = 480
screen = pygame.display.set_mode((width, height))
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
#creating speed
speed = 15
# creating fps
fps = pygame.time.Clock()
snake_position = [100, 50]
snake_body = [[100, 50],
			[90, 50],
			[80, 50],
			[70, 50]
			]
# fruit position
fruit_position = [random.randrange(1, (width//10)) * 10,
				random.randrange(1, (height//10)) * 10]
fruit_spawn = True

score = 0

def show_score(choice, color, font, size):

	#creating font objects
	score_font = pygame.font.SysFont(font, size)
	score_surface = score_font.render('Score : ' + str(score), True, color)
	score_rect = score_surface.get_rect()
	screen.blit(score_surface, score_rect)

#creating game over
def game_over():
	my_font = pygame.font.SysFont('Cambria', 50)
	game_over_surface = my_font.render(
		'Your Score is : ' + str(score), True, red)
	game_over_rect = game_over_surface.get_rect()

	game_over_rect.midtop = (width/2, height/4)

	screen.blit(game_over_surface, game_over_rect)
	pygame.display.flip()
	
	time.sleep(2)
	
	pygame.quit()
	
	quit()


#creating main
direction = 'RIGHT'
change_to = direction
while True:
	#creating key events
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				change_to = 'UP'
			if event.key == pygame.K_DOWN:
				change_to = 'DOWN'
			if event.key == pygame.K_LEFT:
				change_to = 'LEFT'
			if event.key == pygame.K_RIGHT:
				change_to = 'RIGHT'

	if change_to == 'UP' and direction != 'DOWN':
		direction = 'UP'
	if change_to == 'DOWN' and direction != 'UP':
		direction = 'DOWN'
	if change_to == 'LEFT' and direction != 'RIGHT':
		direction = 'LEFT'
	if change_to == 'RIGHT' and direction != 'LEFT':
		direction = 'RIGHT'

	#creating the movement
	if direction == 'UP':
		snake_position[1] -= 10
	if direction == 'DOWN':
		snake_position[1] += 10
	if direction == 'LEFT':
		snake_position[0] -= 10
	if direction == 'RIGHT':
		snake_position[0] += 10

	#creating the growing
	snake_body.insert(0, list(snake_position))
	if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
		score += 10
		fruit_spawn = False
	else:
		snake_body.pop()
		
	if not fruit_spawn:
		fruit_position = [random.randrange(1, (width//10)) * 10,
						random.randrange(1, (height//10)) * 10]
		
	fruit_spawn = True
	screen.fill(black)
	
	for pos in snake_body:
		pygame.draw.rect(screen, green,
						pygame.Rect(pos[0], pos[1], 10, 10))
	pygame.draw.rect(screen, white, pygame.Rect(
		fruit_position[0], fruit_position[1], 10, 10))

	#creating conditions for game over
	if snake_position[0] < 0 or snake_position[0] > width-10:
		game_over()
	if snake_position[1] < 0 or snake_position[1] > height-10:
		game_over()

	for block in snake_body[1:]:
		if snake_position[0] == block[0] and snake_position[1] == block[1]:
			game_over()

	show_score(1, white, 'Cambria', 20)

	pygame.display.update()

	fps.tick(speed)
