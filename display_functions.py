# display_functions.py

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