

cards = []
for rank in range(1, 5):
    for suit in range(1, 14):
        cards.append((rank, suit))
print(cards)
input("Press any key to continue...")

for item in range(0,52):
    print(cards[item])