import snowman
import word_selector

# This is a riff on the old game "hangman", but with a melting snowman instead
#
#     _|@|_
#      (")
#  '--( : )--'
#    (  :  )


word = "puppy"
game = snowman.Game(word_selector.get_word(), 5)

# Start the main thread for the game
print("Guess the word before the snowman melts!")

while game.wrong_guesses <= game.tries and game.word_revealed is False:
    print(game.get_snowman())
    print(f"The mystery word so far: {game.revealed_word()}")
    player_response = input("Guess a letter\n")
    print(f"You entered {player_response}")
    if game.valid_guess(player_response):
        if game.repeat_letter(player_response):
            print(f"I'm sorry, but you already guessed the letter {player_response}.")
            print(f"You've guessed the following letters: {game.guesses}\n")
        else:
            if game.guess(player_response):
                print(f"Congratulations! The letter {player_response} is in the secret word.")
                print(f"You've guessed the following letters: {game.guesses}\n")
            else:
                print(f"I'm sorry, but the letter {player_response} is not in the secret word. "
                      f"That's {game.wrong_guesses} mistakes.")
                print(f"You need to solve the problem before {game.tries + 1} mistakes.")
    else:
        print("Sorry, please pick just one letter from the English alphabet")

if game.word_revealed:
    print(f'Congratulations, you guess the word "{game.word}." You win!')
elif game.wrong_guesses > game.tries:
    print(f'You let the snowman melt! All you had to do was figure out the word "{game.word}"...')
