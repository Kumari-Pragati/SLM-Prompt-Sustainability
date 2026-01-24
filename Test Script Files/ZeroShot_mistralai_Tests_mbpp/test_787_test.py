import unittest
from mbpp_787_code import text_match_three

class TestTextMatchThree(unittest.TestCase):

    def test_text_match_three(self):
        self.assertEqual(text_match_three('abc'), 'Found a match!')
        self.assertEqual(text_match_three('abcd'), 'Not matched!')
        self.assertEqual(text_match_three('aab'), 'Found a match!')
        self.assertEqual(text_match_three('abab'), 'Not matched!')
        self.assertEqual(text_match_three('ababab'), 'Found a match!')
