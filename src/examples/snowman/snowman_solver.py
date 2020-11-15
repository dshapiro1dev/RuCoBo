import random
import re
import string
class Solver:
    """This is where we come up with cool strategies for solving snowman puzzles"""

    def __init__(self, strategy="random", word_length=10):
        self.word_length = word_length
        self.possible_letters = get_possible_letters()
        self.frequent_letters = list("etaoinsrhldcumfpgwybvkxjqz")
        self.strategy = strategy
        self.guess_list = []
        self.possible_words = get_dictionary(word_length)
        self.confirmed_letters = []
        self.excluded_letters = []
        self.remaining_letters = get_possible_letters()
        self.word_so_far = ""
        while len(self.word_so_far) < word_length:
            self.word_so_far += "_"

    def make_guess(self):
        guess = ""
        if self.strategy == "frequency":
            guess = self.frequent_letters.pop(0)
        elif self.strategy == "frequency by length":
            self.guess_list = get_frequency(self.possible_words)
            for letter in self.guess_list:
                if letter in self.remaining_letters:
                    guess = letter
                    self.remaining_letters.remove(letter)
                    break
        else:
            index = random.randint(0, len(self.possible_letters) - 1)
            guess = self.possible_letters.pop(index)
        return guess

    def learn_result(self, letter, result):
        if result:
            if letter not in self.confirmed_letters:
                self.confirmed_letters.append(letter)
        else:
            if letter not in self.excluded_letters:
                self.excluded_letters.append(letter)
        self.possible_words = refine_list(self.possible_words, self.confirmed_letters, self.excluded_letters,
                                          self.word_so_far)

    def update_word_so_far(self, word):
        self.word_so_far = word.lower()


def get_possible_letters():
    return list("abcdefghijklmnopqrstuvwxyz")


def get_frequency(word_list):
    freq = {i: 0 for i in get_possible_letters()}
    for word in word_list:
        for l in word:
            freq[l] += 1
    return sorted(freq, key=lambda x: freq[x], reverse=True)


def refine_list(word_list, included_letters=[], excluded_letters=[], known_word=""):
    refined_list = []

    regex_text = build_regex(known_word, included_letters, excluded_letters)
    regex = re.compile(regex_text)
    refined_list = list(filter(regex.match, word_list))
    return refined_list


def build_regex(known_word, included_letters=[], excluded_letters=[]):

    wild_card = "["
    if len(included_letters) > 0 or len(excluded_letters) > 0:
        wild_card += "^"
        for il in included_letters:
            wild_card += il
        for el in excluded_letters:
            wild_card += el
        wild_card += "]"
    else:
        wild_card += "a-z]"

    letters = list(known_word)
    regex = ""
    for l in letters:
        if l == "_":
            regex += wild_card
        elif l != " ":
            regex += l
    return regex


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
