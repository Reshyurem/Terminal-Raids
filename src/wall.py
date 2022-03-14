from building import *

class Wall(Building):
    def __init__(self, x, y):
        Building.__init__(self, x, y, 1, 1)
        self.hitpoints = 500
        self.type = "Wall"
        self.char = 'W'