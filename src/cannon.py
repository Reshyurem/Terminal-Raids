from building import *

class Cannon(Building):
    def __init__(self, x, y):
        Building.__init__(self, x, y, 2, 2)
        self.range = 10
        self.damage = 20
        self.char = 'C'
        
    def defend(self, enemies):
        for enemy in enemies:
            if(abs(enemy.x - self.posx) + abs(enemy.y - self.posy) <= self.range):
                enemy.hitpoints -= self.damage
                if(enemy.hitpoints <= 0):
                    enemies.remove(enemy)
                    enemy.destroy()
                break
        return enemies
