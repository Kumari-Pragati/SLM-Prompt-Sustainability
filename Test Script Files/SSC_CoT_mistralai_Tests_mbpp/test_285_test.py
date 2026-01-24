import unittest
from mbpp_285_code import text_match_two_three

class TestTextMatchTwoThree(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(text_match_two_three('abab'), 'Found a match!')
        self.assertEqual(text_match_two_three('aaab'), 'Found a match!')
        self.assertEqual(text_match_two_three('ab'), 'Not matched!')

    def test_edge_input(self):
        self.assertEqual(text_match_two_three('aabab'), 'Found a match!')
        self.assertEqual(text_match_two_three('ababab'), 'Not matched!')

    def test_invalid_input(self):
        self.assertNotEqual(text_match_two_three(123), 'Found a match!')
        self.assertNotEqual(text_match_two_three(''), 'Found a match!')
        self.assertNotEqual(text_match_two_three(None), 'Found a match!')
