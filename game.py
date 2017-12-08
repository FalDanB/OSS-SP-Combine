# Import and Initialisation
import pygame
from pygame.locals import *
pygame.init()

from gameSettings import GameSettings
from gameBoard import GameBoard
from scoreBoard import ScoreBoard

# Set Up Game Object
class Game:
    def __init__(self):
        self.settings = GameSettings()
        self.scoreBoard = ScoreBoard(self.settings.numberBallsH)
        self.gameBoard = GameBoard(self.settings.numberBallsH, self.settings.numberBallsV)
game = Game()


# Display configuration
size = (game.settings.numberBallsH*50, (game.settings.numberBallsV+2)*50+50)
screen = pygame.display.set_mode(size)
screen.fill((255,255,255))
pygame.display.set_caption("Combine - F. Geppner & D.Falkenstein")



# Entities

# Action

# Assign Variabeles
gameRunning = True
clock = pygame.time.Clock()

# Loop
while gameRunning:
    # Timer
    clock.tick(30)

    # Event Handling
    for event in pygame.event.get():
        if event.type == QUIT:
            gameRunning = False
            break
    screen.blit(game.scoreBoard.surface, (0,0))
    screen.blit(game.gameBoard.surface, (0,50))
    # Redisplay
    pygame.display.update()

