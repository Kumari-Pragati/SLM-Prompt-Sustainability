import unittest
from mbpp_434_code import text_match_one

class TestTextMatchOne(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(text_match_one(''), 'Not matched!')

    def test_single_a(self):
        self.assertEqual(text_match_one('a'), 'Not matched!')

    def test_single_b(self):
        self.assertEqual(text_match_one('b'), 'Not matched!')

    def test_single_ab(self):
        self.assertEqual(text_match_one('ab'), 'Not matched!')

    def test_multiple_a(self):
        self.assertEqual(text_match_one('aaaaa'), 'Not matched!')

    def test_multiple_ab(self):
        self.assertEqual(text_match_one('ababab'), 'Not matched!')

    def test_match_one_a(self):
        self.assertEqual(text_match_one('aaab'), 'Found a match!')

    def test_match_one_ab(self):
        self.assertEqual(text_match_one('abab'), 'Found a match!')
