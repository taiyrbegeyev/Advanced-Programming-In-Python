# JTSK-350112
# rqballsim.py
# Taiyr Begeyev
# t.begeyev@jacobs-university.de

from random import random

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
    return a, b, n

def gameOver (a , b ):
    """a and b are scores for players in a racquetball game
    RETURNS True if game is over , False otherwise"""
    return a == 15 or b == 15

def simOneGame(probA, probB):
    """Simulates a single game or racquetball between players A and B
    RETURNS A’s final score , B’s final score"""
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver ( scoreA , scoreB ):
        if serving == "A":
            if random () < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random () < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB

def simNGames(n, probA, probB):
    """This function simulates n games and keeps track of how many
        wins there are for each player"""
    winsA = winsB = 0
    for _ in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB

def printSummary ( winsA , winsB ):
    """Prints a summary of wins for each player"""
    n = winsA + winsB
    print ("\nGames simulated: ", n)
    print (" Wins for A: {0} ({1:0.1%}) ".format(winsA , winsA / n ))
    print (" Wins for B: {0} ({1:0.1%}) ".format(winsB , winsB / n ))

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)

main()