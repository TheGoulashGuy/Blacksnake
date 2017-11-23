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

	def calcHandValue(self):
		self.new_value = self.hand[-1]
		self.value_list.insert(0,self.new_value)
		if self.value_list[0] == "K" or self.new_value[0] == "Q" or self.new_value[0] == "J":
			self.value += 10
		elif self.new_value[0] in deckClass.ranks:
			self.value += int(self.new_value[0])
		elif self.new_value[0] == "Ace":
			'''Write function to handle when player is dealt an Ace!'''
			#aceFunction()
			pass
		else:
			pass

	def showHand(self):
		print("Your hand consists of: " + str(self.hand))
		print("Its value is: " + str(self.value))
