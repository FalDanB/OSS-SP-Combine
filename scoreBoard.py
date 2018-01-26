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

    def graphics(self, screen, font, score):
        i = 0
        for hs in self.highScores:
            if hs[1] != 0 and i < 7:
                ts = font.render(datetime.datetime.strptime(hs[0], "%Y-%m-%d %H:%M:%S.%f").strftime("%d/%m/%y %H:%M") +
                                 " " + hs[1].__str__(), True, (200, 200, 0))
                tshadow = font.render(datetime.datetime.strptime(hs[0], "%Y-%m-%d %H:%M:%S.%f").strftime("%d/%m/%y %H:%M") +
                                 " " + hs[1].__str__(), True, (0, 0, 0))
                screen.blit(tshadow, (self.width + (self.width * 0.1) + 2, (self.height * 0.1) + (self.height / 16 * i) + 2))
                screen.blit(ts, (self.width + (self.width * 0.1), (self.height * 0.1) + (self.height/16 * i)))
                i += 1

        textshadow = font.render(score.__str__(), True, (0, 0, 0))
        textsurface = font.render(score.__str__(), True, (200, 200, 0))

        screen.blit(textshadow, (self.width + (self.width * 0.5) + 2, (self.height * 0.72) + 2))
        screen.blit(textsurface, (self.width + (self.width*0.5), self.height*0.72))

    def updateHighScore(self, newScore):
        newScoreDate = datetime.datetime.now()
        for i in range(0, len(self.highScores)-1):
            print (str(newScore) + str(self.highScores[i]))
            if newScore > self.highScores[i][1]:
                if self.highScores[i][2] == False:
                    for j in range (len(self.highScores)-2,i,-1):
                        self.highScores[j] = self.highScores[j-1]
                self.highScores[i] = (str(newScoreDate), newScore, True)
                break
        print (self.highScores)

    def saveHighScore(self):
        con = sqlite3.connect("highscores.db")
        c = con.cursor()
        for i in range(0,len(self.highScores)-1):
            print(i)
            query = "UPDATE highscores SET scoreDate = '" + self.highScores[i][0] + "', score = " + str(self.highScores[i][1]) + " WHERE rank = " + str(i+1) + ";"
            print(query)
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
        print("No highscores found")
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
            print(query)
            c.execute(query)
        con.commit()
    c.close()
    con.close()
    return highScores


