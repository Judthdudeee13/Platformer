import math
import pygame
import json
import sprites

#class for makeing tiles re-usable
class tile:
    def __init__(self, tile_info, tile_size, new_width, new_height):
        #find the width of the image
        sprite_sheet_width = pygame.image.load("spritesheet.png").get_width()
        number_of_tiles_in_a_row = sprite_sheet_width/tile_size

        self.tile_info = tile_info

        #find which piece of the spritesheet this tile is
        id = self.tile_info["id"]
        
        #find x and y locations on spritesheet
        y = math.floor(int(id)/number_of_tiles_in_a_row)
        x = int(id) % number_of_tiles_in_a_row
        
        #pull image for tile
        self.sprite_sheet = sprites.SpriteSheet("spritesheet.png")
        self.tile = self.sprite_sheet.get_image(x, y, tile_size, tile_size)
        self.tile = pygame.transform.scale(self.tile, (new_width, new_height))
        #make and set tile postition
        self.tile_rect = self.tile.get_rect()
        self.tile_size = self.tile.get_width()
        self.tile_rect.x = self.tile_info["x"]*self.tile_size
        self.tile_rect.y = self.tile_info["y"]*self.tile_size

    #load tile on screen
    def load(self, window):
        window.blit(self.tile, self.tile_rect)

    

#class to create background
class Level:
    def __init__(self, window, layer, height, width):

        self.window = window
        #open file
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

        #get information for the level
        self.LEVEL = self.level_info["layers"][self.list_val]["tiles"]

        self.tiles = []
        #sets up tiles
        for x in range(len(self.LEVEL)):
            self.tiles.append(tile(self.LEVEL[x], self.TILE_SIZE, self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        
        

    #function to load tiles
    def load(self):            
        #loads tiles
        for y in self.tiles:
            y.load(self.window)

    def clear(self):
        for x in self.tiles:
            del x
        

