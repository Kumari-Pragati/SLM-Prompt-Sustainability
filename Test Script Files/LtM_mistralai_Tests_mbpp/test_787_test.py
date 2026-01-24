import unittest
from mbpp_787_code import text_match_three

class TestTextMatchThree(unittest.TestCase):
    def test_simple_match(self):
        self.assertEqual(text_match_three('abc'), 'Found a match!')

    def test_min_length_match(self):
        self.assertEqual(text_match_three('a'), 'Not matched!')
        self.assertEqual(text_match_three('ab'), 'Not matched!')

    def test_max_length_match(self):
        self.assertEqual(text_match_three('abcd'), 'Not matched!')
        self.assertEqual(text_match_three('ababab'), 'Not matched!')

    def test_edge_cases(self):
        self.assertEqual(text_match_three('aab'), 'Not matched!')
        self.assertEqual(text_match_three('ab{2}'), 'Not matched!')
        self.assertEqual(text_match_three('ab{4}'), 'Not matched!')

    def test_invalid_input(self):
        self.assertRaises(TypeError, text_match_three, 123)
        self.assertRaises(TypeError, text_match_three, None)
