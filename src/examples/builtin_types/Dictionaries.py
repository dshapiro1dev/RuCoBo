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
