import random
import re
import string


# -----------------------------------------------------------
# Added these features which improve the success:
#         93.61 @ 10k words w/ no forced vowels [ baseline ]
#         94.02 @ 10k words w/ forced vowels
#         96.78 @ 10k words w/ removing words which have letters which are confirmed misses
#         96.91 @ 10k words w/ not double counting letter frequency per word
# xx 1. vowels - force vowel inclusion if not found a vowel
# xx 2. q - follow by u if not chosen
# xx 3. frequency - dont double count letter frequency in words
# xx 4. if already guessed a letter - remove all words with that letter - if letter was a miss
class DanSolver:
    # creation of object
    def __init__(self):
        # permanent variables
        self.vowels = set(list('aeiouy'))

        # temporary variables
        self.guessed_so_far = set([])  # list of letters guessed so far
        self.dict = set([])  # dictionary of words still under consideration
        self.adlist = []  # adaptive list of letter to try sorted by frequency
        self.correctletters = set([])  # set of correct letters guessed so far
        self.missedletters = set([])   # set of missed letters guessed so far

        # pre-load all dictionaries by word length
        self.totaldict = get_dictionary()  # get all words  key: word  value: list of letters
        self.lengthdicts = []  # list: each entry by i -> dictionary set of words with length i
        for i in range(0, 50):
            self.lengthdicts.append(set([]))

        for w in self.totaldict.keys():  # for each word , put into correct bucket
            length = len(self.totaldict[w])
            self.lengthdicts[length].add(w)

    # prepare variables for a new word game
    def initialize(self, wordlength):
        self.guessed_so_far = set([])   # letters guessed so far
        self.adlist = []                # adaptive list of letters sorted by best to worst - for guessing
        self.correctletters = set([])   # set of correct letters guessed so far
        self.missedletters = set([])   # set of missed letters guessed so far
        # note: make a copy of the dictionary - so we dont alter the original !! (not by reference)
        self.dict = self.lengthdicts[wordlength].copy()  # start with dictionary of words of this length

    # select guessing algorithm
    def make_guess(self, revealed_so_far):
        guess = self.ds_solver(revealed_so_far)
        return guess

    # new efficient DS solver
    def ds_solver(self, reveal):
        revset = set(reveal)  # set of unique revealed letters so far (includes the '_')
        removes = set([])     # will hold a set of words to remove from dictionary

        # check if this round revealed any new miss letters - filter dictionary if yes
        missed = self.guessed_so_far - revset  # letters which were guessed, but are not in word
        if len(missed) > len(self.missedletters):  # a new letter was missed
            newmissed = (missed - self.missedletters).pop()
            self.missedletters = missed  # update our missed letter list
            for lword in self.dict:  # process each word in dictionary
                if newmissed in lword:
                    removes.add(lword)

        # check if this round revealed any new success letters - filter dictionary if yes
        if len(revset) > 1 and len(self.dict) > 1:  # only process if new revealed letter & not already guessed word
            revset.remove('_')
            if len(revset) > len(self.correctletters):  # a new letter has been revealed - update the dictionary
                # get the newly revealed letter
                newletter = (revset - self.correctletters).pop()  # new letter revealed on this round
                self.correctletters = revset              # update list of correct letters to include it

                # process the newly revealed letter
                present = set([])  # indices of all the locations where the letter was revealed
                for i in range(0, len(reveal)):
                    if reveal[i] == newletter:
                        present.add(i)
                absent = set(range(0, len(reveal))) - present  # locations where the letter should not be

                # filter the dictionary
                # 1. all the places where the letter exists - confirm its there
                # 2. all the places where the letter does not exist - confirm its not there
                for lword in self.dict:  # process each word in dictionary
                    llist = self.totaldict[lword]  # convert word into list of letters
                    reject = False
                    for i in present:
                        if llist[i] != newletter:
                            reject = True
                            break
                    if not reject:
                        for i in absent:
                            if llist[i] == newletter:
                                reject = True
                                break
                    if reject:
                        removes.add(lword)

        if len(removes):
            # update the dictionary - removing rejected words
            for word in removes:
                self.dict.remove(word)

            # updated frequency preference only for a specified dictionary
            self.adlist = get_frequency_for_dict(self.dict)

        # first time - get adaptive list
        if len(self.adlist) == 0:
            self.adlist = get_frequency_for_dict(self.dict)

        # check if found any vowels so far (and not already guessed all vowels ) - if not, force a vowel
        force_vowel = False
        if(len(revset.intersection(self.vowels)) == 0) and not self.vowels.issubset(self.guessed_so_far):
            force_vowel = True

        # make best guess
        found_guess = False
        k = 0
        guess = 'a'
        while not found_guess and k < len(self.adlist):
            if self.adlist[k] not in self.guessed_so_far:
                guess = self.adlist[k]
                if force_vowel:
                    found_guess = guess in self.vowels
                else:
                    found_guess = True
            k += 1

        # if 'q' exists in word and not guessed a 'u' - force 'u'  [ if not already found word ]
        if ('q' in revset) and ('u' not in self.guessed_so_far) and (len(self.dict) > 1) and (guess != 'u'):
            guess = 'u'

        # record the guess
        self.guessed_so_far.add(guess)

        return guess


class BozSolver:
    """Specific strategy as defined by Brian Bozzuto"""

    def __init__(self):
        # This assumes that all games will pull from the common set of possible letters and words.
        self.available_letters = get_possible_letters()
        self.available_words = get_dictionary()

        # variables that will be set during initialization of a new game
        self.confirmed_letters = []
        self.excluded_letters = []
        self.remaining_letters = []
        self.word_so_far = ""
        self.possible_words = []

    def initialize(self, word_length):
        # This is called to initialize a new game under the same basic assumptions of available words & letters
        # It requires the length of the mystery word and will immediately begin paring down the possible list of words
        self.confirmed_letters = []
        self.excluded_letters = []
        self.remaining_letters = get_possible_letters()
        self.possible_words = self.available_words

    def make_guess(self, word_so_far=""):
        self.possible_words = self.refine_list(self.possible_words, self.excluded_letters, word_so_far)
        guess_list = get_frequency_for_dict(self.possible_words)
        guess = ""
        for letter in guess_list:
            if letter in self.remaining_letters:
                guess = letter
                self.remaining_letters.remove(letter)
                self.excluded_letters.append(letter)
                break
        return guess

    def refine_list(self, word_list, excluded_letters=[], known_word=""):
        regex_text = self.build_regex(known_word, excluded_letters)
        regex = re.compile(regex_text)
        refined_list = list(filter(regex.match, word_list))
        return refined_list

    def build_regex(self, known_word, excluded_letters=[]):
        wild_card = "["
        if len(excluded_letters) > 0:
            wild_card += "^"
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


def get_possible_letters():
    return list("abcdefghijklmnopqrstuvwxyz")


def get_frequency_for_dict(indict):
    freq = {i: 0 for i in get_possible_letters()}
    for word in indict:
        for ltt in set(word):
            freq[ltt] += 1
    return sorted(freq, key=lambda x: freq[x], reverse=True)


def get_dictionary(length=0):
    whitelist = set('abcdefghijklmnopqrstuvwxyz\n')  # only use these characters - remove everything else
    fname = "/usr/share/dict/words"
    fhand = open(fname)
    data = fhand.read().lower()
    fdata = ''.join(filter(whitelist.__contains__, data))
    words = fdata.split('\n')
    indict = {}
    for w in words:
        if len(w) == length or length == 0:
            indict[w] = list(w)

    return indict

