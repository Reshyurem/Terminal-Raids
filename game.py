import sys 
import os
sys.path.append(os.path.relpath("./src"))
from input import *
from townhall import *
from village import *
from barbarian import *
from cannon import *
from wall import *
from hut import *

buildings = [TownHall(7,5), Cannon(5,5), Cannon(11, 5), Wall(5,8), Wall(6, 8), Wall(7,8), Wall(8,8), Wall(9,8), Wall(10,8), Wall(11,8), Wall(12,8), Hut(4,3), Hut(6,3), Hut(8,3), Hut(10,3), Hut(12,3)]
enemies = []

village = Village(buildings, enemies)
village.displayLevel()

x1 = int(input("Choose X Coordinate of spawn point 1: ")) - 1
y1 = int(input("Choose Y Coordinate of spawn point 1: ")) - 1
x2 = int(input("Choose X Coordinate of spawn point 2: ")) - 1
y2 = int(input("Choose Y Coordinate of spawn point 2: ")) - 1
x3 = int(input("Choose X Coordinate of spawn point 3: ")) - 1
y3 = int(input("Choose Y Coordinate of spawn point 3: ")) - 1

x = int(input("Choose X Spawn Point of King: ")) - 1
y = int(input("Choose Y Spawn Point of King: ")) - 1

village.spawnpoints(x1, y1, x2, y2, x3, y3, x, y)

actions = [x1, y1, x2, y2, x3, y3, x, y]

while(1):
    tt = input_to(Get(), timeout=village.delay())
    actions.append(tt)
    if(tt == '1' or tt == '2' or tt == '3'):
        village.addEnemy(int(tt))
    elif(tt == 'r'):
        village.rageSpell()
    elif(tt == 'h'):
        village.healSpell()
    elif(tt == 'w' or tt == 's' or tt == 'd' or tt == 'a'):
        village.kingMove(tt)
    elif(tt == ' '):
        village.kingAttack()
    village.updateLevel()
    if(village.checkVictory()):
        village.printVictory()
        fileName = input("Enter file name for replay: ").strip()
        fileName = "./replay/" + fileName + ".txt"
        with open(fileName, 'w') as replay:
            replay.writelines("%s\n" % action for action in actions)
        break
    # time.sleep(village.delay())
