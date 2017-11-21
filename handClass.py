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

	def calcHandValue(self):
		for key in self.hand:
			self.newValue = int(deckClass.ranks.get(key[0]))
			self.value += self.newValue

	def showHand(self):
		print(self.hand)
		print(self.value)
