import unittest
from mbpp_756_code import text_match_zero_one

class TestTextMatchZeroOne(unittest.TestCase):
    def test_simple_match(self):
        self.assertEqual(text_match_zero_one('ab'), 'Found a match!')

    def test_simple_no_match(self):
        self.assertEqual(text_match_zero_one('xyz'), 'Not matched!')

    def test_pattern_match(self):
        self.assertEqual(text_match_zero_one('ab?'), 'Found a match!')

    def test_pattern_no_match(self):
        self.assertEqual(text_match_zero_one('abc'), 'Not matched!')

    def test_empty_input(self):
        self.assertEqual(text_match_zero_one(''), 'Not matched!')

    def test_edge_case(self):
        self.assertEqual(text_match_zero_one('a'), 'Found a match!')

    def test_edge_case2(self):
        self.assertEqual(text_match_zero_one('b'), 'Found a match!')

    def test_edge_case3(self):
        self.assertEqual(text_match_zero_one('ab?'), 'Found a match!')
