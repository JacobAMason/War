# War.py
# Jacob Mason
# jm2232
#
# 1 = Diamonds
# 2 = Clubs
# 3 = Hearts
# 4 = Spades
#
#  Append Order: (This is important to understand the debug stream.
#
#  In non-double war cases: the winner's card is always appended first.
#
#  In double war cases:
#     The first cards appended are the final "decision" cards. The winner is appended first.
#     Second, the winner of the war's facedown cards are appended, followed by the loser's cards.
#     Third, the orginal tied cards are appended in the order of whoever won the war.
#
#  TL;DR: The winner's cards are appended first, but in reverse order to the chronology of events.
#  Huh?: Just press the enter key a bunch.
#

import random
import time
import ctypes

####### GLOBAL VARIABLES #######

# Set ACES_HIGH to False to make Aces low and True to make Aces High
ACES_HIGH = True

# Set DEBUG to True to activate verbose mode.
# You can always type "debug" at the enter key prompt to get current card stats, even if this is False.
DEBUG = False

############ HEADER ############
# Cool Title Text
def print_header():
    print()
    print(" WWWWWWWW                           WWWWWWWW                                  ")
    print(" W::::::W                           W::::::W                                  ")
    print(" W::::::W                           W::::::W                                  ")
    print(" W::::::W                           W::::::W                                  ")
    print("  W:::::W           WWWWW           W:::::Waaaaaaaaaaaaa  rrrrr   rrrrrrrrr   ")
    print("   W:::::W         W:::::W         W:::::W a::::::::::::a r::::rrr:::::::::r  ")
    print("    W:::::W       W:::::::W       W:::::W  aaaaaaaaa:::::ar:::::::::::::::::r ")
    print("     W:::::W     W:::::::::W     W:::::W            a::::arr::::::rrrrr::::::r")
    print("      W:::::W   W:::::W:::::W   W:::::W      aaaaaaa:::::a r:::::r     r:::::r")
    print("       W:::::W W:::::W W:::::W W:::::W     aa::::::::::::a r:::::r     rrrrrrr")
    print("        W:::::W:::::W   W:::::W:::::W     a::::aaaa::::::a r:::::r            ")
    print("         W:::::::::W     W:::::::::W     a::::a    a:::::a r:::::r            ")
    print("          W:::::::W       W:::::::W      a::::a    a:::::a r:::::r            ")
    print("           W:::::W         W:::::W       a:::::aaaa::::::a r:::::r            ")
    print("            W:::W           W:::W         a::::::::::aa:::ar:::::r            ")
    print("             WWW             WWW           aaaaaaaaaa  aaaarrrrrrr            ")
    
######### SHUFFLE DECK #########
# This function takes the full, organized deck and divides it randomly in between
# the two players.  The decks have to be global so all the functions can modify them.
# Shuffle is a function because it needs to be called every time a new game is ran.
# Shuffle clears the decks before making new ones, so the first time the game is run,
# the decks are cleared.


def shuffle():
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
            
    if DEBUG == True:
            print("\n", PLAYER_DECK)
            print("\n", PC_DECK)
            
    print("\n\n\t\tTime to play War!")
    
    return

######### GET PICTURE ###########
# Returns the graphic equivalent of a card when passed a card's tuple.
# Returns in the form of an array containing each line's string.

def get_picture(cardTuple):
    
    if cardTuple[0]==1:
        pic3 = "| :/\: |"
        pic4 = "| :\/: |"         
    elif cardTuple[0]==2:
        pic3 = "| :(): |"
        pic4 = "| ()() |"        
    elif cardTuple[0]==3:
        pic3 = "| (\/) |"
        pic4 = "| :\/: |"        
    else:
        pic3 = "| :/\: |"
        pic4 = "| (__) |"
        
    if cardTuple[1] > 1 and cardTuple[1] < 10:
        pic2 = str(cardTuple[1]) + "."
        pic5 = "'" + str(cardTuple[1])
    elif cardTuple[1] == 10:    
        pic2 = str(cardTuple[1])
        pic5 = str(cardTuple[1])
    elif cardTuple[1] == 11:
        pic2 = "J."
        pic5 = "'J"
    elif cardTuple[1] == 12:
        pic2 = "Q."
        pic5 = "'Q"         
    elif cardTuple[1] == 13:
        pic2 = "K."
        pic5 = "'K" 
    else:
        pic2 = "A."
        pic5 = "'A"

    picture = [".------.", "|" + pic2 + "--. |", pic3, pic4, "| '--" + pic5 + "|", "`------'"]
    
    for line in picture:
        print(line)
    
    return
        
########## GET NAME #############
# get_name() takes a cardTuple (A suit and rank) and returns the equivalent string.

def get_name(cardTuple):
    
    if cardTuple[0]==1:
        suit = "Diamonds"        
    elif cardTuple[0]==2:
        suit = "Clubs"       
    elif cardTuple[0]==3:
        suit = "Hearts"
    else:
        suit = "Spades"  
    
    if cardTuple[1] == 1:
        rank = "Ace"       
    elif cardTuple[1] == 2:
        rank = "Two"        
    elif cardTuple[1] == 3:
        rank = "Three"
    elif cardTuple[1] == 4:
        rank = "Four"
    elif cardTuple[1] == 5:
        rank = "Five"
    elif cardTuple[1] == 6:
        rank = "Six"
    elif cardTuple[1] == 7:
        rank = "Seven"
    elif cardTuple[1] == 8:
        rank = "Eight"
    elif cardTuple[1] == 9:
        rank = "Nine"    
    elif cardTuple[1] == 10:
        rank = "Ten"      
    elif cardTuple[1] == 11:
        rank = "Jack"      
    elif cardTuple[1] == 12:
        rank = "Queen"      
    elif cardTuple[1] == 13:
        rank = "King"       
    else: # when cardTuple == 14 because of high Aces
        rank = "Ace"       
    
    return (rank + " of " + suit)


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

def double_war():
    
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
    
    winner = flip_cards()  # Run the flip_cards function to get a deciding card.
    
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

def card_compare(playerCard, PCCard):
    
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
        winner = double_war()

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
    
def flip_cards():
    playerCard = PLAYER_DECK.pop(0)
    PCCard = PC_DECK.pop(0)
    print()
    print("The Computer's card is the ", get_name(PCCard), ".", sep="")
    get_picture(PCCard)
    print()
    get_picture(playerCard)
    print("Your card is the ", get_name(playerCard), ".", sep="") 
    
    
    time.sleep(.5)
    
    return card_compare(playerCard, PCCard)  # this passes through the winner


############## MAIN ROUND ##############
# This function is what keeps polling the user.  It holds the current match data
# and will continually be called as long as the player keeps wanting to play.
# This function monitors the global variables that are necessary to keep the game
# running. If either deck is emptied, the game is over. If a double war is attempted
# but cannot be performed because a party lacks enough cards, endGame will end the
# loop.  Regardless of how the loop ends, main_round passes the loser to the_game.

def main_round():
    endGame = "" 
    while(PLAYER_DECK != [] and PC_DECK != [] and endGame != "END_Player" and endGame != "END_PC"):
        
        print("\n\nYou have", len(PLAYER_DECK), "cards.  The computer has", len(PC_DECK), "cards.")
        
        stats = input("\nPress the enter key to flip. ")
        print("\n" * 23)
        
        if stats == "debug":
            print("\nPLAYER_DECK:", PLAYER_DECK)
            print("\nPC_DECK:", PC_DECK)
            print("\nDeck size:", (len(PLAYER_DECK) + len(PC_DECK)), "cards.")
        else:
            endGame = flip_cards()
            print()
    
    if PLAYER_DECK == [] or endGame == "END_Player":
        return "Player"
    else:
        return "PC"
    
    
############### THE GAME ################
# the_game is the function that keeps the entire program running. It initializes
# the decks and calls main_round, which returns the winner of each round.

def the_game():
    playAgain = "y"
    while playAgain == "y":
        print_header()
        print("\n"*6)
        input("Press the enter key to begin...")
        print("\n"*16)        
        shuffle()      
        loser = main_round()      
        if loser == "Player":
            print("\nOh no! You've run out of cards!")
            print("Sorry, you've lost the game.")
        else:
            print("\nThe computer has run out of cards!")
            print("Congratulations, you've won!")
            
        playAgain = input("\nWould you like to play again? (y/n) ")
        
################################################
# This is where it all begins.return "END_Player"

the_game()
MessageBox = ctypes.windll.user32.MessageBoxW
MessageBox(None, 'Thanks for playing!', 'Goodbye!', 0)