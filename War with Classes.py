import random
import time

class Deck:    
    def __init__(self):
        self.cards = []
        self.acesHigh = (input("Are Aces high? (y/n) ") == "y")
        for x in range(1, 5):
            if self.acesHigh:
                for y in range(2, 15):
                    self.cards.append((x, y))
            else:
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
        self.Card = ()
        self.owner = owner    
        
    def flip_card(self):
        return self.Deck.pop(0)

class Card:
    def __init__(self, cardTuple):
        self.cardTuple = cardTuple
        self.suit = cardTuple[0]
        self.rank = cardTuple[1]
    
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
    
    def compare(self, otherCard):
        if self.rank > otherCard.rank:
            print("\nYou are the winner!")
            winner = self.owner
        elif self.rank < otherCard.rank:
            print("\nThe Computer is the winner!")
            winner = otherCard.owner
        else:
            print("\nThese cards are equal: It's a tie!")
            time.sleep(2)
            input("\nPress the enter key to proceed with DOUBLE WAR!")
            winner = "Tie"
            
        time.sleep(.5)
        
        return winner        
        

Deck = Deck() #initialize deck
Player, PC = Hand("Player"), Hand("PC") #initialize hands. The string will represent the name of the winner.
Deck.shuffle([Player, PC]) #shuffle the deck to both players

print(Player.Deck)
print(PC.Deck)

print(len(Player.Deck))
print(len(PC.Deck))

Player.Card = Player.flip_card()  #card1 and card2 are tuples
PC.Card = PC.flip_card()

print(playerCard)
playerCard.draw()
print(PCCard)
PCCard.draw()

winner = playerCard.compare(PCCard)
print(winner)