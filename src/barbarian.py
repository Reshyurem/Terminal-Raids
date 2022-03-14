import math
from playsound import playsound
from colorama import Style

class Barbarian:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.char = 'B'
        self.hitpoints = 90
        self.totalHP = 50
        self.damage = 25

    def move(self, grid, buildings):
        mindist = 999
        closest = -1
        for i, building in enumerate(buildings):
            if building.char == 'W' or building.char == 'D':
                continue
            dist = abs(self.x - building.posx) + abs(self.y - building.posy)
            if(dist < mindist):
                mindist = dist
                closest = i
        if(closest == -1):
            return grid
        if(self.x > buildings[closest].posx and self.y > buildings[closest].posy):
            if(grid[self.x - 1][self.y - 1] == 'W'):
                for wall in buildings:
                    if(wall.x == self.x - 1 and wall.y == self.y - 1):
                        wall.damageTaken += self.damage
                        if(wall.hitpoints <= wall.damageTaken):
                            buildings.remove(wall)
                            self.x -= 1
                            self.y -= 1
                        break
            elif(grid[self.x - 1][self.y - 1] == buildings[closest].char):
                buildings[closest].damageTaken += self.damage
                if(buildings[closest].hitpoints <= buildings[closest].damageTaken):
                    buildings[closest].damageTaken = buildings[closest].hitpoints
                    buildings[closest].destroy()
                    # buildings.remove(buildings[closest])
                    self.x -= 1
                    self.y -= 1
            else:
                self.x -= 1
                self.y -= 1
            
        elif(self.x < buildings[closest].posx and self.y < buildings[closest].posy):
            if(grid[self.x + 1][self.y + 1] == 'W'):
                for wall in buildings:
                    if(wall.x == self.x + 1 and wall.y == self.y + 1):
                        wall.damageTaken += self.damage
                        if(wall.hitpoints <= wall.damageTaken):
                            buildings.remove(wall)
                            self.x += 1
                            self.y += 1
                        break
            elif(grid[self.x + 1][self.y + 1] == buildings[closest].char):
                buildings[closest].damageTaken += self.damage
                if(buildings[closest].hitpoints <= buildings[closest].damageTaken):
                    buildings[closest].damageTaken = buildings[closest].hitpoints
                    buildings[closest].destroy()
                    # buildings.remove(buildings[closest])
                    self.x += 1
                    self.y += 1
            else:
                self.x += 1
                self.y += 1
        elif(self.x > buildings[closest].posx and self.y < buildings[closest].posy):
            if(grid[self.x - 1][self.y + 1] == 'W'):
                for wall in buildings:
                    if(wall.x == self.x - 1 and wall.y == self.y + 1):
                        wall.damageTaken += self.damage
                        if(wall.hitpoints <= wall.damageTaken):
                            buildings.remove(wall)
                            self.x -= 1
                            self.y += 1
                        break
            elif(grid[self.x - 1][self.y + 1] == buildings[closest].char):
                buildings[closest].damageTaken += self.damage
                if(buildings[closest].hitpoints <= buildings[closest].damageTaken):
                    buildings[closest].damageTaken = buildings[closest].hitpoints
                    buildings[closest].destroy()
                    # buildings.remove(buildings[closest])
                    self.x -= 1
                    self.y += 1
            else:
                self.x -= 1
                self.y += 1
        elif(self.x < buildings[closest].posx and self.y > buildings[closest].posy):
            if(grid[self.x + 1][self.y - 1] == 'W'):
                for wall in buildings:
                    if(wall.x == self.x + 1 and wall.y == self.y - 1):
                        wall.damageTaken += self.damage
                        if(wall.hitpoints <= wall.damageTaken):
                            buildings.remove(wall)
                            self.x += 1
                            self.y -= 1
                        break
            elif(grid[self.x + 1][self.y - 1] == buildings[closest].char):
                buildings[closest].damageTaken += self.damage
                if(buildings[closest].hitpoints <= buildings[closest].damageTaken):
                    buildings[closest].damageTaken = buildings[closest].hitpoints
                    buildings[closest].destroy()
                    # buildings.remove(buildings[closest])
                    self.x += 1
                    self.y -= 1
            else:
                self.x += 1
                self.y -= 1
        return buildings
        
    def display(self, grid):
        grid[self.x][self.y] = self.char
        return grid

    def csym(self):
        bar = self.hitpoints / self.totalHP
        if(bar < 0.3):
            return Style.BRIGHT + self.char + Style.RESET_ALL
        elif(bar < 0.6):
            return Style.NORMAL + self.char + Style.RESET_ALL
        else:
            return Style.DIM + self.char + Style.RESET_ALL

    def sym(self):
        return self.char
    
    def heal(self):
        self.hitpoints = int(1.5 * self.hitpoints)
        if(self.hitpoints > self.totalHP):
            self.hitpoints = self.totalHP

    def destroy(self):
        playsound('./src/audio/barbarianDestroyed.mp3')