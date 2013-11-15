# card_logic.py

import random
import logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

class Deck:    
    def __init__(self, acesHigh):
        """
        Contract: bool ==> NULL
        Purpose: Initiliazes the deck.
        """
        self.cards = []
        # The old way to assign cards was to let the user decide if Aces were to be high.
        # I'm keeping the method listed so I can add it back later when I make a configuration menu.
        # self.acesHigh = (input("Are Aces high? (y/n) ") == "y")
        self.acesHigh = acesHigh
        for x in range(1, 5):
            if self.acesHigh:
                log.debug("Aces are high")
                for y in range(2, 15):
                    self.cards.append((x, y))
            else:
                log.debug("Aces are low")
                for y in range(1, 14):
                    self.cards.append((x, y))
        return
                    
    def shuffle(self, users):
        """
        Contract: List of User objects ==> NULL
        Purpose: Shuffles the cards from the main deck to all the Users.
        """
        random.shuffle(self.cards)
        while self.cards != []:
            for i in range(len(users)):
                if self.cards != []:
                    users[i].Deck.append(self.cards.pop())
        return

class User:
    def __init__(self, name):
        """
        Contract: string ==> NULL
        Purpose: Initializes a User, turning the string into the user's name.
        """
        self.Deck = []
        # Calling .name on a User will return the username as a string
        self.name = name
        return
        
    def __str__(self):
        """
        Contract: NULL ==> string
        Purpose: Returns the name of the user.
        """
        return self.name
        
    def flip_one(self):
        """
        Contract: NULL ==> list of the card tuple and the object itself:  [(1,2), <User object>]
        Purpose: To pop a card from a given User's deck.
        """
        #
        return [self.Deck.pop(0), self]
    
    def flip_three(self):
        """
        Contract: NULL ==> list of three card tuples:  [(1,2), (1,3), (4,1)]
        Purpose: to pop three cards during double 
        """
        return [self.Deck.pop(0), self.Deck.pop(0), self.Deck.pop(0)] #pop the top card three times and return all of the cards.
    
    def empty(self, losers): #append object to the list if it has lost
        """
        Contract: List of losers which are User objects ==> list of User objects
        Purpose: To determine if a user is out of cards.
        """
        if len(self.Deck) < 1:
            print(self, "has run out of cards!")
            losers.append(self)
        log.debug("empty returning: losers: %s", losers)
        return losers
    
    def double_check(self, survivors, loserCards): #append object to the list if it has lost as well as appending its cards.
        """
        Contract: List of survivors which are User objects, List of tuples of cards ==> List of survivors which are User objects, List of tuples of cards
        Purpose: To determine if users are out of cards and then append them to a junk deck that will be added to the winner
        """      
        if len(self.Deck) < 4:
            loserCards.extend(self.Deck)
        else:
            survivors.append(self)
            
        log.debug("double_check returning: survivors: %s loserCards: %s", survivors, loserCards)
        return survivors, loserCards

class Card:
    def __init__(self, cardList):  #cardList = [(suit, rank), <User object>]
        """
        Contract: list of a tuple and a User object ==> NULL
        Purpose: Initializes a card for use in displaying names and pictures.
        """
        self.cardTuple = cardList[0]
        self.suit = self.cardTuple[0]
        self.rank = self.cardTuple[1]
        self.owner = cardList[1]
        return
        
    def __str__(self):      
        """
        Contract: NULL ==> string
        Purpose: Print out the name of a card.
        """
        if self.suit==1:
            suit = "Diamonds"        
        elif self.suit==2:
            suit = "Clubs"       
        elif self.suit==3:
            suit = "Hearts"
        else:
            suit = "Spades"  
        
        if self.rank == 1:
            rank = "Ace"       
        elif self.rank == 2:
            rank = "Two"        
        elif self.rank == 3:
            rank = "Three"
        elif self.rank == 4:
            rank = "Four"
        elif self.rank == 5:
            rank = "Five"
        elif self.rank == 6:
            rank = "Six"
        elif self.rank == 7:
            rank = "Seven"
        elif self.rank == 8:
            rank = "Eight"
        elif self.rank == 9:
            rank = "Nine"    
        elif self.rank == 10:
            rank = "Ten"      
        elif self.rank == 11:
            rank = "Jack"      
        elif self.rank == 12:
            rank = "Queen"      
        elif self.rank == 13:
            rank = "King"       
        else: # when cardTuple == 14 because of high Aces
            rank = "Ace"       
        
        return (rank + " of " + suit)