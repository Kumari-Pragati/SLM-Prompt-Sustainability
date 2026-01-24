import unittest
from mbpp_454_code import text_match_wordz

class TestTextMatchWordz(unittest.TestCase):

    def test_match_wordz(self):
        self.assertEqual(text_match_wordz('hello world'), 'Not matched!')
        self.assertEqual(text_match_wordz('hello worldz'), 'Found a match!')
        self.assertEqual(text_match_wordz('hello worldz world'), 'Found a match!')
        self.assertEqual(text_match_wordz('hello worldz worldz'), 'Found a match!')
        self.assertEqual(text_match_wordz('hello worldz worldz world'), 'Found a match!')
        self.assertEqual(text_match_wordz('hello worldz worldz worldz'), 'Found a match!')
        self.assertEqual(text_match_wordz('hello worldz worldz worldz world'), 'Found a match!')
        self.assertEqual(text_match_wordz('hello worldz worldz worldz worldz'), 'Found a match!')
