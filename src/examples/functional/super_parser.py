# This function will return a dictionary with the top N most common words used and a count of how often each was used
# The 'topcount' parameter allow you to specify just how many results to return and will default to 10 if now value
# is provided
import string
import collections


def word_counter(phrase, topcount=10):
    # this line makes a dictionary that is used to translate all punctuation marks to a blank value, and sets all
    # letters to be lower case. It produces a list of each work as it occurs in the string
    wordlist = phrase.translate(str.maketrans('', '', string.punctuation)).lower().split()
    # this line takes the list produced above and puts it into a counter to count the most used words
    counts = collections.Counter(wordlist).most_common(topcount)
    # return the results as a dictionary
    return dict(counts)
