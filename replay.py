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
import time

buildings = [TownHall(7,5), Cannon(5,5), Cannon(11, 5), Wall(5,8), Wall(6, 8), Wall(7,8), Wall(8,8), Wall(9,8), Wall(10,8), Wall(11,8), Wall(12,8), Hut(4,3), Hut(6,3), Hut(8,3), Hut(10,3), Hut(12,3)]
enemies = []

fileName = input("Enter file name for replay: ")
fileName = "./replay/" + fileName + ".txt"

village = Village(buildings, enemies)
village.displayLevel()

actions = []

# open file and read the content in a list
with open(fileName, 'r') as replay:
    actions = [cur[:len(cur) - 1] for cur in replay.readlines()]

x1 = int(actions[0])
y1 = int(actions[1])
x2 = int(actions[2])
y2 = int(actions[3])
x3 = int(actions[4])
y3 = int(actions[5])
x = int(actions[6])
y = int(actions[7])

for i in range(8):
    actions.pop(0)

count = 0

village.spawnpoints(x1, y1, x2, y2, x3, y3, x, y)

while(1):
    tt = actions[count]
    count += 1
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
        break
    time.sleep(village.delay())
