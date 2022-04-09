import random
import sys
def blackjack():
    """This sets up the recursive algorithm so that
    the player can keep playing after each hand."""
    gameOver = False
    def dealCard(): # Note to self. () are important dum dum!
        """Deal a random card from Ace (11) to King (one of four 10s)"""
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        dealtCard = random.choice(cards)
        return dealtCard
    def score(cards):
        """Calculate the score to see if it's under or over 21 and if Blackjack occurs."""
        if sum(cards) == 21 and len(cards) == 2:
            return 0    
        if 11 in (cards) and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)
    
    # define the player and dealer card total values by calling
    
    # Player and computer must start with an empty "hand" (list)
    dealerHand = []
    playerHand = []
    
    # the above "score" function with the respective hand as the argument
    playerScore = score(playerHand)
    dealerScore = score(dealerHand)

    # initial round, dealing 2 cards to player and computer dealer
    for _ in range(2):
            dealerHand.append(dealCard())
            playerHand.append(dealCard())


    # Dealer hand shows index 0 only because player only gets
    # to see Dealer's first card until the hand ends.
    print(f"""Dealer shows {dealerHand[0]} {dealerScore}
    You have {playerHand} {playerScore}""")
    while gameOver == False:
        if dealerScore == 0 or playerScore == 0 or playerScore > 21:
            gameOver = True
        else:
            if input("Hit or Stand? ") == "hit":
                playerHand.append(dealCard())
                playerScore = score(playerHand)
                print(f"{playerHand[-1]} {playerHand} [{playerScore}]")
            else:
                if dealerScore < 17:
                    dealerHand.append(dealCard)
                    dealerScore = score(dealerHand)
                    if dealerScore > 21:
                        print("Dealer busts!")
                        gameOver = True
    if input("Play again? ").lower == "yes" or "y":
        blackjack()
    else:
        sys.exit()
blackjack()