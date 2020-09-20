# if we want to programmatically get the list of files in a directory
# we can use glob:  and send it a <format> of how the file looks
# it will find all files of that form

# get list of files - that have the shape *.txt  ie:  anything.txt
#  here '*' is a regular expression - it means "anything"
import glob
flist = (glob.glob("../../../../RuCoBo/data/presidentspeeches/raw/*.txt"))

# print each file in the directory
for file in flist:
    print(file)

# we could also get a list of files only from the 1870's like this
flist = (glob.glob("../../../../RuCoBo/data/presidentspeeches/raw/187*.txt"))

print("-----------------------\n\n\n 1870s \n")
for file in flist:
    print(file)

