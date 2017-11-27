#!/usr/bin/python3

import random

ranks = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'K':10, 'Q':10, 'J':10, 'A':0}
suits = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
deck = list()

class Deck(object):
	def __init__(self):
		pass

	def createDeck(self):
		for key in ranks:
			for s in suits:
				deck.append(str(key) + ' of ' + str(s))
		random.shuffle(deck)
