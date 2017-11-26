#!/usr/bin/python3

import deckClass

class Hand(object):
	def __init__(self, name, bet):
		self.name = name
		self.bet = bet
		self.hand = list()
		self.value_list = list()
		self.value = 0

	def dealCard(self):
		self.new_card = deckClass.deck.pop()
		self.hand.append(self.new_card)
		for card in self.hand:
			self.new_value = deckClass.ranks[card[0]]
		self.value += self.new_value

	def showHand(self):
		print("Your hand consists of: " + str(self.hand))
		print("Its value is: " + str(self.value))
