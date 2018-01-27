#Game Board for Combine Game

import pygame
from ballGrid import BallGrid
from ball import Ball
import time

class GameBoard:

    def __init__(self, settings):
        self.width = int(settings.normalWidth * settings.scaleFactor * 0.5)
        self.height = int(settings.normalHeight * settings.scaleFactor)
        self.ballsWidth = settings.numberBallsH
        self.ballsHeight = settings.numberBallsV
        self.ballDimension = settings.ballDimension*settings.scaleFactor
        self.ballGrid = BallGrid(self.ballsWidth, self.ballsHeight+2)
        self.ballImages = []
        self.allBalls = []
        self.ball_down = 0

    #preloads the ball images
    def preloadBalls(self, settings):
        self.ball_down = pygame.image.load("images/ball_down.png").convert_alpha()
        self.ball_down = pygame.transform.scale(self.ball_down, (int(self.ballDimension), int(self.ballDimension)))
        for i in range(len(settings.ballColours)):
            if i > 0:
                image = pygame.image.load("images/ball_"+ settings.ballColours[i]+".png").convert_alpha()
                image = pygame.transform.scale(image,(int(self.ballDimension),int(self.ballDimension)))
                self.ballImages.append(image)

    #draws the game board overlay
    def graphics(self, screen):
        overlgame = pygame.image.load("images/overlgame2.png").convert_alpha()
        overlgame = pygame.transform.scale(overlgame, (self.width, int(self.height*0.865)))
        screen.blit(overlgame, (10, 30))

    # creates two random balls based on current game level
    def createRandomBalls(self, level):
        balls = self.ballGrid.createRandomBalls(level)
        x = int(self.ballsWidth/2)   # Get Starting Point for new ball in row 2, midscreen
        self.ballGrid.grid[1][x] = balls[0]
        self.ballGrid.grid[1][x+1] = balls[1]
        return [[x,1], [x+1,1]]  #return ball positions for movements later

    # creates a Ball
    def createBall(self, x=0, y=0, level=1):
        ball = Ball(x,y,level)
        self.allBalls.append(ball)
        if y>= 2:
            self.ballGrid.grid[y][x] = level

    #moves player balls to the left
    def moveLeft(self, balls):
        if balls[0].x > 0 and balls[1].x > 0: #move only if no ball at left edge
            balls[0].x = balls[0].x - 1
            balls[1].x = balls[1].x - 1

    #moves player balls to the right
    def moveRight(self, balls, maxX):
        if maxX > balls[0].x and maxX > balls[1].x: #move only if no ball at right edge
            balls[0].x = balls[0].x + 1
            balls[1].x = balls[1].x + 1

    #rotates player balls
    def moveUp(self, balls, maxX):
        #stack balls vertically if horizontally aligend
        if balls[0].x > balls[1].x:
            balls[0].x -= 1
            balls[0].y -= 1
        elif balls[1].x > balls[0].x:
            balls[1].x -= 1
            balls[1].y -= 1
        #stack balls horizontally if vertically aligend
        elif balls[0].x == balls[1].x:
            if balls[1].y > balls[0].y:
                balls[0].y += 1
                balls[1].x += 1
            elif balls[0].y > balls[1].y:
                balls[1].y += 1
                balls[0].x += 1
        if balls[0].x > maxX or balls[1].x > maxX: #correct if balls exceed space on the right
            balls[0].x -= 1
            balls[1].x -= 1

    #intiates dropping of player balls
    def moveDown(self, balls):
        if balls[0].y < balls[1].y:
            self.dropBall(balls[1])
            self.dropBall(balls[0])
        else:
            self.dropBall(balls[0])
            self.dropBall(balls[1])

    #drops a ball on top of the stack
    def dropBall(self, ball):
        newY = self.getStackHeight(ball.x)
        self.ballGrid.grid[newY-1][ball.x] = ball.level
        ball.y = newY-1

    #returns a ball based on its x and y positions
    def getBall(self, x, y):
        for ball in self.allBalls:
            if ball.x == x and ball.y == y:
                return ball
        return 0

    #returns the height of a ball stack / column
    def getStackHeight(self, x):
        for i in range(0, len(self.ballGrid.grid)):
            if (self.ballGrid.grid[i][x] > 0):
                return i
        return len(self.ballGrid.grid)

    #check if the game has ended
    def checkIfEnded(self, balls):
        for i in range(0, len(self.ballGrid.grid[0])):
            if self.ballGrid.grid[1][i] > 0:
                return True
        return False

    #checks if at least three balls of the same colour are combined and to be burst
    def checkBursts(self, newBalls, maxLevel, screen):
        ball0Chain=[newBalls[0]]        # array holding chain of same colour balls for ball 0
        ball1Chain=[newBalls[1]]        # array holding chain of same colour balls for ball 1
        mergedBallChains = []           # array holding all chains with more than 3 balls
        newBalls[0].checked = True
        self.checkNeighbours(newBalls[0],ball0Chain)
        if newBalls[1].checked == False: #get the chain for Ball1 only if not already checked
            newBalls[1].checked = True
            self.checkNeighbours(newBalls[1],ball1Chain)
        collapse = False
        if len(ball0Chain) >= 3:
            self.removeBalls(ball0Chain, screen)
            self.createMergedBall(ball0Chain, maxLevel)
            collapse = True
            mergedBallChains.append(ball0Chain)
        if len(ball1Chain) >= 3:
            self.removeBalls(ball1Chain, screen)
            self.createMergedBall(ball1Chain, maxLevel)
            collapse = True
            mergedBallChains.append(ball1Chain)
        self.clearChecked() #set all balls to unchecked
        if collapse:
            self.collapseColumns()
            self.checkAllBalls(maxLevel, mergedBallChains, screen)
        return mergedBallChains

    def checkNeighbours(self, ball, chain):
        #Check Ball on Left
        for i in ["left", "right", "up", "down"]: #define routine for four neighbouring directions
            deltaX = 0
            deltaY = 0
            check = False
            if i == "left":
                #print("Checking ball on left")
                deltaX = -1
                if ball.x > 0 and self.ballGrid.grid[ball.y + deltaY][ball.x+deltaX] > 0:
                    check = True
            elif i == "right":
                #print("Checking ball on right")
                deltaX = 1
                if ball.x < len(self.ballGrid.grid[0])-1 and self.ballGrid.grid[ball.y + deltaY][ball.x+deltaX] > 0:
                    check = True
            elif i == "up":
                #print("Checking ball on top")
                deltaY = -1
                if ball.y > 2 and self.ballGrid.grid[ball.y + deltaY][ball.x+deltaX] > 0:
                    check = True
            elif i == "down":
                #print("Checking ball on bottom")
                deltaY = 1
                if ball.y < len(self.ballGrid.grid)-1 and self.ballGrid.grid[ball.y + deltaY][ball.x+deltaX] > 0:
                    check = True
            if check:
                #print("check")
                #print ("ball " + str(i) + ": " + str(self.ballGrid.grid[ball.y+deltaY][ball.x+deltaX]))
                if self.ballGrid.grid[ball.y+deltaY][ball.x+deltaX] == ball.level:  # Check if ball has same Level
                    #print("Same Level!")
                    neighbourBall = self.getBall(ball.x+deltaX, ball.y+deltaY)
                    if neighbourBall != 0:
                        if neighbourBall.checked == False: #Continue only if ball has not already been checked
                            #print("ball not yet checked")
                            neighbourBall.checked = True
                            chain.append(neighbourBall)
                            self.checkNeighbours(neighbourBall,chain)

    #draws the ball grid
    def draw_grid(self, plBalls, screen):
        if len(plBalls) > 0:
            screen.blit(self.ballImages[plBalls[0].level-1], (plBalls[0].x*self.ballDimension + 20, plBalls[0].y*self.ballDimension + 40))
            screen.blit(self.ballImages[plBalls[1].level-1], (plBalls[1].x * self.ballDimension + 20, plBalls[1].y * self.ballDimension + 40))
        counterx = 0
        countery = 0
        for i in self.ballGrid.grid:
            for j in i:
                if j > 0:
                    screen.blit(self.ballImages[j - 1], (counterx * self.ballDimension + 20, countery * self.ballDimension + 40))
                counterx = counterx + 1
            countery = countery + 1
            counterx = 0
        self.graphics(screen)

    #clear checked flag from all balls
    def clearChecked(self):
        for i in self.allBalls:
            i.checked = False

    #remove balls from grid, show cracked ball
    def removeBalls(self, chain, screen):
        for ballToRemove in chain:
            screen.blit(self.ball_down, (ballToRemove.x * self.ballDimension + 20, ballToRemove.y * self.ballDimension + 40))
            time.sleep(0.1)
            pygame.display.flip()
            self.ballGrid.grid[ballToRemove.y][ballToRemove.x] = 0 # remove from grid
            self.allBalls.remove(self.getBall(ballToRemove.x, ballToRemove.y)) #remove from Balls Array

    #Create a merged ball after ball burst
    def createMergedBall(self,chain, maxLevel):
        ballLevel = chain[0].level
        if ballLevel < maxLevel:
            bottomY = -1 # temp variable for position of most bottom ball
            for i in chain:
                if i.y > bottomY: #get position of most bottom ball
                    bottomY = i.y
                    bottomBall = i
                elif i.y == bottomY: #use right-most ball if more balls are on bottom
                    if i.x < bottomBall.x:
                        bottomBall = i
            self.createBall(bottomBall.x, bottomBall.y, bottomBall.level+1)

    #Collapse Columns after each bursting
    def collapseColumns(self):
        for colID in range(0,len(self.ballGrid.grid[0])): #loop through columns
            rowID = len(self.ballGrid.grid)-1 #loop through rows in reverse order (except top 2)
            while rowID>=2:
                if self.ballGrid.grid[rowID][colID] == 0:
                    ballFound = False
                    i = 1
                    while ballFound == False and rowID-i >= 2: #check spaces on top until ball has been found or top row is reached
                        if self.ballGrid.grid[rowID-i][colID] > 0:
                            ballFound = True
                            self.ballGrid.grid[rowID][colID] = self.ballGrid.grid[rowID-i][colID] # put ball level in empty space on grid
                            self.ballGrid.grid[rowID-i][colID] = 0 # clear old ball positin
                            ball = self.getBall(colID, rowID-i) # save the new position in ball object
                            ball.x = colID
                            ball.y = rowID
                        i+=1
                rowID-=1

    #check all balls in grid for burts
    def checkAllBalls(self, maxLevel, mergedBallChains, screen):
        #print("CheckAllBalls")
        chainFound = False
        for ball in self.allBalls:
            if ball.checked == False:
                chain = [ball]
                ball.checked = True
                self.checkNeighbours(ball, chain)
                # print("Chain length: " + str(len(chain)))
                #for ball in chain:
                    # print("X: " + str(ball.x) + " Y: " + str(ball.y) + " L: " + str(ball.level))
                if len(chain) >= 3:
                    self.removeBalls(chain, screen)
                    self.createMergedBall(chain, maxLevel)
                    chainFound = True
                    mergedBallChains.append(chain)
            self.collapseColumns()
            self.clearChecked()
        if chainFound == True:
            self.checkAllBalls(maxLevel, mergedBallChains, screen)

