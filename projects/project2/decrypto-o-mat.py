# Gaze upon my works and despair! You thought that encrypted file was lost to the ages.
# Despair no more, for the decrypt-o-mat will take the encrypted file with its complimentary key and return your file

# Variables for source & destination
source_path = "../../projects/project2/files/not-a-secret.txt"
source_file = source_path[source_path.rfind("/") + 1:]
destination_path = "../../projects/project2/files/a-secret-revealed.txt"
key_path = "../../projects/project2/files/not-a-decoder.txt"

# open the key file and load it into a dictionary with the encrypted word as the key
key_map = {}
with open(key_path, "r") as key_file:
    for line in key_file:
        key = line[:line.find(",")]
        value = line[line.find(",")+1:].rstrip().strip("'")
        key_map[key] = value

# open the encrypted file and load each number into a list
with open(source_path, "r") as encrypted_file:
    enc_msg = encrypted_file.read().split(" ")

# create a new file by re-mapping the encrypted numbers back to their keyed values
dec_msg = ""
for item in enc_msg:
    dec_msg += key_map[item]
    dec_msg += " "

with open(destination_path, "w") as decrypted_file:
    decrypted_file.write(dec_msg.replace('\\n', '\n'))

print(f"You're file is decrypted and available at {destination_path}, but don't tell anyone!")
