# Week 2.py
# Jacob Mason
# jm2232
# October 9th
#
# This program is designed to meet the expectations of weeks 1 and 2 of the Card Project.
# 

####### GLOBAL VARIABLES #######
#
# CARD_1 is the player's card and CARD_2 is the PC's card. The domain of these
# tuples is: (x, y) where:
#
# x = suit
#    1 = Diamonds
#    2 = Clubs
#    3 = Hearts
#    4 = Spades
#
# y = rank
#    1 = Ace
#    2 = 2
#    ...
#    10 = 10
#    11 = Jack
#    12 = Queen
#    13 = King
#    14 = Ace
#
# Implied above, aces can be either high or low.
# 

CARD_1 = (1, 1)
CARD_2 = (4, 14)

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
    else: # when cardTuple[1] == 14 because of high Aces
        rank = "Ace"       
    
    return (rank + " of " + suit)

############ CARD COMPARE ###########
# Pass card Tuples into this function to receive a printed output of the result
def card_compare(playerCard, PCCard):
    print("The computer's card is the ", get_name(PCCard), ".", sep="")
    print("Your card is the ", get_name(playerCard), ".", sep="")     
    if playerCard[1] > PCCard[1]:
        print("\nYou are the winner!")
        winner = "Player"
    elif playerCard[1] < PCCard[1]:
        print("\nThe Computer is the winner!")
        winner = "PC"
    else:
        print("\nThese cards are equal: It's a tie!")

############## MAIN ##############
card_compare(CARD_1, CARD_2)
