# war_engine.py
# This module contains the three main functions needed to play war.

import random
import time
import logging
from card_logic import *
from draw_cards import draw_cards
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

def double_war(winnerList, users):
    """
    Contract: List of winners which are User instances, List of User objects ==> winner which is a User object, List of User objects
    Purpose: To resolve tied cases.
    """    
    survivors = []
    loserCards = []      

    for i in winnerList: # who has enough cards to compete?
        survivors, loserCards = i.double_check(survivors, loserCards)
    log.debug("survivors: %s", survivors)
    
    #from here on out, we use survivors because only those who have enough cards can participate

    # if no players can actually participate, we're going to give them back their cards.
    # This won't do anything if the competing players didn't have any cards.
    if len(survivors) == 0:
        return [], users
    else:
        for user in list(set(winnerList)-set(survivors)):
            user.Deck = []
        
    if len(survivors) == 1: # Only one user left, the winner of the round.
        survivors[0].Deck.extend(loserCards) # Get all the cards from the loser(s) and extend the winner's deck by those cards.
        log.debug("users: %s", users)
        return survivors[0], users
        
    cardsDown = []
    for i in survivors: # Get three cards from every user object that has enough cards to compete
        # this is similar to the card appending statement found in the flip_cards function, but it doesn't turn the cards objects into
        # card lists with rank and suit because it doesn't need to compare or manipulate them. It only needs to append them to the deck of the winner.
        cardsDown.extend( i.flip_three() )
    log.debug("cardsDown: %s", cardsDown)
    
    winner, survivors = flip_cards(survivors) # Run the flip_cards function to get a winner. Winner is a User object.
    
    winner.Deck.extend(cardsDown)
    log.debug("Appended cards to %s", winner)

    return winner, users #returns the winner
    
def card_compare(cardsUp, users): # cardsUp is a list of the card objects in play.
    """
    Contract: List of Card objects, List of User objects ==> winner List, List of User objects
    Purpose: To compare cards and assign them to the winner.
    """
    ranksList = []
    
    for cardObject in cardsUp: #convert our card objects into tuples.
        ranksList.append([cardObject.rank, cardObject.owner, cardObject.suit])
        
    ranksList.sort(key=lambda x: x[0], reverse=True)  # ranksList = [[13, <User object>, 2], [10, <User object>, 1], [rank, <User object>, suit], ... ]
    log.debug("ranksList: %s", ranksList)
   
    winnerList = []
    
    if ranksList[0][0] == ranksList[1][0]: # This is the double_war case
        input("A tie! Press enter to proceed with WAR! ")
        
        log.debug("winnerList: %s", winnerList)
        for i in range(len(ranksList)):
            if ranksList[0][0] == ranksList[i][0]:
                winnerList.append(ranksList[i][1]) # Append the User Object to the winner list so we can develop a list of winners
                log.debug("winnerList (during loop -if): %s", winnerList)
            else:
                log.debug("winnerList (during loop -else): %s", winnerList)
                break # The for loop can stop if the cards aren't tying.
        log.debug("winnerList (after loop): %s", winnerList)
        winner, users = double_war(winnerList, users)  # winnerList = [<User object1>,<User object2>,...]
            
    else: # This is the non-double_war case.
        print(ranksList[0][1], "is the winner!")
        winner = ranksList[0][1]  
     
    if winner != []:  
        for cardObject in cardsUp: # Make a regular (suit, rank) tuple set from the given data so we can append it.
            winner.Deck.append((cardObject.suit, cardObject.rank))
    else:
        for card in ranksList: #This returns the original flipped cards back to the owners.
            card[1].Deck.append((card[2],card[0]))
        print("Nobody had enough cards to play double war. Everyone gets their cards back.")
                
    return winner, users
                    
def flip_cards(users):
    """
    Contract: List of User objects ==> winner, List of User objects
    Purpose: Flip a card from the deck of every user, printing the results on the screen.
    """
    cardsUp = []
    for i in range(len(users)):
        log.debug("User: %s", users[i])
        cardsUp.append( Card(users[i].flip_one()) ) #the flip_one method pulls a card from a given User's deck
        log.debug("Card: %s", str(cardsUp[i]))
    
    print()
    draw_cards(cardsUp)
    print()
    
    return card_compare(cardsUp, users) #return the winner and the users