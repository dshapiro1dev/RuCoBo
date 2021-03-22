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
    global game_over, hedgehog_score, fox_score
    game_over = True


def update():
    global fox_score
    global hedgehog_score
    global game_over

    if not game_over:
        if keyboard.left:
            fox.x -= 6
        elif keyboard.right:
            fox.x += 6
        elif keyboard.up:
            fox.y -= 6
        elif keyboard.down:
            fox.y += 6

        fox_coin_collected = fox.colliderect(coin)

        if fox_coin_collected:
            fox_score += 1
            place_coin()

        if not hedgehog.colliderect(fox):
            if hedgehog.y > coin.y:
                hedgehog.y -= 1.75
            elif hedgehog.y < coin.y:
                hedgehog.y *= 1.05
            if hedgehog.x > coin.x:
                hedgehog.x -= 1.75
            elif hedgehog.x < coin.x:
                hedgehog.x *= 1.05

        hedgehog_coin_collected = hedgehog.colliderect(coin)

        if hedgehog_coin_collected:
            hedgehog_score += 1
            place_coin()

    elif game_over:
        hedgehog.x = 0
        hedgehog.y = 0
    elif game_over and keyboard.space:
        game_over = False
        hedgehog_score = 0
        fox_score = 0
        if not hedgehog.colliderect(fox):
            if hedgehog.y > coin.y:
                hedgehog.y -= 1.75
            elif hedgehog.y < coin.y:
                hedgehog.y *= 1.05
            if hedgehog.x > coin.x:
                hedgehog.x -= 1.75
            elif hedgehog.x < coin.x:
                hedgehog.x *= 1.05
        clock.schedule(time_up, 20.0)


clock.schedule(time_up, 20.0)
place_coin()
pgzrun.go()
