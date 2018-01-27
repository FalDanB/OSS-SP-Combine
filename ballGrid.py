#Ball Grid for Combine Game

class BallGrid:
    def __init__(self, w, h):
        self.grid = [[0 for x in range(w)] for y in range(h)] #set up ball grid based on settings

    def __str__(self): # print ball grid
        for i in self.grid:
            print (i.__str__())
