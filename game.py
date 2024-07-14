#import stuff
import pygame
from sys import exit

#prepare stuff
pygame.init() #very important

#import images
programIcon = pygame.image.load("graphics/icon.png")

background = pygame.image.load("background/background.png")

gameoverscreen = pygame.image.load("background/died.png")

secretending = pygame.image.load("background/secretending.png")

player = pygame.image.load("graphics/player.png")
player_rect = player.get_rect(midbottom = (200, 400))

enemy = pygame.image.load("graphics/enemy.png")
enemy_rect = enemy.get_rect(midbottom = (700, 400))

#prepare some other stuff idk about
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("very dangerous!")
pygame.display.set_icon(programIcon)
Clock = pygame.time.Clock() #haha fps limiter

#set up audio stuff
gamemusic = "music/dangerous.mp3"
secretmusic = "music/gigachad.mp3"
gameovermusic = "music/trololo.mp3"
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(gamemusic)
pygame.mixer.music.play(-1, 0.0, 0)

#variables
enemyspeed = 5
player_gravity = 0
groundlevel = 400
playerinair = 0
gameover = 0
enemyexhaustion = 0
musicplaying = 0

#inside game stuff
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    playery = player_rect.y

    screen.blit(background,(0, 0))
    screen.blit(player, player_rect)
    screen.blit(enemy, enemy_rect)

    enemy_rect.x -= enemyspeed

    keysdown = pygame.key.get_pressed()
    if keysdown[pygame.K_SPACE] and playerinair == 0 and gameover == 0:
        player_gravity = -25
        playerinair = 1

    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom > groundlevel:
        player_rect.bottom = groundlevel
        playerinair = 0

    if enemy_rect.right < 0:
        enemy_rect.left = 800
        enemyexhaustion += 1

    if player_rect.colliderect(enemy_rect):
        enemyspeed = 0
        player_gravity = 0
        playerinair = 0
        gameover = 1
        screen.blit(gameoverscreen, (0, 0))
        if musicplaying == 0:
            musicplaying = 1
            pygame.mixer.music.load(gameovermusic)
            pygame.mixer.music.play(-1, 0.0, 0)

    if enemyexhaustion == 10:
        enemyspeed = 0
        player_gravity = 0
        playerinair = 0
        gameover = 1
        screen.blit(secretending, (0, 0))
        if musicplaying == 0:
            musicplaying = 1
            pygame.mixer.music.load(secretmusic)
            pygame.mixer.music.play(-1, 0.0, 0)

    pygame.display.update()
    Clock.tick(60) #limit fps to 60