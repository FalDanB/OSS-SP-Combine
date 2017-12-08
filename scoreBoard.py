import pygame
from pygame.locals import *

class ScoreBoard():
    def __init__(self, numberBallsH):
        self.surface = pygame.Surface((numberBallsH*50,50))
        self.surface.fill((0,0,0))


