from card_logic import *
import logging
logging.basicConfig(level=logging.INFO)
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

loser = "Noner" #loser is set to the loser of a round if one is eliminated.
end_game = "None"

# Gameplay starts here and continues as long as there is more than one player.
while(len(users) > 1):
    
    totalDeckSize = 0
    for i in users: #i represents a single user. This loop will iterate through all users playing
        log.debug("%s: %s Cards: %s", i, len(i.Deck), i.Deck)
        totalDeckSize += len(i.Deck)
        print(i, "has", len(i.Deck), "cards. ", end="")
    log.debug("Total number of cards: %i", totalDeckSize)
    
    print("\nPress the enter key to flip. ")
              
    end_game, users = flip_cards(users) #flip some cards.
    
    for i in users:
        users, loser = i.empty(1, users) #check and see if all the users can still play

    print()
    
# Exit While loop

print()
if loser == users[0]:
    print("Sorry, ", users[0], ", you've lost.", sep="")
else:
    print("Congratulations, ", users[0], ", you've won!", sep="")

