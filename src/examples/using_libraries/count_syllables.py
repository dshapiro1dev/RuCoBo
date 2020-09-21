# we are going to import the PyPhen library - which processes words in natural languages
# here we will use it to count the number of syllables in a word

# first you must install the library like this - in a terminal
# pip3 install pyphen

# at bottom of Pycharm is the name of Python being run - if you click on it
# go to interpreter settings
# you should be able to see which libraries are now imported

# import our library
import pyphen

# test syllable hyphenation
dic = pyphen.Pyphen(lang='en')   # choose english as our language
test = dic.inserted('beautiful') # hyphenate a random word
print(test)  # beau-ti-ful  note: how it breaks the word up with hyphens into syllables

test = dic.inserted('invincibility') # lets try another word
syllables = test.split("-")  # this time split the word by the hyphens to get the syllables
print(syllables)  # ['in', 'vin', 'ci', 'bil', 'i', 'ty'] - a list which each syllable
print("Num syllables %d" % len(syllables))  # prints out the number of syllables



