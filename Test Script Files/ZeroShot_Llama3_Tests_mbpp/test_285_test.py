import unittest
from mbpp_285_code import text_match_two_three

class TestTextMatchTwoThree(unittest.TestCase):

    def test_match(self):
        self.assertEqual(text_match_two_three('abab'), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_match_two_three('abc'), 'Not matched!')

    def test_match_with_three(self):
        self.assertEqual(text_match_two_three('ababab'), 'Found a match!')

    def test_no_match_with_three(self):
        self.assertEqual(text_match_two_three('abcabc'), 'Not matched!')

    def test_match_with_two(self):
        self.assertEqual(text_match_two_three('abab'), 'Found a match!')

    def test_no_match_with_two(self):
        self.assertEqual(text_match_two_three('abc'), 'Not matched!')

    def test_match_with_three_and_two(self):
        self.assertEqual(text_match_two_three('abababab'), 'Found a match!')

    def test_no_match_with_three_and_two(self):
        self.assertEqual(text_match_two_three('abcabcabc'), 'Not matched!')
