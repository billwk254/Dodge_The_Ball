import pygame
from settings import Settings
import game_functions as gf

def start_game():
    """A function that starts the game"""
    pygame.init()
    dodge_settings = Settings()
    screen = pygame.display.set_mode((dodge_settings.screen_width,dodge_settings.screen_height))
    pygame.display.set_caption("Dodge The Ball")
    gf.gameloop(dodge_settings, screen)


start_game()