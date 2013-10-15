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
from display_functions import *
from card_brain import *


####### GLOBAL VARIABLES #######

# Set ACES_HIGH to False to make Aces low and True to make Aces High
ACES_HIGH = True

# Set DEBUG to True to activate verbose mode.
# You can always type "debug" at the enter key prompt to get current card stats, even if this is False.
DEBUG = True


############## MAIN ROUND ##############
# This function is what keeps polling the user.  It holds the current match data
# and will continually be called as long as the player keeps wanting to play.
# This function monitors the global variables that are necessary to keep the game
# running. If either deck is emptied, the game is over. If a double war is attempted
# but cannot be performed because a party lacks enough cards, endGame will end the
# loop.  Regardless of how the loop ends, main_round passes the loser to the_game.

def main_round(DECK, PLAYER_DECK, PC_DECK):
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
            endGame = flip_cards(DEBUG)
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
        DECK, PLAYER_DECK, PC_DECK = shuffle(ACES_HIGH, DEBUG)
        if DEBUG == True:
                print("\n", PLAYER_DECK)
                print("\n", PC_DECK)        
        loser = main_round(DECK, PLAYER_DECK, PC_DECK)      
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