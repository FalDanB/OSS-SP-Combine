
class BallGrid:
    def __init__(self, w, h):
        self.grid = [[0 for x in range(w)] for y in range(h)]

    def __str__(self):
        for i in self.grid:
            print (i.__str__())
