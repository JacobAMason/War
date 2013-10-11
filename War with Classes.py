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
    users.append(Hand(userName)) #initialize hands. The string will represent the name of the winner.

Deck.shuffle(users) #shuffle the deck and deal to all players


while("playcontinues" == "playcontinues"):
    for i in users: #i represents a single user. This loop will iterate through all users playing
        log.debug("%s: %s Cards: %s", i.owner, len(i.Deck), i.Deck)
    
    card = []
    for i in range(0, len(users)):
        log.debug("Iteration: %i", i)
        log.debug("User: %s", users[i].owner)
        card.append( Card(users[i].flip_card()) )
        log.debug("Card: %s", str(card[i])) 
    
    for i in range(1, len(users)):
        print(card[i], "\t", end="")
        
    print()
    for i in range(1, len(users)):
        card[i].draw()
        
    print()
    card[0].draw()
    print(card[0])
    print()
    
    winner = card[0].compare(card[1])
    
    
    
    input("Press enter key to continue...")