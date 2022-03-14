from playsound import playsound
from colorama import Fore, Style
class Building:
    def __init__(self, x, y, h, w):
        self.hitpoints = 100
        self.damageTaken = 0
        self.gold = 0
        self.elixir = 0
        self.x = x
        self.y = y
        self.height = h
        self.width = w
        self.posx = x + int(w / 2)
        self.posy = y + int(h / 2)
        self.type = "Not Wall"
        self.char = 'B'

    def sym(self):
        return self.char
    
    def csym(self):
        bar = self.damageTaken / self.hitpoints
        if(bar <= 0.5):
            return Fore.GREEN + self.char + Style.RESET_ALL
        elif(bar <= 0.8):
            return Fore.YELLOW + self.char + Style.RESET_ALL
        elif(bar < 1):
            return Fore.RED + self.char + Style.RESET_ALL
        else:
            return self.char
    
    def destroy(self):
        self.char = 'V'
        # self.char = 'D'
        playsound('./src/audio/buildingDestroyed.mp3')

    def display(self, grid):
        for i in range(self.height):
            for j in range(self.width):
                grid[self.x + j][self.y + i] = self.sym()
        return grid