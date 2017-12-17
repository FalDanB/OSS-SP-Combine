import pygame
from pygame.locals import *

class GameBoard:

    def __init__(self, normalWidth, normalHeight, scaleFactor):
        self.width = int(normalWidth * scaleFactor * 0.5)
        self.height = int(normalHeight * scaleFactor)
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA, 32)
        #backgroundIMG = pygame.image.load("images/background1.jpg")
        #backgroundIMG = pygame.transform.scale(backgroundIMG, (numberBallsH*50,(numberBallsV+2)*50))
        #self.surface.blit(backgroundIMG, (0,0))

    def graphics(self):
        overlgame = pygame.image.load("images/overlgame.png").convert_alpha()
        overlgame = pygame.transform.scale(overlgame, (self.width, self.height))
        self.surface.blit(overlgame, (0, 0))

