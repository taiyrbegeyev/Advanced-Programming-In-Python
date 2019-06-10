# JTSK-350112
# rqballsim.py
# Taiyr Begeyev
# t.begeyev@jacobs-university.de

from random import random

# new method
def alternate_serving(serv):
    if serv == "A":
        serv = "B"
    else:
        serv = "A"
    return serv

def printIntro():
    """Prints an introduction to the program"""
    print("This program simulates a game of racquetball \
between two players called \"A\" and \"B\". \
The abilities of each player is indicated by a \
probability ( a number between 0 and 1) that the \
player wins the point when serving. Player A \
always has the first serve")

def getInputs():
    """Get the input from the user"""
    a = float(input("Probability of player A to win a serve ? "))
    b = float(input("Probability of player B to win a serve ? "))
    n = int(input("How many games to simulate? "))
    prob = {
        "A": a,
        "B": b
    }
    return prob, n

def gameOver ( score ):
    """a and b are scores for players in a racquetball game
    RETURNS True if game is over , False otherwise"""
    return score["A"] == 15 or score["B"] == 15

def simOneGame(prob):
    """Simulates a single game or racquetball between players A and B
    RETURNS A’s final score , B’s final score"""
    serving = "A"
    score = {
        "A": 0,
        "B": 0
    }

    while not gameOver ( score ):
        if random () < prob[serving]:
            score[serving] = score[serving] + 1
        else:
            serving = alternate_serving(serving)
    return score

def simNGames(n, prob):
    """This function simulates n games and keeps track of how many
    wins there are for each player"""
    wins = {
        "A": 0,
        "B": 0
    }
    
    for _ in range(n):
        score = simOneGame(prob)
        if score["A"] > score["B"]:
            wins["A"] += 1
        else:
            wins["B"] += 1
    return wins

def printSummary ( wins ):
    """Prints a summary of wins for each player"""
    n = wins["A"] + wins["B"]
    print ("\nGames simulated: ", n)
    print (" Wins for A: {0} ({1:0.1%}) ".format(wins["A"] , wins["A"] / n ))
    print (" Wins for B: {0} ({1:0.1%}) ".format(wins["B"] , wins["B"] / n ))

def main():
    printIntro()
    prob, n = getInputs()
    wins = simNGames(n, prob)
    printSummary(wins)

main()