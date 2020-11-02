# characters allowed
whitelist = set('abcdefghijklmnopqrstuvwxyz\n')  # only use these characters - remove everything else

# get list of all available words
fname = "/usr/share/dict/words"
fhand = open(fname)
data = fhand.read().lower()
fdata = ''.join(filter(whitelist.__contains__, data))
words = fdata.split('\n')
dict = {}
for w in words:
    if(len(w)>1):
        dict[w] = {}

# count frequency of letters in english dictionary
freq = {}
ltrs = list(fdata.replace('\n',''))
for l in ltrs:
    if l in freq:
        freq[l] += 1
    else:
        freq[l] = 1

# sort letters by least to most common - create ranking
letter_rank = {}
i = 1
for l in sorted(freq.keys(), key= lambda x: freq[x] , reverse=True):
    print(f"{l} -> {freq[l]}  ")
    letter_rank[l] = i
    i+=1

# give a difficulty score to each word
difficulty = {}
for w in dict.keys():
    # count unique number of letters in word
    letters = {}
    for l in list(w):
        letters[l] = 1
    metric1 = len(letters.keys()) # how many unique letters

    # sum up difficulty of letters based on frequency
    metric2 = 0
    for l in letters.keys():
        metric2 = metric2 + letter_rank[l]

    # store metrics
    difficulty[w] = { "m1" : metric1, "m2" : metric2}

# sort by metric2 (sum of difficulty of letters)
for l in sorted(difficulty.keys(), key= lambda x: difficulty[x]["m2"] , reverse=False):
    print(l,end=" ")
    print(len(l),end=' ')                        # length of word
    print(difficulty[l]['m1'],end=" ")   # how many unique letters
    print(difficulty[l]['m2'],end="\n")  # sum of letter unusualness scores
