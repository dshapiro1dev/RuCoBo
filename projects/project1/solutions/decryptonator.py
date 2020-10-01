# Week 1 - Assignment 1
# Write a program that will decode the "ya.encrypted" file using the "ya.key" key

# Read the encrypted file
file = open("../../../data/project1/ya.encrypted", "r")

# A brute force version simply scripting each replacement individually
# as each .replace returns a string, we can just string them together
for line in file:
    # each "replace" function returns a string, which is used to replace the next value and those are applied to the
    # string this string is then returned
    print(line.strip().replace("1", "a").replace("5", "e").replace("8", "h").replace("9", "i").
          replace("!", "r").replace("@", "s").replace("#", "t").replace("&", "v").replace("^", "w").replace("`", "y"))

file.close()

# this is kind of clunky, but it should work and doesn't require too many lines. However, if the key changes
# the line above will need to be reworked
