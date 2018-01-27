import pygame
from pygame.locals import *
import sqlite3
import datetime


class ScoreBoard:
    def __init__(self, settings):
        self.width = int(settings.normalWidth * settings.scaleFactor * 0.5)
        self.height = int(settings.normalHeight * settings.scaleFactor)
        self.highScores = loadHighscore(self)

    def img(self, screen):
        overlscore = pygame.image.load("images/overlscore2.png").convert_alpha()
        overlscore = pygame.transform.scale(overlscore, (self.width-10, self.height))

        screen.blit(overlscore, (self.width+10, 0))

    def graphics(self, screen, settings, score):
        i = 0

        for hs in self.highScores:
            if hs[2] == False:
                colour = (255,255,255)
            else:
                colour = (220,220,0)

            if hs[1] != 0 and i < 7:
                font = pygame.font.SysFont(pygame.font.get_fonts()[2], int(48*settings.scaleFactor))
                ts = font.render(str(i+1) + ". " + datetime.datetime.strptime(hs[0], "%Y-%m-%d %H:%M:%S.%f").strftime("%d/%m/%y"), True, colour)
                tshadow = font.render(str(i+1) + ". " + datetime.datetime.strptime(hs[0], "%Y-%m-%d %H:%M:%S.%f").strftime("%d/%m/%y"),True, (0, 0, 0))
                screen.blit(tshadow, (self.width + (self.width * 0.1) + 2, (self.height * 0.1) + (self.height / 16 * i) + 2))
                screen.blit(ts, (self.width + (self.width * 0.1), (self.height * 0.1) + (self.height/16 * i)))

                font = pygame.font.SysFont(pygame.font.get_fonts()[2], int(48*settings.scaleFactor), True)
                tScoreShadow = font.render(str(hs[1]), True, (0,0,0))
                tScoreShadow_rect = tScoreShadow.get_rect()
                tScoreShadow_rect.top = (self.height * 0.1) + (self.height / 16 * (i) +2)
                tScoreShadow_rect.right = (1.8 * self.width) + (self.width * 0.1) + 2
                screen.blit(tScoreShadow, tScoreShadow_rect)
                tScore = font.render(str(hs[1]), True, colour)
                tScore_rect = tScore.get_rect()
                tScore_rect.top = (self.height * 0.1) + (self.height / 16 * (i))
                tScore_rect.right = 1.8 * self.width + (self.width * 0.1)
                screen.blit(tScore, tScore_rect)
                i += 1

        #Render Player Score
        textshadow = font.render(score.__str__(), True, (0, 0, 0))
        textshadow_rect = textshadow.get_rect()
        textshadow_rect.top = (self.height*0.73) + 2
        textshadow_rect.right = self.width + (self.width * 0.9) + 2
        screen.blit(textshadow, textshadow_rect)
        textsurface = font.render(score.__str__(), True, (220, 220, 0))
        textsurface_rect = textsurface.get_rect()
        textsurface_rect.top = (self.height*0.73)
        textsurface_rect.right = self.width + (self.width * 0.9)
        screen.blit(textsurface, textsurface_rect)

    def updateHighScore(self, newScore):
        scoreExists = False
        for i in range(0,len(self.highScores)):
            if self.highScores[i][2] == True:
                #print(self.highScores[i][1])
                self.highScores[i][1] = newScore
                scoreExists = True
        self.highScores.sort(key = lambda x: x[1], reverse = True)
        #print(self.highScores)
        if scoreExists == False:
            newScoreDate = datetime.datetime.now()
            for i in range(0, len(self.highScores)-1):
                if newScore > self.highScores[i][1]:
                    for j in range (len(self.highScores)-2,i+1,-1):
                           self.highScores[j] = self.highScores[j-1]
                    self.highScores[i] = [str(newScoreDate), newScore, True]
                    break


    def saveHighScore(self):
        con = sqlite3.connect("highscores.db")
        c = con.cursor()
        for i in range(0,len(self.highScores)-1):
            #print(i)
            query = "UPDATE highscores SET scoreDate = '" + self.highScores[i][0] + "', score = " + str(self.highScores[i][1]) + " WHERE rank = " + str(i+1) + ";"
            #print(query)
            c.execute(query)
        con.commit()
        c.close()
        con.close()

def loadHighscore(self):
    highScoresExist = True
    con = sqlite3.connect("highscores.db")
    c = con.cursor()
    try:
        c.execute("SELECT * FROM highscores")
        highScoreData = c.fetchall()
        con.commit()
    except sqlite3.OperationalError:
        #print("No highscores found")
        highScoresExist = False
    if highScoresExist:
        highScores = []
        for score in highScoreData:
            highScores.append((score[1],score[2], False))
    else:
        highScores = [("-",0, False) for x in range(1,11)]
        c.execute("CREATE TABLE IF NOT EXISTS highscores (rank INTEGER PRIMARY KEY, scoreDate text, score NUMBER)")
        for i in range(1,11):
            query = "INSERT INTO highscores (rank, scoreDate, score) VALUES ("+ str(i) + ", '-', 0);"
            #print(query)
            c.execute(query)
        con.commit()
    c.close()
    con.close()
    return highScores


