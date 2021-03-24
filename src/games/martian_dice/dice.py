from random import choice
from random import seed
from time import time


class Die:
    def __init__(self, start_blank=False):
        self.faces = ['chicken', 'cow', 'human', 'tank', 'death-ray', 'death-ray']
        self.active = True
        if start_blank:
            self.value = 'blank'
        else:
            self.value = self.roll()

    def roll(self):
        if self.active:
            seed(time())
            self.value = choice(self.faces)
        return self.value


class Dice():
    def __init__(self, quantity, start_blank=False):
        self.quantity = quantity
        self.dice = []
        self.new_roll = True
        x = 0
        while x < self.quantity:
            self.dice.append(Die(start_blank))
            x += 1
        self.sort()

    def reroll(self):
        self.new_roll = True
        for each_die in self.dice:
            each_die.roll()
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
