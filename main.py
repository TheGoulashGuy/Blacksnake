#!/usr/bin/python3

import handClass, deckClass #Don't forget to import winCheck and other needed modules

print('''
Welcome to Blacksnake, a Python implementation of Blackjack. *Gambling is not encouraged*
''')

def winCheck():
	pass

player_name_input = input("Enter your name: ")
player_bet_input = input("Enter the amount of money you'd like to bet: ")
player_hand = handClass.Hand(str(player_name_input), int(player_bet_input))
dealer_hand = handClass.Hand('dealer', 0)

def playerHits():
	player_hand.dealCard()
	player_hand.calcHandValue()
	player_hand.showHand()

deckClass.new_deck.createDeck() #This creates the card deck and shuffles it.
player_hand.dealCard() #This deals 1st of player's 2 initial cards
player_hand.dealCard() #This deals 2nd of player's 2 initial cards
dealer_hand.dealCard()
dealer_hand.dealCard()
#player_hand.calcHandValue()
player_hand.showHand()

game_in_session = True
while game_in_session == True:
	playerChoice = input("Would you like to stand (s) or hit (h)? ")
	if playerChoice == 'h':
		playerHits()
	elif playerChoice == 's':
		#wincheck() #This function will set game_in_session to false if someone has won, thus ending the main game loop.
		pass
	else:
		print('Error, please input "h" or "s": ')
		print(playerChoice)
