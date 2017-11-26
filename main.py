#!/usr/bin/python3

import handClass, deckClass

print("Welcome to Blacksnake, a Python implementation of Blackjack. *Gambling is not encouraged*")

def winCheck():
	pass

player_name_input = input("Enter your name: ")
player_bet_input = float(input("Enter the amount of money you'd like to bet: $"))
player_hand = handClass.Hand(str(player_name_input), player_bet_input)
dealer_hand = handClass.Hand('dealer', 0)

def playerHits():
	player_hand.dealCard()
	player_hand.showHand()
	if player_hand.value == 21:
		print("Congratulations, you win $" + str(player_bet_input) + "!")
		print("The dealer's hand value was " + str(dealer_hand.value))
		exit()
	if player_hand.value > 21:
		print("You've busted--the dealer wins.")
		print("The dealer's hand value was " + str(dealer_hand.value))
		exit()
	else:
		pass

def playerStands():
	print(dealer_hand.value)
	if player_hand.value <= 21 and player_hand.value > dealer_hand.value:
		print("Congratulations, you win $" + str(player_bet_input) + "!")
		print("The dealer's hand value was " + str(dealer_hand.value))
		exit()
	elif player_hand.value == dealer_hand.value:
		print("It's a draw.")
		exit()
	elif dealer_hand.value > 21:
		print("The dealer busted--you win " + str(player_bet_input + "!"))
		exit()
	else:
		print("The dealer won.")
		exit()

'''These function calls will begin the initial setup of the game'''
new_deck = deckClass.Deck() #These two lines create the card deck and shuffle it.
new_deck.createDeck()

player_hand.dealCard() #This deals 1st of player's 2 initial cards
player_hand.dealCard() #This deals 2nd of player's 2 initial cards
if player_hand.value == 21:
	print("You got dealt a Blackjack! You win " + str(player_bet_input) + "!")
	exit()
else:
	pass

dealer_hand.dealCard()
dealer_hand.dealCard()
if dealer_hand.value == 21:
	print("The dealer pulled a Blackjack. You lose.")
	exit()
else:
	pass

player_hand.showHand()

game_in_session = True
while game_in_session == True:
	player_choice = input("Would you like to stand (s) or hit (h)?\n>>")
	print("\n")
	if player_choice == 'h':
		playerHits()
	elif player_choice == 's':
		playerStands()
	else:
		print('Error, please input "h" or "s":\n>>=')
		print("\n")

	if dealer_hand.value <= 16:
		dealer_hand.dealCard()
	else:
		pass
