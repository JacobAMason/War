# card_logic.py

import random
import time
import logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

random.seed(20)

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
        # Calling .owner on a Hand will return the username as a string
        self.owner = owner
        
    def __str__(self):
        return self.owner
        
    def flip_card(self):
        #returns the card and the owner:  [(1,2), "Player"]
        return [self.Deck.pop(0), self.owner]
    
    def flip_three(self):
        return [self.Deck.pop(0), self.Deck.pop(0), self.Deck.pop(0)] #pop the top card three times and return all of the cards.
    
    def empty(self, losers): #append object to the list if it has lost
        if len(self.Deck) < 1:
            print(self, "has run out of cards!")
            losers.append(self)
        log.debug("empty returning: losers: %s", losers)
        return losers
    
    def double_check(self, onlyWinners, loserCards): #append object to the list if it has lost as well as appending its cards.
        if len(self.Deck) < 4:
            loserCards.extend(self.Deck)
        else:
            onlyWinners.append(self)
            
        log.debug("double_check returning: onlyWinners: %s loserCards: %s", onlyWinners, loserCards)
        return onlyWinners, loserCards

class Card:
    def __init__(self, cardList):  #cardList = [[(2,13), 'Computer 1'], [(suit,rank), 'username'], ... ]
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
    
def double_war(winner, users):
    
    winnerObjs = []
    for winnerString in winner: # First step: turn the winner string list into a list of user objects with those winner strings
        for userObject in users:
            if winnerString == str(userObject):
                winnerObjs.append(userObject) 
    log.debug("winnerObjs: %s", winnerObjs)
    
    onlyWinners = []
    loserCards = []
    for i in winnerObjs: # who has enough cards to compete?
        onlyWinners, loserCards = i.double_check(onlyWinners, loserCards)
    log.debug("onlyWinners: %s", onlyWinners)
    
     #from here on our, we use onlyWinners because only those who have enough cards can participate
    
    if len(onlyWinners) == 1: # Only one user left, the winner of the round.
        onlyWinners[0].Deck.extend(loserCards) # Get all the cards from the loser and extend the winner's deck by those cards.
        users[users.index(onlyWinners[0])]=onlyWinners[0] # write over the winner's deck with the cards from the user he beat
        log.debug("users: %s", users)
        return winner, users
        
    cardsDown = []
    for i in onlyWinners: # Get three cards from every user object that has enough cards to compete
        # this is similar to the card appending statement found in the flip_cards function, but it doesn't turn the cards objects into
        # card lists with rank and suit because it doesn't need to compare or manipulate them. It only needs to append them to the deck of the winner.
        cardsDown.extend( i.flip_three() )
        
    log.debug("cardsDown: %s", cardsDown)
    
    winner, onlyWinners = flip_cards(onlyWinners) # Run the flip_cards function to get a winner. This winner is a string.
    
    for i in onlyWinners: # The results of the flipcards function need to be written to the individual users, only overwriting the users participating
        users[users.index(i)]=i
    
    for userObject in users:
        if winner == str(userObject):
            userObject.Deck.extend(cardsDown)
            log.debug("Appended cards to %s", userObject)

    return winner, users #returns the string of the winner
    
def card_compare(cardsUp, users): # cardsUp is a list of the card objects in play.
    ranksList = []
    
    for cardObject in cardsUp: #convert our card objects 
        ranksList.append([cardObject.rank,cardObject.owner])
        
    ranksList.sort()
    ranksList.reverse()  # ranksList = [[13, "Computer 2"], [10, "Computer 1], [rank, "username"], ... ]
    log.debug("ranksList: %s", ranksList)
   
    winner = []
    
    if ranksList[0][0] == ranksList[1][0]: # This is the double_war case
        input("A tie! Press enter to proceed with WAR! ")
        
        log.debug("winner: %s", winner)
        for i in range(len(ranksList)):
            if ranksList[0][0] == ranksList[i][0]:
                winner.append(ranksList[i][1]) # Append the string to the winner list so we can develop a list of winners
                log.debug("winner (during loop -if): %s", winner)
            else:
                log.debug("winner (during loop -else): %s", winner)
                break # The for loop can stop if the cards aren't tying.
        log.debug("winner (after loop): %s", winner)
        winner, users = double_war(winner, users)  # winner = ["User 1", "User 2", ... , "User n"]
            
    else: # This is the non-double_war case.
        print(ranksList[0][1], "is the winner!")
        winner = ranksList[0][1]
        
    for i in users: # Iterate over all the users and find which one is the winner, then append all the card
        if str(i) == winner:
            for cardObject in cardsUp: # Make a regular (suit, rank) tuple set from the given data so we can append it.
                i.Deck.append((cardObject.suit, cardObject.rank))
                
    return winner, users
                    
def flip_cards(users):
    cardsUp = []
    for i in range(0, len(users)):
        log.debug("User: %s", users[i])
        cardsUp.append( Card(users[i].flip_card()) ) #the flip_card method pulls a card from a given Hand object's deck
        log.debug("Card: %s", str(cardsUp[i]))
    
    for i in range(1, len(users)):
        print(cardsUp[i], "\t", end="")
        
    print()
    for i in range(1, len(users)):
        cardsUp[i].draw()
        
    print()
    cardsUp[0].draw()
    print(cardsUp[0])
    print()
    
    return card_compare(cardsUp, users) #return the winner
    
    