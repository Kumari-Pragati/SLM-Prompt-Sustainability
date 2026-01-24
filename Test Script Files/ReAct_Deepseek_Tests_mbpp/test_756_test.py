import unittest
from mbpp_756_code import text_match_zero_one

class TestTextMatchZeroOne(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_match_zero_one('ab'), 'Found a match!')
        self.assertEqual(text_match_zero_one('a'), 'Found a match!')
        self.assertEqual(text_match_zero_one('b'), 'Found a match!')
        self.assertEqual(text_match_zero_one('ab'), 'Found a match!')

    def test_edge_cases(self):
        self.assertEqual(text_match_zero_one(''), 'Not matched!')
        self.assertEqual(text_match_zero_one('a'*1000), 'Found a match!')
        self.assertEqual(text_match_zero_one('b'*1000), 'Found a match!')
        self.assertEqual(text_match_zero_one('ab'*1000), 'Found a match!')

    def test_explicitly_handled_error_cases(self):
        self.assertRaises(TypeError, text_match_zero_one, 123)
        self.assertRaises(TypeError, text_match_zero_one, ['a', 'b'])
