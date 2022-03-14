from building import *

class TownHall(Building):
    def __init__(self, x, y):
        Building.__init__(self, x, y, 3, 4)
        self.hitpoints = 200
        self.elixir = 300
        self.gold = 300
        self.char = 'T'