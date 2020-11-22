import word_selector
import snowman
import snowman_solver

print("Starting a game")



round = 0
games = 100
wins = 0
guesses_needed = []

while round < games:
    round += 1
    tries = 0
    game_result = "Loss"
    challenge_word = word_selector.get_word()
    my_solver = snowman_solver.Solver("frequency by length", len(challenge_word))
    my_game = snowman.Game(challenge_word, 12)
    while my_game.word_revealed is False:
        tries += 1
        guess = my_solver.make_guess()
        round_result = my_game.guess(guess)
        # print(f"Word so far: {my_game.revealed_word()} Guessing the letter {guess}: {result}")
    if tries <= my_game.tries:
        wins += 1
        game_result = "Win"
    guesses_needed.append(tries)
    print(f"Round {round}: Word is {challenge_word}, result: {game_result}")



print(f"Played {games} rounds and won {wins}")
print(f"Win rate: {wins/games}")
print(f"Average guesses to solve: {sum(guesses_needed)/len(guesses_needed)}")
print(f"Least guesses to solve: {min(guesses_needed)}")
print(f"Most guesses to solve: {max(guesses_needed)}")
