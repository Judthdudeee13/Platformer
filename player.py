import pygame

#class for the players
class Player:
    #set up player
    def __init__(self, image, size, window):
        self.image = pygame.transform.scale(pygame.image.load(image), (size, size))
        self.rect = self.image.get_rect()
        self.window = window
        self.rect.x = 40
        self.rect.y = 720
    #load player
    def load(self):
        self.window.blit(self.image, self.rect)

    #move player
    def move(self, direction):
        if direction == 'left':
            self.rect.x -=2
            self.check_collisions()
        if direction == 'right':
            self.rect.x +=2
            self.check_collisions()
        if direction == 'up':
            self.rect.y -=2
            self.check_collisions()
        if direction == 'down':
            self.rect.y +=2
            self.check_collisions()
        
    #check collisions(for later)
    def check_collisions(self):
        pass

