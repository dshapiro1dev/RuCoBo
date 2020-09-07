# Files: documents containing typically text or data
# files live in directories on our disk, and remain after we reboot computer

# Python can read in files to use them or can write out files to disk

# First lets see how to open and read a file
# We open a text file called "if", with the 'r' flag, which means read only
#  'fhandle' is the "file handle" - it points to the file
fhandle = open("../../../data/poems/if","r")

# lets read the file - one line at a time
firstline = fhandle.readline()
print("The first line: \n" + firstline.strip())

# now lets read the whole rest of the  file
# the 'for' loops over every line in the file handle - each time grabbing it into the string ll
# notice that the ll string has a newline ("\n") - which we strip
# otherwise it would print 2 new lines between each line - since print automatically adds a newline too
for ll in fhandle:
    print(ll.strip())

# and finally we need to close the file handle down when we're done. This tells python we're finished w/ the file
fhandle.close()

# now what if we want to improve on an already fine piece of literature
# lets replace:  'man' with  'yak'   everytime we see it
#          and:  'men' with   'yaks'  everytime we see it
print("---------------\n And now to improve on Kipling's masterpiece: \n\n")
fhandle = open("../../../data/poems/if","r")
for ll in fhandle:
    ll = ll.replace("man","yak")
    ll = ll.replace("men","yaks")
    # remember - strings are immutable, so we have to create a new string and overwrite the old one
    # here:  ll is effectively replaced with a new (and better) version
    print(ll.strip())

# we are now sad that we will lose the improvements we made, but we dont want to mangle the original
# lets record our improved Kipling poem for generations to come
# we will save the new and improved version to a new file ie: write to a file
# be careful!  do not overwrite the original
orig_handle = open("../../../data/poems/if","r")  # original file for "r" reading only
new_handle  = open("../../../data/poems/if_yaks","w")  # new file - notice "w" for writing

for ll in orig_handle:
    ll = ll.replace("man","yak")
    ll = ll.replace("men","yaks")
    ll = ll.replace("Man","Yak") # python does exactly what you say: above we only replaced lower case men w/ yaks

    print(ll.strip(),file=new_handle)

orig_handle.close()
new_handle.close()

# now lets say we forgot to add something to the file
# we dont want to redo the whole thing,  just add some stuff to the end
# for this we use the 'append'  setting in the open command
new_handle  = open("../../../data/poems/if_yaks","a")  # file already exists - notice "a" for append
print("\n-> This improvement on Kipling proudly brought to you by: RuCoBo Yaks",file=new_handle)
new_handle.close() # and as always - close the file after we're done


# files live in a directory
# sometimes we want to see all the files that exist in a directory
import os  # this is the first time we 'import' - we bring a library in - will cover this later
flist = os.listdir("../../../data/presidentspeeches/raw/") # flist gets all files in directory
for f in flist[1:5]:  # lets print the first 5 files in this directory
    print(f)

