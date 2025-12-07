import pygame, time
from pygame.locals import *
pygame.init()
CLOCK = pygame.time.Clock()

# set up window size

HEIGHT = 800
WIDTH = 800

jump_count = 2

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


gravity_var = True
jump_var = True

# charater
player = pygame.image.load("character_plat.png")
p = player.get_rect()
p.centerx = 250
p.centery = 250
p_mask = pygame.mask.from_surface(player)
def draw_floor():
    global ground
    global g
    global g_mask 
    ground = pygame.image.load("ground.png")
    g = ground.get_rect()
    g.topleft = (0, 700)
    g_mask = pygame.mask.from_surface(ground)
    window.blit(ground, g)

class platforms:
    def __init__ (self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def load_platform(self):
        platform = pygame.image.load(self.image)
        platform_rect = platform.get_rect()
        platform_rect.x = self.x
        platform_rect.y = self.y
        window.blit(platform, platform_rect)
    
        global gravity_var
        global jump_count
        global jump_var

        offset_x = platform_rect.x - p.x
        offset_y = platform_rect.y - p.y
        platform_mask = pygame.mask.from_surface(platform)
        if p_mask.overlap(platform_mask, (platform_rect.x - p.x, platform_rect.y - p.y)):
            p.y -= 1
            gravity_var = False
        elif p_mask.overlap(platform_mask, ((platform_rect.x - 1) - p.x, (platform_rect.y - 1) - p.y)):
            gravity_var = False
            jump_count = 2
            jump_var = True
        if offset_y > -50 and offset_y < -25 and offset_x < 29 and offset_x > -200:
            p.y += 1
            gravity_var = True
            jump_var = False






def collison_detection():
    global jump_count
    global jump_var
    if p_mask.overlap(g_mask, (g.x - p.x, g.y - p.y)):
        p.y -= 1
    elif p_mask.overlap(g_mask, ((g.x - 1) - p.x, (g.y - 1) - p.y)):
       p.y += 0
       jump_count = 2
       jump_var = True

def player_move():
    global p
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        p.centerx += 2
        
    if keys[pygame.K_a]:
        p.centerx -= 2

    # gravity
    collison_detection()
    
def gravity():
    if not p_mask.overlap(g_mask, ((g.x - 1) - p.x, (g.y - 1) - p.y)) and not p_mask.overlap(g_mask, (g.x - p.x, g.y - p.y)):
        p.y += 5

def jump():
    global jump_var
    keys = pygame.key.get_pressed()
    global jump_count
    if keys[K_w] and jump_count > 0:
        for x in range(30):
            if jump_var:
                p.y -= 5
            jump_var = True
            window.fill(WHITE)
            collison_detection()
            player_move()
            draw_floor()
            platform1.load_platform()
            platform2.load_platform()
            platform3.load_platform()
            platform4.load_platform()
            platform5.load_platform()

            window.blit(player, p)
            pygame.display.update()
            CLOCK.tick(80)
        jump_count -= 1

platform1 = platforms(400, 600, "platform_1.png")
platform2 = platforms(500, 200, "platform_1.png")
platform3 = platforms(350, 400, "platform_1.png")
platform4 = platforms(690, 200, "platform_1.png")
platform5 = platforms(690, 500, "platform_1.png")

# main loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
    
    window.fill(WHITE)
    draw_floor()
    platform1.load_platform()
    platform2.load_platform()
    platform3.load_platform()
    platform4.load_platform()
    platform5.load_platform()

    player_move()
    jump()
    if gravity_var:
        gravity()
    gravity_var = True
    window.blit(player, p)


    pygame.display.update()
    CLOCK.tick(80)


# quit pygame(nothing else below)
pygame.quit()