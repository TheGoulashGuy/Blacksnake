#!/usr/bin/python3

import deckClass

class Hand(object):
	def __init__(self, name, bet):
		self.name = name
		self.bet = bet
		self.hand = list()
		self.value = 0

	def dealCard(self):
		self.new_card = deckClass.deck.pop()
		self.hand.append(self.new_card)
		self.value += self.new_card

	''''def calcHandValue(self):
		for integer in self.hand:
		self.newValue = self.hand
		print(self.newValue)
		self.value += self.newValue'''

	def showHand(self):
		print("Your hand consists of: " + str(self.hand))
		print("It's value is: " + str(self.value))
