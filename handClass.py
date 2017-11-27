#!/usr/bin/python3

import deckClass, pdb

class Hand(object):
	def __init__(self, hand, value):
		self.hand = list()
		self.value = 0

	def dealCard(self):
		self.new_card = deckClass.deck.pop()
		if self.new_card[0] == 'A':
			if self.value + 11 <= 21:
				self.value += 11
			else:
				self.value += 1
		else:
			self.value += deckClass.ranks[self.new_card[0]]
		self.hand.append(self.new_card)
	def showHand(self):
		print("Your hand consists of: " + str(self.hand))
		print("Its value is: " + str(self.value))
