# Strings
# Here we will learn about the String in Python

# strings hold a list of characters, numeric/alphabet/symbol etc
# it is a basic Python structure and has a lot of functionality built around it

# strings can be defined using
# '   a single quote
# "   a double quote
# """ a triple double quote
# they allow the string to contain different special characters
# if you want a string to be able to hold  " (double quotes) - then you can not surround it with double quotes
# Python would get confused.
# Therefore  single quotes allow for strings containing double quotes
# vice-versa for double quotes and single quotes
#  triple-double quotes are special.  See the examples below
single_quote = 'Single quote allow you to embed "double" quotes in your string.'
double_quote = "Double quote allow you to embed 'single' quotes in your string."
triple_quote = """Triple quotes allows to embed "double quotes" as well as 'single quotes' in your string. 
And can also span across multiple lines."""

# here we print the different strings defined above
print(single_quote)
print(double_quote)
print(triple_quote)

# strings are 'immutable' - you can not change part of the string once its defined
triple_quote = '''This is triple quoted string using "single" quotes.'''
# lets look at referencing parts of the string - we can access different locations within the string
# notice that in coding,  0 is the first element (not 1)
print(triple_quote[0])  # prints T  1st character
print(triple_quote[1])  # prints h  2nd character
print(triple_quote[10]) # prints i  11th character
# print(triple_quote[10000])  # the string is not this long - this will create an IndexError

# but if you try to change a character within the string - you can not.
# strings once defined are immutable
# if you uncomment this - you will get: "str object does not support item assignment"
# triple_quote[3] = "x"

# however if you create a new string  - you can do all sorts of changes to the original
# this creates a new copy of the string - but inserts <invasion> at location 6
triple_quote_new = triple_quote[0:5] + " <invasion> " + triple_quote[6:]
print(triple_quote_new)

# strings allow us to see how long they are.  Here notice its 6 long,
# even though the last character "f" is in index 5
teststr = 'abcdef'
print(" The length of this string is:")
print( len(teststr) )
print(" The last character is:")
print( teststr[5])

# you can also print parts of a string like this - here characters 2,3,4
# notice the interesting indexing
#  1  - actually means the 2nd character (since 0 is the first)
#  :  - means until
#  4  - means the 5th character, but not including it
# -> so this takes the 2, 3, and 4th character  'bcd'
print( teststr[1:4] )

# spaces are characters just like any other
spacey = 'abc   def'
print(spacey[2:7]) # will print c___d  - where _  are spaces, since there are 3 spaces in the string

# Python is very flexible and allows indexing a string from the back
# this indexing uses negative numbers like this
print(teststr[-1]) # this will print the very last character in the string 'f'
print(teststr[-3:-1]) #  'de'  - notice the range end is non-inclusive (only last 2 characters)

# there are other ways to access strings like this
print( teststr[3:] ) # def   - start at location 4 (ie: index 3)  - go to end
print( teststr[:-2]) # abcd  - at at begining (ie: index 0) - go to 2 from end (not including the 2nd last)

# you can also 'stride' through a string - taking every n'th character
number_string = "1020304050"
print(number_string[0:-1:2])  # start at first char, go to last character - but take every 2nd -> prints: 12345

print(number_string[0::2]) # this is the same - we just dont specify the last character - its implied
print(number_string[0:10:2]) # this is the same too - the string is 10 characters long
# even this is the same - notice how we replaced 10 , w/ the length of the string from python
print(number_string[0:len(number_string):2])

# a cool trick is you can reverse a string - by using negative strides
print(number_string[::-1]) # starts at beginning, ends at end, but goes _backward_ by 1 step -> 0504030201
print(number_string[::-2]) # same, but goes backwards by 2 steps -> 00000

# ----------------------------------------------------------------------
# now for some typical operations one can do with strings

# first putting strings together  [ fancy word:  concatenation ]
s1 = "yak"
s2 = "barbeque"
s3 = s1 + " " + s2  # can we combine these into a single string - yes:
print(s3) # yak barbeque  ( if we do not add the " ", we would get:  yakbarbeque - not readable, but still delicious)

# you can not concatenate things that are different: like a string and a number
nm = 12
strg = "I ate yak number "
# print(strg + nm) # this will throw error:  "can only concatenate str to str"

# but if we convert the number to a string using  str() - concatenation will work
# here  12  ,the number, gets changed to "12" the string
print(strg + str(nm)) # I ate yak number 12

# we can 'multiply' strings - effectively replicating them
print( s1*2 + " give it back") # here multiplies yak by 2, giving:  yakyak give it back
print( s1*30 ) # severe yak infestation

# we can check if one string exists within another (membership)
# i'm going to sneak in an  'if' conditioner here - to be discussed later
s1 = 'yak'
s2 = 'kayak'
s3 = 'my kitchen'
if(s1 in s2):
    print("Yes there is a " + s1 + " in the " + s2) # yak is part of kayak
if(s1 in s3):
    print("Yes there is a " + s1 + " in " + s3)
else:
    print("Unfortunately there is no " + s1 + " in " + s3)

# other things you can do
print( s1.capitalize() ) # Yak  - first character capitalized
print( s1.upper()) # YAK

print( s1.islower() )  # True  "yak" is all lower case
print( s1.isupper() )  # False  "yak" is not capitalized
print( s1.upper().isupper() )  # True  -> 2 operations in one: first convert to uppercase, then check if uppercase

# find a string within a string
ridiculous = "once upon a time there was a little fairy named buttermug <waldo> who loved to grill yak steak"
print( ridiculous.find('waldo') ) # 59 -> at index 59 of this string, 'waldo' is hiding
print( ridiculous.find('emu'))   # -1  -> no emus in here though

# you can also count how many times a string occurs within another
stranger = "fairies waldo love waldo to eat waldo with cheese waldo"
print( stranger.count('waldo') ) # 4 -> there are 4 waldos in there

# remove annoying empty spaces at start of a line
really = "           why must you start the line with so much whitespace"
print( really.lstrip()) # 'why must you start...'

# lets replace certain parts of a string with another
messedup = 'i lovx xmus morx than yaks but dont txll anyonx'
print( messedup.replace('x','e'))  # find every x  and replace with an e  - fixing the string

# lets split a sentence into words
# here we will split by the whitespace
sentence = "yak tartar is served only at the finest and most unusual establishments. Avoid them"
words = sentence.split(' ')
print(words)  # now we have a list of words, instead of a string with a sentence
print(words[0:2])  # take only the first two words

# there are a riduculous number of inbuilt functions you can do on strings
# to see them and play with them type  sx="test,  then sx.  in PyCharm - and it will show you a long list of options
sx = "test"
#  type this below in PyCharm and see the list:   sx.