#!/usr/bin/python env

from card import Card
from random import shuffle

class Deck(object):
    """deck of cards"""
    managed = False

    def __init__(self):
        self.cards = []

        for suit in ["hearts", "spades", "diamonds", "clubs"]:
            for card in range(2, 11):
                self.cards.append(Card(card, suit))

            for card in ["jack", "queen", "king", "ace"]:
                self.cards.append(Card(card, suit))

        num_jokers = 2
        for _ in range(num_jokers):
            self.cards.append(Card("joker"))

    def shuffle(self):
        shuffle(self.cards)

    def draw(self):
        return self.cards.pop()
