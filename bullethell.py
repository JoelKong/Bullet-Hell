#Importing
import pygame
import math
import random

#Initiating game
pygame.init()
pygame.font.init()
resolution = 1500, 800 
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption('Bullet Hell')
background = pygame.image.load("Resources/Images/background.png")
fps = pygame.time.Clock()
fps.tick(60)
backgroundmusic = pygame.mixer.music.load("Resources/Audio/gamemusic.mp3")
pygame.mixer.music.play(-1)


#Classes setup
class player(object):
	display = True
	hero = pygame.image.load("Resources/Images/player.png")
	def __init__(self, x , y):
		self.x = x
		self.y = y
		self.speed = 5
		self.hitbox = (self.x + 50, self.y + 20, 150, 200)
		self.health = 1500

	def draw(self, screen):
		if self.display == True:
			screen.blit(self.hero , (self.x, self.y))
			self.hitbox = (self.x + 50, self.y + 20, 150, 200)
			pygame.draw.rect(screen, (0,128,0), (self.hitbox[0], self.hitbox[1] + 220 , 50 -(0.1 * (10 - self.health)), 10))
			pygame.draw.rect(screen, (255,255,0), (self.hitbox[0], self.hitbox[1] + 240 , 50 - (4 * (10 - stamina)), 10))

	def destroy(self):
		self.display = False

class player_projectile(object):
	def __init__(self, x , y, radius, color):
		self.x = x
		self.y = y
		self.speed = 10
		self.radius = radius
		self.color = color
		self.damage = random.randint(15,25)

	def draw(self, screen):
		pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

class enemy(object):
	display = True
	boss = pygame.image.load("Resources/Images/enemyship1.png")
	def __init__(self, x, y, changedirection):
		self.x = x
		self.y = y
		self.speed = 10
		self.path = [x, changedirection]
		self.hitbox = (self.x + 8, self.y + 150, 370, 140)
		self.health = 8000

	def draw(self, screen):
		if self.display == True:
			self.enemymove()
			screen.blit(self.boss, (self.x,self.y))
			self.hitbox = (self.x + 8, self.y + 150, 370, 140)
			pygame.draw.rect(screen, (255,0,0), (self.hitbox[0] +65, self.hitbox[1] -20 , 50 -(0.03 * (10 - self.health)), 10))

	def enemymove(self):
		if enemymovement == True:
			if self.speed > 0:
				if self.x < self.path[1] + self.speed:
					self.x += self.speed
				else:
					self.speed = self.speed * -1
					self.x += self.speed
			else:
				if self.x > self.path[0] - self.speed:
					self.x += self.speed
				else:
					self.speed = self.speed * -1
					self.x += self.speed
	
	def destroyenemy(self):
		self.display = False

class enemy_projectile(object):
	def __init__(self, x, y, radius, color):
		self.x = x
		self.y = y
		self.speed = 10
		self.radius = radius
		self.color = color
		self.angle = 0
		self.xdiff = 0
		self.ydiff = 0
		self.damage = random.randint(15,20)

	def draw(self, screen):
		pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

class attack_pattern1(object):
	def __init__(self, x, y, radius, color):
		self.x = x
		self.y = y
		self.speed = 10
		self.radius = radius
		self.color = color
		self.angle = 0
		self.xdiff = 0
		self.ydiff = 0
		self.damage = random.randint(15,20)

	def draw(self, screen):
		pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

class attack_pattern2(object):
	def __init__(self, x, y, radius, color):
		self.x = x
		self.y = y
		self.speed = 10
		self.radius = radius
		self.color = color
		self.angle = 0
		self.xdiff = 0
		self.ydiff = 0
		self.damage = random.randint(15,20)

	def draw(self, screen):
		pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

class healthboost(object):
	health = pygame.image.load("Resources/Images/health.png")
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.heal = 400
		self.speed = 10

	def draw(self, screen):
		screen.blit(self.health, (self.x, self.y))

	
#Drawing the classes
def redraweverything():
	screen.blit(background, (0,0))
	jet.draw(screen)
	badass.draw(screen)
	if boost == True:
		hpboost.draw(screen)
	for bullet in bullets:
		bullet.draw(screen)
	for lazer in enemybullets:
		lazer.draw(screen)
	for pattern1 in enemyattackpattern1:
		pattern1.draw(screen)
	for pattern2 in enemyattackpattern2:
		pattern2.draw(screen)
	scoreboard = font.render('SCORE: ' + str(score), 1, (0,255,255))
	screen.blit(scoreboard, (50,50))

#Drawing main menue
def mainmenuedraw():
	screen.blit(background, (0,0))
	gamename = fontgamename.render('BULLET HELL', 1, (25,25,112))
	start = font.render('Press S to start', 1, (64,244,208))
	controls1 = font.render('Arrow keys to move', 1,(64,244,208))
	controls2 = font.render('Hold W to shoot', 1, (64,244,208))
	pause = font.render('Press P to pause', 1, (64,244,208))
	dash = font.render('Hold shift to dash', 1, (64,244,208))
	screen.blit(gamename, (600,300))
	screen.blit(start, (600,370))
	screen.blit(controls1, (600,440))
	screen.blit(controls2, (600,510))
	screen.blit(pause, (600,580))
	screen.blit(dash, (600,650))

#Drawing lose screen
def losescreen():
	losescreen = fontendgame.render('YOU LOSE!!',1, (255,0,0))
	retry = font.render('Press R to retry', 1,(0,0,0))
	goback = font.render('Press M to go back to main menu', 1,(0,0,0))
	screen.blit(losescreen, (600,550))
	screen.blit(retry, (600,620))
	screen.blit(goback, (600,690))

#Drawing win screen
def winscreen():
	winscreen = fontendgame.render('YOU WIN!!', 1, (0,255,0))
	retry = font.render('Press R to retry', 1,(0,0,0))
	goback = font.render('Press M to go back to main menu', 1,(0,0,0))
	screen.blit(winscreen, (600,550))
	screen.blit(retry, (600,620))
	screen.blit(goback, (600,690))

#Drawing pause screen
def pausescreen():
	pausescreen = fontendgame.render('PAUSED', 1, (25,25,112))
	startagain = font.render('Press S to resume', 1,(123,104,238))
	screen.blit(pausescreen, (600,550))
	screen.blit(startagain, (600,690))

#Defining variables
stamina = 50
mainmenue = True
gamestart = False
movement = True
enemymovement = True
lose = False
win = False
enemyshoot = True
playershoot = True
pause = False
playerhit = True
boost = True
stopboosting = True
jet = player(0, 500)
badass = enemy(-100, -100, 1200)
hpboost = healthboost(random.randint(50,1200), -150)
bullets = []
enemybullets = []
enemyattackpattern1 = []
enemyattackpattern2 = []
buffup = []
enemyhp = badass.health
playerhp = jet.health
score = 0
font = pygame.font.SysFont('comicsans', 40, True)
fontgamename = pygame.font.SysFont('comicsans', 80, True)
fontendgame = pygame.font.SysFont('comicsans', 80, True)

#Main Menue loop
while mainmenue:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_s:
				lose = False
				badass.display = True
				enemymovement = True
				win = False
				enemyshoot = True
				playershoot = True
				pause = False
				playerhit = True
				winlose = True
				boost = True
				stopboosting = True
				boostfalldown = True
				mainmenue = False
				gamestart = True
				jet.display = True
				jet.health = 1500
				movement = True
				playerhp = 1500
				enemyhp = 8000
				badass.health = 8000
				jet.x = 0
				jet.y = 500
				badass.x = -100
				badass.y = -100
				hpboost.x = random.randint(50,1200)
				hpboost.y = -150
				jet.draw(screen)
				badass.draw(screen)
				hpboost.draw(screen)
				score = 0
				stamina = 50				

	screen.fill(0)
	mainmenuedraw()
	pygame.display.update()


#Main Loop				
	while gamestart:
		screen.fill(0)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit(0)
	

#Projectile limit and hitboxes(player)
		if playerhit == True:
			for bullet in bullets:
				if (bullet.y - bullet.radius) < (badass.hitbox[1] + badass.hitbox[3]) and (bullet.y + bullet.radius) > badass.hitbox[1]:
					if (bullet.x - bullet.radius) < (badass.hitbox[0] + badass.hitbox[2]) and (bullet.x + bullet.radius) > badass.hitbox[0]:
						bullets.pop(bullets.index(bullet))
						badass.health -= bullet.damage
						enemyhp -= bullet.damage
						score += 10

				if bullet.y < 800 and bullet.y > 0:
					bullet.y -= bullet.speed
				else:
					bullets.pop(bullets.index(bullet))
	
	
		if badass.health < 0:
			badass.destroyenemy()
			enemyhp = 0
			enemymovement = False
			win = True
			enemyshoot = False
			movement = False
			playerhit = False
			playershoot = False
			for lazer in enemybullets:
				enemybullets.pop(enemybullets.index(lazer))
			for bullet in bullets:
				bullets.pop(bullets.index(bullet))
			for pattern1 in enemyattackpattern1:
				enemyattackpattern1.pop(enemyattackpattern1.index(pattern1))
			for pattern2 in enemyattackpattern2:
				enemyattackpattern2.pop(enemyattackpattern2.index(pattern2))
			

		if badass.health < 5000:
			for pattern2 in enemyattackpattern2:
				if enemymovement == True:
					if (pattern2.y - pattern2.radius) < (jet.hitbox[1] + jet.hitbox[3]) and (pattern2.y + pattern2.radius) > jet.hitbox[1]:
						if (pattern2.x - pattern2.radius) < (jet.hitbox[0] + jet.hitbox[2]) and (pattern2.x + pattern2.radius) > jet.hitbox[0]:
							enemyattackpattern2.pop(enemyattackpattern2.index(pattern2))
							jet.health -= pattern2.damage
							playerhp -= pattern2.damage
							score -= 10

				if enemymovement:
					if pattern2.y > -800 and pattern2.y < 800:
						pattern2.xdiff = 1000 - pattern2.x
						pattern2.ydiff = 1000 - pattern2.y
						pattern2.angle = math.atan2(pattern2.ydiff, pattern2.xdiff)
						pattern2.y += int(math.sin(pattern2.angle) * pattern2.speed)
						pattern2.x += int(math.cos(pattern2.angle) * pattern2.speed)
					else:
						enemyattackpattern2.pop(enemyattackpattern2.index(pattern2))

			if enemyshoot == True:
				if len(enemyattackpattern2) < 10:
					enemyattackpattern2.append(attack_pattern2(badass.x + 200, badass.y + 290, 6, (255,0,0)))


#Projectile limit and hitboxes(enemy)
		for lazer in enemybullets:
			if enemymovement == True:
				if (lazer.y - lazer.radius) < (jet.hitbox[1] + jet.hitbox[3]) and (lazer.y + lazer.radius) > jet.hitbox[1]:
					if (lazer.x - lazer.radius) < (jet.hitbox[0] + jet.hitbox[2]) and (lazer.x + lazer.radius) > jet.hitbox[0]:
						enemybullets.pop(enemybullets.index(lazer))
						jet.health -= lazer.damage
						playerhp -= lazer.damage
						score -= 10
			if enemymovement:
				if lazer.y > -800 and lazer.y < 800:
					lazer.xdiff = jet.x + 100 - lazer.x
					lazer.ydiff = 900 - lazer.y
					lazer.angle = math.atan2(lazer.ydiff, lazer.xdiff)
					lazer.y += int(math.sin(lazer.angle) * lazer.speed)
					lazer.x += int(math.cos(lazer.angle) * lazer.speed)
				else:
					enemybullets.pop(enemybullets.index(lazer))

		for pattern1 in enemyattackpattern1:
			if enemymovement == True:
				if (pattern1.y - pattern1.radius) < (jet.hitbox[1] + jet.hitbox[3]) and (pattern1.y + pattern1.radius) > jet.hitbox[1]:
					if (pattern1.x - pattern1.radius) < (jet.hitbox[0] + jet.hitbox[2]) and (pattern1.x + pattern1.radius) > jet.hitbox[0]:
						enemyattackpattern1.pop(enemyattackpattern1.index(pattern1))
						jet.health -= pattern1.damage
						playerhp -= pattern1.damage
						score -= 10

			if enemymovement:
				if pattern1.y > -800 and pattern1.y < 800:
					pattern1.xdiff = 3000 - pattern1.x
					pattern1.ydiff = 3000 - pattern1.y
					pattern1.angle = math.atan2(pattern1.ydiff, pattern1.xdiff)
					pattern1.y += int(math.sin(pattern1.angle) * pattern1.speed)
					pattern1.x += int(math.cos(pattern1.angle) * pattern1.speed)
				else:
					enemyattackpattern1.pop(enemyattackpattern1.index(pattern1))

		if jet.health < 0:
			jet.destroy()
			playerhp = 0
			movement = False
			lose = True
			enemyshoot = False
			enemymovement = False
			playerhit = False
			playershoot = False
			for lazer in enemybullets:
				enemybullets.pop(enemybullets.index(lazer))
			for bullet in bullets:
				bullets.pop(bullets.index(bullet))
			for pattern1 in enemyattackpattern1:
				enemyattackpattern1.pop(enemyattackpattern1.index(pattern1))
			for pattern2 in enemyattackpattern2:
				enemyattackpattern2.pop(enemyattackpattern2.index(pattern2))


#Movement
		if movement:
			key = pygame.key.get_pressed()	
			if key[pygame.K_LEFT]:
				jet.x -= jet.speed
			elif key[pygame.K_RIGHT]:
				jet.x += jet.speed
			if key[pygame.K_UP]:
				jet.y -= jet.speed
			elif key[pygame.K_DOWN]:
				jet.y += jet.speed
			if key[pygame.K_LSHIFT]:
				if stamina > 0:
					jet.speed = 25
					stamina -= 4
				else:
					jet.speed = 15
			else:
				stamina += 1
				jet.speed = 15

			if stamina < 0:
				stamina = 0
			if stamina > 50:
				stamina = 50

#HealthBoost
		if boostfalldown == True:
			if jet.health < 600:
				hpboost.y += hpboost.speed
		if hpboost.y > 800:
			boost = False
		if hpboost.y - 100 < (jet.hitbox[1] + jet.hitbox[3]) and hpboost.y+100 > jet.hitbox[1]:
			if hpboost.x - 100 < (jet.hitbox[0] + jet.hitbox[2]) and hpboost.x + 100 > jet.hitbox[0]:
				if stopboosting == True:
					jet.health = jet.health + hpboost.heal
					stopboosting = False
					boost = False


#Bullet setup(player)
		if playershoot == True:
			if key[pygame.K_w]:
				if len(bullets) < 8:
					bullets.append(player_projectile(jet.x + 130, jet.y, 6, (0,255,0)))

#Bullet setup(enemy)
		if enemyshoot == True:
			if len(enemybullets) < 15:
				enemybullets.append(enemy_projectile(badass.x + 210, badass.y + 300 , 6, (255,0,0)))
			if len(enemyattackpattern1) < 10:
				enemyattackpattern1.append(attack_pattern1(badass.x + 220, badass.y + 310 , 6, (255,0,0)))
		
		
#Screen borders
		if jet.x > 1250:
			jet.x = 1250
		elif jet.x < 0:
			jet.x = 0
		if jet.y > 550:
			jet.y = 550
		elif jet.y < 0:
			jet.y = 0

#Score
		if score < 0:
			score = 0
	
#Update
		redraweverything()
		pygame.display.update()

#Losescreen
		if lose:
			pause = False
			winlose = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_m:
					mainmenue = True
					gamestart = False
				if event.key == pygame.K_r:
					jet.display = True
					jet.health = 1500
					movement = True
					playerhp = 1500
					enemyhp = 8000
					badass.health = 8000
					jet.x = 0
					jet.y = 500
					badass.x = -100
					badass.y = -100
					hpboost.x = random.randint(50,1200)
					hpboost.y = -150
					jet.draw(screen)
					badass.draw(screen)
					hpboost.draw(screen)
					lose = False
					win = False
					enemyshoot = True
					enemymovement = True
					playershoot = True
					pause = False
					playerhit = True
					winlose = True
					boost = True
					stopboosting = True
					boostfalldown = True
					score = 0
					stamina = 50

			losescreen()
			pygame.display.update()

#Winscreen
		if win:
			pause = False
			winlose = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_m:
					mainmenue = True
					gamestart = False
				if event.key == pygame.K_r:
					jet.display = True
					jet.health = 1500
					movement = True
					playerhp = 1500
					enemyhp = 8000
					badass.health = 8000
					jet.x = 0
					jet.y = 500
					badass.x = -100
					badass.y = -100
					hpboost.x = random.randint(50,1200)
					hpboost.y = -150
					jet.draw(screen)
					badass.draw(screen)
					hpboost.draw(screen)
					lose = False
					win = False
					badass.display = True
					enemymovement = True
					enemyshoot = True
					enemymovement = True
					playershoot = True
					pause = False
					playerhit = True
					winlose = True
					boost = True
					stopboosting = True
					boostfalldown = True
					score = 0
					stamina = 50

			winscreen()
			pygame.display.update()

#Pausescreen
		if winlose == True:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					pause = True
				if event.key == pygame.K_s:
					movement = True
					enemymovement = True
					enemyshoot = True
					playershoot = True
					pause = False
					playerhit = True
					boostfalldown = True

			if pause == True:
				movement = False
				enemymovement = False
				enemyshoot = False
				playershoot = False
				playerhit = False
				boostfalldown = False
				pausescreen()

			pygame.display.update()
	
		


