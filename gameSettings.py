
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
        self.level1BallScore = 5
        self.level2BallScore = 10
        self.level3BallScore = 20
        self.level4BallScore = 40
        self.level5BallScore = 80
        self.level6BallScore = 160
        self.level7BallScore = 320
        self.level8BallScore = 640
        self.level9BallScore = 1280
        self.level10BallScore = 2560
