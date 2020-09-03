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


print(3)