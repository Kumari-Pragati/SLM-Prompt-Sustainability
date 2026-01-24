import unittest
from mbpp_756_code import text_match_zero_one

class TestTextMatchZeroOne(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_match_zero_one('ab'), 'Found a match!')
        self.assertEqual(text_match_zero_one('a'), 'Found a match!')
        self.assertEqual(text_match_zero_one('b'), 'Found a match!')
        self.assertEqual(text_match_zero_one(''), 'Not matched!')

    def test_edge_cases(self):
        self.assertEqual(text_match_zero_one('a'*10000 + 'b'), 'Found a match!')
        self.assertEqual(text_match_zero_one('b'*10000 + 'a'), 'Found a match!')
        self.assertEqual(text_match_zero_one('a'*10000 + 'b'*10000), 'Found a match!')

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            text_match_zero_one(123)
        with self.assertRaises(TypeError):
            text_match_zero_one(None)
        with self.assertRaises(TypeError):
            text_match_zero_one(True)
        with self.assertRaises(TypeError):
            text_match_zero_one(['a', 'b'])
