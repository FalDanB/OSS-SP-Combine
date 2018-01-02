
class GameSettings:
    def __init__(self):
        #Window Dimension
        self.normalHeight = 960
        self.normalWidth = 1280
        self.scaleFactor = 0.5

        #BallGrid Dimension
        self.numberBallsH = 7
        self.numberBallsV = 7
        self.ballDimension = 86

        #Ball Colours
        self.ballColours = ("", "green", "yellow", "orange", "red", "pink", "purple", "blue", "cyan", "black", "white")

        #Ball Scores
        self.levelBallScore = (5, 10, 20, 40, 80, 160,20, 640, 1280, 2560)
