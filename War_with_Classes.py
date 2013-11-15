from card_logic import *
from war_engine import *
from war_save_load_new import *
import war_gui
gui = war_gui.gui()
import logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

#gui.welcome()

users = gui.get_users()

print()
print(' To save your game, type "save" at any time.')
print()

# Gameplay starts here and continues as long as there is more than one player.
while(len(users) > 1):
    
    totalDeckSize = 0
    for i in users: #i represents a single user. This loop will iterate through all users playing and get the number of cards they have.
        log.debug("%s: %s Cards: %s", i, len(i.Deck), i.Deck)
        totalDeckSize += len(i.Deck)
        print(i, "has", len(i.Deck), "cards. ", end="")
    log.debug("Total number of cards: %i", totalDeckSize)
    
    command = input("\nPress the enter key to flip. ")
    
    if command.startswith("s"):
        save_game(users)
    else:
        winner, users = flip_cards(users) #flip some cards. Winner is never used here.
        
        losers = []
        for i in users:
            log.debug("users (empty checker): %s", users)
            losers = i.empty(losers) #check and see if all the users can still play
        
        if users[0] in losers: #if the human is among the losers, end the game now
            break
        else:
            for i in losers: # if the human is not among the losers, just eject the computer from the users list
                users.remove(i)
    
        print()
    
# Exit While loop

print()
log.debug("losers: %s", losers)
log.debug("users[0]: %s", users[0])
if users[0] in losers:
    print("Sorry, ", users[0], ", you've lost.")
else:
    print("Congratulations, ", users[0], ", you've won!")