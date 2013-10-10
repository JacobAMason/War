# card_logic.py

import random
import time
import logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

class Deck:    
    def __init__(self, acesHigh):
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
                    
    def shuffle(self, userList):
        i = 0
        while self.cards != []:
            for user in userList:
                if self.cards != []:
                    poppedCard = self.cards.pop(random.randint(0, 51 - i))
                    user.Deck.append(poppedCard)
                    i += 1
        return

        
class Hand:
    def __init__(self, owner):
        self.Deck = []
        #self.Card = ()
        # Calling .owner on a Hand will return the username as a string
        self.owner = owner
        
    def flip_card(self):
        #returns the card and the owner:  [(1,2), "Player"]
        return [self.Deck.pop(0), self.owner]

    
class Card:
    def __init__(self, cardList):
        self.cardTuple = cardList[0]
        self.suit = self.cardTuple[0]
        self.rank = self.cardTuple[1] 
        self.owner = cardList[1]
        
    def __str__(self):      
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
        
    def draw(self):
        if self.suit==1:
            pic3 = "| :/\: |"
            pic4 = "| :\/: |"         
        elif self.suit==2:
            pic3 = "| :(): |"
            pic4 = "| ()() |"        
        elif self.suit==3:
            pic3 = "| (\/) |"
            pic4 = "| :\/: |"        
        else:
            pic3 = "| :/\: |"
            pic4 = "| (__) |"
            
        if self.rank > 1 and self.rank < 10:
            pic2 = str(self.rank) + "."
            pic5 = "'" + str(self.rank)
        elif self.rank == 10:    
            pic2 = str(self.rank)
            pic5 = str(self.rank)
        elif self.rank == 11:
            pic2 = "J."
            pic5 = "'J"
        elif self.rank == 12:
            pic2 = "Q."
            pic5 = "'Q"         
        elif self.rank == 13:
            pic2 = "K."
            pic5 = "'K" 
        else:
            pic2 = "A."
            pic5 = "'A"
    
        picture = [".------.", "|" + pic2 + "--. |", pic3, pic4, "| '--" + pic5 + "|", "`------'"]
        
        for line in picture:
            print(line)
        
        return      
    
def card_compare(cardsUp, users): # cardsUp is a list of the card objects in play.

    ranksList = []
    for card in cardsUp:
        ranksList.append([card.rank,card.owner])
        
    ranksList.sort()
    ranksList.reverse()
    
    if ranksList[0][0] == ranksList[1][0]:
        winner = "Tie"
    else:
        print(ranksList[0][1], "is the winner!")
        winner = ranksList[0][1]
        
    for i in range(0, len(users)):
        try:
            if(users[i].owner == winner):
                for card in cardsUp: # Make a regular (suit, rank) tuple set from the given data so we can append it.
                    users[i].Deck.append((card.suit, card.rank))
        except:
            break 