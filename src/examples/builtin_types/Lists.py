# lists are ordered collections of things
# while a single variable holds one thing (like a number or string etc)
# a list holds a collection of things, in a certain order

# lets make a list of spices in our kitchen
# notice we use square brackets, which tells Python this is a list
# and use commas to separate
spices = ["cumin","pepper","cinnamon","dessicated yak horn","salt","dirt"]

# now lets see how to access our list
# lists start counting at zero (0)
# so the first entry is 0, the second entry is 1, the third entry is 2
# here the third entry is cinnamon
third_spice = spices[2]
print(third_spice)

# we can make a list a collection of anything
# here we have a mix of:  integers (eg: 1), strings and floats (37.5)
# a float is non-integer number
jumbled = [1, "yak fur",37.5, "emu pancreas"]
print(jumbled)

# lists have in-built functions
# lets look at sorting the list
# (notice there are duplicates, that's fine)
outoforder = [3,1,5,77,8,9,8,3]
outoforder.sort()  # this sorts the list in place and updates it
print(outoforder)

# now how do we modify the list
# lets change the 2nd element (note: indexed by [1] ) to 99
start = [1,2,3,3,3]
start[1] = 99
print(start)

# lets add (append) some number to the list
start.append(77)
start.append("yak")
print(start)  # 1, 99, 3, 3, 3, 77, "yak"   -> we have added 77 and "yak" to the end

# --------------------
# removing from a list

# how do we delete an element - here one we know
start.remove("yak")
print(start)  # the yak is gone (good riddance)

# what if we try remove an element that appears multiple times
# notice it only removes one of the '3's  (there were three 3's)
start.remove(3)
print(start)

# removing a non-existing element will crash
# start.remove(255)

# we can also remove an element by its location
del start[0] # removes the first element
print(start)

# --------------
# now some basic functions on list
testit = [1,2,3,4,5,88]
print(len(testit))  # 6 elements in the list  [ length ]
print(max(testit))  # maximum value in list is 88
print(min(testit))  # minimum value in list is 1

# lets see "membership" - ie: can we find an element in a list using the function "in"
beasties = ["otter","gnat","yak","sloth"]
if "orangutan" in beasties:
    print("YES - we found an orangutan")
else:
    print("NO - there is no orangutan")

if "yak" in beasties:
    print("YES - we found a yak")
else:
    print("NO - there is no yak")

# what do you think happens when you sort a list that has no obvious sorting - lets see
huh = [1,22,3.1415,"beastie",8,"dirty sok",27,"yak ear"]
#huh.sort()  # this command will crash - it does not work
beasties.sort()  # but this will work - since its only words - python sorts by alphabetical order
print(beasties)

# interestingly you can do operations on list
list1 = [1,2,5]
list2 = [8,9,20]
listboth = list1 + list2
print(listboth)  # 1 2 5 8 9 20   <- puts the list together using a "+"

# other fun things
listboth.reverse() # what do you think this does

