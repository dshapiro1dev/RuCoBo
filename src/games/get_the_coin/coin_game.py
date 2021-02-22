import pgzrun
from random import randint
from pgzero import clock
from pgzero.actor import Actor

WIDTH = 400
HEIGHT = 400
hedgehog_score = 0
fox_score = 0
game_over = False

fox = Actor("fox")
fox.pos = 100, 100

coin = Actor("coin")
coin.pos = 200, 200

hedgehog = Actor("hedgehog")
hedgehog.pos = 300, 300


def draw():
    screen.fill("aquamarine")
    fox.draw()
    coin.draw()
    hedgehog.draw()
    screen.draw.text(f"Fox Score: {str(fox_score)}\t\t"
                     f"Hedgehog Score: {str(hedgehog_score)}", color="black", topleft=(10, 10))
    if game_over:
        screen.fill("pink")
        screen.draw.text(f"Fox Score: {str(fox_score)}\t\t"
                         f" Hedgehog Score: {str(hedgehog_score)}",
                         topleft=(10, 10), fontsize=26, bold=True)


def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))


def time_up():
    global game_over
    game_over = True


def update():
    global fox_score
    global hedgehog_score

    if keyboard.left:
        fox.x -= 4
    elif keyboard.right:
        fox.x += 4
    elif keyboard.up:
        fox.y -= 4
    elif keyboard.down:
        fox.y += 4

    fox_coin_collected = fox.colliderect(coin)

    if fox_coin_collected:
        fox_score += 1
        place_coin()

    if keyboard.a:
        hedgehog.x -= 4
    elif keyboard.d:
        hedgehog.x += 4
    elif keyboard.w:
        hedgehog.y -= 4
    elif keyboard.s:
        hedgehog.y += 4

    hedgehog_coin_collected = hedgehog.colliderect(coin)

    if hedgehog_coin_collected:
        hedgehog_score += 1
        place_coin()


clock.schedule(time_up, 30.0)
place_coin()
pgzrun.go()