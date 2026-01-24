import unittest
from mbpp_879_code import text_match

class TestTextMatch(unittest.TestCase):

    def test_text_match_positive(self):
        self.assertEqual(text_match('acb'), 'Found a match!')
        self.assertEqual(text_match('abc'), 'Found a match!')
        self.assertEqual(text_match('ab'), 'Found a match!')
        self.assertEqual(text_match('a123b'), 'Found a match!')
        self.assertEqual(text_match('a!!!b'), 'Found a match!')

    def test_text_match_negative(self):
        self.assertEqual(text_match('ab'), 'Not matched!')
        self.assertEqual(text_match('ba'), 'Not matched!')
        self.assertEqual(text_match('a'), 'Not matched!')
        self.assertEqual(text_match('b'), 'Not matched!')
        self.assertEqual(text_match(''), 'Not matched!')
