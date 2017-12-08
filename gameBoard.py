import pygame
from pygame.locals import *

class GameBoard:

    def __init__(self, numberBallsH, numberBallsV):
        self.surface = pygame.Surface((numberBallsH*50,(numberBallsV+2)*60))
        backgroundIMG = pygame.image.load("images/background1.jpg")
        backgroundIMG = pygame.transform.scale(backgroundIMG, (numberBallsH*50,(numberBallsV+2)*50))
        self.surface.blit(backgroundIMG, (0,0))
        pygame.draw.line(self.surface, (255,0,0),(0,100),(numberBallsH*50,100), 1)

