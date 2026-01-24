import unittest
from mbpp_285_code import text_match_two_three

class TestTextMatchTwoThree(unittest.TestCase):
    def test_typical_match(self):
        self.assertEqual(text_match_two_three('abab'), 'Found a match!')
        self.assertEqual(text_match_two_three('aaab'), 'Found a match!')
        self.assertEqual(text_match_two_three('aab'), 'Found a match!')

    def test_typical_no_match(self):
        self.assertEqual(text_match_two_three('abc'), 'Not matched!')
        self.assertEqual(text_match_two_three('ab'), 'Not matched!')
        self.assertEqual(text_match_two_three('a'), 'Not matched!')

    def test_edge_cases(self):
        self.assertEqual(text_match_two_three('ababab'), 'Found a match!')
        self.assertEqual(text_match_two_three('aabab'), 'Not matched!')
        self.assertEqual(text_match_two_three('abababab'), 'Not matched!')

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, text_match_two_three, 123)
        self.assertRaises(TypeError, text_match_two_three, None)
        self.assertRaises(TypeError, text_match_two_three, [])
