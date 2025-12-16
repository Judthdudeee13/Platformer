# Platformer Game

A 2D platformer game built with Python and Pygame.

## Overview

This is a tile-based platformer game that uses sprite sheets for graphics and JSON-based level definitions.

## Project Structure

- `main.py` - Main game loop and window setup
- `level.py` - Level loading and tile management classes
- `sprites.py` - SpriteSheet class for extracting sprites from sprite sheets
- `levels.json` - Level configuration and tile data
- `spritesheet.png` - Sprite sheet containing game graphics

## Running the Game

The game runs via VNC display since it's a graphical Pygame application:

```bash
python main.py
```

## Technical Details

- Window size: 800x800 pixels
- FPS: 80
- Framework: Pygame 2.6.1
- Python: 3.11

## Development Notes

- The `tile` class handles sprite extraction from the sprite sheet based on tile ID
- The `Level` class loads level data from `levels.json` and manages tile rendering
- Levels are organized in layers (e.g., "Background")
