from math import *
import pygame
import random
import game_functions as gf
import time

class Ball:
    """A class that creates the balls that the player aims to avoid and defines their movement on the screen"""
    def __init__(self,radius,speed,dodge_settings,screen):
        self.dodge_settings = dodge_settings
        self.screen = screen
        self.screen_width = dodge_settings.screen_width
        self.screen_height = dodge_settings.screen_height
        self.colors = dodge_settings.colors
        self.x = 0
        self.y = 0
        self.r = radius
        self.color = 0
        self.speed = speed
        self.angle = 0

    def createball(self):
        """A function that creates the balls and randomly assigns a color to them"""
        self.x = self.screen_width/2 - self.r
        self.y = self.screen_height/2 - self.r
        self.color = random.choice(self.colors)
        self.angle = random.randint(-180,180)

    def move(self):
        """a function that defines the balls movement on the screen and what happens when they hit the edges
        of the screen"""
        self.x += self.speed*cos(radians(self.angle))
        self.y += self.speed*sin(radians(self.angle))

        if self.x < self.r or self.x + self.r > self.screen_width:
            self.angle =180 -self.angle
        if self.y < self.r or self.y + self.r > self.screen_height:
            self.angle *= -1

    def draw(self):
        """A function that draws the balls onto the screen"""
        pygame.draw.ellipse(self.screen,self.color,(self.x - self.r,self.y -self.r,self.r*2,self.r*2))

    def collision(self,radius):
        """A functions that checks for collisions between the balls and the player ands calls the gameover function"""
        pos = pygame.mouse.get_pos()
        dist = ((pos[0] - self.x)**2 +(pos[1] -self.y)**2)**0.5
        if dist <= self.r + radius:
            gf.play_music("gameover.mp3")
            time.sleep(2)
            gf.gameover(self.screen,self.dodge_settings)



