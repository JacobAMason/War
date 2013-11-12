#war_save_load_new.py
from card_logic import Deck
from card_logic import User
import pickle

def save_game(users):
    userName = str(users[0])
    outFile = open((userName + '.dat'), "wb")

    pickle.dump(users, outFile)
        
    outFile.close()
    
def load_game(userName):
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
    BigDeck = Deck(True) #initialize deck. True means Aces are high
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
    # every user in the list will be turned into an object of class User
    users = []
    for userName in userNameList:
        users.append(User(userName)) # initialize Users. The string will represent the name of the winner.
    
    BigDeck.shuffle(users) #shuffle the deck and deal to all players
    
    return users