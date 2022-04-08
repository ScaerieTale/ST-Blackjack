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
print(dealCard())
