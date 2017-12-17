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
        self.scoreBoard = ScoreBoard(self.settings)
        self.gameBoard = GameBoard(self.settings)

game = Game()


# Display configuration
size = (int(game.settings.normalWidth * game.settings.scaleFactor), int(game.settings.normalHeight * game.settings.scaleFactor))
screen = pygame.display.set_mode(size)
screen.fill((255,255,255))
pygame.display.set_caption("Combine - F. Gnepper & D.Falkenstein")
game.gameBoard.graphics(game.settings)
game.scoreBoard.graphics()
game.gameBoard.preloadBalls(game.settings)
background = pygame.image.load('images/background_1280X960.jpg')
background = pygame.transform.scale(background, (int(game.settings.normalWidth * game.settings.scaleFactor), int(game.settings.normalHeight * game.settings.scaleFactor)))
screen.blit(background, (0,0))

# Entities

# Action

# Assign Variables
game.level = 2
gameRunning = True
clock = pygame.time.Clock()


# Loop
playerBallPos = game.gameBoard.createRandomBalls(game.level)

while gameRunning:
    # Timer
    clock.tick(30)
    game.gameBoard.drawUpperGrid(game.settings)

    # Event Handling
    for event in pygame.event.get():
        if event.type == QUIT:
            gameRunning = False
            break
        if event.type == KEYDOWN:
            if event.key == K_DOWN or event.key == K_s:
                print("down")
            if event.key == K_UP or event.key == K_w:
                print("up")
            if event.key == K_LEFT or event.key == K_a:
                game.gameBoard.moveLeft(playerBallPos)
            if event.key == K_RIGHT or event.key == K_d:
                game.gameBoard.moveRight(playerBallPos, game.settings.numberBallsH)

    screen.blit(game.gameBoard.surface, (0, 0))
    screen.blit(game.scoreBoard.surface, (int(size[0]*0.5), 0))
    # Redisplay
    pygame.display.update()

