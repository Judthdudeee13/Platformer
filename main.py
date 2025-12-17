#call pygame and python modules
import pygame, time
#other files
import level, player, music
#call document for platformer levels
import json


#set up pygame
pygame.init()

#fps for game
CLOCK = pygame.time.Clock()

# set up window size
HEIGHT = 800
WIDTH = 800

#set up window
window = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("platformer")

#set up background
background = level.Level(window, "Background", HEIGHT, WIDTH)

#load level1
level_1 = level.Level(window, "Level_1", HEIGHT, WIDTH)

#load player
player1 = player.Player("player.png", 40, window)

background.load()
level_1.load()

#load and play music
sounds = music.Music()
sounds.music(sounds.level1)




# main loop
run = True
while run:
    #check all key inputs
    keys = pygame.key.get_pressed()

    #check for key presses
    if keys[pygame.K_w]:
        player1.move('up')
    if keys[pygame.K_s]:
        player1.move('down')
    if keys[pygame.K_a]:
        player1.move('left')
    if keys[pygame.K_d]:
        player1.move('right')
    
    #load everything
    background.load()
    level_1.load()
    player1.load()

    #update display
    pygame.display.flip()
    #runs at 80 FPS
    CLOCK.tick(60)

    #close pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

# quit pygame(nothing else below)
pygame.quit()