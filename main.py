#!/usr/bin/python3

import handClass, deckClass

print("Welcome to Blacksnake, a Python implementation of Blackjack. *Gambling is not encouraged*")

def winCheck():
	pass

player_name_input = input("Enter your name: ")
player_bet_input = input("Enter the amount of money you'd like to bet: $")
player_hand = handClass.Hand(str(player_name_input), int(player_bet_input))
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
		exit()
	else:
		pass

def playerStands():
	if player_hand.value <= 21 and dealer_hand.value < player_hand.value:
		print("Congratulations, you win $" + str(player_bet_input) + "!")
		print("The dealer's hand value was " + str(dealer_hand.value))
		exit()
	else:
		print("Dealer wins.")
		exit()

'''These function calls will begin the initial setup of the game'''
new_deck = deckClass.Deck() #These two lines create the card deck and shuffle it.
new_deck.createDeck()

player_hand.dealCard() #This deals 1st of player's 2 initial cards
player_hand.dealCard() #This deals 2nd of player's 2 initial cards

dealer_hand.dealCard()
dealer_hand.dealCard()

player_hand.showHand()

game_in_session = True
while game_in_session == True:
	player_choice = input("Would you like to stand (s) or hit (h)? ")
	if player_choice == 'h':
		playerHits()
	elif player_choice == 's':
		playerStands()
		#wincheck() #This function will set game_in_session to false if someone has won, thus ending the main game loop.
		pass
	else:
		print('Error, please input "h" or "s": ')

	if dealer_hand.value <= 16:
		dealer_hand.dealCard()
	else:
		pass
