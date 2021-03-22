import pgzrun
import random
from random import randint
from pgzero.animation import animate
from pgzero.clock import clock
from pgzero.actor import Actor

FONT_COLOR = (255, 255, 255)
WIDTH = 1000
HEIGHT = 700
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X, CENTER_Y)
FINAL_LEVEL = 20
START_SPEED = 20
COLORS = ["green", "blue"]

game_over = False
game_complete = False
current_level = 1
stars = []
animations = []


def draw():
    global stars, current_level, game_complete, game_over
    screen.clear()
    screen.blit("space", (0, 0))
    if game_over:
        display_message("GAME OVER!", "TRY AGAIN!", "ENDING LEVEL: " + str(current_level - 1), "Press The Space Bar To Play Again!")
    elif game_complete:
        display_message("YOU WON!", "WELL DONE!", "ENDING LEVEL: " + str(current_level - 1), "Press The Space Bar To Play Again!")
    else:
        for star in stars:
            star.draw()


def make_stars(number_of_extra_stars):
    colors_to_create = get_colors_to_create(number_of_extra_stars)
    new_stars = create_stars(colors_to_create)
    layout_stars(new_stars)
    animate_stars(new_stars)
    return new_stars


def get_colors_to_create(number_of_extra_stars):
    colors_to_create = ["red"]
    for i in range(0, number_of_extra_stars):
        random_color = random.choice(COLORS)
        colors_to_create.append(random_color)
    return colors_to_create


def create_stars(colors_to_create):
    new_stars = []
    for color in colors_to_create:
        star = Actor(color + "-star")
        new_stars.append(star)
    return new_stars


def layout_stars(stars_to_layout):
    number_of_gaps = len(stars_to_layout) + 1
    gap_size = WIDTH / number_of_gaps
    random.shuffle(stars_to_layout)
    for index, star in enumerate(stars_to_layout):
        new_x_pos = (index + 1) * gap_size
        star.x = new_x_pos
    return []


def animate_stars(stars_to_animate):
    for star in stars_to_animate:
        random_speed_adjustment = randint(0, 5)
        duration = START_SPEED - current_level - random_speed_adjustment
        star.anchor = ("center", "bottom")
        animation = animate(star, duration=duration, on_finished=handle_game_over, y=HEIGHT)
        animations.append(animation)


def handle_game_over():
    global game_over
    game_over = True


def on_mouse_down(pos):
    global stars, current_level
    for star in stars:
        if star.collidepoint(pos):
            if "red" in star.image:
                red_star_click()
            else:
                handle_game_over()


def red_star_click():
    global current_level, stars, animations, game_complete
    stop_animations(animations)
    if current_level == FINAL_LEVEL:
        game_complete = True
    else:
        current_level += 1
        stars = []
        animations = []


def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()


def display_message(heading_text, sub_heading_text, sub_sub_heading_text, sub_sub_sub_heading_text):
    screen.draw.text(heading_text, fontsize=90, center=CENTER, color=FONT_COLOR)
    screen.draw.text(sub_heading_text, fontsize=30, center=(CENTER_X, CENTER_Y + 40), color=FONT_COLOR)
    screen.draw.text(sub_sub_heading_text, fontsize=30, center=(CENTER_X, CENTER_Y - 40), color=FONT_COLOR)
    screen.draw.text(sub_sub_sub_heading_text, fontsize=40, center=(CENTER_X, CENTER_Y - 80), color=FONT_COLOR)


def update():
    global stars, game_complete, game_over, current_level
    if len(stars) == 0:
        stars = make_stars(current_level)
    if (game_complete, game_over) and keyboard.space:
        stars = []
        current_level = 1
        game_complete = False
        game_over = False


def shuffle():
    global stars
    if stars:
        x_values = [star.x for star in stars]
        random.shuffle(x_values)
        for index, star in enumerate(stars):
            new_x = x_values[index]
            animation = animate(star, duration=1, x=new_x)
            animations.append(animation)


clock.schedule_interval(shuffle, randint(0, 1))
pgzrun.go()
