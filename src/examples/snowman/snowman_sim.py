import word_selector
import snowman
import snowman_solver

print("Starting a game")



round = 0
games = 50000
wins = 0
guesses_needed = []

stats = {} # track statistics


while round < games:
    round += 1
    tries = 0
    game_result = "Loss"
    challenge_word = word_selector.get_word()
#    my_solver = snowman_solver.Solver("frequency by length", len(challenge_word))
    my_solver = snowman_solver.Solver("ds adaptive", len(challenge_word))  # 93 % success

    my_game = snowman.Game(challenge_word, 12)

    # keep statistics
    length = len(my_game.word) # length of the word
    if length in stats:
        stats[length]['num'] += 1
    else:
        stats[length] = {}
        stats[length]['num'] = 1
        stats[length]['win'] = 0

    while my_game.word_revealed is False:
        tries += 1
        guess = my_solver.make_guess(my_game.revealed_letters)
        round_result = my_game.guess(guess)
        # print(f"Word so far: {my_game.revealed_word()} Guessing the letter {guess}: {result}")
    if tries <= my_game.tries:
        wins += 1
        print(f"Win rate: {wins / round}")
        game_result = "Win"
        stats[length]['win'] += 1

    # output stats
#    print(stats)
    print('STATISTICS SO FAR')
    for ll in sorted(stats.keys()):
        pct = stats[ll]['win'] / stats[ll]['num'] * 100
        print(f" Round: {round}  Length: {ll}  Num: {stats[ll]['num']}  Wins: {stats[ll]['win']}   Pct: {pct}")

    guesses_needed.append(tries)
 #   print(f"Round {round}: Word is {challenge_word}, result: {game_result}")



print(f"Played {games} rounds and won {wins}")
print(f"Win rate: {wins/games}")
print(f"Average guesses to solve: {sum(guesses_needed)/len(guesses_needed)}")
print(f"Least guesses to solve: {min(guesses_needed)}")
print(f"Most guesses to solve: {max(guesses_needed)}")
