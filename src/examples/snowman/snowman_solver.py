import random


class Solver:
    """This is where we come up with cool strategies for solving snowman puzzles"""

    def __init__(self, strategy="random", word_length=10):
        self.word_length = word_length
        self.possible_letters = get_possible_letters()
        self.frequent_letters = list("etaoinsrhldcumfpgwybvkxjqz")
        self.strategy = strategy
        self.guess_list = []

    def make_guess(self):
        if self.strategy == "frequency":
            guess = self.frequent_letters.pop(0)
        elif self.strategy == "frequency by length":
            if len(self.guess_list) == 0:
                self.guess_list = get_frequency(self.word_length)
            guess = self.guess_list.pop(0)
        else:
            index = random.randint(0, len(self.possible_letters) - 1)
            guess = self.possible_letters.pop(index)

        return guess


def get_possible_letters():
    return list("abcdefghijklmnopqrstuvwxyz")


def get_frequency(length=0):
    dict = get_dictionary(length)
    freq = {i: 0 for i in get_possible_letters()}
    for word in dict:
        for l in word:
            freq[l] += 1
    return sorted(freq, key= lambda x: freq[x], reverse=True)


def get_dictionary(length=0):
    whitelist = set('abcdefghijklmnopqrstuvwxyz\n')  # only use these characters - remove everything else
    fname = "/usr/share/dict/words"
    fhand = open(fname)
    data = fhand.read().lower()
    fdata = ''.join(filter(whitelist.__contains__, data))
    words = fdata.split('\n')
    dict = []
    for w in words:
        if length > 0:
            if len(w) == length:
                dict.append(w)
        else:
            if len(w) > 1:
                dict.append(w)
    return dict


# print("testing")
# print(get_frequency(6))
