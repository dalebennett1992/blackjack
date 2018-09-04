#!/usr/bin/python

import unittest

import blackjack


class TestCard(unittest.TestCase):

    def test_to_string(self):
        card = blackjack.Card(suit='Diamonds', rank='Ace')
        self.assertEqual(str(card), 'Ace of Diamonds')


if __name__ == "__main__":
    unittest.main()
