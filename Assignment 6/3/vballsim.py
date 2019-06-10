# JTSK-350112
# vballsim.py
# Taiyr Begeyev
# t.begeyev@jacobs-university.de

from random import random

def alternate_serving(serv):
    if serv == "A":
        serv = "B"
    else:
        serv = "A"
    return serv

def getInputs():
    """Get the input from the user"""
    a = float(input("Probability of team A to win a serve ? "))
    b = float(input("Probability of team B to win a serve ? "))
    n = int(input("How many games to simulate? "))
    prob = {
        "A": a,
        "B": b
    }
    return prob, n

# Version 1 : Only serving team scores

def printIntro_1():
    """Prints an introduction to the program"""
    print("This program simulates a game of volleyball \
between two teams called \"A\" and \"B\". \
The abilities of each team is indicated by a \
probability ( a number between 0 and 1) that the \
team wins the point when serving. Team A \
always has the first serve")

def gameOver_1( score ):
    """a and b are scores for teams in a volleyball game
    RETURNS True if game is over , False otherwise"""
    if score["A"] == 15 and score["A"] - score["B"] >= 2:
        return score["A"]
    elif score["B"] == 15 and score["B"] - score["A"] >= 2:
        return score["B"]

def simOneGame_1(prob):
    """Simulates a single game or volleyball between teams A and B
    RETURNS A’s final score , B’s final score"""
    serving = "A"
    score = {
        "A": 0,
        "B": 0
    }

    while not gameOver_1 ( score ):
        if random () < prob[serving]:
            score[serving] += 1
        else:
            serving = alternate_serving(serving)
    return score

def simNGames_1(n, prob):
    """This function simulates n games and keeps track of how many
    wins there are for each team"""
    wins = {
        "A": 0,
        "B": 0
    }
    
    for _ in range(n):
        score = simOneGame_1(prob)
        if score["A"] > score["B"]:
            wins["A"] += 1
        else:
            wins["B"] += 1
    return wins

# Version 2 : Both teams can score

def printIntro_2():
    """Prints an introduction to the program"""
    print("This program simulates a game of volleyball \
between two teams called \"A\" and \"B\". \
The abilities of each team is indicated by a \
probability ( a number between 0 and 1) that the \
team wins the point when serving. Both teams can score")

def gameOver_2( score ):
    """a and b are scores for teams in a volleyball game
    RETURNS True if game is over , False otherwise"""
    return score["A"] == 25 or score["B"] == 25

def simOneGame_2(prob):
    """Simulates a single game or volleyball between teams A and B
    RETURNS A’s final score , B’s final score"""
    serving = "A"
    score = {
        "A": 0,
        "B": 0
    }

    while not gameOver_2 ( score ):
        if random () < prob[serving]:
            score[serving] += 1
        else:
            serving = alternate_serving(serving)
            score[serving] += 1            
    return score

def simNGames_2(n, prob):
    """This function simulates n games and keeps track of how many
    wins there are for each team"""
    wins = {
        "A": 0,
        "B": 0
    }
    
    for _ in range(n):
        score = simOneGame_2(prob)
        if score["A"] > score["B"]:
            wins["A"] += 1
        else:
            wins["B"] += 1
    return wins

def printSummary( wins ):
    """Prints a summary of wins for each team"""
    n = wins["A"] + wins["B"]
    print ("\nGames simulated: ", n)
    print (" Wins for A: {0} ({1:0.1%}) ".format(wins["A"] , wins["A"] / n ))
    print (" Wins for B: {0} ({1:0.1%}) ".format(wins["B"] , wins["B"] / n ))

def main_version_1():
    printIntro_1()
    prob, n = getInputs()
    wins = simNGames_1(n, prob)
    printSummary(wins)

def main_version_2():
    printIntro_2()
    prob, n = getInputs()
    wins = simNGames_2(n, prob)
    printSummary(wins)

main_version_1()
main_version_2()