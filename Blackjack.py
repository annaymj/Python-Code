#File: Blackjack.py
#
#Description: In this Blackjack.py, it reads the rank of the card from the players, and calculates the sum of the card ranks,
#whoever reaches Blackjack (2 cards with the sum of 21) wins, and if no Blackjack reached, the one with the closest number to 21(<21) wins.
#
#Student's Name:Mengjie Yu
#
#Student's UT EID:my3852
#
#Course Name: CS 313E 
#
#Unique Number: 53260
#
#Date Created:2/4/2013
#
#Date Last Modified:

import string, math, random

class Card (object):
    RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    SUITS = ('S', 'D', 'H', 'C')

    def __init__ (self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__ (self):
        if self.rank == 1:
            rank = 'A'
        elif self.rank == 13:
            rank = 'K'
        elif self.rank == 12:
            rank = 'Q'
        elif self.rank == 11:
            rank = 'J'
        else:
            rank = self.rank
        return str(rank) + self.suit

    def __eq__ (self, other):
        return (self.rank == other.rank)

    def __ne__ (self, other):
        return (self.rank != other.rank)

    def __lt__ (self, other):
        return (self.rank < other.rank)

    def __le__ (self, other):
        return (self.rank <= other.rank)

    def __gt__ (self, other):
        return (self.rank > other.rank)

    def __ge__ (self, other):
        return (self.rank >= other.rank)

class Deck (object):
    def __init__ (self):
        self.deck = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                card = Card (rank, suit)
                self.deck.append(card)

    def shuffle (self):
        random.shuffle (self.deck)

    def __len__ (self):
        return len (self.deck)

    def deal (self):
        if len(self) == 0:
            return None
        else:
            return self.deck.pop(0)

class Player (object):
    def __init__ (self, cards):
        self.cards = cards

    def hit (self, card):             #definition of hitting a card
        self.cards.append(card)

    def getPoints (self):
        count = 0
        for card in self.cards:
            if card.rank > 9:
                count += 10
            elif card.rank == 1:
                count += 11
            else:
                count += card.rank
        # deduct 10 if Ace is there and needed as 1
        for card in self.cards:
            if count <= 21:
                break
            elif card.rank == 1:
                count = count - 10
        return count

  # does the player have 21 points or not
    def hasBlackjack (self):
        return len (self.cards) == 2 and self.getPoints() == 21

  # complete the code so that the cards and points are printed
    def __str__ (self):
        hand=''
        for i in range(len(self.cards)):
            hand=hand+str(self.cards[i])+' '
        return (hand+ ' - '+ str(self.getPoints())+' points')
          

# Dealer class inherits from the Player class
class Dealer (Player):
    def __init__ (self, cards):
        Player.__init__ (self, cards)
        self.show_one_card = True   #meaning of show_one_card???

  # over-load the hit function() in the parent class
  # add cards while points < 17, then allow all to be shown
    def hit (self, deck):
        self.show_one_card = False
        while self.getPoints() < 17:
            self.cards.append (deck.deal())

  # return just one card if not hit yet
    def __str__ (self):
        if self.show_one_card:
            return str(self.cards[0])
        else:
            return Player.__str__(self)

class Blackjack (object):
    def __init__ (self, numPlayers):
        self.deck = Deck()
        self.deck.shuffle()
        self.numPlayers = numPlayers
        self.Players = []

        for i in range (self.numPlayers):
            self.Players.append (Player([self.deck.deal(), self.deck.deal()]))
        self.dealer = Dealer ([self.deck.deal(), self.deck.deal()])

    def play (self):
        # Print the cards that each player has
        for i in range (self.numPlayers):
            print ('Player ' + str(i + 1) + ': ' + str(self.Players[i]))

    # Print the cards that the dealer has
        print ('Dealer: ' + str(self.dealer))

    # Each player hits until he says no
        playerPoints = []
        for i in range (self.numPlayers):
            while True:
                print ('Player'+str(i+1),end='')
                choice = input (', do you want to hit? [y / n]: ')
                if choice in ('y', 'Y'):
                    (self.Players[i]).hit (self.deck.deal())
                    points = (self.Players[i]).getPoints()
                    print ('Player ' + str(i + 1) + ': ' + str(self.Players[i]))
                    if points >= 21:
                        break
                else:
                    break
            playerPoints.append ((self.Players[i]).getPoints())

    # Dealer's turn to hit
        self.dealer.hit (self.deck)
        dealerPoints = self.dealer.getPoints()
        print ('Dealer: ' + str(self.dealer) + ' - ' + str(dealerPoints))

        # determine the outcome; you will have to re-write the code
        # it was written for just one player having playerPoints
        for i in range(len(playerPoints)):                          #loop through all the players
            if playerPoints[i] > 21:                                #if the player got over 21, he/she loses                      
                print ('Player '+str(i+1)+' loses')
            elif dealerPoints > 21:                                 #if dealer got over 21,he loses
                print ('Player '+str(i+1)+' wins')
            elif Player.hasBlackjack(self.Players[i]):              #as long as player got blackjack, he/she wins
                print ('Player '+str(i+1)+' wins')
            elif Player.hasBlackjack(self.dealer) or dealerPoints==21:
                if playerPoints == 21:                              #if player doesn't get Blackjack but got 21points, she/he reaches a tie
                    print ('Player '+str(i+1)+'reaches a tie')
                else:
                    print ('Player '+str(i+1)+' loses')
            elif dealerPoints <21:                                  #if both player and dealer got less than 21 points
                if playerPoints[i] > dealerPoints:                  # if player got higher score than dealer, he wins
                    print ('Player '+str(i+1)+' wins')
                elif playerPoints[i] == dealerPoints:               # If they got same points, it ties
                    print ('Player '+str(i+1)+'ties')
                else:                                               # if player got lower score than dealer, he loses
                    print ('Player '+str(i+1)+' loses')

def main ():
    numPlayers = eval (input ('Enter number of players: '))
    while (numPlayers < 1 or numPlayers > 6):
        numPlayers = eval (input ('Enter number of players: '))
    game = Blackjack (numPlayers)
    game.play()

main()
