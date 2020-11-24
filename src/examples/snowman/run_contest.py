import word_selector
import snowman
import snowman_solver

from datetime import datetime
now = datetime.now()

# parameters
num_games = 150000   # number of rounds to run per contest
num_allowed = 6  # number of missed guesses per word for a victory [classic hangman: 6 ]

# create a guesser object
# guesser = snowman_solver.Solver()
guesser = snowman_solver.BozSolver()

# create a tracker of contest success
wins   = 0
losses = 0
tracker = []

# create output file of statistics
fhand = open("stats-yael.txt","w")
print("word,length,right,wrong,guesses,outcome",file=fhand)

# run contest over selected number of words
for r in range(0,num_games):
    # pick a word - create a snowman game for it
    word = word_selector.get_word("natan")
    game = snowman.Game(word, num_allowed)

    # initialize guesser
    guesser.initialize(len(word))

    # run game
    while game.word_revealed is False:
        guess = guesser.make_guess(game.revealed_letters)
        result = game.guess(guess)

    # collect stats
    info = {}
    info['word'] = word
    info['length'] = len(word)
    info['num_hit'] = game.right_guesses
    info['num_miss'] = game.wrong_guesses
    info['guess_order'] = game.guesses
    info['win'] = game.wrong_guesses<=num_allowed
    tracker.append(info)
    glist = ""
    glist = glist.join(game.guesses)
    stat = ""
    if(info['win']):
        stat = "WIN "
        wins += 1
    else:
        stat = "LOSS"
        losses += 1
    success = "{:.2f}".format(100 * wins / (wins + losses))
    print(datetime.now(),f" WinRate: {success}  {stat} {r} word: {word} len: {len(word)} misses: {game.wrong_guesses}  list: ",glist)
    print(f"{word},{len(word)},{game.right_guesses},{game.wrong_guesses},{glist},{stat}",file=fhand,flush=True)


# compute overall statistics for contest
print(3)