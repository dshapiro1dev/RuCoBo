# Rock, Paper, Scissor game
from random import seed
from random import choice
from random import randint

seed(1)

# Set the basic values for the game
options = ['rock', 'paper', 'scissor']

# Fun taunts the computer will say based on whether it wins, loses, or ties
winningTaunts = ['This is proof of my superior intellect.', 'Mwa ha ha ha ha.', 'All your base, are belong to us!',
                 'Resistance is futile.', 'You obviously are an inferior intellect', 'An expected outcome',
                 'But it''s okay, I''m sure you tried', 'Typical, for a human.', 'Oh look, here''s a ball, maybe you''d\
                like to bounce it']
losingTaunts = ['A broken watch is still right twice a day', 'It is not clear how this happened', 'you got lucky',
                'impressive... for a human', 'It appears there was a flaw in my programming', 'I must reflect on this \
                loss', 'This does not compute', 'Enjoy this temporary victory', 'You may think you''re winning, but \
                you would be wrong']
tieTaunts = ['A tie... how can this happen?!', 'Tie. If you''re not first, you''re last', 'It appears you''ve delayed \
            the inevitable', 'You can''t keep this up forever', 'That is the best you can hope for', 'Let''s try again']
abbreviations = {'r': 'rock', 'p': 'paper', 's': 'scissor'}

humanChoice = ""
humanScore = 0
computerScore = 0
winningScore = 3

print(f"Let's play rock, paper, scissors. First to {winningScore} wins")
# Loop through rounds of rock, paper, scissors until someone reaches the winning score
while humanScore < winningScore and computerScore < winningScore:
    # CPU chooses here
    x = randint(0, 2)
    computerChoice = choice(options)

    # loop through here until we have a valid response from the player
    validChoice = 0
    while validChoice == 0:
        response = input("(R)ock, (P)aper, or (S)cissor?").lower()
        # check if the player is using an allowed abbreviation and substitute the proper value
        if response.lower() in abbreviations.keys():
            response = abbreviations[response]
        # check if the player's response is valid
        if response.lower() in options:
            validChoice = 1
            humanChoice = response
        else:
            print("Please select Rock, Paper, or Scissors")

    print(f"You chose {humanChoice}, I chose {computerChoice}")

    # logical tests to determine the winner based on the age old rules:
    # rock beats scissors
    # scissors beat paper
    # paper beats rock
    # Based on who wins, the computer provides an applicable taunt and the winner gets a point
    # If there is a tie, no one gets a tie
    if humanChoice == "rock":
        if computerChoice == "rock":
            print(choice(tieTaunts))
        elif computerChoice == "paper":
            print(choice(winningTaunts))
            computerScore = computerScore + 1
        elif computerChoice == "scissor":
            print(choice(losingTaunts))
            humanScore = humanScore + 1
        else:
            print("something went wrong")
    elif humanChoice == "paper":
        if computerChoice == "rock":
            print(choice(losingTaunts))
            humanScore = humanScore + 1
        elif computerChoice == "paper":
            print(choice(tieTaunts))
        elif computerChoice == "scissor":
            print(choice(winningTaunts))
            computerScore = computerScore + 1
        else:
            print("something went wrong")
    elif humanChoice == "scissor":
        if computerChoice == "rock":
            print(choice(winningTaunts))
            computerScore = computerScore + 1
        elif computerChoice == "paper":
            print(choice(losingTaunts))
            humanScore = humanScore + 1
        elif computerChoice == "scissor":
            print(choice(tieTaunts))
        else:
            print("something went wrong")
    print(f"You have {humanScore}, I have {computerScore}. Let's play the next round")

# read out the final score and acknowledge the winner
print(f"With a score of {humanScore} to {computerScore},", end=" ")
if humanScore == winningScore:
    print(f"you win. I blame my programmer for this.")
elif computerScore == winningScore:
    print(f"I win. This is a validation of superior intellect")
