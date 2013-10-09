import random

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
                    
    def shuffle(self):
        i = 0
        playerDeck = []
        PCDeck = []
        while self.cards != []:
            card = self.cards.pop(random.randint(0, 51 - i))
            playerDeck.append(card)
            i += 1
            card = self.cards.pop(random.randint(0, 51 - i))
            PCDeck.append(card)
            i += 1
        return playerDeck, PCDeck
            
    def flip_card(self, deck):
        return deck.pop(0)
    
    def add(self, cardTuple):
        self.cards.append(self.cardTuple)
                    
class Card:
    def __init__(self, cardTuple):
        self.cardTuple = cardTuple
        self.suit = cardTuple[0]
        self.rank = cardTuple[1]
        
    def compare(self, PCCard):
        if self.rank > PCCard.rank:
            print("\nYou are the winner!")
            winner = "Player"
        elif self.rank < PCCard.rank:
            print("\nThe Computer is the winner!")
            winner = "PC"
        else:
            print("\nThese cards are equal: It's a tie!")
            time.sleep(2)
            input("\nPress the enter key to proceed with DOUBLE WAR!")
            winner = double_war()
    
        if winner == "Player":
            playerDeck.cards.append(self.cardTuple)
            playerDeck.cards.append(PCCard.cardTuple)
        if winner == "PC":
            PCDeck.cards.append(PCCard.cardTuple)
            PCDeck.cards.append(self.cardTuple)
            
        time.sleep(.5)
        
        return winner
    
    def name(self):
        
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

Deck = Deck() #initialize deck
playerDeck, PCDeck = Deck.shuffle() #shuffle the deck to both players
playerCard = Card(Deck.flip_card(playerDeck))
print(playerCard.name())
playerCard.draw()
PCCard = Card(Deck.flip_card(PCDeck))
print(PCCard.name())
PCCard.draw()
print(playerCard.beats(PCCard))
