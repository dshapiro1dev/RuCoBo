from random import choice
from random import seed
from time import time


class Die:
    def __init__(self):
        self.faces = ['chicken', 'cow', 'human', 'tank', 'death-ray', 'death-ray']
        self.value = self.roll()

    def roll(self):
        seed(time())
        return choice(self.faces)

class Dice():
    def __init__(self, quantity):
        x = 0
        self.dice = []
        while x < quantity:
            self.dice.append(Die())
            x += 1
        self.sort()

    def sort(self):
        self.dice = sorted(self.dice, key=lambda die: die.value)

if __name__ == "__main__":
    x = 0
    my_dice = Dice(13)
    my_dice.sort()
    for die in my_dice.dice:
        x += 1
        print(f"Roll {x}: {die.value}")