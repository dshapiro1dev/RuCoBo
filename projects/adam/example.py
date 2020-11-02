fileHandle = open("../../../RuCoBo/data/presidentspeeches/raw/1789-04-30-first-inaugural-address.txt", "r")

numOfWords = 0
maxCharCountInWord = 0
longestWordsSoFar = []

whitelist = set('abcdefghijklmnopqrstuvwxyz ')

for ll in fileHandle:

    cleaned = ''.join(filter(whitelist.__contains__, ll.lower()))
    words = cleaned.split()

    for word in words:

        if len(word) >= maxCharCountInWord:
            maxCharCountInWord = len(word)
            print(word)
            print(str(maxCharCountInWord))
            longestWordsSoFar.append(word)

    numOfWords += len(words)

fileHandle.close()

longestWords = []
for word in longestWordsSoFar:
    if len(word) == maxCharCountInWord:
        longestWords.append(word)

# print number of words in doc
print("Number of words in document is " + str(numOfWords))
print("Longest words in speech are " + str(maxCharCountInWord))
print("characters long. and the words are: " + str(longestWords))