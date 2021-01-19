# This is the main RPS module
import brainRPSAI
import danRPSAI

# definitions
values = {'r': 0, 'p': 1, 's': 2}  # rock:0  paper:0  scissors:0

# --------------------------------------------
# winner function: given 2 players  p1, and p2
# returns: 0 = draw, 1 = p1 wins  , 2 = p2 wins
# p1 and p2 must be in ['r','p','s']  - else function returns -1 if invalid entry
def getWinner(p1, p2):
    if p1 in values and p2 in values:
        return (values[p1] - values[p2]) % 3
    return -1

def getWinnerName(v):
    if v==0:
        return "draw"
    if v==1:
        return "p1"
    if v==2:
        return "p2"
    return ""

# --------------------------------------------
# fixEntry: given any variant of entry, converts into proper ['r','p','s']
# returns ['r','p','s'] - else function returns -1 if invalid entry
def fixEntry(entry):
    proper = list(entry.lower())[0]
    if proper in values:
        return proper
    return -1


def entryWord(entry):
    if entry=='p':
        return "paper"
    if entry=='r':
        return "rock"
    if entry=='s':
        return "scissors"
    return ""


def trackStats( w, t):
    winnerName = getWinnerName(w)
    t[ winnerName ]+=1

    p1pct   = round(100 * t["p1"]   / ( t["p1"] + t["p2"] + t["draw"] ),2)
    p2pct   = round(100 * t["p2"]   / ( t["p1"] + t["p2"] + t["draw"] ),2)
    drawpct = round(100 * t["draw"] / ( t["p1"] + t["p2"] + t["draw"] ),2)

    print(f"P1win:{p1pct} P2win:{p2pct} Draw:{drawpct}")
    return 1

# ==========================================================
# main loop


if __name__ == "__main__":
    # configuration
    n = 10000  # number of games to play

    # get user names  [ here user1: human, user2: ai, but can also use AI for both ]
    user1 = "unknown"
    while user1 not in list("yatndb"):
        user1 = input("Who are you [ y=yael, a=adam, t=trevor, n=natan, d=daniel b=brian [yatndb]")
    user2 = "danAI"

    # create AIs  [ send info to AI: N , competitor name ]
    # ai = danRPSAI.RPSAI(n,user1)  # replace this w/ <name>RPSAI,  here user1 is the competitor's name
    ai = brainRPSAI.RPSAI(n, user1)  # replace this w/ <name>RPSAI,  here user1 is the competitor's name

    # statistics
    tally = {}
    tally["p1"] = 0
    tally["p2"] = 0
    tally["draw"]  = 0

    # run N games
    for i in range(n):
        print(f"\nRunning game {i}")

        # make a play
        e1 = fixEntry(input("Play: [r,p,s] "))  # get entry from human player
  #      e1 = ai.choosePlay()  # temp - remove - this should be the HUMAN entry
        e2 = ai.choosePlay()
        winner = getWinner(e1,e2)  # 0:draw  1:player1  2:player2

        # send the outcome to the AI module
        ai.outcome( e1, e2, winner)  # e1: human entry   e2: AI entry  winner: 0,1,2 -> [draw, p1 win , p2 win ]

        # determine winner
        print(f"Human: {entryWord(e1)}   AI: {entryWord(e2)}  Winner: {winner}")

        # track statistics
        trackStats( winner , tally)



    print()