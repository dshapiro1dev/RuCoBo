# import libraries we need
import pyphen  # library for
import string  # library to deal with strings
import glob    # getting list of files
import re      # regular expression library

# get list of files in directory
flist = (glob.glob("../../../data/presidentspeeches/raw/*.txt"))

# create "drop" list:  common words
droplist = ['the','of','to','and','in','a','that','is','for','be','it',
            'have','by','this','as','with','which','are','will','on','has',
            'all','been','or','from','but','they','was','at','its','an','can','would',
            'more','who','so','were','these','should','them','any','there','if','other',
            'such','now','those','one','do','than','may','must','what','had',
            'when','thats','just','because',
            'i','we','you','their','my','not','our','.','no','upon','shall','us','some','here','he',
            'about','his','your'
            ]
dropdict = {}
for d in droplist:
    dropdict[d] = 1

# setup data structures
whitelist = set('abcdefghijklmnopqrstuvwxyz .')  # only use these characters - remove everything else
wordcount = {} # will store a dictionary: for each president - a dictionary of words with their counts
overall = {}

# read files - count words
for fname in flist:   # process each file in the list of files
    fhand = open(fname,"r") # open file , get file handle

    # read first line - get president name
    pres = fhand.readline().lower().replace("president: ","").replace("\n","") # get presidents name

    # create a dictionary for this president - if does not already exists
    if pres not in wordcount:
        wordcount[pres] = {}

    # read entire speech into a single string - scrub the string
    all = fhand.read().lower() # read all data in file
    all = all.replace("\n"," ") # remove all new lines
    all = re.sub('\s+',' ',all) # compress multiple spaces into one
    cleaned = ''.join(filter(whitelist.__contains__, all)) # keep only allowed characters
    sentences = cleaned.split('.')
    cleaned = cleaned.replace('.','')
    words = cleaned.split() # make list of words, splitting entire speech by whitespace

    # make map of word counts
    for w in words:
        # track dictionary for this president
        if w in dropdict:  # drop common words
            continue
        if w in wordcount[pres]:
           wordcount[pres][w] += 1
        else:
           wordcount[pres][w] = 1

        # also track the overall dictionary for all presidents in one place
        if w in dropdict:  # drop common words
            continue
        if w in overall:
            overall[w] +=1
        else:
            overall[w] = 1

    fhand.close()

# finished processing all files
# -----------------------------

# ----------------------------------------------------
# for each president - print the 15 most common words
for president in sorted(wordcount.keys()):
    print("President:" + president, end='::  ')
    thisdict = wordcount[president] # dictionary for this president
    for k in sorted(thisdict.items(), key=lambda x: x[1], reverse=True)[1:12]:
        print(str(k[0]) + ":" + str(k[1]),end=" ")
    print()

# ----------------------------------------------------
# compute complexity of english language by president
print('============================================================')
for president in sorted(wordcount.keys()):
    print("President:" + president, end=':: ')

    # compute statistics
    # - number of words per speech
    # - number of sentences per speech
    # - mean syllables per word