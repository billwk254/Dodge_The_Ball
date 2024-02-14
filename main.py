import pygame
import sys
import os
from settings import Settings
import game_functions as gf

def resource_path(relative_path):
    """
    Get absolute path to a resource
    :param relative_path:
    :return:
    """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
def start_game():
    """A function that starts the game"""
    pygame.init()
    dodge_settings = Settings()
    screen = pygame.display.set_mode((dodge_settings.screen_width,dodge_settings.screen_height))
    pygame.display.set_caption("Dodge The Ball")
    gf.gameloop(dodge_settings, screen)


start_game()