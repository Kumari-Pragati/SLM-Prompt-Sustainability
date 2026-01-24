import unittest
from mbpp_787_code import text_match_three

class TestTextMatchThree(unittest.TestCase):

    def test_match(self):
        self.assertEqual(text_match_three('ababab'), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_match_three('abc'), 'Not matched!')

    def test_match_with_non_matching_text(self):
        self.assertEqual(text_match_three('ababababab'), 'Found a match!')

    def test_no_match_with_non_matching_text(self):
        self.assertEqual(text_match_three('abcd'), 'Not matched!')

    def test_match_with_non_matching_text_and_non_matching_pattern(self):
        self.assertEqual(text_match_three('abc'), 'Not matched!')

    def test_match_with_non_matching_text_and_matching_pattern(self):
        self.assertEqual(text_match_three('ababab'), 'Found a match!')
