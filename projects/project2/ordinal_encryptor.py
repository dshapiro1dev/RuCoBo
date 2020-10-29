# This script will replace each character with its ordinal number

# This is the path of the file that I would like to read
source_path = "../../data/presidentspeeches/raw/1789-04-30-first-inaugural-address.txt"
source_file = source_path[source_path.rfind("/") + 1:]
destination_path = "../../projects/project2/files/secret.encrypt"
print(f"Preparing to encrypt filename: {source_file}")

# open the file and read it into a large string
with open(source_path, "r") as file_object:
    rawSpeech = file_object.read()

# create a new string consisting of ordinal numbers space delineated
encSpeech = ""
for character in rawSpeech:
    encSpeech += str(ord(character))
    encSpeech += " "

# strip the last space
encSpeech = encSpeech.rstrip()

with open(destination_path, 'w') as file_object:
    file_object.write(encSpeech)

print(f"File successfully encrypted and available at {destination_path}")


