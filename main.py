#!/usr/bin/python3

import handClass, deckClass

print('''
Welcome to Blacksnake, a Python implementation of Blackjack. *Gambling is not encouraged*
''')

def winCheck():
	pass

player_name_input = input("Enter your name: ")
player_bet_input = input("Enter the amount of money you'd like to bet: $")
player_hand = handClass.Hand(str(player_name_input), int(player_bet_input))
dealer_hand = handClass.Hand('dealer', 0)

def playerHits():
	player_hand.dealCard()
	player_hand.calcHandValue()
	player_hand.showHand()

def playerStands():
	dealer_hand.dealCard()
	dealer_hand.calcHandValue()
	if dealer_hand.value <= 21:
		print("Dealer wins.")
	else:
		pass
deckClass.new_deck.createDeck() #This creates the card deck and shuffles it.
player_hand.dealCard() #This deals 1st of player's 2 initial cards
player_hand.calcHandValue()
player_hand.dealCard() #This deals 2nd of player's 2 initial cards
player_hand.calcHandValue()
dealer_hand.dealCard()
dealer_hand.calcHandValue()
dealer_hand.dealCard()
dealer_hand.calcHandValue()
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

	if dealer_hand.value <=16:
		dealer_hand.dealCard()
	else:
		pass
	print("Dealer hand value is: " + str(dealer_hand.value))
