import unittest
from mbpp_787_code import text_match_three

class TestTextMatchThree(unittest.TestCase):
    def test_simple_match(self):
        self.assertEqual(text_match_three('ababab'), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_match_three('abc'), 'Not matched!')

    def test_empty_input(self):
        self.assertEqual(text_match_three(''), 'Not matched!')

    def test_pattern_with_spaces(self):
        self.assertEqual(text_match_three('a b c'), 'Not matched!')

    def test_pattern_with_punctuation(self):
        self.assertEqual(text_match_three('a,b,c'), 'Not matched!')

    def test_pattern_with_numbers(self):
        self.assertEqual(text_match_three('a1b2c3'), 'Not matched!')

    def test_pattern_with_special_chars(self):
        self.assertEqual(text_match_three('a!b@c'), 'Not matched!')
