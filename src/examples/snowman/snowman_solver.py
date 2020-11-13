import random


class Solver:
    """This is where we come up with cool strategies for solving snowman puzzles"""

    def __init__(self, word_length):
        self.word_length = word_length
        self.possible_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                                 'r', 's', 't',
                                 'u', 'v', 'w', 'x', 'y', 'z']

    def make_guess(self):
        index = random.randint(0, len(self.possible_letters) - 1)
        guess = self.possible_letters.pop(index)
        return guess

print("testing")
testgame = Solver(10)

x = 0
while x < 10:
    print(testgame.make_guess())
    x +=1
