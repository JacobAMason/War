# draw_cards.py

def draw_cards(cards):
    """
    Contract: NULL ==> string
    Purpose: Print the image of the card.
    """
    picturesList = []
    for card in cards:
        if card.suit==1:
            pic3 = "| :/\: |"
            pic4 = "| :\/: |"         
        elif card.suit==2:
            pic3 = "| :(): |"
            pic4 = "| ()() |"        
        elif card.suit==3:
            pic3 = "| (\/) |"
            pic4 = "| :\/: |"        
        else:
            pic3 = "| :/\: |"
            pic4 = "| (__) |"
            
        if card.rank > 1 and card.rank < 10:
            pic2 = str(card.rank) + "."
            pic5 = "'" + str(card.rank)
        elif card.rank == 10:    
            pic2 = str(card.rank)
            pic5 = str(card.rank)
        elif card.rank == 11:
            pic2 = "J."
            pic5 = "'J"
        elif card.rank == 12:
            pic2 = "Q."
            pic5 = "'Q"         
        elif card.rank == 13:
            pic2 = "K."
            pic5 = "'K" 
        else:
            pic2 = "A."
            pic5 = "'A"
            
        # This section pieces together the image using a bunch of conctenation.
        whiteBuffer = max([len(str(card)), len(str(card.owner))])*" "
        pic1 = whiteBuffer + " "*2 + ".------."
        pic2 = "  " + str(card.owner) + (len(whiteBuffer) - len(str(card.owner)))*" " + "|" + pic2 + "--. |"
        pic3 = whiteBuffer + " "*2 + pic3
        pic4 = str(card) + (len(whiteBuffer) - len(str(card)))*" " + " "*2 + pic4
        pic5 = whiteBuffer + " "*2 + "| '--" + pic5 + "|"
        pic6 = whiteBuffer + " "*2 + "`------'"
        
        picture = [pic1, pic2, pic3, pic4, pic5, pic6]
        
        picturesList.append(picture)
        
    finalImage = ["", "", "", "", "", ""]
    for picture in picturesList[1:]: #ignore the index of picturesList. It's the main user.
        for i in range(6):
            finalImage[i] += picture[i] + " "*4
            
    for i in range(6):
        print(finalImage[i])
        
    print()    
    
    for i in range(6):
        print(picturesList[0][i]) #print the main user's card