#   The # is a comment - it is put at a front of a line , to inform the reader only
#   Python does not read any lines starting with a # - it jumps right over them. They are called comments

#   This script should be run in the debugger step by step - to see how each line works

# PrintCommand
# this script shows how the print command works
# each example will be separated by a line

# print a basic string
print("This is a basic print - about emus")
print("-------------------------------")

# you need parentheses - the print statement below will not work - uncomment and try it
# notice that if you leave this line in - Python will tell you
# "SyntaxError: Missing parentheses in call to 'print'. Did you mean print("This won't work , you need parentheses")?
# print "This won't work , you need parentheses"

# if you want to see what type 'print' is  - its a predefined builtin function
print("The type of 'print' is: ")
print(type(print))
print("-------------------------------")

# if you want to add a newline between prints - ie: on 2 different lines
print("Hello, emu ");print("Hello, yak")
print("-------------------------------")

# an empty print statement creates a newline only
print("first line -  yak-attack: the emus are coming - then there will be a space ")
print()
print("there is a gap above")
print("-------------------------------")

# you can create a list of items - and a separator - and print knows to print them separated by it
# lets print a list of things separated by a comma
print('apple','orange','fruit','dirty-sock','yak-teriyaki, sep=',')
print("-------------------------------")

# you can also use the special character \n which means explicitly new line
# lets print a list of stuff separated by new lines
print('emu','yak','poodle','grilled-poodle',sep='\n')
print("-------------------------------")

# now lets see how we can print out variables
# variables store values in different formats for us
# lets use a data type 'list' - it stores a list of stuff
# here I have put 3 numbers into the list - and called the list 'example_list'
example_list = [1,99,-3]
# then here we print out the list - separated by spaces
print(example_list,sep=" ")
print("-------------------------------")


# print is a more complex function - than it lets on
# when you type print in PyCharm - it will show you the structure of the print function
# print(values, sep, end, file, flush)
# this means that print can take a single parameter  eg print("1")
# but you can also give it more instructions (parameters)
# ->  sep:  tells print if you want to separate the entries (we used this above)
# ->  end:  tells print how to finish the string
#           the default it will use is appending a "\n" - a new line
#           but we can say - actually end the print with something else
# so here - we are going to print a string - and instead of a newline - end it with :, then print another
# this will output:    string1:string2     - separated by a colon
print("yak number1",end=":")
print("yak number2")
print("-------------------------------")

# if we use a list, and an end specification - it will print the list
# and then put a "end" character at the end of list
# output here will be:
# [1, 2, 3, 4]:[1, 2, 3, 4]
# notice that print shows that "junk" is a list - by printing it with the square brackets
junk  = [1,2,3,4]
print(junk,end=":")
print(junk)
print("-------------------------------")

# now lets see what the other parameters do - lets look at the 'file' parameter
# this allows us to write not to the screen, but to a file on our disk
# this command creates a new file called  junkyfile.txt - and gives it a name within Python
# the name of the file handle is 'danoutputfile' - we will use it shortly
# the "w"  tells Python to create the file for writing - if a file like this already exists
# too bad - it will be deleted and overwritten by this command
danoutputfile = open("junkyfile.txt","w")
# after running this command - I'm going to look for the file - and here it is
# Daniels-Air-2:PycharmProjects danielshapiro$ find * | grep junkyfile
# RuCoBo/src/examples/basic/junkyfile.txt

# next - lets write some stuff to this file
print("This is my junky file",file=danoutputfile)
print("A really junky file,  yeah yeah yeah",file=danoutputfile)


# and finally we need to close the file - so that Python knows to write everything pending to it and complete
danoutputfile.close()

# lets see my file
# Daniels-Air-2:basic danielshapiro$ cat junkyfile.txt
# This is my junky file
# A really junky file,  yeah yeah yeah
print("-------------------------------")

# flush parameter - is to tell Python to keep flushing data to file, do not wait
# sometimes when you write a tremendous amount, it keeps a buffer of stuff and only
# flushes occasionally.  If you want to force it to flush after the print statement use Flush
print("flush this sucker now",flush=True)
print("-------------------------------")

# now we will show how to accept input from a user
# here we will prompt the user in an overly polite and possibly irreverent manner
# then print out what they have provided.
testit = input("dear esteemed and honorable user, type your very important input in here: ")
print("Dear user - you typed: ")
print(testit)
# so lets try it out: I ran this and typed  'this is my junky input'  - and the result is below:
# dear esteemed and honorable user, type your very important input in here: this is my junky input
# Dear user - you typed:
# this is my junky input
