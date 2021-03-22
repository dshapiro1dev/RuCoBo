import pgzrun

from random import randint
from pgzero.actor import Actor
from pgzero.keyboard import keyboard

WIDTH = 800
HEIGHT = 600

balloon = Actor("balloon")
balloon.pos = 400, 300

bird = Actor("bird-up")
bird.pos = randint(2000, 3000), randint(10, 100)

house = Actor("house")
house.pos = randint(2000, 3000), 460

tree = Actor("tree")
tree.pos = randint(2000, 3000), 450

bird_up = True
up = False
game_over = False
score = 0
number_of_updates = 0


def display_high_score():
    screen.draw.text(f"Score: {score}", (300, 50), color="black", fontsize=100)
    screen.draw.text(f"Press The Space Bar To Play Again", (200, 20), color="black", fontsize=50)


def draw():
    screen.blit("background", (0, 0))
    if not game_over:
        balloon.draw()
        bird.draw()
        house.draw()
        tree.draw()
        screen.draw.text(f"Score: {str(score)}", (700, 5), color="black")
    else:
        display_high_score()


def on_mouse_down():
    global up
    up = True
    balloon.y -= 50


def on_mouse_up():
    global up
    up = False


def flap():
    global bird_up
    if bird_up:
        bird.image = "bird-down"
        bird_up = False
    else:
        bird.image = "bird-up"
        bird_up = True


def update():
    global game_over, score, number_of_updates
    if not game_over:
        if not up:
            balloon.y += 1

        if bird.x > 0:
            bird.x -= 15
            if number_of_updates == 9:
                flap()
                number_of_updates = 0
            else:
                number_of_updates += 1
        else:
            bird.x = randint(800, 1000)
            bird.y = randint(10, 150)
            score += 1
            number_of_updates = 0

        if house.right > 0:
            house.x -= 8
        else:
            house.x = randint(800, 1000)
            score += 1

        if tree.right > 0:
            tree.x -= 8
        else:
            tree.x = randint(800, 1000)
            score += 1

        if balloon.top < 0 or balloon.bottom > 560:
            game_over = True

        if balloon.collidepoint(bird.x, bird.y) or \
                balloon.collidepoint(house.x, house.y) or \
                balloon.collidepoint(tree.x, tree.y):
            game_over = True

    if game_over and keyboard.space:
        score = 0
        game_over = False
        balloon.pos = 400, 300
        bird.pos = randint(1200, 1600), randint(10, 100)
        house.pos = randint(800, 1600), 460
        tree.pos = randint(800, 1600), 450


pgzrun.go()
