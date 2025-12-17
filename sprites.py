import pygame

pygame.init()

class SpriteSheet:
    def __init__(self, filename):
        # Load the sheet and convert with alpha for transparency
        self.sheet = pygame.image.load(filename).convert_alpha()

    #makes new image 
    def get_image(self, x, y, width, height):
        #makes rect of tile area
        rect = pygame.Rect(x*width, y*height, width, height)
        #pulls rect from image
        image = self.sheet.subsurface(rect)
        return image

# Example Usage:
# ss = SpriteSheet('my_spritesheet.png')
# # Extract a sprite located at (0, 0) with a width of 32 and height of 32
# sprite = ss.get_image(0, 0, 32, 32)


