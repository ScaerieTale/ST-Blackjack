import random
# Based on Ace being worth 11 until the hand > 21 when it becomes 1
# I'm assuming 11 as value for now.  I'm going to try putting
# cards in a function so I can *hopefully*
# call a later function with 1 instead of 11.  Fingers crossed :)
def dealCard(): # Note to self. () are important dum dum!
    """Deal a random card from Ace (11) to King (one of four 10s)"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    dealtCard = random.choice(cards)
    return dealtCard

#I'm looking at the sample game again and I notice she uses
# a list to keep track of the cards.  That one had me scratching
# my head at first wondering how I'd avoid
# the cards getting added together in the display haha

#Going to just make two empty lists for now that I can write to.  Probably need
# an iterating loop (for loop?) to deal 2 cards each.

dealerHand = []
playerHand = []
for i in range(2):
        dealerHand.append(dealCard())
        playerHand.append(dealCard())


# Dealer hand shows index 0 only because player only gets
# to see Dealer's first card until the hand ends.
print(f"""Dealer shows {dealerHand[0]}
You have {playerHand}""")