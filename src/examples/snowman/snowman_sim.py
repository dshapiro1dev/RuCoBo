import word_selector
import snowman
import snowman_solver

print("Starting a game")

challenge_word = word_selector.get_word()
my_solver = snowman_solver.Solver(len(challenge_word))
my_game = snowman.Game(challenge_word, 5)
tries = 0

while my_game.word_revealed is False:
    tries += 1
    guess = my_solver.make_guess()
    result = my_game.guess(guess)
    print(f"Word so far: {my_game.revealed_word()} Guessing the letter {guess}: {result}")

print(f"Found the work {my_game.word} in {tries} tries")
