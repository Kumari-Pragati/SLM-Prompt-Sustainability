import unittest
from mbpp_285_code import text_match_two_three

class TestTextMatchTwoThree(unittest.TestCase):
    def test_simple_match(self):
        self.assertEqual(text_match_two_three('ab'), 'Found a match!')
        self.assertEqual(text_match_two_three('aab'), 'Found a match!')
        self.assertEqual(text_match_two_three('aaab'), 'Found a match!')

    def test_edge_cases(self):
        self.assertEqual(text_match_two_three('abab'), 'Found a match!')
        self.assertEqual(text_match_two_three('a'), 'Not matched!')
        self.assertEqual(text_match_two_three('ababab'), 'Not matched!')
        self.assertEqual(text_match_two_three(''), 'Not matched!')
        self.assertEqual(text_match_two_three('abababab'), 'Not matched!')
