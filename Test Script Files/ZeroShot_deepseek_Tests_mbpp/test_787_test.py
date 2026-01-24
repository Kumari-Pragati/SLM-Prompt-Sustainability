import unittest
from mbpp_787_code import text_match_three

class TestTextMatchThree(unittest.TestCase):

    def test_match_three(self):
        self.assertEqual(text_match_three('abc'), 'Found a match!')
        self.assertEqual(text_match_three('abbc'), 'Found a match!')
        self.assertEqual(text_match_three('abbbc'), 'Found a match!')
        self.assertEqual(text_match_three('abbbbc'), 'Not matched!')
        self.assertEqual(text_match_three('ac'), 'Not matched!')
