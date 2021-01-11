import random
import time
import math

# statistics to track
#   1. opponent sequences of length 1 through depth -> frequency since inception
#   2. opponent sequences of length 1 through depth -> decaying frequency by EMA
#   3. 2d sequences of length 1 through depth -> frequency since inception
#   4. 2d sequences of length 1 through depth -> decaying frequency by EMA
#   5. win,draw,loss rate since inception
#   6. win,draw,loss rate decaying by EMA

# 1:  paper > scissors > rock

class RPSAI:

    def __init__(self, n, competitor):
        """Initialize the RPS AI """
        self.counter = 0  # counter of this game
        self.n = n
        self.depth = 3
        self.time = time.time()
        self.competitor = competitor  # competitor name
        random.seed(time.time())

        # open file for tracking data
        self.data_fhand = open("data/" + self.competitor + ".data","a")

        # series
        self.series = []   # series of events [ one entry:  e1, e2, w ]

        # trailing sequences
        self.oppseq = []   # set of opponent sequences of diff lengths, up to last move

        # counters
        self.d1_freq_all = []
        self.d1_freq_ema = []
        self.d2_freq_all = []
        self.d2_freq_ema = []
        self.wdl_all = {}
        self.wdl_ema = {}

        # decays
        self.gamma = []

        # initialize decays
        for i in range(0,self.depth+1):
            hl = 3 + i * 3  # length:1  hl:6,  length:2 hl:9  etc
            gm = math.exp( math.log(0.5)/hl )
            self.gamma.append(gm)

        # initialize counters
        for i in range(0,self.depth+1):
            self.d1_freq_all.append({})
            self.d1_freq_ema.append({})
            self.d2_freq_all.append({})
            self.d2_freq_ema.append({})

    # -------------------------------
    # choosePlay: select a play to make
    def choosePlay(self):
        values = ['r','p','s']  # possible values rock, paper, scissor
        winplay = { 'r':'p', 'p':'s', 's':'r'}  # what to play key: opponent prediction  value: my winning move response
        r = random.uniform(0,1)  # random number between 0 and 1

        # initial distribution
        dist = { 'r':[0,1/3], 'p':[1/3,2/3], 's':[2/3,1]}

        # estimate likelihood of play from opponent

        # skew probability towards most winning'est move - adjust dist

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
        print(f"{self.counter},{self.competitor},danAI,{e1},{e2},{winner}",file=self.data_fhand,flush=True)

        # compute realized trailing sequences of length 1 thru length N
        s = ""  # s: single, ie: just opponent
        b = ""  # b: both,   ie: both players plays together
        d1_seqs = [""]  # sequences of increasing length of opponent
        d2_seqs = [""]  # sequences of increasing length of  opponent/our tuples
        for i in range(1,self.depth+1):
            if len(self.series)>=i:
                s = self.series[-i][0] + s
                b = self.series[-i][0] + self.series[-i][1] + ":" + b
                d1_seqs.append(s)
                d2_seqs.append(b)
        self.d1seq = d1_seqs  # store the most recent set of sequences of opponent only
        self.d2seq = d2_seqs  # store the most recent set of sequences [pr:rs -> opp=p,mine=r, then opp=r,mine=s ]

        # -------------------
        # update statistics
        # opponent-only sequence
        for i in range(1,len(self.d1seq)):
            seq = self.d1seq[i]  # most recent sequence of this length

            # cumulative statistics: opponent sequences
            if seq in self.d1_freq_all[i]:
                self.d1_freq_all[i][seq] +=1
            else:
                self.d1_freq_all[i][seq] =1

            # ema statistics: opponent sequences
            for s in self.d1_freq_ema[i].keys():   # decay all entries
                self.d1_freq_ema[i][s] *= self.gamma[i]
            if seq in self.d1_freq_ema[i]:         # add most recent sequence
                self.d1_freq_ema[i][seq] += (1 - self.gamma[i])
            else:
                self.d1_freq_ema[i][seq] = (1 - self.gamma[i])

        # combined sequence
        for i in range(1, len(self.d2seq)):
            seq = self.d2seq[i]

            # cumulative statistics: opponent sequences
            if seq in self.d2_freq_all[i]:
                self.d2_freq_all[i][seq] += 1
            else:
                self.d2_freq_all[i][seq] = 1

            # ema statistics: opponent sequences
            for s in self.d2_freq_ema[i].keys():  # decay all entries
                self.d2_freq_ema[i][s] *= self.gamma[i]
            if seq in self.d2_freq_ema[i]:  # add most recent sequence
                self.d2_freq_ema[i][seq] += (1 - self.gamma[i])
            else:
                self.d2_freq_ema[i][seq] = (1 - self.gamma[i])

        return
