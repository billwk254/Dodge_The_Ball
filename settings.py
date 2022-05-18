import pygame
class Settings():
    """A class with the settings for the game """
    def __init__(self):
        self.screen_width = 1024
        self.screen_height = 700
        self.clock = pygame.time.Clock()
        self.bg_color = (51,51,51)
        self.playercolor = (255,255,255)
        self.red = (203,67,53)
        self.yellow = (241, 196, 15)
        self.blue = (46, 134, 193)
        self.green = (34, 153, 84)
        self.purple = (136, 78, 160)
        self.orange = (214, 137, 16)
        self.colors = [self.red,self.yellow,self.blue,self.green,self.purple,self.orange]
        self.score = 0