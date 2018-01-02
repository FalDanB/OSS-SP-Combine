import pygame
from ballGrid import BallGrid
import time
from sets import Set


class GameBoard:

    def __init__(self, settings):
        self.width = int(settings.normalWidth * settings.scaleFactor * 0.5)
        self.height = int(settings.normalHeight * settings.scaleFactor)
        self.ballsWidth = settings.numberBallsH
        self.ballsHeight = settings.numberBallsV
        self.ballDimension = settings.ballDimension*settings.scaleFactor
        self.surface = pygame.Surface((self.width+10, self.height), pygame.SRCALPHA, 32)
        self.ballGrid = BallGrid(self.ballsWidth, self.ballsHeight)
        self.balls = []

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
        for i in range(len(settings.ballColours)):
            if i > 0:
                image = pygame.image.load("images/ball_"+ settings.ballColours[i]+".png").convert_alpha()
                image = pygame.transform.scale(image,(int(self.ballDimension),int(self.ballDimension)))
                self.balls.append(image)

    def graphics(self, screen):
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
        screen.blit(overlgame, (10, 30))

    def createRandomBalls(self, level):
        balls = self.ballGrid.createRandomBalls(level)
        x = int(self.ballsWidth/2)   # Get Starting Point for new ball in row 2, midscreen
        self.ballGrid.grid[1][x] = balls[0]
        self.ballGrid.grid[1][x+1] = balls[1]
        return [[x,1], [x+1,1]]  #return ball positions for movements later

    def check_left(self, ball):
        if ball[0].isLeft:
            if ball[0].x > 0:
                if self.ballGrid.grid[ball[0].y][ball[0].x-1] == 0:
                    return True
        if ball[1].isLeft:
            if ball[1].x > 0:
                if self.ballGrid.grid[ball[1].y][ball[1].x - 1] == 0:
                    return True
        return False

    def moveLeft(self, ball):
        if self.check_left(ball):
            ball[0].x = ball[0].x - 1
            ball[1].x = ball[1].x - 1

    def check_right(self, ball):
        if ball[0].isLeft:
            if ball[1].x < self.ballsWidth - 1:
                if self.ballGrid.grid[ball[1].y][ball[1].x + 1] == 0:
                    return True
        if ball[1].isLeft:
            if ball[0].x < self.ballsWidth - 1:
                if self.ballGrid.grid[ball[0].y][ball[0].x + 1] == 0:
                    return True
        return False

    def moveRight(self, ball):
        if self.check_right(ball):
            ball[0].x = ball[0].x + 1
            ball[1].x = ball[1].x + 1

    def check_down(self, ball):
        if ball[0].y < self.ballsHeight + 1:
            if self.ballGrid.grid[ball[0].y + 1][ball[0].x] == 0 and self.ballGrid.grid[ball[1].y + 1][ball[1].x] == 0:
                return True
        return False

    def check_near(self, ball):
        ret = Set([(ball[0].y, ball[0].x)])
        counter = 1
        checkforRound = False
        if ball[0].isLeft:
            if ball[0].level < len(self.balls):
                try:
                    if self.ballGrid.grid[ball[0].y+1][ball[0].x] == ball[0].level:
                        temp = self.check_second(ball[0].x, ball[0].y+1, "ulr", ball[0].level)
                        torem = 0
                        for i in temp:
                            if isinstance(i, (int, long)):
                                counter = counter + i
                                torem = i
                        temp.discard(torem)
                        ret.update(temp)
                except IndexError:
                    print "Nicht unten linker Ball"

                try:
                    if self.ballGrid.grid[ball[0].y][ball[0].x-1] == ball[0].level:
                        temp = self.check_second(ball[0].x - 1, ball[0].y, "uol", ball[0].level)
                        torem = 0
                        for i in temp:
                            if isinstance(i, (int, long)):
                                counter = counter + i
                                torem = i
                        temp.discard(torem)
                        ret.update(temp)
                except IndexError:
                    print "Nicht links"

                try:
                    if self.ballGrid.grid[ball[0].y-1][ball[0].x] == ball[0].level:
                        temp = self.check_second(ball[0].x, ball[0].y-1, "olr", ball[0].level)
                        torem = 0
                        for i in temp:
                            if isinstance(i, (int, long)):
                                counter = counter + i
                                torem = i
                        temp.discard(torem)
                        ret.update(temp)
                except IndexError:
                    print "Nicht oben linker Ball"

                if counter >= 3:
                    self.change_color(ball[0], ret)
                    checkforRound = True
            ##################################################Rechter Ball##########################################################
            if ball[1].level < len(self.balls):
                ret = Set([(ball[1].y, ball[1].x)])
                counter = 1
                try:
                    if self.ballGrid.grid[ball[1].y+1][ball[1].x] == ball[1].level:
                        temp = self.check_second(ball[1].x, ball[1].y + 1, "ulr", ball[1].level)
                        torem = 0
                        for i in temp:
                            if isinstance(i, (int, long)):
                                counter = counter + i
                                torem = i
                        temp.discard(torem)
                        ret.update(temp)
                except IndexError:
                    print "Nicht unten rechter Ball"

                try:
                    if self.ballGrid.grid[ball[1].y][ball[1].x+1] == ball[1].level:
                        temp = self.check_second(ball[1].x + 1, ball[1].y, "uor", ball[1].level)
                        torem = 0
                        for i in temp:
                            if isinstance(i, (int, long)):
                                counter = counter + i
                                torem = i
                        temp.discard(torem)
                        ret.update(temp)
                except IndexError:
                    print "Nicht rechts"

                try:
                    if self.ballGrid.grid[ball[1].y-1][ball[1].x] == ball[1].level:
                        temp = self.check_second(ball[1].x, ball[1].y - 1, "olr", ball[1].level)
                        torem = 0
                        for i in temp:
                            if isinstance(i, (int, long)):
                                counter = counter + i
                                torem = i
                        temp.discard(torem)
                        ret.update(temp)
                except IndexError:
                    print "Nicht oben"
                if counter >= 3:
                    self.change_color(ball[1], ret)
                    checkforRound = True
        return checkforRound

    def check_second(self, x, y, flags, level):
        ret = Set([(y, x)])
        counter = 1
        if "u" in flags:
            try:
                if self.ballGrid.grid[y + 1][x] == level and (y+1, x) not in ret:
                    temp = self.check_second(x, y+1, "ulr", level)
                    torem = 0
                    for i in temp:
                        if isinstance(i, (int, long)):
                            counter = counter + i
                            torem = i
                    temp.discard(torem)
                    ret.update(temp)
            except IndexError:
                print "Index Error"

        elif "o" in flags:
            try:
                if self.ballGrid.grid[y - 1][x] == level and (y+1, x) not in ret:
                    temp = self.check_second(x, y-1, "olr", level)
                    torem = 0
                    for i in temp:
                        if isinstance(i, (int, long)):
                            counter = counter + i
                            torem = i
                    temp.discard(torem)
                    ret.update(temp)
            except IndexError:
                print "Index Error"

        elif "l" in flags:
            try:
                if self.ballGrid.grid[y][x-1] == level and (y+1, x) not in ret:
                    temp = self.check_second(x-1, y, "uol", level)
                    torem = 0
                    for i in temp:
                        if isinstance(i, (int, long)):
                            counter = counter + i
                            torem = i
                    temp.discard(torem)
                    ret.update(temp)
            except IndexError:
                print "Index Error"

        elif "r" in flags:
            try:
                if self.ballGrid.grid[y][x+1] == level and (y+1, x) not in ret:
                    temp = self.check_second(x+1, y, "uor", level)
                    torem = 0
                    for i in temp:
                        if isinstance(i, (int, long)):
                            counter = counter + i
                            torem = i
                    temp.discard(torem)
                    ret.update(temp)
            except IndexError:
                print "Index Error"
        ret.add(counter)
        return ret

    def change_color(self, ball, chArr):
        ball.level = ball.level + 1
        for i in chArr:
            #print i.__str__()
            self.ballGrid.grid[i[0]][i[1]] = self.ballGrid.grid[i[0]][i[1]] + 1
        #self.ballGrid.__str__()
        #time.sleep(1)
        self.collapse(ball, chArr)

    def collapse(self, ball, chArr):
        tempHigh = (0, 0)
        for i in chArr:
            if i[0] > tempHigh[0]:
                tempHigh = i
        for i in chArr:
            if i[0] != tempHigh[0] or i[1] != tempHigh[1]:
                self.ballGrid.grid[i[0]][i[1]] = 0
                #time.sleep(0.5)
        ball.x = tempHigh[1]
        ball.y = tempHigh[0]


    def moveDown(self, ball):
        if self.check_down(ball):
            ball[0].y = ball[0].y + 1
            ball[1].y = ball[1].y + 1
            return 0                    #erstelle keine neuen Balls
        else:
            ball[0].isPlayer = False
            ball[1].isPlayer = False
            counter = 0
            self.ballGrid.grid[ball[0].y][ball[0].x] = ball[0].level
            self.ballGrid.grid[ball[1].y][ball[1].x] = ball[1].level
            while self.check_near(ball) and counter < len(self.balls):
                counter = counter + 1
            if ball[0].y == 1:
                return 2
            else:
                return 1                    #erstelle neue Balls

    def draw_grid(self, plBalls, screen):
        if len(plBalls) > 0:
            screen.blit(self.balls[plBalls[0].level-1], (plBalls[0].x*self.ballDimension + 20, plBalls[0].y*self.ballDimension + 40))
            screen.blit(self.balls[plBalls[1].level-1], (plBalls[1].x * self.ballDimension + 20, plBalls[1].y * self.ballDimension + 40))
        counterx = 0
        countery = 0
        for i in self.ballGrid.grid:
            for j in i:
                if j > 0:
                    screen.blit(self.balls[j - 1], (counterx * self.ballDimension + 20, countery * self.ballDimension + 40))
                counterx = counterx + 1
            countery = countery + 1
            counterx = 0
        self.graphics(screen)
