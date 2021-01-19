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
        self.series = []   # series of events [ one entry:  e1, e2, w ]           self.d2_freq_ema.append({})

    # -------------------------------
    # choosePlay: select a play to make
    def choosePlay(self):
        values = ['r','p','s']  # possible values rock, paper, scissor
        winplay = { 'r':'p', 'p':'s', 's':'r'}  # what to play key: opponent prediction  value: my winning move response
        r = random.uniform(0,1)  # random number between 0 and 1

        # initial distribution

        if self.counter == 0:  # Our first round should likely go to paper, because people pick rocks. They are fools!
            dist = {'r': [0, 2 / 6], 'p': [2 / 6, 5 / 6], 's': [5 / 6, 1]}
        elif self.counter == 1:  # Favor scissors
            dist = {'r': [0, 1 / 6], 'p': [1 / 6, 3 / 6], 's': [3 / 6, 1]}
        else:
            dist = {'r': [0, 1 / 3], 'p': [1 / 3, 2 / 3], 's': [2 / 3, 1]}

        # pick a random entry from distribution
        play = "none"
        for tp in dist.keys():
            if r>=dist[tp][0] and r<=dist[tp][1]:
                play = tp


        return play

    # --------------------------------
    # record outcome:
    #   e1: other player  [r,p,s]
    #   e2: our move      [r,p,s]
    #   winner:  [0,1,2] = draw, competitor win, we win
    def outcome(self, e1, e2, winner):
        # record time series
        oc = [e1,e2,winner]
        self.series.append(oc)
        self.counter+=1
        return
