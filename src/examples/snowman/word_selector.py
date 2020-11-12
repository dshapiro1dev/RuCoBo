from random import seed
from random import choice
from time import time

# characters allowed
whitelist = set('abcdefghijklmnopqrstuvwxyz\n')  # only use these characters - remove everything else


def get_word():
    with open("/usr/share/dict/words") as file_object:
        data = file_object.read().lower()
        words = ''.join(filter(whitelist.__contains__, data)).split('\n')
    seed(time())
    return choice(words)
