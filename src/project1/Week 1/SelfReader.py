# Week 1 - Assignment 2, make a script that reads itself

# Open this file as read only
myFile = open("SelfReader.py", "r")

# For each line, print it out
for aLine in myFile:
    print(aLine.strip())
myFile.close()

# Hi mom!!!
