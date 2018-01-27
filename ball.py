#Ball Class for Combine Game

class Ball:

    def __init__(self, x=0, y=0, level = 1, isPlayer = True):
        self.level = level
        self.y = y
        self.x = x
        self.isPlayer = isPlayer
        self.checked = False

