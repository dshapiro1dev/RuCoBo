# determine file to work with
fname = "../../../data/presidentspeeches/raw/1789-04-30-first-inaugural-address.txt"

# file handles for my files
enc_file = open("../../../tmp/enc_p2.txt", "w")  # my encrypted file
dec_file = open("../../../tmp/dec_p2.txt", "w")  # my decrypted file

# read original file into a single string
fhandle = open(fname, "r")
orig = fhandle.read()

# ----------------------
# encrypt
for c in range(0, len(orig)):
    # read in the original
    cc = orig[c]  # the original character
    nn = ord(cc)  # the ascii number for the original character

    # encrypt the character
    new_nn = nn + 23
    if new_nn > 255:
        new_nn = new_nn - 255
    new_cc = chr(new_nn)

    # output the encrypted character
    print(new_cc, end='', file=enc_file)

enc_file.close()

# ----------------------
# decrypt
enc_file = open("../../../tmp/enc_p2.txt", "r")  # my encrypted file
enc_data = enc_file.read()

for c in range(0, len(enc_data)):
    # read in the encrypted character
    cc = enc_data[c]  # the encrypted character
    nn = ord(cc)  # the ascii number for the encrypted character

    # decrypt the character
    new_nn = nn - 23
    if new_nn < 0:
        new_nn = new_nn + 255
    new_cc = chr(new_nn)
    print(new_cc, end='', file=dec_file)

dec_file.close()
enc_file.close()
