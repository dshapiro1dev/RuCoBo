# Behold the Encrypt-o-mat! It will take your sensitive files and make it such that no one but those you trust will
# be able to see what you write.

# Variables for source & destination
source_path = "../../data/presidentspeeches/raw/1789-04-30-first-inaugural-address.txt"
source_file = source_path[source_path.rfind("/") + 1:]
destination_path = "../../projects/project2/files/not-a-secret.txt"
key_path = "../../projects/project2/files/not-a-decoder.txt"

# open the file and read it into a large string
with open(source_path, "r") as file_object:
    raw_text = file_object.read()

# convert the text to a list, then load each unique value to a library. Note that the split is based on " "
# this means that two words separated from a carriage return are considered one "word" to be encrypted
text_list = raw_text.split(" ")
i = 1
word_map = {' ': '0'}
for word in sorted(text_list):
    if word not in word_map.values() and len(word) > 0:
        word_map[word] = str(i)
        i += 1

# replace a completely blank space with a single space. This is because the single space is lost when doing split
text_list = [' ' if x == '' else x for x in text_list]

# begin building the encoded text by replacing each word with its map key number
enc_text = ""
for word in text_list:
    enc_text += word_map[word]
    enc_text += " "

# create the encrypted file
with open(destination_path, 'w') as enc_file:
    enc_file.write(enc_text.rstrip())

# create the key for decrypting
with open(key_path, 'w') as enc_key:
    for key, value in word_map.items():
        enc_key.write(f"{value},{repr(key)}\n")

print(f"File successfully encrypted and available at {destination_path}")
print(f"Don't tell anyone that your key is available at {key_path}")


