# Import and Initialisation
import pygame
from pygame.locals import *
pygame.init()
from gameSettings import GameSettings
from gameBoard import GameBoard
from scoreBoard import ScoreBoard
from ball import Ball


# Set Up Game Object
class Game:
    def __init__(self):
        self.settings = GameSettings()
        self.scoreBoard = ScoreBoard(self.settings)
        self.gameBoard = GameBoard(self.settings)
        self.allballs = []

    def create_ball(self):
        ball1 = Ball()
        ball2 = Ball()
        ball2.x = 1
        ball2.level = 2
        ball2.isLeft = False
        self.allballs.append(ball1)
        self.allballs.append(ball2)

    def get_player_balls(self):
        ret = []
        for i in self.allballs:
            if i.isPlayer and i.isLeft:
                ret.append(i)
            elif i.isPlayer and not i.isLeft:
                ret.append(i)
        return ret

    def is_player_ball(self):
        for i in self.allballs:
            if i.isPlayer:
                return True
        return False


game = Game()


# Display configuration
size = (int(game.settings.normalWidth * game.settings.scaleFactor), int(game.settings.normalHeight * game.settings.scaleFactor))
screen = pygame.display.set_mode(size)
screen.fill((255,255,255))
pygame.display.set_caption("Combine - F. Gnepper & D.Falkenstein")
game.gameBoard.graphics(screen)
game.scoreBoard.graphics(screen)
game.gameBoard.preloadBalls(game.settings)
background = pygame.image.load('images/background_1280X960.jpg')
background = pygame.transform.scale(background, (int(game.settings.normalWidth * game.settings.scaleFactor), int(game.settings.normalHeight * game.settings.scaleFactor)))
screen.blit(background, (0,0))

# Entities

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
                check_value = game.gameBoard.moveDown(game.get_player_balls())
                if check_value == 1:
                    game.create_ball()
                elif check_value == 2:
                    print "Ende"
            if event.key == K_UP or event.key == K_w:
                print("up")
            if game.is_player_ball() and (event.key == K_LEFT or event.key == K_a):
                game.gameBoard.moveLeft(game.get_player_balls())
            if game.is_player_ball() and (event.key == K_RIGHT or event.key == K_d):
                game.gameBoard.moveRight(game.get_player_balls())
            if event.key == K_INSERT:
                game.create_ball()

    # Redisplay
    screen.fill((0,0,0))
    screen.blit(background, (0,0))
    game.scoreBoard.graphics(screen)
    game.gameBoard.draw_grid(game.get_player_balls(), screen)

    pygame.display.flip()



