from random import seed, random
from random import choice
from time import time

# characters allowed
whitelist = set('abcdefghijklmnopqrstuvwxyz\n')  # only use these characters - remove everything else


def get_word(rocoboian =""):
    word = ""
    if rocoboian == "adam":

        # get list of all available words
        with open("/usr/share/dict/words") as file_object:
            data = file_object.read().lower()
            words = ''.join(filter(whitelist.__contains__, data)).split('\n')
            fData = ''.join(filter(whitelist.__contains__, data))

        dictionary = {}
        for w in words:
            if len(w) > 1:
                dictionary[w] = {}

        # count frequency of letters in english dictionary
        freq = {}
        someLetters = list(fData.replace('\n', ''))
        for d in someLetters:
            if d in freq:
                freq[d] += 1
            else:
                freq[d] = 1

        # sort letters by least to most common - create ranking
        letter_rank = {}
        i = 1
        for d in sorted(freq.keys(), key=lambda x: freq[x], reverse=True):
            # print(f"{d} -> {freq[d]}  ")
            letter_rank[d] = i
            i += 1

        # give a difficulty score to each word
        difficulty = {}
        for w in dictionary.keys():
            # count unique number of letters in word
            letters = {}
            for d in list(w):
                letters[d] = 1
            metric1 = len(letters.keys())  # how many unique letters

            # sum up difficulty of letters based on frequency
            metric2 = 0
            for d in letters.keys():
                metric2 = metric2 + letter_rank[d]

            # store metrics
            difficulty[w] = {"m1": metric1, "m2": metric2}

        hard_word_list = []
        for d in sorted(difficulty.keys(), key=lambda x: difficulty[x]["m2"], reverse=False):
            # print(d)
            wordLength = len(d)
            if wordLength > 5:
                continue
            elif wordLength < 2:
                continue
            else:
                hard_word_list.append(d)

        seed(time())
        word = choice(hard_word_list)

    elif rocoboian == "yael":
        # whitelist = set('abcdefghijklmnopqrstuvwxyz\n')  # only use these characters - remove everything else
        evilet = set(['x', 'q', 'z', 'j'])
        # get list of all available words
        fname = "/usr/share/dict/words"
        fhand = open(fname)
        data = fhand.read().lower()
        fdata = ''.join(filter(whitelist.__contains__, data))
        words = fdata.split('\n')

        # loop over words - and only select those which have no repeated characters
        mylist = []  # list of keep words
        for w in words:
            # check if w  has repeated letters or not
            letters = list(w)  # makes a new list with every letter in "w" in it
            letterdict = {}
            # if the letter is the first, put it as a new entry in the letterdict,
            goodword = True
            for letter in letters:
                # if there is a new letter in letter that is not in letterdict, add it to it
                if letter in letterdict.keys():
                    # seen this letter before, since their is already a key for it
                    goodword = False  # so that you know this isn't a good snowman word
                else:
                    # not seen this letter before,
                    letterdict[letter] = 1  # there are no repeats in letters, meaning everything  is okay.

            # if w  has NO repeated letters , then put it into my special list
            if goodword:
                mylist.append(w)
        # print(mylist)
        # put this word into mylist since its ok
        # print(len(mylist))
        # next,sort words less than 7 long
        shortdict = []
        for wordet in mylist:
            wow = set(wordet)
            if len(wordet) < 4 and wow.intersection(evilet):
                shortdict.append(wordet)
        # and with at least one of Z J Q X

        word = choice(shortdict)

    elif rocoboian == "trevor":

        allowed_letters = set("abcdefghijklmnopqrstuvwxyz\n")
        path_to_dictionary = "/usr/share/dict/words"

        dictionary_file = open(path_to_dictionary)
        words = dictionary_file.read().lower()

        allowed_words = ''.join(filter(allowed_letters.__contains__, words))
        word_list = allowed_words.split('\n')
        hard_word_list = []

        for w in word_list:
            if 2 < len(w) < 4 and "j" in w:
                hard_word_list.append(w)

        word = choice(hard_word_list)

    elif rocoboian == "natan":
        dict = {'perm': 1}
        word = choice(list(dict.keys()))

    else:
        with open("/usr/share/dict/words") as file_object:
            data = file_object.read().lower()
            words = ''.join(filter(whitelist.__contains__, data)).split('\n')
        seed(time())
        word = choice(words)

    return word
