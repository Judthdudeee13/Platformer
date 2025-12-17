import pygame

#set up music player
pygame.mixer.init()
pygame.mixer.music.set_volume(0.5)

#music 
class Music:
    #load music files
    def __init__(self):
        self.level1 = "a_slow_day.mp3"
        self.level_music = [self.level1]

    #load music
    def music(self, level):
        for level_music in self.level_music:
            if level == level_music:
                pygame.mixer.music.load(level_music)
            pygame.mixer.music.play(-1)
            
    #sound effects(for later)
    def sound_effect(self):
        pass
