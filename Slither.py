import pygame
import time
import random

# Initializing all modules in pygame
pygame.init()

screen_height = 620
screen_width = 780
block_size = 15
apple_width = 15

font_size = 12
small_font = pygame.font.SysFont("comicsansms",  font_size)
med_font = pygame.font.SysFont("comicsansms",  font_size*2)
large_font = pygame.font.SysFont("comicsansms",  int(font_size*3.5))

#large_font.set_bold(True)
#med_font.set_bold(True)

# screen object referrring to real screen, next giving game a name
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('snake apple')

# Setting Game icon
#icon = pygame.image.load('apple2.png')
#pygame.display.set_icon(icon)

clock = pygame.time.Clock()
FPS = 15

#colors
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
green = (0, 155, 0)
android  = (0, 255, 87)
gold = (255, 215, 0)
light_Silver = (230, 230, 230)

screen.fill(white)
pygame.display.update()

# Images
snakeHead = pygame.image.load('SnakeHead.png')
snakeTail = pygame.image.load('SnakeTail.png')
snakeBody = pygame.image.load('snakeBody.png')
Image = [pygame.image.load('image1.jpg'),pygame.image.load('image2.jpg'),pygame.image.load('image3.jpg'),pygame.image.load('image4.jpg')]
Two = pygame.image.load('two.jpg')
From = pygame.image.load('of.jpg')
The = pygame.image.load('the.jpg')
JonDead = pygame.image.load('dead.jpg')
RunFlash = pygame.image.load('flash.jpg')
flashNarrow = pygame.image.load('flashNarrow.jpg')
pb = pygame.image.load('pb.jpg')
thunder = pygame.image.load('thunder.jpg')
scorecard = pygame.image.load('scorecard.png')
scoreSymbol = pygame.image.load('scoreSymbol.png')
scoreSymbol2 = pygame.image.load('arrowRight.png')

run = True
gameOver = False
image_no = 1;

Turn = {}
fpscount = 0

score = 0
highscore = 0

def x_y():
	x = random.randrange(0, (screen_width - apple_width)/apple_width)
	y = random.randrange(3, (screen_height - apple_width)/apple_width)

	return [x,y]

def DrawApple(apple_x, apple_y, image_no):
	screen.blit(Image[image_no], (apple_x, apple_y))	


def DrawSnake(block_size, snakeList, HeadDirection):

	if HeadDirection != "":
		tempHead = snakeHead
	
		if HeadDirection == "left":
			tempHead = pygame.transform.rotate(snakeHead, 90)
		if HeadDirection == "right":
			tempHead = pygame.transform.rotate(snakeHead, 270)
		if HeadDirection == "down":
			tempHead = pygame.transform.rotate(snakeHead, 180)

		screen.blit(tempHead, (snakeList[-1][0], snakeList[-1][1]))

	else:
		screen.blit(snakeHead, (snakeList[-1][0], snakeList[-1][1]))

	for co_ord in snakeList[:-1]:
		screen.blit(snakeBody, (co_ord[0], co_ord[1]))

def fill_the_screen(score, apple_x, apple_y, snakeList, HeadDirection, image_no):
					
	screen.fill(white)
	screen.blit(thunder, (0, 0))
	screen.blit(scorecard, (230, 0))
	screen.blit(scoreSymbol, (270, 0))
	display_message(("Score :" + str(score)), black, -290, "med")
	screen.blit(scoreSymbol2, (480, 0))
	DrawApple(apple_x, apple_y, image_no)
	DrawSnake(block_size, snakeList, HeadDirection)
	pygame.display.update()
		
def isSnake_Eating_Apple(x_cord, y_cord, block_size, apple_x, apple_y, apple_width):
	
	if ( x_cord >= apple_x and x_cord < apple_x + apple_width ) or ( x_cord + block_size > apple_x and x_cord + block_size <= apple_x + apple_width ):
		if ( y_cord >= apple_y and y_cord < apple_y + apple_width ) or ( y_cord + block_size > apple_y and y_cord +block_size <= apple_y + apple_width ):
			return True
	return False

def Generate_apple_Coord(snakeList):

	while 1:
		apple_x = random.randrange(0, (screen_width - apple_width)/apple_width)
		apple_y = random.randrange(3, (screen_height - apple_width)/apple_width)

		apple_x *= apple_width
		apple_y *= apple_width

		if [apple_x, apple_y] not in snakeList:
			break

	return [apple_x, apple_y]

def GameOverDisplay(apple_x, apple_y, snakeList, HeadDirection):
	
	global	score
	for var in range(7):

		screen.fill(white)
		screen.blit(thunder, (0, 0))	
		screen.blit(scorecard, (230, 0))
		screen.blit(scoreSymbol, (270, 0))
		display_message(("Score :" + str(score)), black, -290, "med")
		screen.blit(scoreSymbol2, (480, 0))
		pygame.display.update()
		time.sleep(0.1)

		fill_the_screen(score, apple_x, apple_y, snakeList, HeadDirection, image_no)
		time.sleep(0.1)

def display_message(msg, color, y_displace = 0, size="small"):
	
	if size == "small":
		textSurface = small_font.render(msg, True, color)
	elif size == "med":
		textSurface = med_font.render(msg, True, color)
	if size == "large":
		textSurface = large_font.render(msg, True, color)

	textRect = textSurface.get_rect()
	textRect.center = screen_width/2, screen_height/2 + y_displace
	screen.blit(textSurface, textRect)

def pause():

	screen.fill(white)
	display_message("Paused", black, -100, "large")
	display_message("Press Space to Resume, q to Quit", black, 40, "med")
	pygame.display.update()

	while 1:
		for events in pygame.event.get():
			if events.type == pygame.QUIT:
				return False

			if events.type == pygame.KEYDOWN:
				if events.key == pygame.K_SPACE:
					return True
				elif events.key == pygame.K_q:
					return False

def introduction_Screen():

	global gameOver
	global highscore
	global score

	score = highscore
	filee = open('Highscore.txt')
	highscore = filee.read()
	filee.close()
	
	screen.fill(white)
	display_message("Welcome to Slither !!", green, -100, "large")
	display_message("Eat as many apples as you can .", black, 0, "med")
	display_message("Try not to touch boundaries and yourself with the head. ", black, 40, "med")
	display_message("Press Spcae-Bar to pause the game", black, 80, "med")
	display_message("Press any key to continue !!", black, 150, "med")
	screen.blit(thunder, (0, 0))	
	screen.blit(scorecard, (235, 0))
	screen.blit(scoreSymbol, (240, 0))
	screen.blit(scoreSymbol2, (487, 0))

	display_message(("High Score: " + str(highscore)), black, -293, "med")
	pygame.display.update()

	intro = True
	while intro:
		for events in pygame.event.get():
			
			if events.type == pygame.QUIT:
				intro = False
				return False
				break

			elif events.type == pygame.KEYDOWN:
				return start()
				intro = False
				break
	
def start():

	global score
	global highscore
	global gameOver
	global run

	score = 0

	x_cord = screen_width/2
	y_cord = screen_height/2
	x_change = 0
	y_change = 0

	image_no = 0;
	snakeList = [[x_cord, y_cord]]
	HeadDirection = "up"
	[apple_x, apple_y] = Generate_apple_Coord(snakeList)
	
	#Flag var to disable up & down movement, left & right
	x_flag = 0
	y_flag = 0

	run = True
	gameOver = False
	
	while run:

		while gameOver == True:
			try:

				screen.blit(pb, (0, 0))	
				display_message("Game Over !!", red, -240, "large")
	
				#print "Scores : ", int(score), int(highscore)
				filee = open('Highscore.txt', 'w')
				if int(score) > int(highscore):
					filee.write(str(score))
				else:
					filee.write(str(highscore))

				filee.close()

				if int(score) > int(highscore):

					display_message("New High Score " + str(score) + " !! Congo !!", green, -180, "med") 
					display_message("Press P to play again, Q to quit", green, -120, "med") 
	
				else:
					display_message("Your Score :"+str(score), green, -160, "med") 
					display_message("Press P to play again, Q to quit", green, -130, "med") 

				pygame.display.update()

				for events in pygame.event.get():
					if events.type == pygame.QUIT:
						return False

					if events.type == pygame.KEYDOWN:
						if events.key == pygame.K_p:
							return True

						elif events.key == pygame.K_q:
							return False

			except:
				pass
	
		if run == False:
			break

		for events in pygame.event.get():
			#print events
			if events.type == pygame.QUIT:
				run = False
				return False
				break

			elif events.type == pygame.KEYDOWN:

				if events.key == pygame.K_LEFT and x_flag == 0:
					HeadDirection = "left"
					x_flag = -1
					y_flag = 0
					x_change = -block_size
					y_change = 0

				elif events.key == pygame.K_RIGHT and x_flag == 0:
					HeadDirection = "right"
					x_flag = -1
					y_flag = 0
					x_change = block_size
					y_change = 0

				elif events.key == pygame.K_UP and y_flag == 0:
					HeadDirection = "up"
					y_flag = -1
					x_flag = 0
					y_change = -block_size
					x_change = 0

				elif events.key == pygame.K_DOWN and y_flag == 0:
					HeadDirection = "down"
					y_flag = -1
					x_flag = 0
					y_change = block_size
					x_change = 0

				elif events.key == pygame.K_SPACE:
					resume = pause()
					if resume == False:
						return False

					fill_the_screen(score, apple_x, apple_y, snakeList, HeadDirection, image_no)
					time.sleep(2)

		x_cord += x_change
		y_cord += y_change
		
		if x_cord >= screen_width or x_cord < 0 or y_cord >= screen_height or y_cord < 40:
			
			GameOverDisplay(apple_x, apple_y, snakeList, HeadDirection)
			gameOver = True
			

		if gameOver == False:
			if x_change + y_change != 0 and gameOver == False:
				snakeList.append([x_cord, y_cord])
				
				#Checking whether snake is eating itself !! :( :P
				if [x_cord, y_cord] in snakeList[:-1]:

					fill_the_screen(score, apple_x, apple_y, snakeList, HeadDirection, image_no)					
					GameOverDisplay(apple_x, apple_y, snakeList, HeadDirection)
					gameOver = True
			
				if isSnake_Eating_Apple(x_cord, y_cord, block_size, apple_x, apple_y, apple_width):
					
					fill_the_screen(score, apple_x, apple_y, snakeList, HeadDirection, image_no)
					image_no = random.randrange(0,4)
					[apple_x, apple_y] = Generate_apple_Coord(snakeList)
					score += 10

				else:
					snakeList.pop(0)
				
			fill_the_screen(score, apple_x, apple_y, snakeList, HeadDirection, image_no)
	
		clock.tick(FPS)
		
	screen.fill(white)
	pygame.display.update()

while 1:
	again = introduction_Screen()
	if again == False:
	
		# Diplaying Final message
		screen.blit(JonDead, (0, 0))	
		display_message("Game Over", red, 0, "large")
		pygame.display.update()
		time.sleep(1)
		break

pygame.quit()