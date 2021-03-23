import pgzrun
from pgzero.actor import Actor
from dice import Die
from dice import Dice

# Set the width and height of the screen
WIDTH = 800
HEIGHT = 600

# Game Variables
dice_count = 13
dice_width = 35

dice = []
x = 0
left_pos = 5

my_dice = Dice(dice_count)

my_die = Die()

"""while x <= dice_count:
    dice.append(Actor(my_die.roll(), topleft=(left_pos, 5)))
    left_pos += (dice_width) * 1.5
    x += 1"""
for die in my_dice.dice:
    dice.append(Actor(die.value, topleft=(left_pos, 5)))
    left_pos += dice_width * 1.5

def draw():
    # draw the screen with a specified color
    screen.fill((50, 210, 235))

    for die in dice:
        die.draw()

# this command makes all the magic happen!
pgzrun.go()