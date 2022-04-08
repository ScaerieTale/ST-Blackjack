import random
# So the first thing I'm going to
# need is a while loop to actually make
# the game loop around.  I'm going to do that
# first because otherwise the damn thing breaks.

# Second thing I'll need to do is set up a dictionary
# or a list to define the cards.  Initially I'm just going to
# be working with straight numbers, i.e. 1 = Ace, 11 = Jack, etc
#I can figure out the rest once I've got the bare bones basics working.
#When I do get that working though I'm going to need four suits of cards
# I think a Dictionary and then a List will be the way to go here.
# Hearts: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11: Jack, 12: Queen, 13: King, maybe?]
# No idea how I'm going to handle the logic of Ace being worth 1 or 11 though...

# Game AI will be easy enough, just have a random choice
# pull from the list, or heck, in this early stage, a simple
# call from a range.

# If Dealer hand > 18 and Player hand <= 18, Stand.
# That way the Dealer still tries to win if the player
# is winning.