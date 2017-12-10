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
        self.scoreBoard = ScoreBoard(self.settings.normalWidth, self.settings.normalHeight, self.settings.scaleFactor)
        self.gameBoard = GameBoard(self.settings.normalWidth, self.settings.normalHeight, self.settings.scaleFactor)

game = Game()


# Display configuration
size = (int(game.settings.normalWidth * game.settings.scaleFactor), int(game.settings.normalHeight * game.settings.scaleFactor))
screen = pygame.display.set_mode(size)
screen.fill((255,255,255))
pygame.display.set_caption("Combine - F. Gnepper & D.Falkenstein")
game.gameBoard.graphics()
game.scoreBoard.graphics()



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
    screen.blit(game.gameBoard.surface, (0, 0))
    screen.blit(game.scoreBoard.surface, (int(size[0]*0.5), 0))
    # Redisplay
    pygame.display.update()

