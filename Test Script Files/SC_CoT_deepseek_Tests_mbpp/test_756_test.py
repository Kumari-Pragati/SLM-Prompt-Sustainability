import unittest
from mbpp_756_code import text_match_zero_one

class TestTextMatchZeroOne(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_match_zero_one('ab'), 'Found a match!')
        self.assertEqual(text_match_zero_one('a'), 'Not matched!')
        self.assertEqual(text_match_zero_one('b'), 'Not matched!')

    def test_boundary_case(self):
        self.assertEqual(text_match_zero_one(''), 'Not matched!')

    def test_edge_case(self):
        self.assertEqual(text_match_zero_one('a'*10000 + 'b'), 'Found a match!')
        self.assertEqual(text_match_zero_one('b'*10000 + 'a'), 'Not matched!')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            text_match_zero_one(123)
        with self.assertRaises(TypeError):
            text_match_zero_one(None)
