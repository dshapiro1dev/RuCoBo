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

new_role = False

# Deployed Dice
tank_dice = []
death_ray_dice = []

# details for the stat button
start_button = Rect(700, 10, 80, 30)
tank_count = Rect(700, 50, 80, 30)
death_ray_count = Rect(700, 90, 80, 30)
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

    screen.draw.filled_rect(tank_count, GRAY)
    screen.draw.textbox(f"T: {len(tank_dice)}", tank_count, color="black")

    screen.draw.filled_rect(death_ray_count, GRAY)
    screen.draw.textbox(f"D: {len(death_ray_dice)}", death_ray_count, color="black")

    for die in dice:
        die.draw()


def update():
    screen.draw.textbox(f"T: {len(tank_dice)}", tank_count, color="black")
    screen.draw.textbox(f"D: {len(death_ray_dice)}", death_ray_count, color="black")
    for index in range(len(my_dice.dice)):
        if dice[index].image == 'tank' and my_dice.dice[index].active:
            deploy_tank(dice[index])
            my_dice.dice[index].active = False
    my_dice.new_roll = False


def on_mouse_down(pos):
    if start_button.collidepoint(pos):
        my_dice.reroll()
        for index in range(len(my_dice.dice)):
            dice[index].image = my_dice.dice[index].value
            print(f"New value {index}: {my_dice.dice[index].value}")
            dice[index].draw()

    for each in dice:
        if each.collidepoint(pos) and each.image == 'death-ray':
            print('deploying deathrays!')
            for index in range(len(my_dice.dice)):
                if dice[index].image == 'death-ray' and my_dice.dice[index].active:
                    my_dice.dice[index].active = False
                    deploy_death_ray(dice[index])




def deploy_die(die, dice_list, die_pos):
    animate(die, pos=(die_pos, (100 + (40 * len(dice_list)))))
    dice_list.append(die)

def deploy_death_ray(death_ray):
    death_ray_dice.append(death_ray)
    animate(death_ray_dice[-1], pos=(450, (60 + (40 * len(death_ray_dice)))))

def deploy_tank(tank):
    animate(tank, pos=(300, (100 + (40 * len(tank_dice)))))
    tank_dice.append(tank)


# this command makes all the magic happen!
pgzrun.go()
