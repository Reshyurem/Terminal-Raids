import os
import colorama
import time
from barbarian import *
from king import *

class Village:
    def __init__(self, listOfBuildings, listOfEnemies):
        self.width = 20
        self.height = 20
        self.rage = 0
        self.heal = False
        self.maxBarbarians = 10
        self.noOfBarbarians = 0
        self.grid = []
        self.cgrid = []
        self.buildings = listOfBuildings
        self.enemies = listOfEnemies
        col = []
        ccol = []
        for i in range(self.height):
            col.append('V')
            ccol.append('V')
        for i in range(self.width):
            self.grid.append(col.copy())
            self.cgrid.append(ccol.copy())
        
        for building in listOfBuildings:
            for i in range(building.width):
                for j in range(building.height):
                    self.grid[building.x + i][building.y + j] = building.sym()
                    self.cgrid[building.x + i][building.y + j] = building.csym()

    def updateLevel(self):
        if(self.rage > 0):
            for enemy in self.enemies:
                if(enemy.char == 'K'):
                    continue
                self.buildings = enemy.move(self.grid, self.buildings)
            for i in range(self.width):
                for j in range(self.height):
                    self.grid[i][j] = 'V'
                    self.cgrid[i][j] = 'V'
            for building in self.buildings:
                for i in range(building.width):
                    for j in range(building.height):
                        self.grid[building.x + i][building.y + j] = building.sym()
                        self.cgrid[building.x + i][building.y + j] = building.csym()
            for enemy in self.enemies:
                self.grid[enemy.x][enemy.y] = enemy.sym()
                self.cgrid[enemy.x][enemy.y] = enemy.csym()
            self.displayLevel()
            time.sleep(0.5)
            for enemy in self.enemies:
                if(enemy.char == 'K'):
                    continue
                self.buildings = enemy.move(self.grid, self.buildings)
            for building in self.buildings:
                if(building.char == 'C'):
                    self.enemies = building.defend(self.enemies)
            for i in range(self.width):
                for j in range(self.height):
                    self.grid[i][j] = 'V'
            for building in self.buildings:
                for i in range(building.width):
                    for j in range(building.height):
                        self.grid[building.x + i][building.y + j] = building.sym()
                        self.cgrid[building.x + i][building.y + j] = building.csym()
            for enemy in self.enemies:
                self.grid[enemy.x][enemy.y] = enemy.sym()
                self.cgrid[enemy.x][enemy.y] = enemy.csym()
            self.displayLevel()
            self.rage -= 1
        else:
            for enemy in self.enemies:
                if(enemy.char == 'K'):
                    continue
                self.buildings = enemy.move(self.grid, self.buildings)
            for building in self.buildings:
                if(building.char == 'C'):
                    self.enemies = building.defend(self.enemies)
            for i in range(self.width):
                for j in range(self.height):
                    self.grid[i][j] = 'V'
                    self.cgrid[i][j] = 'V'
            for building in self.buildings:
                for i in range(building.width):
                    for j in range(building.height):
                        self.grid[building.x + i][building.y + j] = building.sym()
                        self.cgrid[building.x + i][building.y + j] = building.csym()
            for enemy in self.enemies:
                self.grid[enemy.x][enemy.y] = enemy.sym()
                self.cgrid[enemy.x][enemy.y] = enemy.csym()
            self.displayLevel() 

    def displayLevel(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        st = "   "
        for i in range(self.width):
            st = st + " " * (6 - len(str(i + 1))) + str(i + 1)
        print(st) 
        for r in range(self.height):
            st = "     "
            if r == 0:
                for col in range(self.width):
                    st = st + "______" 
                print(st)
    
            st = "     "
            for col in range(self.width):
                st = st + "|     "
            print(st + "|")
            
            st = "  " + str(r + 1) + " " * (3 - len(str(r + 1)))
            for col in range(self.width):
                st = st + "|  " + str(self.cgrid[col][r]) + "  "
            print(st + "|") 
    
            st = "     "
            for col in range(self.width):
                st = st + "|_____"
            print(st + '|')
    
        print()
        print("Barbarians used: " + str(self.noOfBarbarians) + "/" + str(self.maxBarbarians))
        elixir = 0
        gold = 0
        for building in self.buildings:
            elixir += int(building.elixir * building.damageTaken / building.hitpoints)
            gold += int(building.gold * building.damageTaken / building.hitpoints)
        print("Elixir: " + str(elixir))
        print("Gold: " + str(gold))
        print("[", end='')
        for i in range(20):
            if((i + 1) / 20 <= self.kingHealth()):
                print("#", end='')
            else:
                print(" ", end='')
        print("]")
    
    def spawnpoints(self, x1, y1, x2, y2, x3, y3, x, y):
        if(self.grid[x1][y1] != 'V' or self.grid[x2][y2] != 'V' or self.grid[x3][y3] != 'V' or self.grid[x][y] != 'V'):
            raise Exception("Spawn Points can not coincide with Buildings")
        else:
            self.sp = []
            self.sp.append((x1, y1))
            self.sp.append((x2, y2))
            self.sp.append((x3, y3))
            self.enemies.append(King(x,y))
    
    def delay(self):
        if(self.rage == 0):
            return 1
        else:
            return 0.5
    
    def checkVictory(self):
        flag = True
        for i in self.buildings:
            if(i.char != 'D' and i.char != 'W'):
                flag = False
                break
        if((len(self.enemies) == 0 and self.noOfBarbarians == self.maxBarbarians) or flag == True):
            return True
        else:
            return False
    
    def printVictory(self):
        if(len(self.enemies) == 0 and self.noOfBarbarians == self.maxBarbarians):
            print("You have lost!")
        else:
            print("You have won!")
    
    def addEnemy(self, i):
        if(self.noOfBarbarians < self.maxBarbarians):
            # print(self.noOfBarbarians, self.maxBarbarians)
            self.enemies.append(Barbarian(self.sp[i - 1][0], self.sp[i - 1][1]))
            self.noOfBarbarians += 1
    
    def healSpell(self):
        for enemy in self.enemies:
            enemy.heal()
    
    def rageSpell(self):
        self.rage = 8
    
    def kingMove(self, direction):
        for enemy in self.enemies:
            if(enemy.char == 'K'):
                if(enemy.hitpoints > 0):
                    enemy.move(direction, self.grid)
                break
    
    def kingAttack(self):
        for enemy in self.enemies:
            if(enemy.char == 'K'):
                if(enemy.hitpoints > 0):
                    enemy.attack(self.buildings)
                break

    def kingHealth(self):
        for enemy in self.enemies:
            if(enemy.char == 'K'):
                return enemy.hitpoints / enemy.totalHP
        return 0

# resh = Village(0, 19, 1, 19, 2, 19)
# resh.displayLevel()