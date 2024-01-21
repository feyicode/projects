from random import *

cards = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "B1", "B2", "B3", "B4", "B5", "B6", "B7","B8", "B9", "B10", "Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9", "Y10"]
totalcards = 30
import random
random.shuffle(cards)

player1cards = []
player2cards = []

running = True

print("Card Game!")
print("------------------------------")

print("Welcome to the Card Game! This is a 2 player game, using a deck of cards.")
print('''
Player 1 takes the top card from the deck.

Player 2 takes the next card from the deck.

If both players have a card of the same color, the highest number wins.

If both players have cards with different colors, the winning color is shown below.

Red v Black = Red

Yellow v Red = Yellow

Black v Yellow = Black

The winner of each round keeps both cards, players keep playing until there are no more cards.

The cards are being shuffled as we speak...
    ''')

running = True

name = input("And, what is  your name?").lower()

if name == "feyisara":
    print("You are an authorised player, let's keep playing!")
    cont = input("Would you like to continue? y/n ").lower()
elif name == "ashrafi":
    print("You are an authorised player, let's keep playing!")
    cont = input("Would you like to continue? y/n ").lower()
elif name == "holly":
    print("You are an authorised player, let's keep playing!")
    cont = input("Would you like to continue? y/n ").lower()
else:
    print("Unauthorised player.")
    quit()

while cont == "y" and len(cards) > 0:
    print("\nExcellent, a card is now being drawn for Player 1.")
    player1chosencard = cards.pop()
    print("\nThe system has selected ",player1chosencard," for Player 1.")
    print("A card is now being drawn for Player 2.")
    player2chosencard = cards.pop()
    print("The system has selected ",player2chosencard," for Player 2.")
    print("There are", len(cards), "cards in the deck, currently.")
    if player1chosencard[0] == "R" and player2chosencard[0] == "Y":
        print("\n\nPlayer 1's card  is red, whilst Player 2's card is yellow, meaning that Player 2 wins and keeps BOTH cards.")
        cont = "pause" 
        player2cards.append(player1chosencard)
        player2cards.append(player2chosencard)
        cont = input("Would you like to continue? y/n ")  
    elif player2chosencard[0] == "R" and player1chosencard[0] == "Y":
        print("\n\nPlayer 1's card  is yellow, whilst Player 2's card is red, meaning that Player 1 wins and keeps BOTH cards.")
        cont = "pause"
        player1cards.append(player1chosencard)
        player1cards.append(player2chosencard)
        cont = input("Would you like to continue? y/n ")  
    elif player1chosencard[0] == "B" and player2chosencard[0] == "R":
        print("\n\nPlayer 1's card is black whilst Player 2's chosen card is red, meaning that Player 2 wins and keeps BOTH cards.")
        cont = "pause"
        player2cards.append(player1chosencard)
        player2cards.append(player2chosencard)
        cont = input("Would you like to continue? y/n ")  
    elif player2chosencard[0] == "B" and player1chosencard[0] == "R":
        print("\n\nPlayer 1's card is red whilst Player 2's chosen card is black, meaning that Player 1 wins and keeps BOTH cards.")
        cont = "pause" 
        player1cards.append(player1chosencard)
        player1cards.append(player2chosencard)
        cont = input("Would you like to continue? y/n ")  
    elif player1chosencard[0] == "B" and player2chosencard[0] == "Y":
        print("\n\nPlayer 1's card is black whilst Player 2's chosen card is yellow, meaning that Player 1 wins and keeps BOTH cards.")
        cont = "pause" 
        player1cards.append(player1chosencard)
        player1cards.append(player2chosencard)
        cont = input("Would you like to continue? y/n ")  
    elif player2chosencard[0] == "B" and player1chosencard[0] == "Y":
        print("\n\nPlayer 1's card is yellow whilst Player 2's chosen card is black, meaning that Player 2 wins and keeps BOTH cards.")
        player2cards.append(player1chosencard)
        player2cards.append(player2chosencard)
        cont = "pause" 
        cont = input("Would you like to continue? y/n ")  
    elif player1chosencard[0] == player2chosencard[0]:
        print("The cards are the same colours, now processing...")
        if player1chosencard[1] > player2chosencard[1]:
            print("\n\nPlayer 1's card is the same colour as Player 2's, but Player 1's card number is higher! Congrats, Player 1 wins this round and keeps BOTH cards.")
            cont = "pause"
            player1cards.append(player1chosencard)
            player1cards.append(player2chosencard)
            cont = input("Would you like to continue? y/n ")  
        elif player2chosencard[1] > player1chosencard[1]:
            print("\n\nPlayer 1's card is the same colour as Player 2's, but Player 1's card number is lower! Congrats, Player 2 wins this round and keeps BOTH cards.")
            cont = "pause"
            player2cards.append(player1chosencard)
            player2cards.append(player2chosencard)
            cont = input("Would you like to continue? y/n ")  
    else:
        print("Error.")
        running = False



if len(cards) == 0:
    print("The game is now over, your totals will now be calculated.")
    if len(player1cards) > len(player2cards):
        print("Player 1 has more cards (",len(player1cards),") than Player 2 (",len(player2cards),") Congratulations, Player 1!")
    elif len(player1cards) < len(player2cards):
        print("Player 1 has less cards (",len(player1cards),") than Player 2 (",len(player2cards),") Congratulations, Player 2!")
    else:
        print("Error.")
