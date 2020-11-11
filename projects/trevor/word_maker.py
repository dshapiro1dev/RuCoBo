# this module contains the evilest function for picking a word to play snow man.
import random

def hard_word():
    allowed_letters = set("abcdefghijklmnopqrstuvwxyz\n")
    path_to_dictionary = "/usr/share/dict/words"

    dictionary_file = open(path_to_dictionary)
    words = dictionary_file.read().lower()

    allowed_words = ''.join(filter(allowed_letters.__contains__, words))
    word_list = allowed_words.split('\n')
    hard_word_list = []

    for w in word_list:
        if len(w) > 15 and "j" in w:
            hard_word_list.append(w)

    chosen_word = random.choice(hard_word_list)

    return chosen_word