# dictionaries are mappings , allowing us to associate a "key" to a "value"
# an example of a dictionary could look like this - where the keys are type of meat
# and the values are the temperature in Fahrenheit you should serve them at

# cooking dictionary of temperature by critter
# lets go ahead and actually make a dictionary structure
temperatures = {
    'salmon' : 120,
    'beef' : 135,
    'bison' : 130,
    'yak' : 98.6,
    'chicken' : 250,
    'snail' : 'just... no'   #
    }

# a few things to notice here
# the curly braces {}  - make python realize that this is an inbuilt dictionary you are creating
# the entries are separated by commas
# each entry consists of a  key : value    pair
# notice that the values do not have to be of one type - here I actually have 3 (not 2) different kinds of values
# 1.  integer
# 2.  float
# 3.  string
# Can you tell which is which?  If you go in the debugger and inspect temperatures - you will see


# now an intrepid cook can look up the temperature they need in a hurry
# notice that the temperature is an integer - so we need to convert it to a string
# otherwise we can not concatenate a string and an integer
print("Hey python - can you give me the temperature I need to cook bison to?")
print("Why yes clueless cook: " + str(temperatures['bison']))

# here the snail 'temperature' is already a string - but it does not hurt to convert it
# since technically we do not know up front about the helpful entry in the dictionary under 'snail'
print("What about snail - what do I cook a snail to?")
print("Seriously clueless cook: " + str(temperatures['snail']))

# what if we try cook an exotic meat that is not in our dictionary
print("Hey python - I want to cook  iguana cheeks")
if('iguana' in temperatures.keys()):
    print("Iguanas -> do this::" + str( temperatures['iguana']))
else:
    print("Humble apologies - we do not have Iguana cooking instructions. An oversight")
# had we tried to force access to a non-existent key - the program would have crashed
# here we check first if the dictionary knows about Iguanas
# fortunately it does not

# but lets see if we can get the list of keys up front - to know how exhaustive is the dictionary
meats = temperatures.keys()  # this gets the keys into the list called 'means
print(meats)
# will print out:  dict_keys(['salmon', 'beef', 'bison', 'yak', 'chicken', 'snail'])

# and then we can cycle through each delicious critter to see what cooking temperatures are, like
for critter in meats:  # go through each critter
    print("If you're grilling :" + str(critter) + " you should cook to a temperature  : " + str(temperatures[critter]))

# you can not have 2 keys in a dictionary which are the same
lovesmost = {
    'dan' : 'steak',
    'dan' : 'yak burger with fries and a side of mayo on a sesame roll with ketchup'
}
print(lovesmost)
# here there is only one key: 'dan'  - it _must_ be unique
# so python takes the 2nd entry as the only entry  [ clearly thats the superior entry anyway ]
# ie: a dictionary can not have 2 different values for the same key

# now each key:value pair is an item in the dictionary
# technically it is a tuple (we'll learn about those soon)
# so lets iterate through all the items
alltuples = temperatures.items()
for t in alltuples:
    print("key : " + t[0] + "  -> stores value: " + str(t[1]))
# note here:  for the tuple  key:value
# to access the first part (ie: the key) we take the 0th index  t[0]
# to access the second part (ie: the value) we take the 1th index t[1]

# another way to cycle through a dictionary is over the list of keys
keylist = temperatures.keys()
for k in keylist:
    print(" the key is: " + k + " and the value : " + str(temperatures[k]))
# notice again that we always convert to a string, using str()

# now lets get clever - and make a dictionary of dictionaries
yak_recipes = {
    'yak stroganoff' : 'one yak, one strog, lot of noff, 2 onions',
    'yak pasta' : 'one yak, one enormous bowl of pasta',
    'yak tartar' : 'one yak, one very large blender'
}
iguana_recipes = {
    'iguana shake' : 'one iguana, a teaspoon of salt, morphine',
    'iguana burger' : 'one iguana, one bun, 3 tubs of ketchup'
}
# first we created 2 dictionaries
# yak_recipes:  has a few yak recipes
# igauana_recipes: has a few iguana recipes

# and now our dictionary of dictionaries
recipe_book = {
        'yak dict' : yak_recipes,
        'iguana_dict' : iguana_recipes
}

# lets print out the recipe book
print(recipe_book)

# and if you want to access an entry - the doubly nested reference
print(recipe_book['yak dict']['yak tartar'])
# this selects first the yak dictionary, and within that the 'yak tartar' recipe

# you can nest arbitrary number of dictionaries (or any other structure) within other structures ...

# lets make a dictionary of numbers, and those numbers to the power of 3 as the value
cubes = {
    i : i*i*i for i in [1,2,3,4,5]
}
print(cubes)
# this sets up the keys 1,2,3,4,5  and for each of those keys, stores the value: i * i * i  ie: the cube

# now lets sort a dictionary by values
# here we set up come friendly critters, and how much they weigh - in a dictionary
weights = {
    'snail' : 1,
    'ferret' : 5,
    'mammoth' : 1000,
    'overweight mammoth' : 2000,
    'yak' : 100,
    'cow with barbells' : 200
}

# lets sort the animals by weight
# this is a tricky call - lets break it apart
# 1. weights.items() -> this grabs all the items in the dictionary. An item is a tuple of [ animal, weight]
#    ie: this is all the 6 entries in the 'weights' dictionary
# 2. then run a sort function on them - but we are going to specify the function
#    the 'key' by which the sort function will work is going to look within the tuple
#    and access the value in x[1] - remember that the tuple has 2 values
#    x[0] is the key,  x[1] is the value
#    so we are saying: take the item (which is the tuple)
#    take the 2nd part of it (which is the value)
#    and sort using that
# lambda is an interesting thing: it is a function without a name
# we'll get to functions later
sorted_critters = sorted(weights.items(), key=lambda x: x[1])

for i in sorted_critters:
	print(i[0], i[1])

# you should get this:
# snail 1
# ferret 5
# yak 100
# cow with barbells 200
# mammoth 1000
# overweight mammoth 2000

# now lets sort instead by the name of the critter
print("--------\n\n")
sorted_critters = sorted(weights.items(), key=lambda x: x[0])

for i in sorted_critters:
	print(i[0], i[1])

# this time it prints out entries in alphabetic order  c,f,m,o,s,y
# cow with barbells 200
# ferret 5
# mammoth 1000
# overweight mammoth 2000
# snail 1
# yak 100

# the above examples cover both for loops and sorting
# we'll spend a lot more time on these later

