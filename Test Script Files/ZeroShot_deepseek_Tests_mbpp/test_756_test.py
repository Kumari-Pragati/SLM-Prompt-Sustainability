import unittest
from mbpp_756_code import text_match_zero_one

class TestTextMatchZeroOne(unittest.TestCase):

    def test_match_ab(self):
        self.assertEqual(text_match_zero_one('ab'), 'Found a match!')

    def test_match_a(self):
        self.assertEqual(text_match_zero_one('a'), 'Found a match!')

    def test_match_b(self):
        self.assertEqual(text_match_zero_one('b'), 'Not matched!')

    def test_match_ab_multiple(self):
        self.assertEqual(text_match_zero_one('abababab'), 'Found a match!')

    def test_match_empty(self):
        self.assertEqual(text_match_zero_one(''), 'Not matched!')
