import random


class Solver:
    """This is where we come up with cool strategies for solving snowman puzzles"""

    def __init__(self, strategy="random", word_length=10):
        self.word_length = word_length
        self.possible_letters = get_possible_letters()
        self.frequent_letters = list("etaoinsrhldcumfpgwybvkxjqz")
        self.strategy = strategy
        self.guess_list = []
        self.guessed_so_far = []

    def make_guess(self,revealed_so_far):
        if self.strategy == "frequency":
            guess = self.frequent_letters.pop(0)
        elif self.strategy == "frequency by length":
            if len(self.guess_list) == 0:
                self.guess_list = get_frequency(self.word_length)
            guess = self.guess_list.pop(0)
        elif self.strategy == "ds adaptive":
            guess = self.ds_adaptive(revealed_so_far)
        else:
            index = random.randint(0, len(self.possible_letters) - 1)
            guess = self.possible_letters.pop(index)

        return guess

    # TO DO:
    # 1. if  'e' appears in location 'i' only - remove all words w/ 'e' in non-i location
    # 2. remove words that dont have 'e'  at all - if 'e' is revealed as in word
    # 3. choose a letter (all else being equal) - that will cut the tree the most on next round
    def ds_adaptive(self,reveal):
        # get dictionary of words only this long
        dict = get_dictionary(len(reveal))

        # helper variables
        length = len(reveal) # length of word
        removes = {}         # dictionary of words to remove - that are mismatched
        revletters = {}      # dictionary of revealed letters
        for l in reveal:
            if l!='_':
                revletters[l]=1

        # subselect a dictionary with only words that match revealed pattern so far
        for lword in dict:
            llist = list(lword)  # convert word into list of letters
            # filter  : known letter at known position - not there in the word in dictionary
            #           known letter in dictionary word at a position - but is not in the "reveal" at that position
            for i in range(0,length):
                if reveal[i]!='_' and llist[i]!=reveal[i]:
                    removes[lword] = 1
                if llist[i] in revletters.keys() and reveal[i]=='_':
                    removes[lword] = 1

        # create cleaned dictionary only with matching words
        cleandict = []
        for lword in dict:
            if lword not in removes:
                cleandict.append(lword)

        # get frequency only for a specified dictionary
        adaptive_list = get_frequency_for_dict(cleandict)

        # make best guess
        found_guess = False
        k = 0
        guess = 'a'
        while not found_guess:
            if adaptive_list[k] not in self.guessed_so_far:
                guess = adaptive_list[k]
                found_guess = True
            k += 1

        # record the guess
        self.guessed_so_far.append(guess)

        return guess

def get_possible_letters():
    return list("abcdefghijklmnopqrstuvwxyz")

def get_frequency_for_dict(dict):
    freq = {i: 0 for i in get_possible_letters()}
    for word in dict:
        for l in word:
            freq[l] += 1
    return sorted(freq, key= lambda x: freq[x], reverse=True)


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
