import pygame
from pygame.locals import *

class ScoreBoard:
    def __init__(self, settings):
        self.width = int(settings.normalWidth * settings.scaleFactor * 0.5)
        self.height = int(settings.normalHeight * settings.scaleFactor)

    def graphics(self, screen):
        overlscore = pygame.image.load("images/overlscore2.png").convert_alpha()
        overlscore = pygame.transform.scale(overlscore, (self.width-10, self.height))
        screen.blit(overlscore, (self.width+10, 0))



