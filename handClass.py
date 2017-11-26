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
		#self.new_value = self.hand[-1]
		#self.value_list.insert(0,self.new_value)
		for card in self.hand:
			self.new_value = deckClass.ranks[card[0]]
		self.value += self.new_value

		'''
		if self.value_list[0] == "K" or self.new_value[0] == "Q" or self.new_value[0] == "J":
			self.value += 10
		elif self.new_value[0] in deckClass.ranks:
			self.value += int(self.new_value[0])
		elif self.new_value[0] == "A":
			self.ace_value = 0
			if (self.ace_value + 11) + self.value >= 21:
				self.value += 1
			else:
				self.value += 11
		else:
			pass
		'''

	def showHand(self):
		print("Your hand consists of: " + str(self.hand))
		print("Its value is: " + str(self.value))
