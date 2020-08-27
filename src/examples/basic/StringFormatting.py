# we will look at how we can format strings to look like we want them too

# The % operator is an 'interpolation operator'
# %d stands for an integer (ie: a number)
# %s stands for a string
# notice there are two % in the string - and then we provide the values in the parenthese
print('I bought %d used %s on amazon - no refunds of course' % (27, 'yaks'))

# this is useful if we want to print out the values contained in a variable
# notice:  %d is an integer (ie: 1, 2, 3, 4  etc  whole numbers)
#          %f is a float - it allows a number like 2033.285714
# here I print out N and M - in a single printout
# I could also put them into a string
n = 37
m = 37 * 55 - 12 / 7
print('after mangling %d  I get %f' % (n,m))
final = 'after mangling %d  I get %f' % (n,m) # put the results into a string , instead of writing to screen
print(final) # and this does the same thing. first puts the results into a string, then prints the string

# the 'formatter' class is another way to operate - but we'll cover more complex string formatting later
print("I sold {0} delicious {1} on amazon. now the feds are after me".format(198,'yaks'))

