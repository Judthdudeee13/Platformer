import pygame

class Player:
    def __init__(self, image, size, window):
        self.image = pygame.transform.scale(pygame.image.load(image), (size, size))
        self.rect = self.image.get_rect()
        self.window = window
    def load(self):
        self.rect.x = 40
        self.rect.y = 720
        self.window.blit(self.image, self.rect)