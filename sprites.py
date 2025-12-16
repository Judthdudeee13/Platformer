import pygame

pygame.init()

class SpriteSheet:
    def __init__(self, filename):
        # Load the sheet and convert with alpha for transparency
        self.sheet = pygame.image.load(filename).convert_alpha()

    def get_image(self, x, y, width, height):
        # Create a new blank surface for the individual sprite
        image = pygame.Surface([width, height]).convert_alpha()
        # Copy the specific section of the spritesheet onto the new surface
        image.blit(self.sheet, (0, 0), (x, y, width, height))
        # Return the extracted image
        return image

# Example Usage:
# ss = SpriteSheet('my_spritesheet.png')
# # Extract a sprite located at (0, 0) with a width of 32 and height of 32
# sprite = ss.get_image(0, 0, 32, 32)


