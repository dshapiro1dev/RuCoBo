# This is a riff on the old game "hangman", but with a melting snowman instead
#
#     _|@|_
#      (")
#  '--( : )--'
#    (  :  )

# Set some important variables
allowed_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u", "v", "w", "x", "y", "z"]
guessed_letters = []
word = "serendipity"
word_array = list(word)
mistake_count = 0
allowed_mistakes = 5
revealed_letters = []
word_revealed = False
for letter in word_array:
    revealed_letters.append("_")

# A beautiful melting snowman
ascii_art = []
ascii_art.append('     _|@|_\n      (")\n  >--( : )--<\n    (  :  )')
ascii_art.append('          \n      (")\n  >--( : )--<\n    (  :  )')
ascii_art.append('          \n      (")\n     ( : )--<\n    (  :  )')
ascii_art.append('          \n      (")\n     ( : )   \n    (  :  )')
ascii_art.append('          \n         \n     ( : )   \n    (  :  )')
ascii_art.append('          \n         \n             \n    (  :  )')
ascii_art.append('          \n         \n             \n           ')


def print_revealed_word(revealed_so_far):
    print("Your mystery word: ", end="")
    for letter in revealed_so_far:
        print(letter, end="")
    print("\n")


# Start the main thread for the game
print("Guess the word before the snowman melts!")

while mistake_count <= allowed_mistakes and word_revealed is False:
    print(ascii_art[mistake_count])
    print_revealed_word(revealed_letters)
    player_response = input("Guess a letter\n")
    print(f"You entered {player_response}")
    if len(player_response) == 1 and player_response in allowed_letters:
        if player_response in guessed_letters:
            print(f"I'm sorry, but you already guessed the letter {player_response}.")
            print(f"In case you forgot, you've guessed the following letters: {sorted(guessed_letters)}\n")
        else:
            guessed_letters.append(player_response)
            if player_response in word_array:
                print(f"Congratulations! The letter {player_response} is in the secret word.")
                x = 0
                for letter in word_array:
                    if player_response == word_array[x]:
                        revealed_letters[x] = player_response
                    x += 1
            else:
                mistake_count += 1
                print(f"I'm sorry, but the letter {player_response} is not in the secret word. That's {mistake_count}"
                      f" mistakes.")
                print(f"You need to solve the problem before {allowed_mistakes + 1} mistakes.")
        if "_" not in revealed_letters:
            word_revealed = True
    else:
        print("Sorry, please pick just one letter from the English alphabet")

if word_revealed:
    print("Congratulations, you win!")
elif mistake_count > allowed_mistakes:
    print(f"You let the snowman melt! All you had to do was figure out the word {word}...")
