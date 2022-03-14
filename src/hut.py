from building import *

class Hut(Building):
    def __init__(self, x, y):
        Building.__init__(self, x, y, 2, 2)
        self.gold = 100
        self.elixir = 100
        self.char = 'H'