# import libraries we need
import pyphen  # library for
import string  # library to deal with strings
import glob    # getting list of files
import re      # regular expression library

# get list of files in directory
flist = (glob.glob("../../../data/presidentspeeches/raw/*.txt"))

# only keep basic letters
whitelist = set('0123456789abcdefghijklmnopqrstuvwxyz .')  # only use these characters - remove everything else

# create dictionary:  president -> all data
speeches = {}  # key: president   value: all speeches in a single string

# read files - count words
for fname in flist:   # process each file in the list of files
    fhand = open(fname,"r") # open file , get file handle

    # read first line - get president name
    pres = fhand.readline().lower().replace("president: ","").replace("\n","") # get presidents name

    # create entry for this president if needed
    if pres not in speeches:
        speeches[pres] = ""  # create empty string to start

    # read entire speech into a single string - scrub the string
    all = fhand.read().lower() # read all data in file
    all = all.replace("(applause)", " ")  # not part of speech - audience action
    all = all.replace("(laughter)", " ")  # not part of speech - audience action
    all = all.replace("\n"," ") # replace all new lines with spaces
    all = all.replace("mr.", "mister ") # special case:  mister , remove dot
    all = all.replace("mrs.", "missus ") # special case:
    all = all.replace("-", " ") # replace hyphens with space
    all = re.sub('\s+',' ',all) # compress multiple spaces into one
    cleaned = ''.join(filter(whitelist.__contains__, all)) # keep only allowed characters

    # store speech in president's entry
    speeches[pres] += cleaned

# ============================================
# analyze each president
engdict = pyphen.Pyphen(lang='en') # english dictionary
allfk = {}

for pres in speeches.keys():
#    print("Analyzing: " + pres)
    data = speeches[pres]

    # break up data into words and sentences
    sentences = data.split('.')
    words = data.replace('.',' ').split()

    # count total number of syllables
    tot_syl = 0
    for w in words:
        hyp = engdict.inserted(w)
        numsyl = len( hyp.split("-"))
        tot_syl += numsyl
#        print("word: " + w + " split: " + hyp + " n:" + str(numsyl))

    # count
    tot_sen = len(sentences)
    tot_wor = len(words)

    # flesch kincaid
    fk = 206.835 - 1.015 * tot_wor/tot_sen - 84.6 * tot_syl/tot_wor
    allfk[pres] = int(fk)

 # print final analysis
sort_orders = sorted(allfk.items(), key=lambda x: x[1], reverse=True)
for i in sort_orders:
    print(i[1] , i[0])


#Score	School level	Notes
# 100.00–90.00	5th grade	Very easy to read. Easily understood by an average 11-year-old student.
# 90.0–80.0	6th grade	Easy to read. Conversational English for consumers.
# 80.0–70.0	7th grade	Fairly easy to read.
# 70.0–60.0	8th & 9th grade	Plain English. Easily understood by 13- to 15-year-old students.
# 60.0–50.0	10th to 12th grade	Fairly difficult to read.
# 50.0–30.0	College	Difficult to read.
# 30.0–10.0	College graduate	Very difficult to read. Best understood by university graduates.
# 10.0–0.0	Professional	Extremely difficult to read. Best understood by university graduates.