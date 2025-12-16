import math
import pygame
import json
import sprites

#class for makeing tiles re-usable
class tile:
    def __init__(self, id, tile_size, new_width, new_height):
        #find the width of the image
        sprite_sheet_width = pygame.image.load("spritesheet.png").get_width()
        number_of_tiles_in_a_row = sprite_sheet_width/tile_size

        y = math.floor(id/number_of_tiles_in_a_row)
        x = id % number_of_tiles_in_a_row
        
        self.sprite_sheet = sprites.SpriteSheet("spritesheet.png")
        self.tile = self.sprite_sheet.get_image(x, y, tile_size, tile_size)
        self.tile = pygame.transform.scale(self.tile, (new_width, new_height))
        self.tile_rect = self.tile.get_rect()
    

#class to create background
class Level:
    def __init__(self, window, layer, height, width):

        self.window = window

        with open("levels.json", "r") as file:
            self.level_info = json.load(file)

        #level info
        self.TILE_SIZE = self.level_info["tileSize"]
        self.MAP_WIDTH = self.level_info["mapWidth"]
        self.WINDOW_WIDTH = width/self.MAP_WIDTH
        self.MAP_HEIGHT = self.level_info["mapHeight"]
        self.WINDOW_HEIGHT = height/self.MAP_HEIGHT
        #finds what area the list that contains the tiles are on
        for x in range(len(self.level_info["layers"])):
            if self.level_info["layers"][x]["name"] == layer:
                self.list_val = x

        self.LEVEL = self.level_info["layers"][self.list_val]["tiles"]
        
        

    #function to load background
    def load(self):
        tiles = []
        

