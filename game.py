# Import and Initialisation
import pygame
from pygame.locals import *
pygame.init()
from gameSettings import GameSettings
from gameBoard import GameBoard
from scoreBoard import ScoreBoard
from ballGrid import BallGrid
from ball import Ball
from random import randint
import time
import multiprocessing as mp


# Set Up Game Object
class Game:
    def __init__(self):
        self.settings = GameSettings()
        self.scoreBoard = ScoreBoard(self.settings)
        self.gameBoard = GameBoard(self.settings)
        self.ballGrid = [[0 for x in range(self.settings.numberBallsH)] for y in range(self.settings.numberBallsV)]


    def create_balls(self):
        game.gameBoard.createBall(0,1,randint(1,game.level))
        game.gameBoard.createBall(1,1,randint(1,game.level))

    def get_player_balls(self):
        ret = []
        for i in self.gameBoard.allBalls:
            if i.isPlayer:
                ret.append(i)
        return ret

    def is_player_ball(self):
        for i in self.gameBoard.allBalls:
            if i.isPlayer:
                return True
        return False

    def clearPlayerBalls(self):
        balls = game.get_player_balls()
        for i in balls:
            i.isPlayer = False


game = Game()


# Display configuration
size = (int(game.settings.normalWidth * game.settings.scaleFactor), int(game.settings.normalHeight * game.settings.scaleFactor))
screen = pygame.display.set_mode(size)
screen.fill((255,255,255))
pygame.display.set_caption("Combine - F. Gnepper & D. Falkenstein")
game.gameBoard.graphics(screen)
game.scoreBoard.img(screen)
game.gameBoard.preloadBalls(game.settings)
background = pygame.image.load('images/background_1280X960.jpg')
background = pygame.transform.scale(background, (int(game.settings.normalWidth * game.settings.scaleFactor), int(game.settings.normalHeight * game.settings.scaleFactor)))
screen.blit(background, (0,0))

textfont = pygame.font.SysFont('Arial', int(48*game.settings.scaleFactor))

# Entities
game.level = 2
game.score = 0

# Action

# Assign Variables
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
        if event.type == KEYDOWN:
            if game.is_player_ball() and (event.key == K_DOWN or event.key == K_s):
                game.gameBoard.moveDown(game.get_player_balls())
                game.gameBoard.draw_grid(game.get_player_balls(), screen)
                time.sleep(0.2)
                pygame.display.flip()
                mergedBallChains = game.gameBoard.checkBursts(game.get_player_balls(),
                                                              game.settings.maxLevel, screen)  # check if balls are bursting, get chain of burst balls in return
                for chain in mergedBallChains:
                    for ball in chain:
                        game.score += game.settings.levelBallScore[ball.level]  # increase the score for each burst ball
                        if ball.level > game.level:
                            game.level = ball.level  # increase the level if level of merged ball is higher than game level
                if len(mergedBallChains) > 0:
                    game.scoreBoard.updateHighScore(game.score)
                game.clearPlayerBalls()  # set all balls to "unchecked"
                game.create_balls()  # create new player balls
            if event.key == K_UP or event.key == K_w:
                game.gameBoard.moveUp(game.get_player_balls(), game.settings.numberBallsH-1)
            if game.is_player_ball() and (event.key == K_LEFT or event.key == K_a):
                game.gameBoard.moveLeft(game.get_player_balls())
            if game.is_player_ball() and (event.key == K_RIGHT or event.key == K_d):
                game.gameBoard.moveRight(game.get_player_balls(), game.settings.numberBallsH-1)
            if event.key == K_INSERT:
                game.create_balls()
            if game.gameBoard.checkIfEnded(game.get_player_balls()) == True:
                game.scoreBoard.saveHighScore()
                gameRunning = False
                break
            print(game.score)

    # Redisplay
    screen.fill((0,0,0))
    screen.blit(background, (0,0))
    game.scoreBoard.img(screen)
    game.scoreBoard.graphics(screen, textfont, game.score)
    game.gameBoard.draw_grid(game.get_player_balls(), screen)

    pygame.display.flip()



