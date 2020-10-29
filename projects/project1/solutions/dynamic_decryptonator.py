# Week 1 - Assignment 1
# Write a program that will decode the "ya.encrypted" file using the "ya.key" key
# This approach will read the key and the file before returning a result by using the "translate" function
# this function requires us to build a dictionary that shows the ASCII value of a character with a corresponding
# new value. We'll build this list from the key file and then use it with the translate function on the
# encrypted file

# Define a key map where we will store the values from our decryption file
keyMap = {}

# Read the key into a map
fileKey = open("../../../data/project1/ya.key", "r")

# For each line, parse the 3rd and 1st characters such that the 3rd value is the "key" and the 1st value is
# the "mapped" value. Remember that for arrays we start a '0'
for aLine in fileKey:
    # for each line, add to the key map first the ASCII value for the 3rd character and then the corresponding
    # translation value, which is actually the first character in a row
    keyMap.update({ord(aLine[2]): aLine[0]})

# Don't forget to close the file if you aren't using a "while" or "with" command to open it
fileKey.close()

# Open the encrypted file that we want to decrypt
encryptedFile = open("../../../data/project1/ya.encrypted", "r")

# iterate through each line
for aLine in encryptedFile:
    # use the translate function on the line and pass the keyMap that we created to decrypt the text
    print(aLine.strip().translate(keyMap))

# Don't forget to close the file if you aren't using a "while" or "with" command to open it
encryptedFile.close()

# This may be a little more confusing than the simpler version, but it is much more versatile, as a new
# translation key can be processed without changing the code
