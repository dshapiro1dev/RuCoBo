import time
import pgzrun
from pgzero.actor import Actor
from pgzero.rect import Rect
from pgzero.animation import animate
from dice import Dice
from dice import Die

# Set the width and height of the screen
WIDTH = 800
HEIGHT = 600

# Game Variables
dice_count = 13
dice_width = 35
dice = []
x = 0
left_pos = 5

# Deployed Tank Dice
tank_dice = []

# details for the stat button
start_button = Rect(700, 10, 80, 30)
GRAY = 175, 177, 180

my_dice = Dice(dice_count, True)
my_die = Die()

for die in my_dice.dice:
    dice.append(Actor(die.value, topleft=(left_pos, 5)))
    left_pos += dice_width * 1.5


def draw():
    # draw the screen with a specified color
    screen.fill((50, 210, 235))

    screen.draw.filled_rect(start_button, GRAY)
    screen.draw.textbox("Start", start_button, color="black")

    for die in dice:
        die.draw()


def update():
    for index in range(len(my_dice.dice)):
        if dice[index].image == 'tank' and my_dice.dice[index].active:
            deploy_tank(dice[index])
            my_dice.dice[index].active = False


def on_mouse_down(pos):
    if start_button.collidepoint(pos):
        my_dice.reroll()
        for index in range(len(my_dice.dice)):
            dice[index].image = my_dice.dice[index].value
            print(f"New value {index}: {my_dice.dice[index].value}")
            dice[index].draw()


def deploy_tank(tank):
    animate(tank, pos=(300, (100 + (25 * len(tank_dice)))))
    tank_dice.append(tank)


# this command makes all the magic happen!
pgzrun.go()
