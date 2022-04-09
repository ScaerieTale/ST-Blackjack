import random
gameOver = False
def dealCard(): # Note to self. () are important dum dum!
    """Deal a random card from Ace (11) to King (one of four 10s)"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    dealtCard = random.choice(cards)
    return dealtCard
dealerHand = []
playerHand = []
#initial round of first two cards
# sidenote: TIL "_" is the universal symbol for a
# var that will never be called again.  Who knew?
for _ in range(2):
        dealerHand.append(dealCard())
        playerHand.append(dealCard())
def score(cards):
    """Calculate the score to see if it's under or over 21 and if Blackjack occurs."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0    
    if 11 in (cards) and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

playerScore = score(playerHand)
dealerScore = score(dealerHand)

# Dealer hand shows index 0 only because player only gets
# to see Dealer's first card until the hand ends.
print(f"""Dealer shows {dealerHand[0]} {dealerScore}
You have {playerHand} {playerScore}""")

# NOTE TO SLEF = sets, == CHECKS. :)
# Also, no help beyond this point.  I worked this out myself darn it :)
while gameOver == False:
    if dealerScore == 0 or playerScore == 0 or playerScore > 21:
        gameOver = True
    else:
        if input("Hit or Stand? ") == "hit":
            playerHand.append(dealCard())
            playerScore = score(playerHand)
            print(f"{playerHand[-1]} {playerHand} [{playerScore}]")
        else:
           gameOver = True