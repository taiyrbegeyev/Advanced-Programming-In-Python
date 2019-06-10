# JTSK-350112
# deadoralive.py
# Taiyr Begeyev
# t.begeyev@jacobs-university.de

import random

class Card(object):
    """ A card object with a suit and rank."""

    RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

    SUITS = ('Spades', 'Diamonds', 'Hearts', 'Clubs')

    def __init__(self, rank, suit):
        """Creates a card with the given rank and suit."""
        self.rank = rank
        self.suit = suit
        
    def __str__(self):
        """Returns the string representation of a card."""
        if self.rank == 1:
            rank = 'Ace'
        elif self.rank == 11:
            rank = 'Jack'
        elif self.rank == 12:
            rank = 'Queen'
        elif self.rank == 13:
            rank = 'King'
        else:
            rank = self.rank
        return str(rank) + ' of ' + self.suit

class Deck(object):
    """ A deck containing 52 cards."""

    def __init__(self):
        """Creates a full deck of cards."""
        self._cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                c = Card(rank, suit)
                self._cards.append(c)

    def shuffle(self):
        """Shuffles the cards."""
        random.shuffle(self._cards)

    def deal(self):
        """Removes and returns the top card or None 
        if the deck is empty."""
        if len(self) == 0:
           return None
        else:
           return self._cards.pop(0)

    def __len__(self):
       """Returns the number of cards left in the deck."""
       return len(self._cards)

    def __str__(self): 
        """Returns the string representation of a deck."""
        result = ''
        for c in self._cards:
            result = self.result + str(c) + '\n'
        return result

class Player(object):
    """This class represents a player in
    a dead or alive game."""

    def __init__(self, cards):
        self._cards = cards

    def __str__(self):
        """Returns string rep of cards and points."""
        result = ", ".join(map(str, self._cards))
        result += "\n  " + str(self.getPoints()) + " points"
        return result

    def hit(self, card):
        self._cards.append(card)

    def getCard(self):
        return self._cards.pop()

    def getPoints(self):
        """Returns the number of points in the hand."""
        count = 0
        for card in self._cards:
            if card.rank > 9:
                count += 10
            elif card.rank == 1:
                count += 11
            else:
                count += card.rank
        # Deduct 10 if Ace is available and needed as 1
        for card in self._cards:
            if count <= 21:
                break
            elif card.rank == 1:
                count -= 10
        return count

    def hasBlackjack(self):
        """Dealt 21 or not."""
        return len(self._cards) == 2 and self.getPoints() == 21 


class Dealer(Player):
    """Like a Player, but with some restrictions."""

    def __init__(self, cards):
        """Initial state: show one card only."""
        Player.__init__(self, cards)
        self._showOneCard = True

    def __str__(self):
        """Return just one card if not hit yet."""
        if self._showOneCard:
            return str(self._cards[0])
        else:
            return Player.__str__(self)

    def hit(self, deck):
        """Add cards while points < 17,
        then allow all to be shown."""
        self._showOneCard = False
        while self.getPoints() < 17:
            self._cards.append(deck.deal())

class DeadOrAlive(object):
    def __init__(self):
        self._deck=Deck()
        self._deck.shuffle()
        self._player = Player([])
        self._dealer = Player([])
    def play(self):
        cnt1 = 0
        cnt2 = 0
        for i in range(52):
            choice = input("Do you want to play [y/n]?: ")
            if choice == 'Y' or choice == 'y':
                self._player.hit(self._deck.deal())
                self._dealer.hit(self._deck.deal())
                card1 = self._player.getCard()
                card1a = card1.rank
                card2 = self._dealer.getCard()
                card2a = card2.rank
                print("Player 1:\n",card1a)
                print("Player 2:\n",card2a)
                if card1a > card2a:
                    print("Player 1 won")
                    cnt1 += 1
                elif card2a > card1a:
                    print("Player 2 won")
                    cnt2 += 1
                else:
                    if card1.suit == "Spades":
                        print("Player 2 won with", card2.suit)
                        cnt2 += 1
                    elif card1.suit == "Diamonds" and (card2.suit=="Hearts"
                        or card2.suit=="Clubs"):

                        print("Player 2 won with", card2.suit)
                        cnt2 += 1
                    elif card1.suit == "Hearts" and card2.suit=="Clubs":
                        print("Player 2 won with", card2.suit)
                        cnt2 += 1
                    elif card1.suit == card2.suit:
                        print("There is a tie")
                    else:
                        print("Player 1 won with", card1.suit)
                        cnt1 += 1
                if i == 25:
                    print("\nPlayer 1:", cnt1, "wins")
                    print("Player 2:", cnt2, "wins")
            else:
                print("Player 1: ", cnt1, "wins")
                print("Player 2: ", cnt2 ,"wins")
                break

class Blackjack(object):

    def __init__(self):
        self._deck = Deck()
        self._deck.shuffle()
        self._player = Player([self._deck.deal(), self._deck.deal()])
        self._dealer = Dealer([self._deck.deal(), self._deck.deal()])

    def play(self):
        print("Player:\n", self._player)
        print("Dealer:\n", self._dealer)
        while True:
            choice = input("Do you want a hit? [y/n]: ")
            if choice in ("Y", "y"):
                self._player.hit(self._deck.deal())
                points = self._player.getPoints()
                print("Player:\n", self._player)
                if points >= 21:
                    break
            else:
                break
        playerPoints = self._player.getPoints()
        if playerPoints > 21:
            print("You bust and lose")
        else:
            self._dealer.hit(self._deck)
            print("Dealer:\n", self._dealer)
            dealerPoints = self._dealer.getPoints()
            if dealerPoints > 21:
                print("Dealer busts and you win")
            elif dealerPoints > playerPoints:
                print("Dealer wins")
            elif dealerPoints < playerPoints and playerPoints <= 21:
                print("You win")
            elif dealerPoints == playerPoints:
                if self._player.hasBlackjack() and not self._dealer.hasBlackjack():
                    print("You win")
                elif not self._player.hasBlackjack() and self._dealer.hasBlackjack():
                    print("Dealer wins")
                else:
                    print("There is a tie")
   
def main():
    game = DeadOrAlive()
    game.play()

main()