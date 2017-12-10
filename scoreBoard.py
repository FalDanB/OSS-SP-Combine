import pygame
from pygame.locals import *

class ScoreBoard():
    def __init__(self, normalWidth, normalHeight, scaleFactor):
        self.width = int(normalWidth * scaleFactor * 0.5)
        self.height = int(normalHeight * scaleFactor)
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA, 32)

    def graphics(self):
        overlscore = pygame.image.load("images/overlscore.png").convert_alpha()
        overlscore = pygame.transform.scale(overlscore, (self.width, self.height))
        self.surface.blit(overlscore, (0, 0))


