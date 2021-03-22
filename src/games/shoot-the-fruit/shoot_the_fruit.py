import pgzrun
from random import randint
from pgzero import clock
from pgzero.actor import Actor

WIDTH = 300
HEIGHT = 300
apple = Actor("apple")
orange = Actor("orange")
pineapple = Actor("pineapple")
count = []
game_over = False


def draw():
    screen.clear()
    apple.draw()
    orange.draw()
    pineapple.draw()
    screen.draw.text(f"Score: {len(count)}", topleft=(10, 10))


def place_apple():
    apple.x = randint(-10, 310)
    apple.y = randint(-10, 310)
    orange.x = randint(-10, 310)
    orange.y = randint(-10, 310)
    pineapple.x = randint(-10, 310)
    pineapple.y = randint(-10, 310)


def on_mouse_down(pos):
    if apple.collidepoint(pos):
        count.append("1")
        place_apple()
    else:
        print(f"\nFINAL SCORE: {len(count)} points")
        quit()


def time_up():
    global game_over
    game_over = True


clock.schedule(time_up, 1.0)
place_apple()
pgzrun.go()
