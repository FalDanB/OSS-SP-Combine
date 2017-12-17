import pygame
from ballGrid import BallGrid
import math
from pygame.locals import *

class GameBoard:

    def __init__(self, settings):
        self.width = int(settings.normalWidth * settings.scaleFactor * 0.5)
        self.height = int(settings.normalHeight * settings.scaleFactor)
        self.ballsWidth = settings.numberBallsH
        self.ballsHeight = settings.numberBallsV
        self.surface = pygame.Surface((self.width+10, self.height), pygame.SRCALPHA, 32)
        self.ballGridSurface= pygame.Surface((settings.numberBallsH*settings.scaleFactor*settings.ballDimension, (settings.numberBallsV+2)*settings.scaleFactor*settings.ballDimension+10), pygame.SRCALPHA, 32)
        self.ballGrid = BallGrid(self.ballsWidth, self.ballsHeight)


    def preloadBalls(self, settings):
        #Preload Balls
        #self.greenBall = pygame.image.load("images/ball_green.png")
        #self.yellowBall = pygame.image.load("images/ball_yellow.png")
        #self.orangeBall = pygame.image.load("images/ball_orange.png")
        #self.redBall = pygame.image.load("images/ball_red.png")
        #self.pinkBall = pygame.image.load("images/ball_pink.png")
        #self.purpleBall = pygame.image.load("images/ball_purple.png")
        #self.blueBall = pygame.image.load("images/ball_blue.png")
        #self.cyanBall = pygame.image.load("images/ball_cyan.png")
        #self.blackBall = pygame.image.load("images/ball_black.png")
        #self.whiteBall = pygame.image.load("images/ball_white.png")
        #self.ballImages(self.greenBall, self.yellowBall, self.)
        self.balls = []
        for i in range(len(settings.ballColours)):
            if i > 0:
                image = pygame.image.load("images/ball_"+ settings.ballColours[i]+".png").convert_alpha()
                image = pygame.transform.scale(image,(int(settings.ballDimension*settings.scaleFactor),int(settings.ballDimension*settings.scaleFactor)))
                self.balls.append(image)

    def graphics(self, settings):
        overlgame = pygame.image.load("images/overlgame2.png").convert_alpha()
        overlgame = pygame.transform.scale(overlgame, (self.width, int(self.height*0.865)))
        #ballGridRect = pygame.draw.rect(self.ballGridSurface, (0,0,0), (0,0,settings.numberBallsH*settings.scaleFactor*settings.ballDimension,(settings.numberBallsV+2)*settings.scaleFactor*settings.ballDimension))
        #testBall = pygame.image.load("images/ball_green.png").convert_alpha()
        #testBall = pygame.transform.scale(testBall,(int(settings.ballDimension*settings.scaleFactor),int(settings.ballDimension*settings.scaleFactor)))
        #self.ballGridSurface.blit(testBall,(0,0))
        #self.ballGridSurface.blit(testBall,(0,settings.ballDimension*settings.scaleFactor))
        #self.ballGridSurface.blit(testBall,(0,2*settings.ballDimension*settings.scaleFactor+10))
        #self.ballGridSurface.blit(testBall,(0,3*settings.ballDimension*settings.scaleFactor+10))
        #self.ballGridSurface.blit(testBall,(0,4*settings.ballDimension*settings.scaleFactor+10))
        #self.ballGridSurface.blit(testBall,(0,5*settings.ballDimension*settings.scaleFactor+10))
        #self.ballGridSurface.blit(testBall,(0,6*settings.ballDimension*settings.scaleFactor+10))
        #self.ballGridSurface.blit(testBall,(0,7*settings.ballDimension*settings.scaleFactor+10))
        #self.ballGridSurface.blit(testBall,(0,8*settings.ballDimension*settings.scaleFactor+10))
        #self.ballGridSurface.blit(testBall,(settings.ballDimension*settings.scaleFactor,8*settings.ballDimension*settings.scaleFactor+10))
        #self.ballGridSurface.blit(testBall,(2*settings.ballDimension*settings.scaleFactor,8*settings.ballDimension*settings.scaleFactor+10))
        #self.ballGridSurface.blit(testBall,(3*settings.ballDimension*settings.scaleFactor,8*settings.ballDimension*settings.scaleFactor+10))
        #self.ballGridSurface.blit(testBall,(4*settings.ballDimension*settings.scaleFactor,8*settings.ballDimension*settings.scaleFactor+10))
        #self.ballGridSurface.blit(testBall,(5*settings.ballDimension*settings.scaleFactor,8*settings.ballDimension*settings.scaleFactor+10))
        #self.ballGridSurface.blit(testBall,(6*settings.ballDimension*settings.scaleFactor,8*settings.ballDimension*settings.scaleFactor+10))
        #self.ballGridSurface.blit(testBall,(7*settings.ballDimension*settings.scaleFactor,8*settings.ballDimension*settings.scaleFactor+10))
        self.surface.blit(overlgame, (10, 30))
        self.surface.blit(self.ballGridSurface,(20,40))

    def createRandomBalls(self, level):
        balls = self.ballGrid.createRandomBalls(level)
        x = math.floor(self.ballsWidth/2)   # Get Starting Point for new ball in row 2, midscreen
        self.ballGrid.grid[1][x] = balls[0]
        self.ballGrid.grid[1][x+1] = balls[1]
        return [[x,1], [x+1,1]]  #return ball positions for movements later

    def moveLeft(self, pos):
        if pos[0][0] > 0 and pos[1][0] > 0:  #only if not at left border already
            pos[0][0] = pos[0][0]-1 # new position for ball 1
            pos[1][0] = pos[1][0]-1 # new position for ball 2
            if pos[0][0] <= pos[1][0]: # determine which ball goes first to prevent mutual overwriting
                self.ballGrid.grid[pos[0][1]][pos[0][0]] = self.ballGrid.grid[pos[0][1]][pos[0][0]+1] #apply new position of ball1 in grid
                self.ballGrid.grid[pos[0][1]][pos[0][0]+1] = 0 #clear old position of ball1 in grid
                self.ballGrid.grid[pos[1][1]][pos[1][0]] = self.ballGrid.grid[pos[1][1]][pos[1][0]+1] #apply new position of ball2 in grid
                self.ballGrid.grid[pos[1][1]][pos[1][0]+1] = 0 #apply new position of ball2 in grid
            else:
                self.ballGrid.grid[pos[1][1]][pos[1][0]] = self.ballGrid.grid[pos[1][1]][pos[1][0]+1] #apply new position of ball2 in grid
                self.ballGrid.grid[pos[1][1]][pos[1][0]+1] = 0 #apply new position of ball2 in grid
                self.ballGrid.grid[pos[0][1]][pos[0][0]] = self.ballGrid.grid[pos[0][1]][pos[0][0]+1] #apply new position of ball1 in grid
                self.ballGrid.grid[pos[0][1]][pos[0][0]+1] = 0 #clear old position of ball1 in grid


    def moveRight(self, pos, maxPos):
        print(self.ballGrid.grid)
        if pos[0][0] < maxPos-1 and pos[1][0] < maxPos-1:  #only if not at left border already
            pos[0][0] = pos[0][0]+1 # new position for ball 1
            pos[1][0] = pos[1][0]+1 # new position for ball 2
            if pos[0][0] >= pos[1][0]: # determine which ball goes first to prevent mutual overwriting
                self.ballGrid.grid[pos[0][1]][pos[0][0]] = self.ballGrid.grid[pos[0][1]][pos[0][0]-1] #apply new position of ball1 in grid
                self.ballGrid.grid[pos[0][1]][pos[0][0]-1] = 0
                self.ballGrid.grid[pos[1][1]][pos[1][0]] = self.ballGrid.grid[pos[1][1]][pos[1][0]-1] #apply new position of ball2 in grid
                self.ballGrid.grid[pos[1][1]][pos[1][0]-1] = 0
            else:
                self.ballGrid.grid[pos[1][1]][pos[1][0]] = self.ballGrid.grid[pos[1][1]][pos[1][0]-1] #apply new position of ball2 in grid
                self.ballGrid.grid[pos[1][1]][pos[1][0]-1] = 0
                self.ballGrid.grid[pos[0][1]][pos[0][0]] = self.ballGrid.grid[pos[0][1]][pos[0][0]-1] #apply new position of ball1 in grid
                self.ballGrid.grid[pos[0][1]][pos[0][0]-1] = 0

    def drawUpperGrid(self, settings):
        for i in range(2): # loop through first two rows of grid
            for j in range(len(self.ballGrid.grid[i])):
                if self.ballGrid.grid[i][j]>0:
                    ball = self.balls[self.ballGrid.grid[i][j]-1]
                    self.ballGridSurface.blit(ball,(j*settings.ballDimension*settings.scaleFactor,i*settings.ballDimension*settings.scaleFactor))
                    self.surface.blit(self.ballGridSurface,(20,40))

