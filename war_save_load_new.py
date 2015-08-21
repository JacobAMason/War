#war_save_load_new.py
from card_logic import Deck
from card_logic import User
import pickle

def save_game(users):
    """
    Contract: List of User objects ==> NUL
    Purpose: This saves the list of users to a file that shares the name of the initial user.
    """
    userName = str(users[0])
    outFile = open((userName + '.dat'), "wb")

    pickle.dump(users, outFile)
        
    outFile.close()
    return
    
def load_game(userName):
    """
    Contract: string ==> List of User objects OR Blank list
    Purpose: Loads a user's data from the disk.
    """
    try:
        inFile = open((userName + '.dat'), 'rb')
        users = pickle.load(inFile)
        
        inFile.close() 
        print("Game loaded.")
        
        return users
    except:
        print("Sorry, there is no save file for you. Let's start a new game.\n")
        return []
    
def new_game():
    """
    Contract: NULL ==> List of User Objects
    Purpose: This sets up the users list for a new game based on a given name and a number of computer players.
    """
    BigDeck = Deck(True) #initialize deck. True means Aces are high
    userNameList = []
    while userNameList == []: 
        userNameList.append(input("Please enter your name: "))
        
    PCnum = int(input("How many Computer opponents would you like to compete against? "))
    while PCnum <=0 or PCnum > 50:
        print("You must compete against at least 1 Computer and less than 51.")
        PCnum = int(input("How many Computer opponents would you like to compete against? "))
        
    for i in range(0, PCnum):
        userNameList.append("Computer " + str(i+1))  #i is incremented because Computer_0 sounds stupid
    
    # users contains the list of users that will be playing, including PCs
    # every user in the list will be turned into an object of class User
    users = []
    for userName in userNameList:
        users.append(User(userName)) # initialize Users. The string will represent the name of the winner.
    
    BigDeck.shuffle(users) #shuffle the deck and deal to all players
    
    return users

def get_users():
    """
    Contract: NULL ==> list of User objects
    Purpose: This function asks the user if he wants to load a savegame and then either loads or creates a new game.
    """
    loadFile = input("Would you like to load a file? (y/n) ")
    if loadFile[0].lower()=="y":
        userName = input("What is your name? ")
        users = load_game(userName)
        if users == []:
            users = new_game()
    else:
        users = new_game()  
        
    return users 