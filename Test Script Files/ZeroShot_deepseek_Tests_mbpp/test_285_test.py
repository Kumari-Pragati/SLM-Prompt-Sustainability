import unittest
from mbpp_285_code import text_match_two_three

class TestTextMatchTwoThree(unittest.TestCase):

    def test_match_two(self):
        self.assertEqual(text_match_two_three('ab'), 'Found a match!')

    def test_match_three(self):
        self.assertEqual(text_match_two_three('abb'), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_match_two_three('ac'), 'Not matched!')

    def test_match_four(self):
        self.assertEqual(text_match_two_three('abbb'), 'Found a match!')
