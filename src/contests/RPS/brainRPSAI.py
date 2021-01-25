import random
import time
import math


class RPSAI:

    def __init__(self, n, competitor):
        """Initialize the RPS AI """
        self.counter = 0  # counter of this game
        self.n = n
        self.time = time.time()
        self.competitor = competitor  # competitor name
        random.seed(time.time())

        # series
        self.series = []  # series of events [ one entry:  e1, e2, w ]           self.d2_freq_ema.append({})

    # ----------------------`---------
    # choosePlay: select a play to make
    def choosePlay(self):
        guesscounts = self.getGuessCounts()
        mostcommchoice = max(guesscounts, key=guesscounts.get)
        values = ['r', 'p', 's']  # possible values rock, paper, scissor
        winplay = {'r': 'p', 'p': 's',
                   's': 'r'}  # what to play key: opponent prediction  value: my winning move response
        r = random.uniform(0, 1)  # random number between 0 and 1

        bestguess = winplay[mostcommchoice]

        # pick a random entry from distribution
        play = bestguess

        return play

    def getGuessCounts(self):

        counts = {'r': 0, 'p': 0, 's': 0}
        for letter in self.series:
            theirguess = letter[0]
            if theirguess == "r":
                counts["r"] += 1
            elif theirguess == "p":
                counts["p"] += 1
            elif theirguess == "s":
                counts["s"] += 1
        print(counts)
        return counts

    # --------------------------------
    # record outcome:
    #   e1: other player  [r,p,s]
    #   e2: our move      [r,p,s]
    #   winner:  [0,1,2] = draw, competitor win, we win
    def outcome(self, e1, e2, winner):
        # record time series
        oc = [e1, e2, winner]
        self.series.append(oc)
        self.counter += 1
        return
