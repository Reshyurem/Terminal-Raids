from barbarian import *

class King(Barbarian):
    def __init__(self, x, y):
        self.hitpoints = 900
        self.totalHP = 900
        self.char = 'K'
        self.direction = 'w'
        self.x = x
        self.y = y
        self.damage = 90

    def move(self, direction, grid):
        self.direction = direction
        if(direction == 'w' and grid[self.x][self.y - 1] == 'V'):
            self.y -= 1
        elif(direction == 'a' and grid[self.x - 1][self.y] == 'V'):
            self.x -= 1
        elif(direction == 's' and grid[self.x][self.y + 1] == 'V'):
            self.y += 1
        elif(direction == 'd' and grid[self.x + 1][self.y] == 'V'):
            self.x += 1
    
    def attack(self, buildings):
        x = self.x
        y = self.y
        if(self.direction == 'w'):
            y -= 1
        elif(self.direction == 'a'):
            x -= 1
        elif(self.direction == 's'):
            y += 1
        elif(self.direction == 'd'):
            x += 1
        for building in buildings:
            if(building.x <= x and building.y <= y and building.x + building.width > x and building.y + building.height > y):
                building.damageTaken += self.damage
                if(building.hitpoints <= 0):
                    buildings.remove(building)