import random
import time
from display_functions import *

######### SHUFFLE DECK #########
# This function takes the full, organized deck and divides it randomly in between
# the two players.  The decks have to be global so all the functions can modify them.
# Shuffle is a function because it needs to be called every time a new game is ran.
# Shuffle clears the decks before making new ones, so the first time the game is run,
# the decks are cleared.


def shuffle(ACES_HIGH, DEBUG):
    global DECK
    global PLAYER_DECK
    global PC_DECK
    
    DECK, PLAYER_DECK, PC_DECK = [],[],[]
    
    # This generates the unshuffled deck
    # The if condition changes the range for the rank when Aces are high.
    for x in range(1, 5):
        if ACES_HIGH == False:
            for y in range(1, 14):
                DECK.append((x, y))             
        else:
            for y in range(2, 15):
                DECK.append((x, y))
    
    if DEBUG == True: print("\n", DECK)
    
    toggle = True

    # This shuffles the deck and splits it between the computer and player.
    # This is stupid. The while loop runs once. Deal a card to each player in one loop.
    while DECK != []:
        for i in range(0, 52):
            card = DECK.pop(random.randint(0, 51 - i))
            if toggle == True:
                PLAYER_DECK.append(card)
            else:
                PC_DECK.append(card)
            toggle = not toggle
            
    print("\n\n\t\tTime to play War!")
    
    return DECK, PLAYER_DECK, PC_DECK


############ DOUBLE WAR #############
# double_war handles function nesting for multiple instances of war.
# When card_compare realizes that cards have tied, it calls this function to
# resolve the value of "winner" (winner is a variable in card_compare that keeps
# track of who won a dual).
# First: This function checks to make sure both parties can enter double war.
#        They must both have at least four cards to proceed (three to lay down and
#        one to dual with). If one party lacks the necessary cards, that party
#        immediately loses. The function returns a loss string which tells all
#        other functions that calls it to skip all appending steps (which could
#        cause the game to crash) and to pass the loss string along until it
#        reaches main_round.
# Second: This function pops three cards from the top of each party's deck and
#         adds them to facedown groups for both the player and the computer.
# Third: This function calls the flip_cards function again.                               THIS IS WHERE THINGS GET COMPLICATED. 
#        The flip_cards function calls compare_cards and the process semi-repeats.        IF YOU DON'T UNDERSTAND THIS SECTION, NOTHING WILL MAKE SENSE.
#        If card_compare returns a winner (and assigns the deciding card to the
#        winner), flip_cards passes that winner through to the winner variable
#        local to double_war, which assigns the facedown cards to the respectful
#        winner.
# Fourth: This function returns the winner of the double war to the original
#         card_compare so card_compare can assign the tied cards to the winner.

def double_war(DEBUG):
    
    if len(PLAYER_DECK) < 4:
        return "END_Player"
    if len(PC_DECK) < 4:
        return "END_PC"
    
    playerCardsDown = []  # "Down" signifies that these cards are facedown
    PCCardsDown = []
    
    for i in range(0,3): # for loop to iterate three times.
        playerCardsDown.extend([PLAYER_DECK.pop(0)])
        PCCardsDown.extend([PC_DECK.pop(0)])
    
    if DEBUG == True:    
        print()  # some debugging prints
        print("playerCardsDown:", playerCardsDown)
        print("PCCardsDown:", PCCardsDown)
    
    winner = flip_cards(DEBUG)  # Run the flip_cards function to get a deciding card.
    
    if winner == "Player":
        PLAYER_DECK.extend(playerCardsDown)
        PLAYER_DECK.extend(PCCardsDown)
    if winner == "PC":
        PC_DECK.extend(PCCardsDown)
        PC_DECK.extend(playerCardsDown)   

    return winner  #return the winner so card_compare() will know who to assign the tied cards.


############ CARD COMPARE ###########
# card_compare is the engine of this game. It takes the random card flips generated
# by the flip_cards function and finds the winner. If there is a winner on the first
# flip, it's pretty obvious as to who the winner is. If not, the card_compare function
# calls double_war to resolve ties. In all cases, it finds the winner and assigns
# him or her or it to the winner variable.  It then checks its winner variable to
# see who actually won and assign the cards to the bottom of that deck.  This
# function also returns the winner so flip_cards can pass it to double_war if necessary.

def card_compare(playerCard, PCCard, DEBUG):
    
    if playerCard[1] > PCCard[1]:
        print("\nYou are the winner!")
        winner = "Player"
    elif playerCard[1] < PCCard[1]:
        print("\nThe Computer is the winner!")
        winner = "PC"
    else:
        print("\nThese cards are equal: It's a tie!")
        time.sleep(2)
        input("\nPress the enter key to proceed with DOUBLE WAR!")
        winner = double_war(DEBUG)

    if winner == "Player":
        PLAYER_DECK.append(playerCard)
        PLAYER_DECK.append(PCCard)
    if winner == "PC":
        PC_DECK.append(PCCard)
        PC_DECK.append(playerCard)
        
    time.sleep(.5)
    
    return winner  #return the winner so flip_cards() can pass it to double_war() if necessary
        
        
########## FLIP CARDS ##########
# When the enter key is pressed, flip cards pops a card from the top of each player's
# deck and lets the user know what those cards are. It then calls card_compare
# to evaluate the winner, so flip_cards can return it.
    
def flip_cards(DEBUG):
    playerCard = PLAYER_DECK.pop(0)
    PCCard = PC_DECK.pop(0)
    print()
    print("The Computer's card is the ", get_name(PCCard), ".", sep="")
    get_picture(PCCard)
    print()
    get_picture(playerCard)
    print("Your card is the ", get_name(playerCard), ".", sep="") 
    
    
    time.sleep(.5)
    
    return card_compare(playerCard, PCCard, DEBUG)  # this passes through the winner