import unittest
from mbpp_285_code import text_match_two_three

class TestTextMatchTwoThree(unittest.TestCase):

    def test_simple_match(self):
        self.assertEqual(text_match_two_three('ab'), 'Found a match!')
        self.assertEqual(text_match_two_three('abb'), 'Found a match!')
        self.assertEqual(text_match_two_three('abbb'), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_match_two_three('a'), 'Not matched!')
        self.assertEqual(text_match_two_three('abc'), 'Not matched!')
        self.assertEqual(text_match_two_three('abcd'), 'Not matched!')

    def test_empty_string(self):
        self.assertEqual(text_match_two_three(''), 'Not matched!')

    def test_multiple_matches(self):
        self.assertEqual(text_match_two_three('ababab'), 'Found a match!')
        self.assertEqual(text_match_two_three('abababab'), 'Found a match!')

    def test_special_characters(self):
        self.assertEqual(text_match_two_three('a!b'), 'Not matched!')
        self.assertEqual(text_match_two_three('a@b'), 'Not matched!')
        self.assertEqual(text_match_two_three('a#b'), 'Not matched!')
