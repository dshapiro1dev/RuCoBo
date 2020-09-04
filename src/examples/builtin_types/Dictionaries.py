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

