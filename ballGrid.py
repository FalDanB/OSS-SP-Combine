from ball import Ball
from random import randint


class BallGrid:
    def __init__(self, w, h):
        self.grid = [[0 for x in range(w)] for y in range(h+2)]

    def createRandomBalls(self, level):
        ball1 = randint(1,level)
        ball2 = randint(1,level)
        return (ball1, ball2)

    def __str__(self):
        for i in self.grid:
            print i.__str__()
