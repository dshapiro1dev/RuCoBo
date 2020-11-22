# Attack roll with someone who has a plus 3 to hit against an armor class of 13
# process a critical hit if someone rolls a natural 20
# process a critical fail if someone rolls a natural 1
import random
import time


def attack_role(ac, bonus=0):
    #seed our random number generator and get a random number between 1 and 20
    random.seed(time.time())
    die = random.randint(1, 20)

    modified_die = die + bonus

    hit = False
    if die == 20:
        print(f"I rolled {die} and got a crit!")
        hit = True
    elif die == 1:
        print(f"I rolled {die} Don't even try...")
        hit = False
    elif modified_die >= ac:
        print(f"I rolled {die} Whacky whacky")
        hit = True
    else:
        print("oh, I dropped the die and need to roll again")
        hit = False
    return hit

x = 0
while x < 20:
    attack_role(13, 3)
    x += 1