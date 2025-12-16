#call pygame and python modules
import pygame, time
#other files
import level
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

# colors
BLACK = "#000000"
WHITE = "#ffffff"
RED = "#ff0000"
GREEN = "#00ff00"
BLUE = "#0000ff"
ORANGE = "#ffa500"
YELLOW = "#ffff00"
PURPLE = "#800080"

#set up background
background = level.Level(window, "Background", HEIGHT, WIDTH)
background.load()


# main loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #update display
    pygame.display.update()
    #runs at 80 FPS
    CLOCK.tick(80)


# quit pygame(nothing else below)
pygame.quit()