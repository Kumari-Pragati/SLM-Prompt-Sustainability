import unittest
from mbpp_285_code import text_match_two_three

class TestTextMatchTwoThree(unittest.TestCase):
    def test_match_two_characters(self):
        self.assertEqual(text_match_two_three('ab'), 'Found a match!')

    def test_match_three_characters(self):
        self.assertEqual(text_match_two_three('abb'), 'Found a match!')

    def test_no_match_one_character(self):
        self.assertEqual(text_match_two_three('a'), 'Not matched!')

    def test_no_match_four_characters(self):
        self.assertEqual(text_match_two_three('abcd'), 'Not matched!')
