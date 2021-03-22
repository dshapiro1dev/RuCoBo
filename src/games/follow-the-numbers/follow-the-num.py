import pgzrun
from random import randint
from pgzero.actor import Actor

WIDTH = 900
HEIGHT = 600
dots = []
lines = []
next_dot = 0
number_of_dots = 10
game_over = True

for i in range(0, number_of_dots):
    actor = Actor("dot")
    actor.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
    dots.append(actor)


def draw():
    screen.fill("black")
    number = 1
    for dot in dots:
        screen.draw.text(str(number), (dot.pos[0], dot.pos[1] + 12))
        dot.draw()
        number += 1
    for line in lines:
        screen.draw.line(line[0], line[1], (100, 0, 0))


def on_mouse_down(pos):
    global next_dot
    global lines
    global dots
    global game_over
    if dots[next_dot].collidepoint(pos):
        if next_dot:
            lines.append((dots[next_dot - 1].pos, dots[next_dot].pos))

        if next_dot == number_of_dots - 1:
            screen.fill("white")
            lines = []
            dots = []
            game_over = False

        next_dot = next_dot + 1
    else:
        lines = []
        next_dot = 0


pgzrun.go()
