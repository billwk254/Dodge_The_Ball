import random
import pygame
class Target():
    """A class that contains methods for the target that the player is trying to hit while avoiding the balls"""
    def __init__(self,dodge_settings,screen):
        self.screen = screen
        self.colors =dodge_settings.colors
        self.screen_width = dodge_settings.screen_width
        self.screen_height = dodge_settings.screen_height
        self.x = 0
        self.y = 0
        self.w = 20
        self.h = self.w

    def generateNewCoord(self):
        """A function that generates a new random coordinate for the target"""
        self.x = random.randint(self.w,self.screen_width -self.w)
        self.y = random.randint(self.h, self.screen_height -self.h)

    def draw(self):
        """A function that draws the target onto the screen"""
        color = random.choice(self.colors)
        pygame.draw.rect(self.screen,color,(self.x,self.y,self.w,self.h))


