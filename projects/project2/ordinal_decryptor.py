# source and destination for the encrypted file and where the decrypted file should be written
source_path = "../../projects/project2/files/secret.encrypt"
destination_path = "../../projects/project2/files/secret.decrypt"
print(f"Decrypting your file at {source_path}")

# Open the encrypted file
with open(source_path, "r") as file_object:
    encFile = file_object.read()

# convert space delineated string into a list
li = list(encFile.split(" "))

# create a new string consisting of the ordinal numbers in the list converted back to characters
decFile = ""
for item in li:
    decFile += chr(int(item))

with open(destination_path, "w") as file_object:
    file_object.write(decFile)

print(f"Your file is decrypted and available at {destination_path}")