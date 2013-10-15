from card_logic import *
import logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)
  

  
      
Deck = Deck(True) #initialize deck. True means Aces are high
userNameList = []
while userNameList == []: 
    userNameList.append(input("Please enter your name: "))
    
PCnum = int(input("How many Computer opponents would you like to compete against? "))
while PCnum <=0:
    print("You must compete against at least one Computer.")
    PCnum = int(input("How many Computer opponents would you like to compete against? "))
    
for i in range(0, PCnum):
    userNameList.append("Computer " + str(i+1))  #i is incremented because Computer_0 sounds stupid

# users contains the list of users that will be playing, including PCs
# every user in the list will be turned into an object of class Hand
users = []
for userName in userNameList:
    users.append(Hand(userName)) # initialize hands. The string will represent the name of the winner.

Deck.shuffle(users) #shuffle the deck and deal to all players

# Gameplay starts here and continues as long as there is more than one player.
while(len(users) > 1):
    
    totalDeckSize = 0
    for i in users: #i represents a single user. This loop will iterate through all users playing and get the number of cards they have.
        log.debug("%s: %s Cards: %s", i, len(i.Deck), i.Deck)
        totalDeckSize += len(i.Deck)
        print(i, "has", len(i.Deck), "cards. ", end="")
    log.debug("Total number of cards: %i", totalDeckSize)
    
    commands = input("\nPress the enter key to flip. ")
    
    commands
              
    winner, users = flip_cards(users) #flip some cards.
    
    losers = []
    
    for i in users:
        log.debug("users (empty checker): %s", users)
        losers = i.empty(losers) #check and see if all the users can still play
    
    if users[0] in losers: #if the human is among the losers, end the game now
        break
    else:
        for i in losers: # if the human is not among the losers, just eject the computer from the users list
            users.remove(losers[i])

    print()
    
# Exit While loop

print()
log.debug("losers: %s", losers)
log.debug("users[0]: %s", users[0])
if users[0] in losers:
    print("Sorry, ", users[0], ", you've lost.", sep="")
else:
    print("Congratulations, ", users[0], ", you've won!", sep="")

