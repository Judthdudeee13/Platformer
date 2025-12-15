import pygame
import json

with open("levels.json", "r") as file:
    level_info = json.load(file)

TILE_SIZE = level_info["tileSize"]

MAP_WIDTH = level_info["mapWidth"]

MAP_HEIGHT = level_info["mapHeight"]

BACKGROUND = level_info["layers"][1]["tiles"]

print(BACKGROUND)