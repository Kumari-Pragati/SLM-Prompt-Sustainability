import unittest
from mbpp_285_code import text_match_two_three

class TestTextMatchTwoThree(unittest.TestCase):

    def test_text_match_two_three(self):
        self.assertEqual(text_match_two_three('ab'), 'Not matched!')
        self.assertEqual(text_match_two_three('aba'), 'Found a match!')
        self.assertEqual(text_match_two_three('abab'), 'Found a match!')
        self.assertEqual(text_match_two_three('ababab'), 'Found a match!')
        self.assertEqual(text_match_two_three('abc'), 'Not matched!')
        self.assertEqual(text_match_two_three('abbb'), 'Not matched!')
