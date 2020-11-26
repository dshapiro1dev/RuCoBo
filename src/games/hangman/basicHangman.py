# this is a basic hangman game

# choose a word
word = "inconceivable"

# settings
guesses_allowed = 5

# put word into a list - with 1 letter per entry
letters = list(word)

alphabet = list("abcdefghijklmnopqrstuvwxyz")

# now run the hangman loop
hangman_wins = 0  # track: hangman has won
guesser_wins = 0  # track: guesser has won
guesser_list = [] # list of letters already tried by guesser
guesser_misses = 0 # count number of misses

while(not hangman_wins and not guesser_wins):
    print("\n===============================================")
    # print status so far
    print("WORD SO FAR: ", end='')
    missing_letters = 0
    for letter in letters:
        if letter in guesser_list:
            print(letter, end='')
        else:
            print('_', end='')
            missing_letters = 1  # there are still missing letters - user has not won yet
    print('\n')

    print(f"You have missed {guesser_misses} / {guesses_allowed} guesses: so far your guess list: {guesser_list}")
    guess = input("Your guess please: ").lower()

    # check if this is a valid guess [ single character in the alphabet ]
    valid = 1
    valid = valid and len(guess)==1
    valid = valid and guess in alphabet
    if not valid:
        print(f"Your guess: {guess} is not valid [ needs to be single letter in alphabet ] - so I'm ignoring it")
        continue

    # check if already tried this letter
    if(guess in guesser_list):
        print(f"You already tried: {guess} - so I'm ignoring it. Lucky you\n")
        continue
    else:
        guesser_list.append(guess)

    # check if guess is within the word
    if guess in letters:
        print(f"YES  - {guess} is in my word")
    else:
        print(f"NO - {guess} is not in my word")
        guesser_misses += 1



    # check if human has won
    if not missing_letters:
        print("YOU WIN: you guessed all the letters")
        exit(1)

    # check if human has lost
    if guesser_misses >= guesses_allowed:
        print(f"GAME OVER - you missed {guesser_misses} choices")
        exit(1)