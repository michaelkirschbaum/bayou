#!/usr/bin/env python

import unittest
from deck import Deck
from card import Card
import copy

class CardTestCase(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(ValueError):
            Card(2, "red")

        with self.assertRaises(ValueError):
            Card(1, "heart")

        with self.assertRaises(ValueError):
            Card("one", "clubs")

        self.assertIsNotNone(Card("King", "spade"))

        self.assertIsNotNone(Card(4, "Diamonds"))

        self.assertIsNotNone(Card("joker"))

class DeckTestCase(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def tearDown(self):
        # self.deck.delete()
        self.deck = None

    def test_shuffle(self):
        # copy deck
        orig = copy.copy(self.deck.cards)
        self.deck.shuffle()
        self.assertNotEqual(orig, self.deck.cards)

    def test_draw(self):
        card = self.deck.draw()
        self.assertIsNotNone(card)

        # draw all cards
        for _ in range(len(self.deck.cards)):
            self.deck.draw()

        with self.assertRaises(IndexError):
            self.deck.draw()

if __name__ == '__main__':
    unittest.main()
